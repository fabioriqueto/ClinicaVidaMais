import json
import os
import time
from utils import clear_screen, carregar_dados, salvar_dados, limpar_cpf
from pacientes import carregar_pacientes, cadastrar_pacientes

ARQUIVO_FILA = "fila_atendimento.json"

def carregar_fila():
    if os.path.exists(ARQUIVO_FILA):
        with open(ARQUIVO_FILA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_fila(fila):
    with open(ARQUIVO_FILA, "w", encoding="utf-8") as f:
        json.dump(fila, f, indent=4, ensure_ascii=False)

def listar_fila():
    fila = carregar_fila()
    if not fila:
        print("\nNenhum paciente na fila.")
        time.sleep(2)
        return
    print("\n===== FILA DE ATENDIMENTO =====")
    for i, p in enumerate(fila, start=1):
        print(f"{i}. {p['nome']} - CPF: {p['cpf']} - Status: {p.get('status', 'Aguardando')}")
    input("\nPressione ENTER para continuar...")

def chamar_proximo_paciente():
    fila = carregar_fila()
    if not fila:
        print("\nFila vazia.")
        time.sleep(2)
        return
    # procura o primeiro paciente "Aguardando"
    for p in fila:
        if p.get("status", "Aguardando") == "Aguardando":
            p["status"] = "Em atendimento"
            salvar_fila(fila)
            print(f"\nChamando paciente: {p['nome']} (CPF: {p['cpf']})")
            time.sleep(2)
            return
    print("\nNão há pacientes aguardando.")
    time.sleep(2)

def menu_fila():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
===== MENU FILA DE ATENDIMENTO =====
1. Adicionar paciente à fila
2. Listar fila
3. Chamar próximo paciente
0. Voltar ao menu principal
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            from pacientes import localizar_paciente_por_cpf
            cpf = input("Digite o CPF do paciente: ")
            paciente = localizar_paciente_por_cpf(cpf)
            if not paciente:
                print("\nPaciente não encontrado. Cadastre-o antes de adicionar à fila.")
                time.sleep(2)
            else:
                fila = carregar_fila()
                if any(p["cpf"] == cpf for p in fila):
                    print("\nPaciente já está na fila.")
                else:
                    paciente["status"] = "Aguardando"
                    fila.append(paciente)
                    salvar_fila(fila)
                    print("\nPaciente adicionado à fila com sucesso.")
                time.sleep(2)
        elif opcao == "2":
            listar_fila()
        elif opcao == "3":
            chamar_proximo_paciente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            time.sleep(2)