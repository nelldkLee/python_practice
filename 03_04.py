from random import *

def startGame(self):
    numberSet = set()
    answer = 0

    def init():
        num1 = randint(2, 9)
        num2 = randint(2, 9)
        self.answer = num1 * num2
        numberSet.add(answer)
        self.test = 2
        while True:
            if len(numberSet) is 9: break
            numberSet.add(randint(2, 81))
        print('{0} x {1} = ?'.format(num1, num2))
        showNumberList()

    def showNumberList():
        numberList = list(numberSet)
        shuffle(numberList)

        for idx, number in enumerate(numberList):
            print(number, end="    ")
            if((idx+1) % 3 is 0): print()
        answerCheck()
    def answerCheck():
        result = int(input("answer: "))
        if(result is self.answer):
            print("정답")
        else:
            print("오답입니다. 다시 입력하세요.")
            answerCheck()
    init()
startGame(startGame)