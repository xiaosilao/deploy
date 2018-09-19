#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#
import uuid
import random
import time


def make_uuid():
    """
    :return:
    """
    salt_key = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()_'
    symbol = '!@$%^&*()_'
    salt_list = []
    for i in range(60):
        salt_list.append(random.choice(salt_key))
    for i in range(4):
        salt_list.append(random.choice(symbol))
    salt = "%s%s%s" % (''.join(salt_list), time.time(), uuid.uuid4())
    uuid_data = str(uuid.uuid3(uuid.NAMESPACE_DNS, salt))
    return uuid_data
