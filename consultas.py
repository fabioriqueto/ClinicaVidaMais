import time
from utils import clear_screen, carregar_dados, salvar_dados, formatar_cpf

ARQUIVO_CONSULTAS = "consultas.json"
ARQUIVO_PACIENTES = "pacientes.json"
ARQUIVO_MEDICOS = "medicos.json"

def carregar_consultas():
    return carregar_dados(ARQUIVO_CONSULTAS, [])

def salvar_consultas(consultas):
    salvar_dados(ARQUIVO_CONSULTAS, consultas)

def agendar_consulta():
    clear_screen()
    consultas = carregar_consultas()
    pacientes = carregar_dados(ARQUIVO_PACIENTES, [])
    medicos = carregar_dados(ARQUIVO_MEDICOS, [])

    print("\n===== CLÍNICA VIDA+ =====")
    print("=== Agendamento de Consulta ===\n")

    cpf = input("CPF do paciente: ").strip()
    paciente = next((p for p in pacientes if p['cpf'] == cpf), None)
    if not paciente:
        print("⚠️ Paciente não cadastrado.")
        time.sleep(2)
        return

    listar_medicos_resumido(medicos)
    indice_medico = int(input("Escolha o número do médico: ")) - 1
    if not (0 <= indice_medico < len(medicos)):
        print("❌ Médico inválido.")
        time.sleep(2)
        return

    data = input("Data da consulta (DD/MM/AAAA): ")
    hora = input("Horário: ")

    consultas.append({
        "paciente": paciente,
        "medico": medicos[indice_medico],
        "data": data,
        "hora": hora,
        "status": "Agendada"
    })
    salvar_consultas(consultas)
    print("✅ Consulta agendada com sucesso!")
    time.sleep(2)

def listar_medicos_resumido(medicos):
    print("\nMédicos disponíveis:")
    for i, m in enumerate(medicos, start=1):
        print(f"{i:02d}. {m['nome']} - {m['especialidade']}")

def listar_consultas():
    clear_screen()
    consultas = carregar_consultas()
    print("\n===== CLÍNICA VIDA+ =====")
    print("=== Consultas Agendadas ===\n")
    if not consultas:
        print("Nenhuma consulta registrada.\n")
    else:
        for i, c in enumerate(consultas, start=1):
            print(f"{i:02d}. {c['paciente']['nome']} - {c['medico']['nome']} - {c['data']} {c['hora']} ({c['status']})")
    input("\nPressione ENTER para continuar...")

def menu_consultas():
    while True:
        clear_screen()
        print("\n===== CLÍNICA VIDA+ =====")
        print("=== MENU - CONSULTAS ===\n")
        print("1 - Agendar consulta")
        print("2 - Listar consultas")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            agendar_consulta()
        elif opcao == "2":
            listar_consultas()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")
            time.sleep(2)
