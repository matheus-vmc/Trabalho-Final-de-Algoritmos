#Aluno: Matheus Vinicius Maciel da Cunha
#Matricula:20260015011
import os
#Coloquei uma coisa a mais na class, que seria o nome da tarefa
class task:
    name = ""
    status = ""
    descri = ""
    priori = 0
    id = 0
#Função para ordenar os numeros de prioridade da tarefa
#O menor tem a maior prioridade
def ordenar(list_task):
    tamanho = len(list_task)
    for i in range(tamanho):
        for j in range(0,tamanho - i - 1 ):
            if list_task[j].priori > list_task[1+j].priori:
                temp = list_task[j]
                list_task[j] = list_task[j+1]
                list_task[j+1] = temp
#Função para adicionar uma nova tarefa na lista de tarefas
def new_task(list_task):
    #A função os que importei server apenas para limpar o terminal, nada além disso
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Descreva sua Tarefa")
    print("-"*50)
    new = task()
    new.name = input("Digite o nome da sua tarefa:")
    new.status = "Ativa"
    new.descri = input("Digite a descrição da tarefa:")
    print("Defina um numero de prioridade:")
    print("-"*50)
    print("Numero 1: Maior Prioridade")
    print("Numero 2: Prioridade média")
    print("Numero 3: Menor Prioridade")
    while True:
        new.priori = int(input("Numero:"))
        if new.priori == 1:
            ordenar(list_task)
            break
        else:
            if new.priori == 2:
                ordenar(list_task)
                break
            else:
                if new.priori == 3:
                    ordenar(list_task)
                    break
                else:
                    print("Não existe esse nivel de prioridade")
    new.id = len(list_task) + 10
    list_task.append(new)   
    print ("Tarefa cadastrada com sucesso.")

#Função que exibe o conteúdo da lista de tarefas
def visual_task(list_task):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Suas Tarefas:")
    print("-"*50)
    for task in list_task:
        print(f"Nome da Tarefa: {task.name}")
        print(f"Status da Tarefa:{task.status}")
        print(f"Descrição: {task.descri}")
        print(f"Numero de Prioridade:{task.priori}")
        print(f"Numero de Identificação:{task.id}")
        print("-"*50)
    
            
#Essa função serve para marca a tarefa como concluída, ela também verifica se a task já foi concluída
def task_completed(list_task):
    os.system('cls' if os.name == 'nt' else 'clear')
    visual_task(list_task)
    codigo = int(input("Digite o ID da tarefa:"))
    for i in list_task:
        if codigo == i.id:
            if i.status == "Concluida":
                print("Essa tarefa já foi concluida")
                break
            else:
                 i.status = "Concluida"
                 print("Estado da tarefa, mudado com sucesso.")
                 break
    else:
        print("Codigo inválido")
             
    
#Função que faz a tarefa ir de concluída para ativa
def reabrir_task(list_task):
    os.system('cls' if os.name == 'nt' else 'clear')
    visual_task(list_task)
    codigo = int(input("Digite o ID da tarefa:"))
    for i in list_task:
        if codigo == i.id:
             if i.status == "Ativa":
                print("Já está ativa")
             else:
                  i.status = "Ativa"
                  print("Tarefa reaberta com sucesso.")
                  break
        else:
            print("Codigo incorreto, digite novamente")


#Função para editar a descrição da tarefa e o nome dela atravéz do identificador unico
def edit_task(list_task):
    os.system('cls' if os.name == 'nt' else 'clear')
    visual_task(list_task)
    codigo = int(input("Digite o ID da tarefa:"))
    for i in list_task:
        if codigo == i.id:
            while True:
                print("Opção 1: Nome da tarefa")
                print("Opção 2: Descrição da tarefa")
                edit = int(input("Você quer editar qual parte: " ))
                if edit == 1:
                    i.name = input("Digite o novo nome: ")
                    print("Nome da tarefa editado com sucesso")
                    break
                else:
                    if edit == 2:
                        i.descri = input("Digite a nova descrição: ")  
                        print("Descrição da tarefa editada com sucesso")
                        break
                    else:
                        print("Opção inválida")                   
        else:
            print("Codigo Inválido")
def excluir_task(list_task):
    codigo = int(input("Digite o ID: "))

    for i in list_task:
        if codigo == i.id:
            list_task.remove(i)
            print("Tarefa excluída!")
            break
    else:
        print("Tarefa não encontrada")
            
def visual_ativa(list_task):
    for i in list_task:
        if i.status == "Ativa":
            print(f"Nome da Tarefa: {i.name}")
            print(f"Status da Tarefa:{i.status}")
            print(f"Descrição: {i.descri}")
            print(f"Numero de Prioridade:{i.priori}")
            print(f"Numero de Identificação:{i.id}")
            print("-"*50)
def relatorio_estátistico(list_task):
    ativas = 0
    concluidas = 0
    task = 0 
    soma = 0
    for i in list_task:
        if i.status == "Ativa":
            ativas +=1
        else:
            if i.status == "Concluida":
                concluidas +=1
        soma +=i.priori
        task+=1
    media = soma / task
    print("Relátorio Estátistico:")
    print("-" * 50)
    print("Tarefas Ativas:",ativas)
    print("Tarefas Concluídas:",concluidas)
    print ("Média de prioridade:",media)

#Menu principal utilizado para interagir com o programa e aonde é armazenado a lista de tarefas
def menu():
    list_task = []
    
    while True:
        print("Bem vindo ao Sistema de Tarefas")
        print("-" * 50)
        print("Escolha das opçôes para navegar no sistema")
        print("-" * 50)
        print("Opção 1: Nova Tarefa")
        print("Opção 2: Visualizar Tarefa")
        print("Opção 3: Concluir Tarefas")
        print("Opção 4: Reabrir Tarefa")
        print("Opção 5: Editar Tarefas")
        print("Opção 6: Excluir tarefa")
        print("Opção 7: Visualizar somente tarefas ativas")
        print("Opção 8: Relátorio estátistico")
        print("Opção 9: Sair")
        print("-" * 50)
        codigo = int(input("Digite qual opção você deseja selecionar:"))
        if codigo == 1:
            new_task(list_task)
        else:
            if codigo == 2:
                visual_task(list_task)
            else:
                if codigo == 3:
                    task_completed(list_task)
                else:
                    if codigo == 4:
                        reabrir_task(list_task)
                    else: 
                        if codigo == 5:
                            edit_task(list_task)
                        else:
                            if codigo == 6:
                                excluir_task(list_task)
                            else:
                                if codigo == 7:
                                    visual_ativa(list_task)
                                else:
                                    if codigo == 8:
                                        relatorio_estátistico(list_task)
                                    else:
                                        if codigo == 9:
                                            print("-" * 50)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print("Obrigado, volte sempre")
                                            break
                                        else:
                                            print("Codigo Inválido")


menu()
            


    




