import pytest
from random import randrange
from .compte import CompteEpargne

@pytest.mark.ce
class TestCompteEpargne():

    @pytest.fixture
    def compte_epargne(self):
        """ Default CE Account. """
        return CompteEpargne("Username")

    def test_CompteEpargne_a_un_solde_a_zero_par_defaut(self, compte_epargne:CompteEpargne) -> None:
        """ By default, a newly created account should have 0 €. """
        assert compte_epargne.solde == 0

    def test_CompteEpargne_versement_retrait(self,compte_epargne:CompteEpargne):
        montant :int = 150
        compte_epargne.versement(montant)
        compte_epargne.retrait(montant)
        assert compte_epargne.solde == 7.875

    def test_ce_appliquer_interet_versement(self):
        """regular case : interet applied after versement"""
        montant: int = 150
        compte_epargne = CompteEpargne("username")
        compte_epargne.versement(montant)
        assert compte_epargne.solde == 157.5

    def test_ce_appliquer_interet(self):
        """regular case : interet applied after versement AND retrait"""
        montant_V: int = 350
        montant_R: int = 150
        compte_epargne = CompteEpargne("username")
        compte_epargne.versement(montant_V)
        compte_epargne.retrait(montant_R)
        assert compte_epargne.solde == 228.375

    def test_ce_no_overdraft(self):
        """Check if solde after retrait is overdraft_limit;
        assert that your solde cannot """
        montant: int = 250
        compte_epargne = CompteEpargne("username")
        compte_epargne.versement(150)
        with pytest.raises(Exception):
            compte_epargne.retrait(montant)

