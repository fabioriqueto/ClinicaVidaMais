import os
import time
import json

from utils import (
    carregar_dados,
    salvar_dados,
    validar_cpf,
    tratar_nome,
    tratar_telefone,
    tratar_idade,
    input_sn,
    formatar_cpf,
    limpar_cpf,
    input_default,
    clear_screen,
)

ARQUIVO = "pacientes.json"
pacientes = carregar_dados(ARQUIVO, {})

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


def localizar_paciente_por_cpf(cpf: str):

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
            
    paciente = localizar_paciente_por_cpf(cpf)
    input("Pressione ENTER para continuar...")

    return


def altera_dados_paciente(cpf):
    if cpf not in pacientes:
        print("❌ CPF paciente não localizado. Tente novamente!")
        time.sleep(2)
        return

    paciente = tratar_nome(input_default("Digite o nome do paciente: ",pacientes[cpf]['nome']))
    idade = tratar_idade(input(f"Digite a idade [{pacientes[cpf]['idade']}]: "))
    tel_paciente = tratar_telefone(input_default("Digite o telefone: ",pacientes[cpf]['telefone']))
    rg_paciente = input_default("Digite o RG: ",pacientes[cpf]['rg'])
    resposta = input_sn("Deseja concluir a alteração do paciente? (S/N): ")
    if resposta == "S":
        salvar_paciente(paciente, idade, tel_paciente, rg_paciente, cpf, 'Alteração de cadastro:')
        
    else:
        print("Cancelando alteração de cadastro de paciente.")
        time.sleep(2)
    
    paciente = localizar_paciente_por_cpf(cpf)
    input("Pressione ENTER para continuar...")
    return


def cadastrar_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("============= Cadastrar paciente =============\n")
        cpf_paciente = limpar_cpf(input("Entre com o CPF do paciente ou (0) para retornar ao menu: "))
                
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
        cpf_paciente = limpar_cpf(input("Entre com o CPF do paciente ou (0) para retornar ao menu: "))
        
        if cpf_paciente == "0":
            break

        if not validar_cpf(cpf_paciente):
            print("❌ CPF inválido. Tente novamente!")
            time.sleep(2)
            return

        altera_dados_paciente(cpf_paciente)
        break                

def excluir_paciente(cpf):
    nome = pacientes[cpf]["nome"]
    del pacientes[cpf]
    salvar_dados(ARQUIVO, pacientes)
    print(f"🗑️ Paciente {nome} (CPF: {cpf}) excluído!")

def cadastrar_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("============= Cadastrar paciente =============\n")
        cpf_paciente = limpar_cpf(input("Entre com o CPF do paciente ou (0) para retornar ao menu: "))
        
        if cpf_paciente == "0":
            break

        if not validar_cpf(cpf_paciente):
            print("❌ CPF inválido. Tente novamente!")
            time.sleep(2)
            return

        ins_dados_paciente(cpf_paciente)
        break                

def localizar_excluir_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("============== Excluir paciente ==============\n")
        cpf_paciente = limpar_cpf(input("Entre com o CPF do paciente ou (0) para retornar ao menu: "))
        
        if cpf_paciente == "0":
            break

        if not validar_cpf(cpf_paciente):
            print("❌ CPF inválido. Tente novamente!")
            time.sleep(2)
            return
        
        pacientes = carregar_pacientes()
        if cpf_paciente not in pacientes:
            print("❌ CPF paciente não localizado. Tente novamente!")
            time.sleep(2)
            return

        for k, v in pacientes.items():
            if k == cpf_paciente:

                print(f"Paciente: {v['nome']}")
                if v['idade'] == None:
                    print(f"Idade: ---")
                else:
                    print(f"Idade: {v['idade']}")

                print(f"CPF: {v['cpf']} - RG: {v['rg']}")
                print(f"Telefone: {v['telefone']} - Status documentação: {v['documentos_ok']}")

        resposta = input_sn("Deseja excluir este paciente? (S/N): ")
        if resposta == "S":
            excluir_paciente(cpf_paciente)
        else:
            print("Cancelando da ação de exclusão do paciente.")
            time.sleep(2)
            break                



