#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

DEBUG = True
# DEBUG = False
website = "http://127.0.0.1"
# salt api config
salt_cdn_url = 'https://192.168.111.142/'
salt_center_url = "https://10.1.1.215:1559/"
salt_api_url = "https://10.1.1.215:1559/"
salt_user = "saltapi"
salt_api_user = "saltapi"
salt_passwd = 'rzjf_salt_api'
salt_api_pass = "rzjf_salt_api"

# zabbix api info
# zabbix_on = False
zabbix_on = True
zabbix_url = 'http://172.16.200.11/'
zabbix_user = 'Admin'
zabbix_passwd = 'Rzjf@123./*'

pxe_url_api = "http://192.168.115.180:8888/clone/"
Environment = ['prod', 'stag', 'test', 'dev', 'qa']

# salt auth
auth_content = ['vi', 'vim', 'poweroff', 'shutdown', 'rm', 'init', 'reboot', 'useradd', 'userdel', 'userhelper',
                'usermod', 'usernetctl', 'users', "echo"]

# LOGIN_URL = "http://auth.jumeird.com/api/login/?camefrom=jmops"
app_key = "&app_key=e00acc666d4911e3a268fa163e73f605"
app_name = "&app_name=jmops&key=1"
auth_url = "http://auth.xxx.com/"
auth_key = "e00acc666d4911e3a268fa163e73f605"

# 跳板机使用
springboard = "ea76757b5d91c5c96bf58500a5f7eda0"

REDIS_HOST = "10.1.1.142"
REDIS_PORT = 6370
REDIS_DB = 1


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'voilet_cmdb_v1',  # Or path to database file if using sqlite3.
        'NAME': 'cmdb_v2',  # Or path to database file if using sqlite3.
         'USER': 'cmdb',
         'PASSWORD': 'Cmdb*00369',  # Not used with sqlite3.
        'HOST': '10.1.1.142',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        "OPTIONS": {
            "init_command": "SET foreign_key_checks = 0;",
        },
    },

    # 'slave': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'salt',
    #     'USER': 'root',
    #     'PASSWORD': 'wanghui',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}

# from pymongo import MongoClient
# client = MongoClient('localhost',27017)
# db = client['config_center']
# salt tornado api
# salt_tornado_api = "http://10.1.2.21:8888/api/"

swan_url = "http://10.1.1.142:8888/swan_api/"
websocket_url = "10.1.1.142:8888/websocket"
ops_mail = "hejianxiong@51rz.com"
