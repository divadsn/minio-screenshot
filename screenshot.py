#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import os
import clipboard
import requests
import datetime
import sys
import argparse
import upload
import capture

# Minio client dependencies
from minio import Minio
from minio.error import ResponseError

# Libnotify, or notify2 if import fails
try:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
except ImportError:
    import notify2
    Notify = None

# Set a local location to save screenshots
directory = os.path.join(os.path.expanduser("~"), "Screenshots")
if not os.path.exists(directory):
    os.makedirs(directory)
