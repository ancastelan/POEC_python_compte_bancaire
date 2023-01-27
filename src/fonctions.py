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

def check_if_client_is_new(): #MENU DE CONNEXION/PRINCIPAL
    statut_client = 0
    while statut_client != 1 or statut_client != 2 or statut_client != 3:
        print("""
-------------------------------------------------------------------------------
1) Vous voulez acceder a un de vos comptes
2) Vous etes deja detenteur d'un compte et vous voulez en creer un autre
3) Vous etes un nouveau client
-------------------------------------------------------------------------------
        """)
        try:
            statut_client = int(input('Entrez le numero de votre choix : '))
            return statut_client

        except(ValueError):
            print("Veuillez entrer 1, 2 ou 3")


# Fonctions necessaires a la création/modification de compte
def type_compte():
    choix_type_compte = 0
    while choix_type_compte != 1 or choix_type_compte != 2 or choix_type_compte != 0:
        print("""
-------------------------------------------------------------------------------
1) Vous voulez creer un compte courant
2) Vous voulez creer un compte epargne
0) Pour revenir au menu principal
-------------------------------------------------------------------------------
                """)
        try:
            choix_type_compte = int(input('Entrez le numero de votre choix : '))
            if choix_type_compte == 1 or choix_type_compte == 2 or choix_type_compte == 0:
                return choix_type_compte
            else:
                print("Veuillez entrer 1, 2 ou 0")

        except ValueError:
            print("Veuillez entrer 1, 2 ou 0")


def choose_overdraft_limit():
    client_ok = False
    while not client_ok:
        try:
            overdaft_limit = int(input("veuillez entrer une limite de découvert (MAX 2000) : "))
            if -2000 <= overdaft_limit <= 2000:
                return overdaft_limit
            else:
                print('Vous ne pouvez pas depasser 2000€ de découvert')
        except:
            print('Veuillez entrer une somme !\n')

