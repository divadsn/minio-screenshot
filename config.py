#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configobj

config = configobj.ConfigObj("accounts.ini")
selected_account = config.get("selected_account", "")

account = {
    "bucket": config.get(selected_account).get("bucket"),
    "host": config.get(selected_account).get("host"),
    "access_key": config.get(selected_account).get("access_key"),
    "secret_key": config.get(selected_account).get("secret_key"),
    "secure": config.get(selected_account).as_bool("secure")
}
