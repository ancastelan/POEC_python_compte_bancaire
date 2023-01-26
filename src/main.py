# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from compte import CompteEpargne, CompteCourant
from fonctions import account_exist, opendb, table_exist,check_if_client_is_new,type_compte
import sqlite3


if __name__ == '__main__':
    start_app = True #boucle quand le client s'est identifié

    db_test = "first_try.db"
    my_db = opendb(db_test)
    bd_con = my_db[0]
    db_cur = my_db[1]
    if not table_exist('Client', my_db):
        db_cur.execute("CREATE TABLE Client(nom, numero_compte)")
    if not table_exist('Compte', my_db):
        db_cur.execute("CREATE TABLE Compte(nom_proprio, numero_compte, est_epargne, solde, overdraft_limit, pourcentage_agios, pourcantage_interet)")

    print('Bonjour, \nBienvenue a la A.new-BANK !\n\n')
    etat_client = check_if_client_is_new()
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
