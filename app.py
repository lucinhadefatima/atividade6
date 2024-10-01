
#lista
tarefas =  []

while True:
    #tratamento de excecao
    try:
        #isuario cadastra nova tarefa
        nova_tarefa = input("cadastre umna nova tarefa ou 'enter' para exibir as tarefas cadastradas: ")
        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print(f"nova tarefa cadastrada com sucesso")
            continue
        else:
            break
    except Exception as e :
        print(f"nao foi possivel cadastrar nova tarefa. {e}. ")

        #exibie para lista de tarefas 
        for tarefa in tarefas:
            print(tarefa)
