import json
import os
import time

ARQUIVO_EXAMES = "exames.json"


def carregar_exames():
    if os.path.exists(ARQUIVO_EXAMES):
        with open(ARQUIVO_EXAMES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_exames(exames):
    with open(ARQUIVO_EXAMES, "w", encoding="utf-8") as f:
        json.dump(exames, f, indent=4, ensure_ascii=False)


def cadastrar_exame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== CADASTRAR EXAME =====")
    exames = carregar_exames()
    
    codigo = input("Código do exame (ex: EX001): ").strip()
    nome = input("Nome do exame: ").strip()
    tipo = input("Tipo (Laboratorial, Imagem, Outros): ").strip()
    preco = input("Preço (R$): ").strip()
    duracao = input("Duração estimada (minutos): ").strip()

    exame = {
        "codigo": codigo,
        "nome": nome,
        "tipo": tipo,
        "preco": preco,
        "duracao": duracao
    }

    exames.append(exame)
    salvar_exames(exames)
    print(f"\n✅ Exame '{nome}' cadastrado com sucesso!")
    time.sleep(2)


def listar_exames():
    os.system('cls' if os.name == 'nt' else 'clear')
    exames = carregar_exames()

    if not exames:
        print("Nenhum exame cadastrado.")
    else:
        print("===== LISTA DE EXAMES =====")
        for i, e in enumerate(exames, start=1):
            print(f"{i}. {e['nome']} | Tipo: {e['tipo']} | Preço: R$ {e['preco']} | Duração: {e['duracao']} min")

    input("\nPressione ENTER para continuar...")


def localizar_exame_por_nome(nome):
    exames = carregar_exames()
    for e in exames:
        if e["nome"].lower() == nome.lower():
            return e
    return None


def editar_exame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== EDITAR EXAME =====")
    nome = input("Digite o nome do exame a ser editado: ").strip()

    exames = carregar_exames()
    for e in exames:
        if e["nome"].lower() == nome.lower():
            print(f"\nEditando exame: {e['nome']}")
            e["tipo"] = input(f"Tipo [{e['tipo']}]: ") or e["tipo"]
            e["preco"] = input(f"Preço (R$) [{e['preco']}]: ") or e["preco"]
            e["duracao"] = input(f"Duração (min) [{e['duracao']}]: ") or e["duracao"]
            salvar_exames(exames)
            print("\n✅ Exame atualizado com sucesso!")
            time.sleep(2)
            return
    print("\n⚠️ Exame não encontrado.")
    time.sleep(2)


def excluir_exame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== EXCLUIR EXAME =====")
    nome = input("Digite o nome do exame a ser excluído: ").strip()

    exames = carregar_exames()
    novos_exames = [e for e in exames if e["nome"].lower() != nome.lower()]

    if len(novos_exames) == len(exames):
        print("\n⚠️ Exame não encontrado.")
    else:
        salvar_exames(novos_exames)
        print(f"\n✅ Exame '{nome}' removido com sucesso.")
    time.sleep(2)


def menu_exames():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
===== MENU DE EXAMES =====
1. Cadastrar exame
2. Listar exames
3. Editar exame
4. Excluir exame
0. Voltar ao menu principal
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_exame()
        elif opcao == "2":
            listar_exames()
        elif opcao == "3":
            editar_exame()
        elif opcao == "4":
            excluir_exame()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            time.sleep(2)
