#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import distutils.spawn

# List of capture tools for different platforms
tools = {
    "Linux": "scrot -s %s",      # Linux
    "Darwin": "screenshot -s %s" # macOS
}

# Current platform name
platform = platform.system()

# Command syntax of capture tool
cmd = tools[platform]

# Command name
name = cmd.partition(' ')[0]

# Check if capture tool is installed
def is_installed():
    return distutils.spawn.find_executable(name) is not None
