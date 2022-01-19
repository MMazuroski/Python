# Pontifícia Universidade Católica
# Disciplina de Raciocínio Computacional
# Aluna: MARINA ELIZABETH MAZUROSKI
# Curso: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

import random
pontosParaGanhar = 13

# INSERIR JOGADORES
jogadores = []
while True:
    nome = str(input("Digite nome do(a) jogador(a) ou 'fim': "))
    if nome == "fim":
        if len(jogadores) < 2:
            print("Jogadores insuficientes, insira pelo menos mais 1")
        else:
            break
    else:
        jogadores.append(nome)
print("\nJogadores inseridos.\n")

# ZERAR PONTUAÇÃO DE JOGADORES
cerebrosJogadores = []
for i in jogadores:
    cerebros = 0
    cerebrosJogadores.append(cerebros)

# MOSTRAR PLACAR JOGO
def mostrarPlacarJogo(jogadores, cerebrosJogadores):
        print("Placar jogo:\n")
        print(f'{"Jogadores":^15}|{"Cérebros":^15}')
        for i in range(len(jogadores)):
            print(f'{jogadores[i]:^15}|{cerebrosJogadores[i]:^15}')
        input("\nTecle para continuar... \n")
mostrarPlacarJogo(jogadores, cerebrosJogadores)

# FUNÇÕES RODADA
# INICIALIZAR TODOS OS DADOS PRO TURNO
def inicializarPote():
    poteCompleto = ["Verde", "Verde", "Verde", "Verde", "Verde", "Verde", "Amarelo", "Amarelo", "Amarelo", "Amarelo", "Vermelho", "Vermelho", "Vermelho"]  # [6 Verdes, 4 Amarelos, 3 Vermelhos]
    return poteCompleto

# TIRA DADOS PEGOS DO POTE, RETORNA POTE ATUALIZADO
def atualizarPote(corDado, pote):
    pote.remove(corDado)  # Tira dado que foi pego
    return pote

# ATUALIZA POTE COM MENOS DE 3 DADOS
def atualizarPoteVazio(pote, corDadosCerebros):
    input("Pote com menos de 3 dados")
    print("Pote atual:", pote)
    pote = pote + corDadosCerebros
    print("Pote com dados dos cérebros:", pote)
    return pote

# PEGAR DADOS, RETORNA COR DOS DADOS
def pegarDadosDoPote(pote, cor, faces, corDadosCerebros):
    corAtualizada = []  # Zera variável que atualiza cor dos dados
    if len(pote) < 3 and faces.count('P') < 3:
        pote = atualizarPoteVazio(pote, corDadosCerebros)
    for i in range(3):
        if faces[i] == 'P':  # Checagem de dados que deram "passo" para mantê-los na rodada.
            corAtualizada.append(cor[i])  # Manter cor do dado
        else:  # Pegar novos dados
            corAtualizada.append(random.choice(pote))  # Nova cor de dado
            pote = atualizarPote(corAtualizada[i], pote)
    return corAtualizada, pote

# MOSTRAR DADOS SORTEADOS
def mostrarDadosSorteados(cor):
    print("Seus dados são das cores:", cor[0], ", ", cor[1], " e ", cor[2])

def mostrarDadosPote(pote):
    print("Dados restantes no pote: ", pote.count("Verde"), "verde(s), ", pote.count("Amarelo"), "amarelo(s) e ", pote.count("Vermelho"), "vermelho(s). \n")
    #print(f'{" ":5}{cor[0]}, {cor[1]} e {cor[2]}.')

# ROLAR DADOS, RETORNA RESULTADO DAS FACES
def rolarDados(cor):
    input("Tecle para rolar os dados...\n")
    faces = [] # Zera variável que armazena resultado dos dados
    verde = ("CPCTPC")
    amarelo = ("TPCTPC")
    vermelho = ("TPTCPT")
    for i in range(3):
        if cor[i] == 'Verde':
            rolagem = random.choice(verde)
        elif cor[i] == 'Amarelo':
            rolagem = random.choice(amarelo)
        else:
            rolagem = random.choice(vermelho)
        faces.append(rolagem)
    return faces

# SOMA E MOSTRA RESULTADO DO PLACAR DO JOGADOR
def atualizarPlacarJogador(faces, placar):
    placar[0] += faces.count("C") # Cérebros
    placar[1] += faces.count("T") # Tiros
    placar[2] = faces.count("P") # Passos
    return placar

# MOSTRA PONTUAÇÃO
def mostrarResultado(cor, faces):
    print("Dados rolados, você tirou as seguintes faces: ")
    for i in range(3):
        print(f'{cor[i]:>10} -> {faces[i]:}')
    input("Tecle para continuar...\n")
    # print(f'Cérebros: {faces.count("C"):5}')
    # print(f'Tiros: {faces.count("T"):8}')
    # print(f'Passos: {faces.count("P"):7} \n')

# MOSTRA PLACAR DA RODADA
def mostrarPlacarJogador (placar):
    print("Placar atual da rodada:")
    print(f'Cérebros: {placar[0]:5}')
    print(f'Tiros: {placar[1]:8}')
    print(f'Passos: {placar[2]:7} \n')

# GUARDA COR DOS DADOS COM CÉREBROS - CASO DE ACABAR DADOS NO POTE
def guardarCorCerebros(cor, faces, corDadosCerebros):
    for i in range(3):
        if faces[i] == "C":
            corDadosCerebros.append(cor[i])
    return corDadosCerebros

