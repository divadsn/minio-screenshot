#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import os
import pyperclip
import datetime
import upload
import capture
import shortener

# Minio client dependencies
from minio import Minio
from minio.policy import Policy

# Libnotify, or notify2 if import fails
try:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
except ImportError:
    import notify2
    Notify = None

app_name = "minio-screenshot"

# Init notification daemon
if Notify is not None:
    Notify.init(app_name)
else:
    notify2.init(app_name)

# Helper function for notifications
def notify_send(title, message, icon="dialog-information"):
    if Notify is not None:
        notice = Notify.Notification.new(title, message, icon)
    else:
        notice = notify2.Notification(title, message, icon)
        notice.set_hint_string('x-canonical-append', '')
    try:
        notice.show()
    except:
        pass

    print message

# Check if tool to capture screen is defined and if it is installed
if capture.cmd is None:
    print "It seems like your platform (" + capture.platform + ") is not supported right now. [No capture tool defined]"
    exit(1)
elif not capture.is_installed():
    print capture.name + " is not installed, aborting."
    exit(1)

# Set a local location to save screenshots
directory = os.path.join(os.path.expanduser("~"), "Screenshots")
if not os.path.exists(directory):
    os.makedirs(directory)

# Make screenshot and save local (year/month/)
filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S%p") + ".png"
path = os.path.join(directory, filename)
os.system(capture.cmd % path)

# Upload to self-hosted S3 server using Minio
client = Minio(config.account["host"], access_key=config.account["access_key"], secret_key=config.account["secret_key"], secure=config.account["secure"])

# Create bucket if not existing and give public read access
if not client.bucket_exists(config.account["bucket"]):
    client.make_bucket(config.account["bucket"])
    client.set_bucket_policy(config.account["bucket"], '', Policy.READ_ONLY)

# Put screenshot into bucket
client.fput_object(config.account["bucket"], filename, path, content_type='image/png')

# Build shareable link and shorten it
url = ("https" if config.account["secure"] else "http") + "://" + config.account["host"] + "/" + config.account["bucket"] + "/" + filename
if config.account["shorten_url"]:
    url = shortener.goo_shorten_url(url, config.account["googl_key"])

# Copy link to clipboard and show notification, fin.
pyperclip.copy(url)
notify_send("Screenshot uploaded!", url)
