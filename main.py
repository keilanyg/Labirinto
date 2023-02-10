from ast import IfExp
import os

FIM_LINHA = 20
FIM_COLUNA = 19 #DIREITA
INICIO_COLUNA = 0 #ESQUERDA
INICIO_LINHA = 0 # cima 

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]

]


class Maze:
    def __init__(self):
        self.l = 1
        self.c = 0

    def formalabirinto(self):
        lab_impressao = []
        for i, linha in enumerate(labirinto):
            for j, coluna in enumerate(labirinto[i]):
                if labirinto[i][j] == 0:
                    lab_impressao = ' '
                elif labirinto[i][j] == 1:
                    lab_impressao = '|'
                elif labirinto[i][j] == 2:
                    lab_impressao = 'x'
                elif labirinto[i][j] == 3:
                    lab_impressao = '.'
                print(lab_impressao, end='')
            print()

    def andarlabirinto(self):
        os.system("cls")
        esquerda = labirinto[self.l][self.c-1]
        direita = labirinto[self.l][self.c+1]
        cima = labirinto[self.l-1][self.c]
        baixo = labirinto[self.l+1][self.c]

        if direita == 0:
            if self.c < FIM_COLUNA:
                self.c += 1
                labirinto[self.l][self.c] = 2

        elif esquerda == 0:
            if self.c < FIM_COLUNA:
                self.c -= 1
                labirinto[self.l][self.c] = 2

        elif baixo == 0:
            if self.l < FIM_LINHA:
                self.l += 1
                labirinto[self.l][self.c] = 2

        elif cima == 0:
            self.l -= 1
            labirinto[self.l][self.c] = 2

        elif direita == 2:
            self.c += 1
            labirinto[self.l][self.c] = 2
            labirinto[self.l][self.c-1] = 3

        elif (esquerda == 2):
            self.c -= 1
            labirinto[self.l][self.c] = 2
            labirinto[self.l][self.c+1] = 3

        elif (baixo == 2):
            if self.l < FIM_LINHA:
                self.l += 1
                labirinto[self.l][self.c] = 2
                labirinto[self.l-1][self.c] = 3

        elif cima == 2:
            if self.l > INICIO_LINHA:
                self.l -= 1
                labirinto[self.l][self.c] = 2
                labirinto[self.l+1][self.c] = 3

        if self.l == FIM_LINHA:
            print ("FINAL DO LABIRINTO!!!!")

    def automatico(self):
        while self.l != FIM_LINHA or self.c != FIM_COLUNA:
            self.formalabirinto()
            print('\n')
            self.andarlabirinto()

    def run(self):
        self.automatico()


Lab = Maze()
Lab.run()
