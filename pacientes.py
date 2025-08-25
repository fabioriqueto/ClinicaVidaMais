from utils import carregar_dados, salvar_dados, validar_cpf,validar_data_nascimento, calcular_idade, tratar_nome, tratar_telefone, tratar_idade, input_sn, formatar_cpf, clear_screen
import os, time

ARQUIVO = "pacientes.json"
pacientes = carregar_dados(ARQUIVO, {})

import json
import os

ARQUIVO_PACIENTES = "pacientes.json"

def carregar_pacientes():
    """Carrega os pacientes do arquivo JSON."""
    if not os.path.exists(ARQUIVO_PACIENTES):
        return []
    with open(ARQUIVO_PACIENTES, "r", encoding="utf-8") as f:
        return json.load(f)

def listar_todos_pacientes():
    pacientes = carregar_pacientes()
    # Ordena pela chave nome dentro do dicionário
    pacientes_ordenados = dict(sorted(pacientes.items(), key=lambda item: item[1]["nome"].lower()))

    clear_screen()
    print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
    print("== Listagem de pacientes - Ordem Alfabética ==\n")
    print("(Paciente------------------------------) - (CPF---------) - (telefone-----)")

    for cpf, dados in pacientes_ordenados.items():
        print(f"{(dados['nome']+'                                              ')[0:40]} - {formatar_cpf(cpf)} - {dados['telefone']}")
        print('- ' * 38)

    input("Pressione ENTER para continuar...")


def listar_paciente_por_cpf(cpf: str):
    pacientes = carregar_pacientes()
    clear_screen()
    print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
    print("=========== Paciente já cadastrado ===========\n")
    for k, v in pacientes.items():
        if k == cpf:
            print(f"CPF: {v['cpf']} - RG: {v['rg']}")

            if v['idade'] == None:
                print(f"Paciente: {v['nome']} - Idade: --")
            else:
                print(f"Paciente: {v['nome']} - Idade: {v['idade']}")

            print(f"Telefone: {v['telefone']} - Status documentação: {v['documentos_ok']}")
            input("Pressione ENTER para continuar...")


def salvar_paciente(nome, idade, telefone, rg, cpf, acao):
    pacientes[cpf] = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "rg": rg,
        "cpf": cpf,
        "documentos_ok": bool(rg and cpf)
    }
    salvar_dados(ARQUIVO, pacientes)
    print(f"✅ Paciente: {nome} ==> {acao} realizada(o) com sucesso!✅")
    time.sleep(3)

def ins_dados_paciente(cpf):
    if cpf not in pacientes:
        paciente = tratar_nome(input("Digite o nome do paciente: "))
        idade = tratar_idade(input("Digite a idade: "))
        tel_paciente = tratar_telefone(input("Digite o telefone: "))
        rg_paciente = input("Digite o RG: ")
        resposta = input_sn("Deseja concluir o cadastro do paciente? (S/N): ")
        if resposta == "S":
            salvar_paciente(paciente, idade, tel_paciente, rg_paciente, cpf, 'Cadastramento:')
            return
            
        else:
            print("Cancelando inclusão de cadastro de paciente.")
            time.sleep(2)
            return
            
    paciente = listar_paciente_por_cpf(cpf)
    return


def altera_dados_paciente(cpf):
    print(f"Nome: {pacientes[cpf]['nome']}")
    paciente = tratar_nome(input("Digite o nome do paciente: "))
    print(f"Idade: {pacientes[cpf]['idade']}")
    idade = tratar_idade(input("Digite a idade: "))
    print(f"Telefone: {pacientes[cpf]['telefone']}")
    tel_paciente = tratar_telefone(input("Digite o telefone: "))
    print(f"RG: {pacientes[cpf]['rg']}")
    rg_paciente = input("Digite o RG: ")
    resposta = input_sn("Deseja concluir a alteração do paciente? (S/N): ")
    if resposta == "S":
        salvar_paciente(paciente, idade, tel_paciente, rg_paciente, cpf, 'Alteração de cadastro:')
            
    else:
        print("Cancelando alteração de cadastro de paciente.")
        time.sleep(2)
        
    paciente = listar_paciente_por_cpf(cpf)
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

        ins_dados_paciente(cpf_paciente)
        break                

def alterar_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("=============== Alterar paciente ===============\n")
        cpf_paciente = input("Entre com o CPF do paciente ou (0) para retornar ao menu: ")
        
        if cpf_paciente == "0":
            break

        if not validar_cpf(cpf_paciente):
            print("❌ CPF inválido. Tente novamente!")
            time.sleep(2)
            return

        altera_dados_paciente(cpf_paciente)
        break                

