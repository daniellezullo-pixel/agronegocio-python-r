# Dani Zullo_RM571880_fase2_cap9

import json

dados = []

def cadastrar():
    cultura = input("Digite a cultura: ").strip()
    irrigacao = input("Nível de irrigação (Alto/Médio/Baixo): ").strip()

    if cultura == "" or irrigacao == "":
        print("Preencha todos os campos!")
        return

    dados.append({
        "cultura": cultura,
        "irrigacao": irrigacao
    })

    print("Salvo com sucesso!")

def listar():
    if len(dados) == 0:
        print("Nenhum dado ainda.")
    else:
        for item in dados:
            print(f"Cultura: {item['cultura']} | Irrigação: {item['irrigacao']}")

def salvar():
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "0":
        salvar()
        print("Dados salvos!")
        break

    else:
        print("Opção inválida")
