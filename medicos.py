import time
from utils import clear_screen, carregar_dados, salvar_dados

ARQUIVO_MEDICOS = "medicos.json"

def carregar_medicos():
    return carregar_dados(ARQUIVO_MEDICOS, [])

def salvar_medicos(medicos):
    salvar_dados(ARQUIVO_MEDICOS, medicos)

def cadastrar_medico():
    clear_screen()
    medicos = carregar_medicos()
    print("\n===== CLÍNICA VIDA+ =====")
    print("=== Cadastro de Médicos ===\n")

    nome = input("Nome do médico: ").strip()
    especialidade = input("Especialidade: ").strip()
    crm = input("CRM: ").strip()

    medicos.append({
        "nome": nome,
        "especialidade": especialidade,
        "crm": crm
    })
    salvar_medicos(medicos)
    print("✅ Médico cadastrado com sucesso!")
    time.sleep(2)

def listar_medicos():
    clear_screen()
    medicos = carregar_medicos()
    print("\n===== CLÍNICA VIDA+ =====")
    print("=== Lista de Médicos ===\n")
    if not medicos:
        print("Nenhum médico cadastrado.\n")
    else:
        for i, m in enumerate(medicos, start=1):
            print(f"{i:02d}. {m['nome']} - {m['especialidade']} (CRM: {m['crm']})")
    input("\nPressione ENTER para continuar...")

def editar_medico():
    clear_screen()
    medicos = carregar_medicos()
    listar_medicos()
    indice = int(input("\nDigite o número do médico para editar: ")) - 1
    if 0 <= indice < len(medicos):
        m = medicos[indice]
        m['nome'] = input(f"Novo nome ({m['nome']}): ") or m['nome']
        m['especialidade'] = input(f"Nova especialidade ({m['especialidade']}): ") or m['especialidade']
        m['crm'] = input(f"Novo CRM ({m['crm']}): ") or m['crm']
        salvar_medicos(medicos)
        print("✅ Dados do médico atualizados.")
    else:
        print("❌ Médico não encontrado.")
    time.sleep(2)

def excluir_medico():
    clear_screen()
    medicos = carregar_medicos()
    listar_medicos()
    indice = int(input("\nDigite o número do médico para excluir: ")) - 1
    if 0 <= indice < len(medicos):
        excluido = medicos.pop(indice)
        salvar_medicos(medicos)
        print(f"✅ Médico {excluido['nome']} removido com sucesso.")
    else:
        print("❌ Médico não encontrado.")
    time.sleep(2)

def menu_medicos():
    while True:
        clear_screen()
        print("\n===== CLÍNICA VIDA+ =====")
        print("=== MENU - MÉDICOS ===\n")
        print("1 - Cadastrar médico")
        print("2 - Listar médicos")
        print("3 - Editar médico")
        print("4 - Excluir médico")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_medico()
        elif opcao == "2":
            listar_medicos()
        elif opcao == "3":
            editar_medico()
        elif opcao == "4":
            excluir_medico()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")
            time.sleep(2)
