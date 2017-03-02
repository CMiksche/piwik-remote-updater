# Piwik Remote Updater

Only works with piwik auto-update and Python 2.

This script makes a automatic login and clicks on the "update" link in Piwik.

## Procedure
* Login in Piwik.
* Click on Update link.
* Click on Update button.

## General Information
License: GNU General Public License

Author: Christoph Daniel Miksche (m5e.de)

## Installation

1. Use the following command to install all dependencies.

  ```
  pip install pipenv
  pipenv install BeautifulSoup4 lxml mechanize fake_useragent
  ```
  Alternatively if your using Debian:

  ```
  apt install python-beautifulsoup python-mechanize python-lxml python-fake_useragent
  ```

2. Then clone the git repository.

3. After that, please change the variables in the settings.py file.

4. Enter the following command in your commandline.

    ```
    pipenv shell
    python updater.py
    ```

5. If you want to schedule your updates, edit your /etc/crontab file.
