import sqlite3

class JogadorFutsal:
    def __init__(self, nome, posicao, numero_camisa):
        self.__nome = nome
        self.__posicao = posicao
        self.__numero_camisa = numero_camisa

    def get_nome(self):
        return self.__nome

    def get_posicao(self):
        return self.__posicao

    def get_numero_camisa(self):
        return self.__numero_camisa


class BancoDeDadosFutsal:
    def __init__(self, nome_banco='jogadores_futsal.db'):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jogadores (
                nome TEXT,
                posicao TEXT,
                numero_camisa INTEGER
            )
        ''')
        # Confirma as mudanças no banco de dados a seguir:
        self.conn.commit()

    def adicionar_jogador(self, jogador):
        self.cursor.execute('''
            INSERT INTO jogadores VALUES (?, ?, ?)
        ''', (jogador.get_nome(), jogador.get_posicao(), jogador.get_numero_camisa()))
        self.conn.commit()

    def remover_jogador(self, nome):
        self.cursor.execute('DELETE FROM jogadores WHERE nome=?', (nome,))
        self.conn.commit()

    def listar_jogadores(self):
        self.cursor.execute('SELECT * FROM jogadores')
        jogadores = self.cursor.fetchall()
        for jogador in jogadores:
            print(f'Nome: {jogador[0]}, Posição: {jogador[1]}, Número da Camisa: {jogador[2]}')


def main():
    banco_futsal = BancoDeDadosFutsal()

    while True:
        nome = input("Digite o nome do jogador: ")
        posicao = input("Digite a posição do jogador: ")
        numero_camisa = int(input("Digite o número da camisa do jogador: "))

        jogador = JogadorFutsal(nome, posicao, numero_camisa)

        banco_futsal.adicionar_jogador(jogador)

        opcao = input(
            "Deseja cadastrar um novo jogador (C), listar jogadores cadastrados (L), remover jogador (R) ou encerrar "
            "o programa (E)? ").upper()

        if opcao == 'L':
            banco_futsal.listar_jogadores()
        elif opcao == 'R':
            nome_remover = input("Digit o nome do jogador a ser removido: ")
            banco_futsal.remover_jogador(nome_remover)
            print(f"Jogador {nome_remover} removido.")
        elif opcao == 'E':
            break


if __name__ == "__main__":
    main()