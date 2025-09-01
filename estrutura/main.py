# Desenvolvimento de uma Plataforma de Saúde #

# Lista / Dicionário
paciente = dict()
lista_cadastro = list()


# Opção 1: Cadastrar pacientes.
#def cadastro():

# Opção 2: Ver estatísticas
#def estatiscicas():
    
# Opção 3: Buscar paciente
#def buscar():

#opção 4: Listar todos os pacientes
#def Lista():


# Menu 
def menu():
    print("==== SISTEMA CLÍNICA VIDA+ ====")
    opcao = int(input("1. Cadastrar paciente\n"
                      "2. Ver estatísticas\n"
                      "3. Buscar paciente\n"
                      "4. Listar todos os pacientes\n"
                      "5. Sair\n"
                      "Escolha uma opção: "))
    print("="*31,
          "\n")
    
if __name__ == "__main__":
    menu()
    