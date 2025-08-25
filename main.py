from pacientes import cadastrar_pacientes, listar_todos_pacientes, alterar_pacientes
import os, time
from utils  import clear_screen


def menu_pacientes():
    while True:
        clear_screen()
        print("\n===== SISTEMA DE GESTÃO - CLINICA VIDA + =====")
        print("=========== CADASTRO DE PACIENTES ============\n")
        print("1 - Cadastrar Pacientes")
        print("2 - Listar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Retornar ao MENU PRINCIPAL")

        opcao_menu_pacientes = input("Escolha o número que corresponde ao MENU: ")

        if opcao_menu_pacientes == "1":
            cadastrar_pacientes()

        elif opcao_menu_pacientes == "2":
            listar_todos_pacientes()
        elif opcao_menu_pacientes == "3":
            alterar_pacientes()
#        elif opcao_menu_pacientes == "4":
#            excluir_paciente(input("CPF: "))
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
        print("4 - Estatísticas")
        print("5 - Relatórios")
        print("6 - Área Médica")
        print("7 - Agendamento de consultas")
        print("8 - Agendamento de exames")
        print("0 - Sair")

        opcao = input("Escolha o número que corresponde ao MENU: ")

        if opcao == "1":
            menu_pacientes()

#        elif opcao == "2":
#            listar_pacientes()
#        elif opcao == "3":
#            alterar_paciente(input("CPF: "), input("Novo Nome: ") or None, input("Nova Idade: ") or None, input("Novo Tel: ") or None, input("Novo RG: ") or None)
#        elif opcao == "4":
#            excluir_paciente(input("CPF: "))
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
