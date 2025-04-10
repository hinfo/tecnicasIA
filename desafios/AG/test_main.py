
from unittest import TestCase
from ag import Cromossomo


class TestMain(TestCase):
    def test_main(self):
        lista = []
        lista.append(Cromossomo("asfas", "andre"))
        lista.append(Cromossomo("xtfts", "andre"))
        crom = Cromossomo("xtfts","andre")
        assert crom in lista