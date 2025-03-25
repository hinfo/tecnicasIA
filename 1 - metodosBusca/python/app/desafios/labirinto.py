import random
from tkinter import S

from app.core.busca.busca_largura import BuscaLargura
from app.core.busca.busca_profundidade import BuscaProfundidade
from app.core.busca.estado import Estado
from app.core.busca.heuristica import Heuristica
from app.core.busca.mostra_status_console import MostraStatusConsole


class Labirinto(Estado, Heuristica):
    quantidade_obstaculos = 0
    entrada_symbol = "E"
    saida_symbol = "S"
    obstaculo_symbol = "@"
    vazio_symbol = "O"

    def __init__(
        self,
        matriz=None,
        linha_entrada=None,
        coluna_entrada=None,
        linha_saida=None,
        coluna_saida=None,
        op=None,
        dimensao=None,
        porcentual_obsstaculos=None,
    ):
        self.path = {}
        if porcentual_obsstaculos is not None:
            self.quantidade_obstaculos: int = (
                (dimensao * dimensao) * porcentual_obsstaculos / 100
            )
        if matriz is not None:
            self.matriz = matriz
            self.linha_entrada = linha_entrada
            self.coluna_entrada = coluna_entrada
            self.linha_saida = linha_saida
            self.coluna_saida = coluna_saida
            self.op = op
        elif dimensao is not None:
            self.matriz = [[self.vazio_symbol for _ in range(dimensao)] for _ in range(dimensao)]
            self.op = op
            entrada = random.randint(0, dimensao * dimensao - 1)
            saida = random.randint(0, dimensao * dimensao - 1)
            while entrada == saida:
                saida = random.randint(0, dimensao * dimensao - 1)
            conta_posicoes = 0
            for i in range(dimensao):
                for j in range(dimensao):
                    if conta_posicoes == entrada:
                        self.matriz[i][j] = self.entrada_symbol
                        self.linha_entrada = i
                        self.coluna_entrada = j
                    elif conta_posicoes == saida:
                        self.matriz[i][j] = self.saida_symbol
                        self.linha_saida = i
                        self.coluna_saida = j
                    elif self.quantidade_obstaculos > 0 and random.randint(0, 3) == 1:
                        self.quantidade_obstaculos -= 1
                        self.matriz[i][j] = self.obstaculo_symbol
                    else:
                        self.matriz[i][j] = self.vazio_symbol
                    conta_posicoes += 1

    def get_descricao(self):
        return (
            "O jogo do labirinto é uma matriz NxM, onde são sorteadas duas peças:\n"
            "\n"
            "peça que representa o portal de entrada no labirinto;\n"
            "peça que representa o portal de saída no labirinto.\n"
            "A Entrada é o portal em que um personagem qualquer inicia no "
            "labirinto e precisa se movimentar até a Saída. "
            "O foco aqui, é chegar na Saída pelo menor número de movimentos (células). "
            "Entretanto, não pode ser nas diagonais."
        )

    def clonar(self, origem):
        return [row[:] for row in origem]

    def eh_meta(self):
        return (
            self.linha_entrada == self.linha_saida
            and self.coluna_entrada == self.coluna_saida
        )

    def custo(self):
        return 1

    def h(self):
        return 0

    def sucessores(self):
        visitados = []
        self.para_cima(visitados)
        self.para_baixo(visitados)
        self.para_esquerda(visitados)
        self.para_direita(visitados)
        return visitados

    def para_cima(self, visitados):
        if (
            self.linha_entrada == 0
            or self.matriz[self.linha_entrada - 1][self.coluna_entrada] == self.obstaculo_symbol
        ):
            return
        mTemp = self.clonar(self.matriz)
        linhaTemp = self.linha_entrada - 1
        colunaTemp = self.coluna_entrada
        mTemp[self.linha_entrada][self.coluna_entrada] = self.vazio_symbol
        mTemp[linhaTemp][colunaTemp] = self.entrada_symbol
        novo = Labirinto(
            mTemp,
            linhaTemp,
            colunaTemp,
            self.linha_saida,
            self.coluna_saida,
            "Movendo para cima",
        )
        if novo not in visitados:
            visitados.append(novo)

    def para_baixo(self, visitados):
        if (
            self.linha_entrada == len(self.matriz) - 1
            or self.matriz[self.linha_entrada + 1][self.coluna_entrada] == self.obstaculo_symbol
        ):
            return
        mTemp = self.clonar(self.matriz)
        linhaTemp = self.linha_entrada + 1
        colunaTemp = self.coluna_entrada
        mTemp[self.linha_entrada][self.coluna_entrada] = self.vazio_symbol
        mTemp[linhaTemp][colunaTemp] = self.entrada_symbol
        novo = Labirinto(
            mTemp,
            linhaTemp,
            colunaTemp,
            self.linha_saida,
            self.coluna_saida,
            "Movendo para baixo",
        )
        if novo not in visitados:
            visitados.append(novo)

    def para_esquerda(self, visitados):
        if self.coluna_entrada == 0:
            return
        mTemp = self.clonar(self.matriz)
        linhaTemp = self.linha_entrada
        colunaTemp = self.coluna_entrada - 1
        mTemp[self.linha_entrada][self.coluna_entrada] = self.vazio_symbol
        mTemp[linhaTemp][colunaTemp] = self.entrada_symbol
        novo = Labirinto(
            mTemp,
            linhaTemp,
            colunaTemp,
            self.linha_saida,
            self.coluna_saida,
            "Movendo para esquerda",
        )
        if novo not in visitados:
            visitados.append(novo)

    def para_direita(self, visitados):
        if self.coluna_entrada == len(self.matriz) - 1:
            return
        mTemp = self.clonar(self.matriz)
        linhaTemp = self.linha_entrada
        colunaTemp = self.coluna_entrada + 1
        mTemp[self.linha_entrada][self.coluna_entrada] = self.vazio_symbol
        mTemp[linhaTemp][colunaTemp] = self.entrada_symbol
        novo = Labirinto(
            mTemp,
            linhaTemp,
            colunaTemp,
            self.linha_saida,
            self.coluna_saida,
            "Movendo para direita",
        )
        if novo not in visitados:
            visitados.append(novo)

    def __eq__(self, other):
        if isinstance(other, Labirinto):
            return self.matriz == other.matriz
        return False

    def __hash__(self):
        estado = "".join(["".join(row) for row in self.matriz])
        return hash(estado)

    def __str__(self):
        resultado = []
        for row in self.matriz:
            resultado.append("\t".join(row))
            resultado.append("\n")
        resultado.append(
            f"Posição Entrada: {self.linha_entrada},{self.coluna_entrada}\n"
        )
        resultado.append(f"Posição Saida: {self.linha_saida},{self.coluna_saida}\n")
        self.path.update(
            {
                (self.linha_entrada, self.coluna_entrada): (
                    self.linha_saida,
                    self.coluna_saida,
                )
            }
        )
        return f"\n{self.op}\n{''.join(resultado)}\n\n"


