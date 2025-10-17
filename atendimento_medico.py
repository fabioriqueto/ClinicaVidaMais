import json, os, time

ARQUIVO_FILA = "fila_atendimento.json"

def carregar_fila():
    if os.path.exists(ARQUIVO_FILA):
        with open(ARQUIVO_FILA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_fila(fila):
    with open(ARQUIVO_FILA, "w", encoding="utf-8") as f:
        json.dump(fila, f, indent=4, ensure_ascii=False)

def encerrar_atendimento():
    fila = carregar_fila()
    for p in fila:
        if p.get("status") == "Em atendimento":
            p["status"] = "Atendido"
            salvar_fila(fila)
            print(f"\nAtendimento de {p['nome']} encerrado com sucesso.")
            time.sleep(2)
            return
    print("\nNão há pacientes em atendimento.")
    time.sleep(2)

def listar_em_atendimento():
    fila = carregar_fila()
    em_atendimento = [p for p in fila if p.get("status") == "Em atendimento"]
    if not em_atendimento:
        print("\nNenhum paciente em atendimento.")
    else:
        print("\n===== PACIENTES EM ATENDIMENTO =====")
        for p in em_atendimento:
            print(f"{p['nome']} - CPF: {p['cpf']}")
    input("\nPressione ENTER para continuar...")

def menu_medico():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
===== ÁREA MÉDICA =====
1. Listar pacientes em atendimento
2. Encerrar atendimento
0. Voltar ao menu principal
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_em_atendimento()
        elif opcao == "2":
            encerrar_atendimento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            time.sleep(2)
