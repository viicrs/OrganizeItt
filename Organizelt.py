import json

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

def carregar_plano(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_plano(plano, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(plano, file, indent=4)
    except IOError:
        print("Erro ao salvar o plano.")

def adicionar_tarefa(plano):
    descricao = input("Informe a tarefa: ")
    prazo = input("Prazo de entrega: ")
    prioridade = input("Prioridade: ")

    tarefa = {
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "concluida": False
    }
    plano.append(tarefa)
    print("Tarefa adicionada.")

def listar_tarefas(plano):
    if not plano:
        print("Nenhuma tarefa encontrada. Por favor adicione uma.")
        return
    for i, tarefa in enumerate(plano):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i + 1}. {tarefa['descricao']} (Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']}, Status: {status})")

def marcar_concluida(plano):
    listar_tarefas(plano)
    try:
        escolha = int(input("Número da tarefa a ser marcada como concluída: ")) - 1
        if 0 <= escolha < len(plano):
            plano[escolha]["concluida"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def main():
    filename = "plano_estudo.json"
    plano = carregar_plano(filename)

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(plano)
        elif escolha == "2":
            listar_tarefas(plano)
        elif escolha == "3":
            marcar_concluida(plano)
        elif escolha == "4":
            salvar_plano(plano, filename)
            print("Tarefas salvas com sucesso.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
