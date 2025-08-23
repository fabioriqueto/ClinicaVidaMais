from utils import carregar_dados, salvar_dados, validar_cpf,validar_data_nascimento, calcular_idade, tratar_nome, tratar_telefone, tratar_idade, clear_screen
import os, time

ARQUIVO = "pacientes.json"
pacientes = carregar_dados(ARQUIVO, {})

def cadastrar_paciente(nome, idade, telefone, rg, cpf):
    pacientes[cpf] = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "rg": rg,
        "cpf": cpf,
        "documentos_ok": bool(rg and cpf)
    }
    salvar_dados(ARQUIVO, pacientes)
    print(f"✅ Paciente {nome} cadastrado!")
    time.sleep(3)

def ins_dados_paciente(cpf):
    if cpf not in pacientes:
        paciente = tratar_nome(input("Digite o nome do paciente: "))
        idade = tratar_idade(input("Digite a idade: "))
        tel_paciente = tratar_telefone(input("Digite o telefone: "))
        rg_paciente = input("Digite o RG: ")
        cadastrar_paciente(paciente, idade, tel_paciente, rg_paciente, cpf)
        return
    print("\n********** Paciente já cadastrado! ***********")
    time.sleep(2)
    return



def cadastrar_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("============= Cadastrar paciente =============\n")
        cpf_paciente = input("Entre com o CPF do paciente ou (0) para retornar ao menu: ")
        
        if cpf_paciente == "0":
            break

        if not validar_cpf(cpf_paciente):
            print("❌ CPF inválido. Tente novamente!")
            time.sleep(2)
            return


        #localizar_cpf_paciente(cpf_paciente)
        ins_dados_paciente(cpf_paciente)
        break                


