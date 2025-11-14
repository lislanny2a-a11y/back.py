while True:
    try:
        nome = input("Informe seu nome: ")

        if nome == "":
            raise Exception("Ops, nome não pode ser vazio!")

        if nome.isnumeric():
            raise Exception("Ops, nome não pode ser apenas números!")

        break

    except Exception as erro:
        print("Erro:", erro)

while True:
    try:
        idade = input("Informe sua idade: ")

        if idade == "":
            raise Exception(" Ops, A idade não pode ser vazia!")

        idade = int(idade) 

        break 

    except ValueError:
        print("Erro: a idade deve ser um número inteiro!")
    except Exception as erro:
        print("Erro:", erro)

print("\nDADOS DIGITADOS:")
print("Nome:", nome)
print("Idade:", idade)
