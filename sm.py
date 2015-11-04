# sm.py
#
# Copyright (c) 2015 Michael Jiang
# This file is part of ssh-manager under
# the MIT License: https://opensource.org/licenses/MIT

import os
import sqlite3
import sys

config_db_path = os.path.expanduser("~/.sm/config.db")

hosts = []


def check_db_exist():
    return os.path.exists(config_db_path)


def init_config_db():
    with sqlite3.connect(config_db_path) as conn:
        print("Initializing config db...")
        db_file = file("config.db.schema")
        schema = db_file.read()
        conn.executescript(schema)
        print("Initialize completed!")


def load_data():
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id,alias,hostname,password,gmt_create,gmt_modify FROM host")
        for row in cursor.fetchall():
            print row


def show_host():
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id,alias,hostname,password,gmt_create,gmt_modify FROM host")
        for row in cursor.fetchall():
            print row


def add_host(hostname, password, username="root", alias=None):
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        if alias:
            sql = "insert into host(hostname,username,password,alias) values('%s','%s','%s','%s')" % (
                hostname, username, password, alias)
        else:
            sql = "insert into host(hostname,username,password) values('%s','%s','%s')" % (hostname, username, password)

        cursor.execute(sql)
        if cursor.rowcount != 1:
            print("Add host:%s failed." % hostname)
        cursor.close()


def init():
    if not check_db_exist():
        init_config_db()
    else:
        load_data()


if __name__ == "__main__":
    init()

    if len(sys.argv) > 1:
        if sys.argv[1] == "show":
            show_host()
        if sys.argv[1] == "add":
            add_host(hostname=sys.argv[2], username=sys.argv[3], password=sys.argv[4])
