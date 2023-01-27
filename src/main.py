# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from compte import CompteEpargne, CompteCourant
from fonctions import *
from constants import PRCT_AGIOS, PRCT_INTERET
import time
import random
import sqlite3


if __name__ == '__main__':
    start_app = True #boucle quand le client s'est identifié

    db_test = "first_try.db"
    my_db = opendb(db_test)
    bd_con = my_db[0]
    db_cur = my_db[1]
    if not table_exist('Client', my_db):
        db_cur.execute("CREATE TABLE Client(numero_compte integer NOT NULL auto_increment primary key,nom varchar(35) NOT NULL DEFAULT '')")
        db_cur.execute("INSERT INTO Client(numero_compte,nom) VALUES (1,'ADMIN')")
    if not table_exist('Compte', my_db):
        db_cur.execute("CREATE TABLE Compte(nom_proprio varchar(35) NOT NULL DEFAULT '', numero_compte integer, est_epargne varchar(1) NOT NULL DEFAULT 'T', solde float DEFAULT 0, overdraft_limit float DEFAULT 0, pourcentage_agios float DEFAULT 0.1, pourcantage_interet float DEFAULT 0.05, FOREIGN KEY(numero_compte) REFERENCES client(numero_compte))")
        db_cur.execute("INSERT INTO Compte(nom_proprio, numero_compte, est_epargne , solde, overdraft_limit, pourcentage_agios , pourcantage_interet) VALUES ('ADMIN',1,0 , 0, -1000, 0.1, 0.05)")
    bd_con.commit()
    print('Bonjour, \nBienvenue a la A.new-BANK !\n\n')
    etat_client = check_if_client_is_new() # Menu Principal
    if etat_client == 1: # a un compte et veut se connecter
        pass

    elif etat_client == 2: # a deja un compte et veut en creer un autre
        pass


    elif etat_client == 3: #nouveau client veut creer un compte
        print("\n\nBienvenue dans l'assistant de création de compte.\nNous allons maintenant rassembler les information nesessaires a la création de votre compte.")
        nom_client = input('Veuillez entrer votre nom : ').upper()
        est_epargne = type_compte()
        if est_epargne == 0: #JE VEUX REVENIR AU MENU DE CONNEXION
            print('JE VEUX REVENIR AU MENU DE CONNEXION')
            pass

        elif est_epargne == 1: # JE VEUX CREER UN COMPTE COURANT
            overdraft_limit = choose_overdraft_limit()
            print(f'Vous avez choisis une limite de découvert à {overdraft_limit}.')
            print(f'Pour chaque opération ammenant a un solde négatif des agios vous seront pris a hauteur de {PRCT_AGIOS * 100}% de votre nouveau solde !')
            print('Toutes les informations ont été enregistrée, nous procedons a la création de votre compte ...')



            rq_nv_client = f"INSERT INTO Client (nom, numero_compte) VALUES ('{nom_client.upper()}', NULL)"
            db_cur.execute(rq_nv_client)
            bd_con.commit()

            rq_nv_compte = f"INSERT INTO Compte(nom_proprio, est_epargne , solde, overdraft_limit, pourcentage_agios , pourcantage_interet) VALUES ('{nom_client.upper()}',0 , 0,{overdraft_limit}, {PRCT_AGIOS}, {PRCT_INTERET})"
            db_cur.execute(rq_nv_compte)
            bd_con.commit()
            pass

        elif est_epargne == 2: # JE VEUX CREER UN COMPTE EPARGNE
            pass

        else :
            print('LA VARIABLE EST_EPARGNE RETOURNÉ PAR type_compte() a pris une valeur non gérée.')
            pass


    else:
        print('LA VARIABLE ETAT_CLIENT RETOURNÉ PAR check_if_client_is_new() a pris une valeur non gérée.')
        pass


    while start_app == True:
        nom_proprio = input('Veuillez entrer Votre nom : ')
        numero_compte = input('Veuillez entrer votre numero de compte : ')

        # nouveau client
        '''
        rq_nv_cli = f"""INSERT INTO Client (nom_client, numero_compte) VALUES ('{nom_proprio.upper()}', '{numero_compte}') """
        db_cur.execute(rq_nv_cli)
        bd_con.commit()
        '''

        if input('0 pour quiter | 1 pour retourner a la connexion : ') == '0':
            db_cur.close()
            start_app = False
