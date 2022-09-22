#! /usr/bin/env python

import functools

from models.account import Account
from models.getconfig import Configure

config = Configure()


def login_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        account = Account(config.username_correct,
                          config.password_correct,
                          config.verification_code)
        account.login_with_verified()
        return func(*args, **kwargs)

    return wrapper



