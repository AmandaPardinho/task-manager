print("============= GERENCIADOR DE TAREFAS =============")
print("1- NOVA TAREFA")
print("2- INICIAR TAREFA")
print("3- FINALIZAR TAREFA")
print("4- EXIBIR TAREFAS CADASTRADAS")
print("5- SAIR")
print("==================================================")


while(True):
    option = input("Digite o número correspondente à opção desejada: ")
    if option.lstrip('-').isdigit():
        number = int(option)
        break
    else:
        print("Você digitou um número inválido.")
    
match number:
    case 1: # Tarefas não iniciadas
        while(True):
            task = input("Qual tarefa você quer adicionar? ")
            task_undone = []
            task_undone.append(task)
            print(task_undone)
            question = input("Deseja adicionar uma nova tarefa? Digite 'Sim' caso queira adicionar uma nova tarefa ou 'Não' caso não queira adicionar uma nova tarefa: ")
            if(question == 'Sim' or question == 'sim' or question == 's'):
                task = input("Digite a nova tarefa: ")
                print(task_undone)
            elif (question == 'Não' or question == 'não' or question == 'n'):
                break
            else:
                input("Resposta inválida. Digite apenas 'Sim' ou 'Não': ")

# # Tarefas começadas
# task_in_progress = []
# task_undone.pop(0)
# print(f"Tarefas não iniciadas: {task_undone}")
# task_in_progress.append(task)
# print(f"tarefas iniciadas: {task_in_progress}")
# print("Lista de tarefas iniciadas: ")
# for task in range(1, len(task_in_progress)-1):
#     print(f"{range}: {task_in_progress}")
# print(f"Lista de tarefas iniciadas: {task_in_progress}")

# Tarefas finalizadas
#task_completed = []
