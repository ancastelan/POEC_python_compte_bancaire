"""
    Unit testing for Compte Courant.
"""

from random import randrange
import pytest
from src.compte import CompteCourant

@pytest.mark.cc
class TestCompteCourant():
    """ Unit testing for a Compte Courant. """

    @pytest.fixture
    def compte_courant(self) -> CompteCourant:
        """ Generate a default CC. """
        return CompteCourant("Username")

    def test_cc_a_un_solde_a_zero_par_defaut(self, compte_courant
    :CompteCourant) -> None:
        """ By default, a newly created CC has no money in it. """
        # assert compte_courant.nom_proprietaire == "Username"
        assert compte_courant.solde == 0

    def test_cc_un_versement(self,compte_courant :CompteCourant) ->\
            None:
        """ If I add money to my account, it should be there. """

        # arrange
        montant = 150

        # act
        compte_courant.versement(montant)

        # assert
        assert compte_courant.solde == montant

    def test_cc_plusieurs_versements(self,compte_courant
    :CompteCourant) -> None:
        """
            If I add several times money to my account,
            everything should be there.
        """

        # arrange
        montant = 150
        nb_versements = randrange(2, 10)

        # act
        for _ in range(nb_versements):
            compte_courant.versement(montant)

        # assert
        assert compte_courant.solde == nb_versements*montant

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_versement_negatif_genere_exception(self,
                  compte_courant :CompteCourant, montant :int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.versement(montant)

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_retrait_negatif_genere_exception(self,
                  compte_courant :CompteCourant, montant :int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.retrait(montant)

    def test_cc_retrait_trop_eleve_genere_exception(self,
                  compte_courant: CompteCourant) -> None:
        """ Assert that you cannot take money you do not have. """
        montant: int = 150

        compte_courant.versement(montant)
        # act and assert
        with pytest.raises(Exception):
            compte_courant.retrait(montant + montant)

    def test_cc_affichage(self, compte_courant :CompteCourant):
        """ Check object representation """
        assert 'CompteCourant - Solde : 0' in str(compte_courant)

    #renommer "overderaft_limit" par ta variable de limite d'authorisation de decouvert
    def test_cc_overdraft(self):
        """Check if solde after retrait is overdraft_limit;
        assert that your solde cannot """
        montant: int = 250
        compte_courant = CompteCourant("username", overdraft_limit=-200)
        with pytest.raises(Exception):
            compte_courant.retrait(montant)

    def test_cc_appliquer_agios(self):
        """regular case : agios applied in case of solde < 0"""
        montant: int = 150
        compte_courant = CompteCourant("username", overdraft_limit=-1000)
        compte_courant.retrait(montant)
        assert compte_courant.solde == -165

    def test_cc_appliquer_agios(self):
        """regular case : agios applied in case of solde < 0"""
        montant: int = 520
        compte_courant = CompteCourant("username", overdraft_limit=-1000)
        compte_courant.retrait(montant)
        assert compte_courant.solde == -572

    def test_cc_appliquer_agios(self):
        """regular case : agios applied in case of solde < 0"""
        montant: int = 420
        compte_courant = CompteCourant("username", overdraft_limit=-1000)
        compte_courant.retrait(montant)
        assert compte_courant.solde == -462


    def test_cc_appliquer_agios_for_versement_and_retrait1(self):
        """regular case : agios applied in case of solde < 0 for retrait() AND versement()"""

        montant_R: int = 500
        montant_V: int = 150
        compte_courant = CompteCourant("username", overdraft_limit=-1000)
        compte_courant.retrait(montant_R)
        compte_courant.versement(montant_V)
        assert compte_courant.solde == -440

    def test_cc_appliquer_agios_for_versement_and_retrait2(self):
        """regular case : agios applied in case of solde < 0 for retrait() AND versement()"""
        montant_V1: int = 150
        montant_R: int = 400
        montant_V2: int = 270

        compte_courant = CompteCourant("username", overdraft_limit=-1000)
        compte_courant.versement(montant_V1)
        compte_courant.retrait(montant_R)
        compte_courant.versement(montant_V2)
        assert compte_courant.solde == -5.5







