# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from compte import CompteEpargne, CompteCourant
from fonctions import account_exist, opendb, table_exist
import sqlite3
'''
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Python A-new BANK")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()

fen.show()
app.exec_()
'''
#--------------------------------------------------------------------------

if __name__ == '__main__':
    db_test = "first_try.db"
    my_db = opendb(db_test)
    bd_con = my_db[0]
    db_cur = my_db[1]
    if not table_exist('Client', my_db):
        db_cur.execute("CREATE TABLE Client(nom_proprio, numero_compte)")
    if not table_exist('Compte', my_db):
        db_cur.execute("CREATE TABLE Compte(numero_compte, est_epargne, solde, overdraft_limit, pourcentage_agios, pourcantage_interet)")





    print("Let's start coding our bank application !")
    print('Bonjour, \nBienvenue a la A.new-BANK !\n\n')
    nom_proprio = input('Veuillez entrer Votre nom : ')
    numero_compte = input('Veuillez entrer votre numero de compte : ')
    if not account_exist(nom_proprio, numero_compte, my_db):
        rq_nv_cli = f"""INSERT INTO Client (nom_proprio, numero_compte) VALUES ('{nom_proprio.upper()}', '{numero_compte}') """
        db_cur.execute(rq_nv_cli)
        bd_con.commit()


