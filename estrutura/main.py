# Desenvolvimento de uma Plataforma de Saúde #

# Lista / Dicionário
paciente = dict()
lista_cadastro = list()

####################################################################
#TESTE DE CADASTRO
paciente['nome'] = 'Marcos Antonio da Silva'
paciente['idade'] = 74
paciente['telefone'] = '(11) 99999-9999'
lista_cadastro.append(paciente.copy())

paciente['nome'] = 'Ana Julia da Silva'
paciente['idade'] = 45
paciente['telefone'] = '(99) 44444-4444'
lista_cadastro.append(paciente.copy())

paciente['nome'] = 'Silvana Maria Antonia'
paciente['idade'] = 33
paciente['telefone'] = '(11) 33333-41111'
lista_cadastro.append(paciente.copy())
####################################################################


# Opção 1: Cadastrar pacientes.
def cadastro():
    print("==== CADASTRO DE PACIENTE ====")
    paciente['nome'] = str(input("Nome do paciente: ")).capitalize()
    paciente['idade'] = int(input("Idade: "))
    paciente['telefone'] = str(input("Telefone: "))
    lista_cadastro.append(paciente.copy())
    
    print("\nCADASTRO REALIZADO COM SUCESSO!\n")
    
# Opção 2: Ver estatísticas
def estatisticas():
    total_cadastros = 0
    soma_idade = 0
    menor_idade = 999
    maior_idade = 0
    
    for dicionario in lista_cadastro:
        total_cadastros += 1  # Quantidade total de pacientes
        
        soma_idade += dicionario['idade']   # Soma idade dos pacientes
    
        if dicionario['idade'] > maior_idade:   # Paciente mais novo e mais velho
            maior_idade = dicionario['idade']
        
        if dicionario['idade'] < menor_idade:
            menor_idade = dicionario['idade']
            
    idade_média = soma_idade / total_cadastros
    
    # Relatório
    print(f'======== Estatísticas ========\n')
    print(f'Pacientes cadastrados: {total_cadastros} Pacientes')
    print(f'Idade média dos pacientes: {idade_média:.0f} Anos')
    print(f'Paciente mais novo: {menor_idade} anos')
    print(f'Paciente mais velho: {maior_idade} Anos')
    print(f'='*30, '\n')
    
# Opção 3: Buscar paciente
def buscar():
    print("Buscar")

#opção 4: Listar todos os pacientes
def lista():
    print('='*20, 'LISTA DE PACIENTES', '='*20, '\n')
    print(f"{'NOME':^30}|{'IDADE':^7}|{'TELEFONE':^21}|")
    for c in lista_cadastro:

        for chave, valor in c.items():
            if chave == 'nome':
                print(f"{valor:<30}", end='|')
            if chave == 'idade':
                print(f"{valor:^7}", end="|")
            if chave == 'telefone':
                print(f"{valor:^20}", '|')                
    
    print('='*60)
           
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
            estatisticas()
            
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


