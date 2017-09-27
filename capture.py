#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List of capture tools for different platforms
tools = {
    "Linux": "scrot -s %s",      # Linux
    "Darwin": "screenshot -s %s" # macOS
}

import platform
cmd = tools[platform.system()]
