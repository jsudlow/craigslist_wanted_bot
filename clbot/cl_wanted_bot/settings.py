# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cl_wanted_bot'
DOWNLOAD_DELAY = 2 
SPIDER_MODULES = ['cl_wanted_bot.spiders']
NEWSPIDER_MODULE = 'cl_wanted_bot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
