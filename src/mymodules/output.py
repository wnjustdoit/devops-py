# !/usr/bin/python3

import sys


def output_all(msg, resp=0, exit=False):
    print(msg if resp == 0 else f'{msg}, status_code: {resp}')
    if exit:
        sys.exit()
    else:
        sys.stdout.flush()


def output_strict(msg, resp):
    if resp != 0:
        output_error(msg, resp)
    else:
        output_std(msg)


def output_relaxed(msg, resp):
    if resp != 0:
        output_warn(msg, resp)
    else:
        output_std(msg)


def output_error(msg, resp=-1, exit=True):
    output_all(f'ERROR: {msg}', resp, exit)


def output_warn(msg, resp=-1):
    output_all(f'WARN: {msg}', resp)


def output_std(msg):
    output_all(f'INFO: {msg}')
