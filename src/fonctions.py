import sqlite3
import sqlite3 as lite
import sys
import Exeption


def opendb(db):
    try:
        conn = lite.connect(db)
    except lite.Error:
        print("Error open db.\n")
        return False
    cur = conn.cursor()
    return [conn, cur]


def table_exist(nom_table, db):
    ma_req = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{nom_table}'; "
    cur = db[1]
    cur.execute(ma_req)

    if cur.fetchone()[0] == 1:
        return True
    else:
        return False


def account_exist(nom_proprio, numero_compte, db):
    ma_req = f"""SELECT numero_compte FROM Client WHERE numero_compte ='{numero_compte}'"""
    cur = db[1]

    account_list = cur.execute(ma_req).fetchall()
    if len(account_list) == 0:
        return False
    else:
        return True







