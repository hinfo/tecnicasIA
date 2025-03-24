# Atividades Avaliativas

## Métodos de Busca

### Envio e data de entrega
O trabalho deve ser disponibilizado no GitHub pessoal do aluno ou da dupla e o link do repositório do trabalho deve ser enviado para alexz@ufn.edu.br no dia 25/03/2025 até as 18h.

### Enunciado

1) Individual ou em duplas, construir uma apresentação do tipo Power Point que trate do seguinte:
    - O que são métodos de busca
    - Para que servem os métodos de busca
    - As categorias de métodos de busca e suas aplicações 
    - Da modelagem do seguinte problema
        - Há um labirinto (tamanho NxN definido pelo usuário), com M obstáculos (definido pelo usuário), com uma SAÍDA (linha e coluna sorteados). Contudo, este labirinto possui 2 ENTRADAS (linha e coluna sorteadas para cada entrada). Este problema está no repositório de solução da disciplina via o pacote do professor Jomi Hübner. O desafio é fazer com que cada entrada utilize um método de busca definido pelo usuário e o programa gere a solução para cada entrada, comparando as soluções.

2) Individual ou em dupla, construir o programa da modelagem anterior, via o pacote do professor Jomi Hübner. Sugestão é ter como referência o problema já implementado do Labirinto com Obstáculos.

# Respostas:
## O que são métodos de busca
São técnicas utilizada para construção de Sistemas de Comportamento Inteligente que possibillitam a resolução de problemas utilizando o auxílio de uma base de conhecimento, o raciocínio automatizado e aprendizado de máquina
## Para que servem os métodos de busca
Serve para resolver problemas para determinar os passos até a solução final e no auxílio de reconhecimento de padrões

## As categorias de métodos de busca e suas aplicações
- Busca cegas ou de força bruta: Não se sabe o melhor caminho ou não tem dica
   - Utiliza busca por largura/amplitude ou profundidade
- Informados ou heurísticos: 
   - Quando se possui uma informação priveligiada (dica)

## Modelagem labirinto
### Classes, atributos, tipos
Labirinto: matrizNxN de inteiros
Obstáculos: M inteiros
Entrada:
    - linhaEntrada
    - colunaEntrada
Saída:
    - linhaSaidasorteada
    - colunaSaida

### Estados:

- inicial: Matriz inicializada com 0, linhaEntrada, colunaEntrada, linhaSaida e colunaSaida sorteadas   
- final: linhaEntrada == linhaSaida && colunaEntrada == colunaSaida

#### Visitados:
- Estrutura onde serão armazenados os estados já visitados e uma boa forma de guardar é utilizando uma tabela Hash (hash set)

### Métodos de validação:
- jaFoiVisitado -> Verifica se está na estrutura dos  visitados
- ehValido -> valida se pode ocupar aquele estado
- ehMeta -> Valida se é o destino final

### Regras de Transição:
**Métodos da classe:**

- moverParaDireita
- moverParaEsquerda
- moverParaCima
- moverParaBaixo
    

    
        

