#!/bin/sh
cd /var/www/GitIgnoreApi
source env/bin/activate
git clone https://github.com/github/gitignore
gunicorn -w 4 -b 0.0.0.0:8000 App:api_app