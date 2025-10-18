pacientes = []

def cadastrar_paciente():
    """Função para cadastrar um novo paciente."""
    print("\n--- CADASTRAR PACIENTE ---")
    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone (DD) NNNNN-NNNN: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")
    
    # Ilustração visual do paciente sendo cadastrado.
    # Imagine uma ficha de paciente sendo preenchida.

def ver_estatisticas():
    """Função para exibir estatísticas da clínica."""
    print("\n--- ESTATÍSTICAS ---")
    total_pacientes = len(pacientes)
    print(f"Total de pacientes cadastrados: {total_pacientes}")
    
    if total_pacientes > 0:
        idades = [p['idade'] for p in pacientes]
        idade_media = sum(idades) / total_pacientes
        print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    else:
        print("Nenhum paciente cadastrado para calcular estatísticas.")
    
    # Ilustração de um gráfico de pizza simples mostrando a distribuição de pacientes, talvez por idade.

def buscar_paciente():
    """Função para buscar um paciente pelo nome."""
    print("\n--- BUSCAR PACIENTE ---")
    termo_busca = input("Digite o nome do paciente para buscar: ").lower()
    
    encontrados = [p for p in pacientes if termo_busca in p['nome'].lower()]
    
    if encontrados:
        print("\nPacientes encontrados:")
        for paciente in encontrados:
            print(f"Nome: {paciente['nome']}, Idade: {paciente['idade']}, Telefone: {paciente['telefone']}")
    else:
        print("Nenhum paciente encontrado com esse nome.")
        
    # Ilustração de uma lupa procurando por nomes em uma lista.

def listar_todos_pacientes():
    """Função para listar todos os pacientes cadastrados."""
    print("\n--- LISTA DE TODOS OS PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for i, paciente in enumerate(pacientes):
            print(f"[{i+1}] Nome: {paciente['nome']}, Idade: {paciente['idade']}, Telefone: {paciente['telefone']}")
            
    # Ilustração de uma lista de nomes em um caderno ou tela.

def menu_principal():
    """Função principal que exibe o menu e gerencia as opções."""
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_paciente()
        elif escolha == '2':
            ver_estatisticas()
        elif escolha == '3':
            buscar_paciente()
        elif escolha == '4':
            listar_todos_pacientes()
        elif escolha == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# Iniciar o aplicativo
if __name__ == "__main__":
    menu_principal()