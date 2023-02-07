import random

game = "1"
testCount = 1
playerInput = input("숫자입력 : ")
playerList = []
for pindex in range(0,4):
    playerList.append(playerInput[pindex])
print(playerList)
combineList = ['1','2','3','4','5','6','7','8','9','0']

while game=="1":
    game=input("1입력시 컴터 띵킹 나머지 break : ")
    print("띵킹횟수 : ", testCount)
    testCount +=1
    sampleList = random.sample(combineList,4)
    print("컴퓨터의 띵킹 : ", sampleList)
    for hit in range(0,4):"""알고리즘 먼저짜기"""


