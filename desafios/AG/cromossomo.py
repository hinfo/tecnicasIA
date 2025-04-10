class Cromossomo:

    def __init__(self, valor, estado_final):
        self.valor = valor
        self.aptidao = self.calcular_aptidao(estado_final)
    
    def calcular_aptidao(self, estado_final):
        nota = 0
        for i in range(len(estado_final)):
            if i + 1 >= len(self.valor):
                continue

            if self.valor[i] > self.valor[i + 1]:
               nota += 10
               
            if self.valor[i] == estado_final[i]:
                nota -= 10
            
            if estado_final.count(self.valor[i]) > 1:
                nota += 20
            
        return nota
    
    def __eq__(self, other):
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False
    
    def __gt__(self, other):
        return self.aptidao <= other.aptidao
    
    def __str__(self):
        return f"rota={self.valor}, score={self.aptidao}"