# --- Busca pelo nome exato ---
def procurar_paciente_por_nome_exato():
    while True:
        """Procura paciente pelo nome exato."""
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("===== Localizar paciente pelo nome exato =====\n")
        nome_busca = input("Entre com o nome exato do paciente ou (0) para retornar ao menu: ")
        if nome_busca == "0":
            break

        pacientes = carregar_pacientes()

        for cpf, dados in pacientes.items():
            if dados["nome"].strip().lower() == nome_busca.strip().lower():
                print("\n============ Paciente encontrado ===========\n")
                print(f"Nome: {dados['nome']}")
                print(f"Idade: {dados['idade']} anos")
                print(f"Telefone: {dados['telefone']}")
                print(f"CPF: {dados['cpf']}")
                print(f"RG: {dados['rg']}")
                input("Pressione ENTER para continuar...")

                return 

        print("❌ Nenhum paciente encontrado com esse nome exato.")
        return


# --- Busca por parte do nome ---
def listar_paciente_por_nome_parcial():
    while True:
        """Procura pacientes contendo parte do nome (sem diferenciar maiúsculas/minúsculas)."""
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("Localizar/listar pacientes por parcial do nome\n")
        nome_busca = input("Entre com um trecho do nome do paciente ou (0) para retornar ao menu: ")
        if nome_busca == "0":
            break

        pacientes = carregar_pacientes()
        encontrados = []

        for cpf, dados in pacientes.items():
            if nome_busca.lower() in dados["nome"].lower():
                encontrados.append(dados)
        if encontrados:
            encontrados.sort(key=lambda x: x["nome"])
            #print("\n========== Pacientes encontrados ===========\n")
            print("(Paciente------------------------------) - (CPF---------) - (telefone-----)")
            for p in encontrados:
                print(f"{(p['nome']+'                                              ')[0:40]} - {formatar_cpf(p['cpf'])} - {p['telefone']}")
                print('- ' * 38)
            input("Pressione ENTER para continuar...")

        else:
            print("❌ Nenhum paciente encontrado contendo esse nome ou parte do nome.")
            time.sleep(2)
        return            
    
def localizar_paciente_por_cpf_chamada():
    clear_screen()
    print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
    print("======== Localizar paciente pelo CPF =========\n")
    cpf = limpar_cpf(input("Entre com o CPF do paciente ou (0) para retornar ao menu: "))
                
    if cpf == "0":
        return

    if not validar_cpf(cpf):
        print("❌ CPF inválido. Tente novamente!")
        time.sleep(2)
        return

    localizar_paciente_por_cpf(cpf)
    input("Pressione ENTER para continuar...")


def relat_analitico_pacientes():
    # Número total de pacientes
    pacientes = carregar_pacientes()
    clear_screen()
    print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
    print("===== Relatório Analítico / Estatísticas =====\n")

    # Número total de pacientes
    total = len(pacientes)

    # Idade média
    media = sum(dados["idade"] for dados in pacientes.values()) / total

    # Paciente mais novo
    cpf_mais_novo = min(pacientes, key=lambda cpf: pacientes[cpf]["idade"])
    mais_novo = pacientes[cpf_mais_novo]

    # Paciente mais velho
    cpf_mais_velho = max(pacientes, key=lambda cpf: pacientes[cpf]["idade"])
    mais_velho = pacientes[cpf_mais_velho]

    # Exibindo resultados
    print(f"Número total de pacientes: {total}")
    print(f"Idade média dos pacientes: {media:.2f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos) - CPF: {formatar_cpf(cpf_mais_novo)}")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos) - CPF: {formatar_cpf(cpf_mais_velho)}")
    input("Pressione ENTER para continuar...")
