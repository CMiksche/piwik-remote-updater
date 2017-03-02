'''
Piwik Remote Updater

Copyright 2017 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
import settings
import mechanize

# Login to Piwik
browser = mechanize.Browser()
# Set UserAgent
browser.addheaders = [('User-agent', settings.useragent)]
# Ignore robots.txt.  Do not do this without thought and consideration.
browser.set_handle_robots(False)
# Open Site
browser.open(settings.site)
browser.select_form(nr = 0)
browser.form['form_login'] = settings.pusername
browser.form['form_password'] = settings.ppassword
browser.submit()

# Start Update
try:
    req = browser.click_link(url='index.php?module=CoreUpdater&action=newVersionAvailable')
    browser.open(req)
except:
    pass
try:
    browser.select_form(nr = 0)
    browser.submit()
except:
    pass
