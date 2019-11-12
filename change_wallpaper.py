#!/usr/bin/env python3

import os

# This is more of a "hacky" solution that only works for the Gnome desktop
# TODO: OS Detection and Windows support
os.system('gsettings set org.gnome.desktop.background picture-uri "`pwd`/image.jpg"')
