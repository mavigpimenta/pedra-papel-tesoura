import random

def getRandomChoice():
    array = ['pedra', 'papel', 'tesoura']
    return random.choice(array)

def compareResults(userOp, randomOp):


    if userOp == randomOp:
        return 'Empate'
    elif userOp == 'pedra':
        if randomOp == 'papel':
            return 'Você perdeu'
        return 'Você ganhou'
    elif userOp == 'papel':
        if randomOp == 'tesoura':
            return 'Você perdeu'
        return 'Você ganhou'
    elif userOp == 'tesoura':
        if randomOp == 'pedra':
            return 'Você perdeu'
        return 'Você ganhou'

print("Olá! Vamos jogar jokempô? Digite sua opcão!")

def runGame():

    userPoints = 0
    pcPoints = 0

    while True:
        print('> ', end='')
        opUser = input().lower()
        opRandom = getRandomChoice()
        result = compareResults(opUser, opRandom)

        if 'ganhou' in result:
            userPoints += 1
        elif 'perdeu' in result:
            pcPoints += 1

        print("O Computador escolheu {}.\nResultado: {}.\n Placar: Você tem {} pontos, e o PC tem {} pontos. Jogue novamente".format(opRandom, result, userPoints, pcPoints))


runGame()
