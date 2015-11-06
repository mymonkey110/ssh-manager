# sm.py
#
# Copyright (c) 2015 Michael Jiang
# This file is part of ssh-manager under
# the MIT License: https://opensource.org/licenses/MIT


import os
import sqlite3
import sys
from tabulate import tabulate
from getpass import getpass

config_db_path = os.path.expanduser("~/.sm/config.db")

hosts = []


def init_config_db():
    """
    Initialize config
    create sqlite db in {home}/.sm/config.db
    """
    with sqlite3.connect(config_db_path) as conn:
        print("Initializing config db...")
        db_file = file("config.schema")
        schema = db_file.read()
        conn.executescript(schema)
        print("Initialize completed!")


def show_host():
    """
    Show host entry list
    """
    with sqlite3.connect(config_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id,alias,hostname,username FROM host")
        data = cursor.fetchall()
        if len(data) > 0:
            table = [row for row in data]
            print(tabulate(table, headers=["ID", "Alias", "Hostname", "Username"]))
        else:
            print("No host found")


def add_host():
    """
    Add host to db
    """
    hostname = raw_input("hostname(eg:192.168.199.100):")
    username = raw_input("username(default:root):") or 'root'
    password = getpass("password:")
    alias = raw_input("alias:")

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
        else:
            print("Add host:%s success!" % hostname)
        cursor.close()


def remove_host():
    """
    remove host from db
    """
    host_id = raw_input("input host id you want delete:")
    if int(host_id) > 0:
        with sqlite3.connect(config_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM host WHERE id=" + host_id)
            if cursor.rowcount != 1:
                print("host not found")
    else:
        print("bad input")


def init():
    if not os.path.exists(config_db_path):
        init_config_db()


def show_usage():
    print("""
    sm [show|add|remove]
    s | show    show host list
    a | add     add host to db
    r | remove  remove host from db
    """)


if __name__ == "__main__":

    init()

    if len(sys.argv) > 1:
        op = sys.argv[1]
        if op in ['s', 'show']:
            show_host()
        elif op in ['a', 'add']:
            add_host()
        elif op in ['r', 'remove']:
            remove_host()
        else:
            show_usage()
    else:
        show_usage()