# CHECAGEM DOS CÉREBROS E TIROS
def checagemPlacar(placar, faces, placarInicio):
    if placar[1] >= 3:
        input("Você levou mais do que 3 tiros! Você perdeu todos os cérebros da rodada e perdeu a vez!\n")
        placar[0] = placarInicio # Remove cérebros adquiridos na rodada
        continuar = "N"
    elif placar[0] >= pontosParaGanhar:
        input("Parabéns, você comeu 13 cérebros!\nSe até o final do turno você for o único a comer 13 ou mais cérebros, você ganha o jogo!\nTecle para continuar...\n")
        continuar = "N"
    else:
        print("Você comeu", faces.count("C"), "cérebro(s), deixou escapar", faces.count("P"),"cérebro(s) e levou", faces.count("T"),"tiro(s).")
        print("No total são", placar[0], "cérebro(s)!")
        if placar[1] > 0:
            print("Cuidado, se levar mais", (3-placar[1]),"tiro(s), você perderá todos os cérebros da rodada!\n")
        continua = input("Quer continuar? [S/N]\n")
        if continua == "N" or continua == 'n':
            print("Não vai continuar\n")
            continuar = "N"
        else:
            continuar = "S"
    return continuar

def rodada(jogador,cerebros):

    print("Vez do(a) jogador(a)", jogador,", iniciando a rodada com", cerebros, "cérebros.\n")
    input("Vamos jogar, tecle para pegar dados do pote! \n")
    # INICIALIZAR PONTUAÇÃO PRA RODADA
    placar = [cerebros, 0, 0]  # Pegar pontuação atual, resetar tiros e passos
    placarInicioRodada = cerebros  # Guarda valor de cérebros antes do início da rodada, para o caso de 3+ tiros
    cor = [0, 0, 0]  # Inicializar variável que armazena cor dos dados
    faces = [0, 0, 0]  # Inicializar variável que armazena resultado das faces após rolagem
    corDadosCerebros = [] # Inicializa variável que guarda cor dos dados com cérebros

    pote = inicializarPote()
    # print("Inicilizando pote...") # Controle pessoal
    # print("pote: ", pote) # Controle pessoal

    while True:

        print("Pegando dados do pote... \n")
        corEpote = pegarDadosDoPote(pote, cor, faces, corDadosCerebros)
        cor = corEpote[0]
        pote = corEpote[1]
        # print("cor: ", cor) # Controle pessoal
        # print("pote atualizado: ", pote) # Controle pessoal

        # input("Mostrando cor e pote") # Controle pessoal
        mostrarDadosSorteados(cor)
        mostrarDadosPote(pote)

        # input("Rolando dados") # Controle pessoal
        faces = rolarDados(cor)
        # print("faces: ", faces) # Controle pessoal

        # input("Mostrando resultado faces") # Controle pessoal
        mostrarResultado(cor, faces)

        # input("Atualizando placar") # Controle pessoal
        placar = atualizarPlacarJogador(faces, placar)
        # print("placar: ", placar) # Controle pessoal

        # input("Mostrando placar") # Controle pessoal
        mostrarPlacarJogador(placar)

        # input("Guardando cor dos cérebros") # Controle pessoal
        corDadosCerebros = guardarCorCerebros(cor, faces, corDadosCerebros)
        # print("cor dados cérebros:", corDadosCerebros) # Controle pessoal

        # input("Fazendo a checagem") # Controle pessoal
        if checagemPlacar(placar, faces, placarInicioRodada) == "N":
            break
        # input("Voltando pro começo") # Controle pessoal

    return placar[0]

# RODADA DE DESEMPATE
def desempate(jogadores, cerebrosJogadores):
    lideres = [] # Variável que armazena jogadores com pontuação maior do que 13
    cerebrosLideres = [] # Variável que armazena pontuação apenas dos líderes
    for i in range(len(jogadores)):
        if cerebrosJogadores[i] >= pontosParaGanhar:
            lideres.append(jogadores[i])
            cerebrosLideres.append(0)
    for i in range(len(lideres)):
        cerebrosLideres[i] = rodada(lideres[i], cerebrosLideres[i])
    vencedor = lideres[cerebrosLideres.index(max(cerebrosLideres))]
    mostrarPlacarJogo(lideres, cerebrosLideres)
    return vencedor

while max(cerebrosJogadores) < pontosParaGanhar:
    for i in range (len(jogadores)):
        cerebrosJogadores[i] = rodada(jogadores[i], cerebrosJogadores[i])
        print("Fim da rodada do(a) jogador(a)", jogadores[i],".\n")
        mostrarPlacarJogo(jogadores, cerebrosJogadores)
    input("Fim do turno...\n")

if (sum(1 for i in cerebrosJogadores if i >= pontosParaGanhar)) >= 2:
    input("Opa, parece que temos um empate entre jogadores! Os líderes irão jogar agora uma única rodada de desempate!\nTecle para continuar...")
    vencedor = desempate(jogadores, cerebrosJogadores)
    print("Jogador(a)", vencedor, "venceu a rodada de desempate e ganhou o jogo. Parabéns!!!")
else:
    vencedor = jogadores[cerebrosJogadores.index(max(cerebrosJogadores))]
    print("Jogador(a)", vencedor, "comeu mais do que 13 cérebros e ganhou o jogo. Parabéns!!!")
input("\nFIM")