if __name__ == "__main__":
    in_dimensao = input("Digite a dimensão do labirinto[default:10]: ")
    in_qual_metodo = input(
        "Digite o método de busca (1 - Profundidade, 2 - Largura)[default:1]: "
    )
    in_percentual_obstaculos = input("Digite o percentual de obstáculos[default:10]: ")
    try:
        dimensao = int(in_dimensao) if in_dimensao.count == 0 else 10
        qual_metodo = int(in_qual_metodo) if in_qual_metodo.count == 0 else 1
        percentual_obstaculos = (
            int(in_percentual_obstaculos) if in_percentual_obstaculos.count == 0 else 10
        )
        estado_inicial = Labirinto(
            dimensao=dimensao,
            op="estado inicial",
            porcentual_obsstaculos=percentual_obstaculos,
        )
        nodo = None
        if qual_metodo == 1:
            print("busca em PROFUNDIDADE")
            nodo = BuscaProfundidade(mostra_status_console=MostraStatusConsole()).busca(
                estado_inicial
            )
        elif qual_metodo == 2:
            print("busca em LARGURA")
            nodo = BuscaLargura(mostra_status_console=MostraStatusConsole()).busca(
                estado_inicial
            )
        else:
            print("Método não implementado")
        
        if nodo is None:
            print("Puzzle sem solução!")
        else:
            print(f"Solução:\n{nodo.monta_caminho()}\n\n")
    
    except Exception as e:
        print(f"Problemas ao criar o Puzzle: {e}")
