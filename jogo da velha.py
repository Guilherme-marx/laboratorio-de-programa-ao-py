import random

class JogoDaVela:
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
    turno = None

    def __init__(self, jogador_inicial="X"):
        self.turno = jogador_inicial

    def exibir_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificar_tabuleiro(self):
        # Verificações das 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']

        # Verificações das 3 horizontais
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogador_move(self):
        while True:
            jogada = input("Jogada: ")
            if self.verificar_jogada(jogada):
                return jogada
            else:
                print(f"Jogada inválida. Tente novamente.")

    def bot_move(self):
        empty_cells = [key for key in self.tabuleiro if self.tabuleiro[key] == ' ']
        if empty_cells:
            return random.choice(empty_cells)
        return None

    def jogar(self):
        while True:
            self.exibir_tabuleiro()

            if self.turno == "X":
                print(f"Turno do {self.turno}")
                jogada = self.jogador_move()
            else:
                print(f"Turno do {self.turno} (Bot)")
                jogada = self.bot_move()

            self.tabuleiro[jogada] = self.turno

            estado = self.verificar_tabuleiro()

            if estado == "X":
                print("X é o vencedor!!!")
                break

            elif estado == "O":
                print("O é o vencedor!!!")
                break

            if estado == "empate":
                print("EMPATE!!!")
                break

            # Troca o jogador do próximo turno
            self.turno = "X" if self.turno == "O" else "O"

        self.exibir_tabuleiro()


jogo = JogoDaVela("X")  # Inicia com o jogador "X"
jogo.jogar()
