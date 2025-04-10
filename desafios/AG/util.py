import random
from re import U

class Util:
    letras = "abcdefghijklmnopqrstuvwxyz"
    tamanho_letras = len(letras)
    cidades = "123456789"
    tamanho_cidades = len(cidades)
    
    @staticmethod
    def gerar_palavra(n):     
        palavra = ''

        for i in range(n):
            palavra += Util.letras[random.randrange(Util.tamanho_letras)]
        
        return palavra
    
    @staticmethod
    def gerar_rota(n):
        sample = random.sample(range(1, 10), 9)
        rota =  "".join([str(i) for i in sample])

        return rota