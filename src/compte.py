import uuid
from abc import ABC


# import constants

class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nomProprietaire, **kwargs):
        self.nom_proprietaire = nomProprietaire
        self.solde: float = 0
        self.numero_compte = uuid.uuid1()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def retrait(self, montant: int = 0):
        '''
            substract an ammount (as an int) to solde
        '''
        if 0 < montant <= self.solde:
            self.solde -= montant
        else:
            raise Exception('you cannot take money under your overdraft limit.')

    def versement(self, montant: int = 0):
        '''
            add an ammount (as an int) to solde
        '''
        if montant > 0:
            self.solde += montant
        else:
            raise Exception('you cannot add a negative amount')

    def afficherSolde(self):  # pragma: no cover
        print(self)

    def __repr__(self):
        if type(self) == CompteCourant:
            nom_compte = CompteCourant.__name__
            return '{nom} - Solde : {test}'.format(nom=nom_compte, test=self.solde)
        elif type(self) == CompteEpargne:
            nom_compte = CompteEpargne.__name__
            return '{nom} - Solde : {test}'.format(nom=nom_compte, test=self.solde)
        else:
            raise Exception('this is not a CompteCourant or a CompteEpargne')


class CompteCourant(Compte):
    '''
    classe compte courant :
    retrait possible jusqu'a "overdraft_limit"
    application des agios si le solde est negatif après chaque opérations
    '''

    def __init__(self, nomProprietaire, **kwargs):
        self.overdraft_limit = 0
        self.pourcentage_agios = 0.1
        super().__init__(nomProprietaire, **kwargs)

    def retrait(self, montant: int = 0):
        print(self)
        if montant > 0:
            if self.solde - montant > self.overdraft_limit:
                self.solde -= montant
                if self.solde < 0:
                    self.appliquer_agios()
                    print(self)
            else:
                raise Exception('you cannot take money under your overdraft limit.')
        else:
            raise Exception('You cannot take a negative amount of money')

    def versement(self, montant=0):
        print(self)
        if montant > 0:
            self.solde += montant
            if self.solde < 0:
                self.appliquer_agios()
                print(self)
        else:
            raise Exception('you cannot add a negative amount')

    def appliquer_agios(self):
        '''
        substract to solde a percentage of itself based on pourcentage_agios constant
        '''
        if self.solde < 0:
            self.solde = self.solde - (-self.solde * self.pourcentage_agios)


# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------


class CompteEpargne(Compte):
    '''
        classe compte epargne :
        retrait impossible si solde apres opération < 0
        application des interets après chaque opérations
    '''

    def __init__(self, nomProprietaire, **kwargs):
        self.pourcentage_interet = 0.05
        super().__init__(nomProprietaire, **kwargs)

    def versement(self, montant: int = 0):
        print(self)
        if montant > 0:
            self.solde += montant
            self.appliquer_interets()
            print(self)
        else:
            raise Exception('You cannot add a negative amount of money')

    def retrait(self, montant: int = 0):
        print(self)
        if montant > 0:
            if self.solde - montant > 0:
                self.solde -= montant
                self.appliquer_interets()
                print(self)
            else:
                raise Exception("you cannot take money you don't have")
        else:
            raise Exception('You cannot take a negative amount of money')

    def appliquer_interets(self):
        # self.solde += self.solde * pourcentage_interet ?
        self.solde = self.solde + (self.solde * self.pourcentage_interet)
