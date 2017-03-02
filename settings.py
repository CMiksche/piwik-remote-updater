'''
Piwik Remote Updater

Copyright 2017 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
from fake_useragent import UserAgent
ua = UserAgent()

# Piwik Site
site = 'http://'

# Piwik settings
pusername = ''
ppassword = ''

# User agent
useragent = ua.chrome # Create fake user agent
