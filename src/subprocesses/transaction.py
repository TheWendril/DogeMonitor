import json

validSession = False
userName = None

with open('users.json', 'r') as archiveData:
    AllUsers = json.load(archiveData)

def init_Session():

    while not validSession:

        print('Digite o nome do usuário da sessão')
        userName = input()

        for user in AllUsers:
            if user['User'] == userName:
                validSession = True



if __name__ == '__main__':

    init_Session()

    print('==========================\n')
    print('Realizar Transações DOGE!!\n')
    print('==========================\n')

    while 1:
        print('1. Vender DOGECOIN')
        print('2. Comprar DOGECOIN')

        try:
            choose = int(input())

        except Exception:
            print('Por Favor, digite uma opção válida!')

        if choose == 1:

            print('Quantos DOGES?')
            doges_purchased: float(input())
