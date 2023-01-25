# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from compte import CompteEpargne, CompteCourant
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






if __name__ == '__main__':











    print("Let's start coding our bank application !")
    print('Bonjour, \nBienvenue a la A.new-BANK !\n\n')
    nom_proprio = input('Veuillez entrer Votre nom : ')

    pass