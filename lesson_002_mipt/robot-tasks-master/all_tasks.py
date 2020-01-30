#!/usr/bin/python3

import sys

from pyrob.api import run_tasks

if __name__ == '__main__':
    res = run_tasks(headless=True)
    sys.exit(0 if res else -1)
