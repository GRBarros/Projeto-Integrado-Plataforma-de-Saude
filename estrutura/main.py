# Desenvolvimento de uma Plataforma de Saúde #

# Lista / Dicionário
paciente = dict()
lista_cadastro = list()


# Opção 1: Cadastrar pacientes.
def cadastro():
    print("==== CADASTRO DE PACIENTE ====")
    paciente['nome'] = str(input("Nome do paciente: ")).capitalize()
    paciente['idade'] = int(input("Idade: "))
    paciente['Telefone'] = input("Telefone: ")
    lista_cadastro.append(paciente.copy())
    
    print("\nCADASTRO REALIZADO COM SUCESSO!\n")
    
# Opção 2: Ver estatísticas
def estatiscicas():
    print("Estatísticas")
    
# Opção 3: Buscar paciente
def buscar():
    print("Buscar")

#opção 4: Listar todos os pacientes
def lista():
    x = 0
    for c in lista_cadastro:
        x += 1
        print(f"######### PACIENTE {x} #########")
        for chave, valor in c.items():
            print(f"{chave.capitalize()}: {valor}")
        
        print("\n")   
    print("\n")

def sair():
    exit()
    
# Menu 
def menu():
    while True:
        print("==== SISTEMA CLÍNICA VIDA+ ====")
        opcao = int(input("1. Cadastrar paciente\n"
                        "2. Ver estatísticas\n"
                        "3. Buscar paciente\n"
                        "4. Listar todos os pacientes\n"
                        "5. Sair\n"
                        "Escolha uma opção: "))
        print("="*31,
            "\n")
        
        # Estrutura condicional do menu
        if opcao == 1: # Opção para cadastro de pacientes
            cadastro()
        
        elif opcao == 2: # Opção para visualizar as estatísticas
            estatiscicas()
            
        elif opcao == 3: # Opção para pesquisar paciente
            buscar()
        
        elif opcao == 4: # Opção para listar pacientes 
            lista()
        
        elif opcao == 5: # Opção para sair
            sair()
            
        else:
            print("Opção inválida! Tente novamente.\n")
            menu()
        
if __name__ == "__main__":
    menu()
    