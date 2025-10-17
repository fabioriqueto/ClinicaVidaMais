from fila_atendimento import menu_fila
from consultas import menu_consultas
from medicos import menu_medicos    
from fila_atendimento import menu_fila
from atendimento_medico import menu_medico
from exames import menu_exames

from pacientes import (
    relat_analitico_pacientes,
    localizar_paciente_por_cpf_chamada,
    cadastrar_pacientes,
    listar_todos_pacientes,
    alterar_pacientes,
    localizar_excluir_pacientes,
    listar_paciente_por_nome_parcial,
    procurar_paciente_por_nome_exato,
)
import os, time
from utils  import clear_screen

def submenu_relatorio_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("=== SUBMENU === RELATÓRIOS DE PACIENTES ======\n")
        print("1 - Listar pacientes por parte do nome")
        print("2 - Listar todos os pacientes")
        print("3 - Localizar pacientes pelo nome exato")
        print("4 - Localizar pacientes pelo cpf")
        print("0 - Retornar ao MENU anterior")

        opcao_menu_pacientes = input("Escolha o número que corresponde ao MENU: ")

        if opcao_menu_pacientes == "1":
            listar_paciente_por_nome_parcial()

        elif opcao_menu_pacientes == "2":
            listar_todos_pacientes()

        elif opcao_menu_pacientes == "3":
            procurar_paciente_por_nome_exato()

        elif opcao_menu_pacientes == "4":
            localizar_paciente_por_cpf_chamada()

        elif opcao_menu_pacientes == "0":
            break
        else:
            print("❌ Opção inválida!")
            time.sleep(2)


def menu_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("=== MENU === CADASTRO DE PACIENTES ===========\n")
        print("1 - Cadastrar Pacientes")
        print("2 - Listar/Localizar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Retornar ao MENU PRINCIPAL")

        opcao_menu_pacientes = input("Escolha o número que corresponde ao MENU: ")

        if opcao_menu_pacientes == "1":
            cadastrar_pacientes()

        elif opcao_menu_pacientes == "2":
            submenu_relatorio_pacientes()
        elif opcao_menu_pacientes == "3":
            alterar_pacientes()
        elif opcao_menu_pacientes == "4":
            localizar_excluir_pacientes()
        elif opcao_menu_pacientes == "0":
            break
        else:
            print("❌ Opção inválida!")
            time.sleep(2)


def menu():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("============== MENU PRINCIPAL ================\n")
        print("1 - Cadastro de pacientes")
        print("2 - Cadastro de médicos")
        print("3 - Cadastro de exames")
        print("4 - Consultas / Relatórios / Estatísticas")
        print("5 - Área Médica")
        print("6 - Agendamento de consultas / Fila de Atendimento")
        print("0 - Sair")

        opcao = input("Escolha o número que corresponde ao MENU: ")

        if opcao == "1":
            menu_pacientes()
        elif opcao == "4":
            relat_analitico_pacientes()
        elif opcao == "6":
            menu_fila()
        elif opcao == "2":
            menu_medicos()
        elif opcao == "5":
            menu_medico()
        elif opcao == "3":
           menu_exames()
        elif opcao == "0":
            print('Sistema de Gestão finalizado.')
            time.sleep(2)
            clear_screen()
            break


        else:
            print("❌ Opção inválida!aaa")
            time.sleep(2)

if __name__ == "__main__":
    menu()
