import random

class JogoFinanceiro:
    def __init__(self, meta, dinheiro):
        self.meta = meta
        self.dinheiro = dinheiro
        self.rodadas = 0

    def jogar(self):
        print(f"Seu objetivo é economizar dinheiro até atingir a meta de R$ {self.meta}.")

        while self.dinheiro < self.meta:
            self.rodadas += 1
            print(f"Rodada {self.rodadas}")
            print(f"Dinheiro: {self.dinheiro} | Meta: {self.meta}")

            print("Escolha uma ação:")
            print("1 - Comprar algo")
            print("2 - Economizar dinheiro")
            escolha = int(input())

            if escolha == 1:
                preco = random.randint(10, 30)
                if self.dinheiro >= preco:
                    self.dinheiro -= preco
                    print(f"Você comprou algo por {preco}. Dinheiro restante: {self.dinheiro}")
                else:
                    print("Você não tem dinheiro suficiente para comprar isso.")
            elif escolha == 2:
                economia = random.randint(5, 20)
                self.dinheiro += economia
                print(f"Você economizou R$ {economia}. Dinheiro total: R$ {self.dinheiro}")
            else:
                print("Opção inválida. Escolha 1 para comprar ou 2 para economizar.")

        print(f"Parabéns! Você alcançou a meta de R$ {self.meta} em {self.rodadas} rodadas.")

def main():
    print("Bem-vindo à Trilha do Cofrinho!\n")
    meta = int(input("Digite a meta de dinheiro: R$"))
    dinheiro = int(input("Digite a quantidade inicial de dinheiro: R$"))

    jogo = JogoFinanceiro(meta, dinheiro)
    jogo.jogar()

if __name__ == "__main__":
    main()
