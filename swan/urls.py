#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#

from django.conf.urls import patterns, url

"""
项目配置自动化发布
"""
urlpatterns = patterns('',
                       url(r'push/$', "swan.views.swan_push"),
                       url(r'release/$', "swan.views.swan_release"),
                       url(r'log/(?P<uuid>[^/]+)/$$', "swan.views.SwanSelectLog", name="SwanSelectLog"),
                       url(r'swan_select/$', "swan.views.swan_select"),
                       url(r'^swan_select_myfrom/$', "swan.views.swan_select_myfrom"),
                       url(r'^swan_select_botton/$', "swan.views.swan_select_button"),
                       url(r'swan_select_tgt/$', "swan.views.swan_select_tgt"),
                       url(r'^websocket/$', "swan.views.swan_websocket"),
                       url(r'^apply/(?P<uuid>[^/]+)/$', "swan.views.swan_apply"),
                       url(r'^apply/p/$', "swan.views.apply_project"),
                       url(r'^apply/exec/$', "swan.views.apply_auto"),
                       url(r'$', "swan.views.swan_index"),
                       )
