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


def show_host():
    """
    Show host entry list
    :return: None
    """
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id,alias,hostname,username FROM host")
        data = cursor.fetchall()
        if len(data) > 0:
            print("id | alias | hostname | username")
            print("-- | ----- | ------------- | ----")
            for row in data:
                _id, alias, hostname, username = row
                print("%2d | %5s | %15s | %4s" % (_id, alias, hostname, username))
        else:
            print("No host found")


def add_host(hostname, password, username="root", alias=None):
    """
    Add host to db
    :param hostname: hostname
    :param password: ssh password
    :param username: ssh username,default 'root'
    :param alias: host alias
    :return: None
    """
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        if alias:
            sql = "insert into host(hostname,username,password,alias) values('%s','%s','%s','%s')" % (
                hostname, username, password, alias)
        else:
            sql = "insert into host(hostname,username,password) values('%s','%s','%s')" % \
                  (hostname, username, password)

        cursor.execute(sql)
        if cursor.rowcount != 1:
            print("Add host:%s failed." % hostname)
        cursor.close()


def remove_host(alias, _id):
    if not alias and not _id:
        print("please assign host alias or id")

    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        if alias:
            cursor.execute("DELETE FROM host WHERE alias=" + alias)
        else:
            cursor.execute("DELETE FROM host WHERE id=" + _id)


def init():
    if not check_db_exist():
        init_config_db()


def show_usage():
    print("""
    sm [show|add|remove]
    show    show host list
    add     add host to db
    remove  remove host from db
    """)


if __name__ == "__main__":
    init()

    if len(sys.argv) > 1:
        if sys.argv[1] == "show":
            show_host()
        if sys.argv[1] == "add":
            add_host(hostname=sys.argv[2], username=sys.argv[3], password=sys.argv[4])
    else:
        show_usage()
