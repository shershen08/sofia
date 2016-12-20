#!/usr/bin/env python
# encoding: utf-8
# by masterzh


import time

from manage import db, Memory


while True:
    with open('/proc/meminfo', 'r') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    used = total - free - buffers - cache
    # print used/1024

    db.session.add(Memory(used / 1024, int(time.time())))
    db.session.commit()

    time.sleep(3)
