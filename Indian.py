import random

skillPoint=2 # 테스트용 스킬포인트 부여(횟수)
cardOrder=0 # 카드순서 변수
playerCard = 0 # 플레이어 카드 초기화
comCard = 0 # 컴퓨터 카드 초기화
indianPlaying = True # 게임진행 변수
indianIndex = 0 # 테스트용 변수
indianDeck = [] # 카드덱
comPoint = 10 # 컴퓨터 돈
playerPoint = 10 # 플레이어 돈
winRate = 0 # 컴퓨터 승률계산
drawRate = 0 # 컴퓨터 승률계산

def shuffleDeck():
    list=[card1 for card1 in range(1,11)] # 1~10 카드넣기
    list += list # 1~10 덱 복사
    random.shuffle(list) # 덱 셔플
    for jungbok in range(0, 19):
        if list[jungbok] == list[jungbok + 1]:
            list = shuffleDeck()
    return list

def drawCard():
    global cardOrder
    global playerCard, comCard
    global indianDeck

    if cardOrder == 20: #카드 다썼을경우 셔플
        indianDeck = shuffleDeck()
        cardOrder = 0
    playerCard = indianDeck[cardOrder] # 플레이어 카드배분
    comCard = indianDeck[cardOrder+1] # 컴퓨터 카드배분
    cardOrder += 2

def indianCom():
    global indianDeck, comDeck
    global winRate
    global drawRate
    comDeck.remove(playerCard)
    for index in comDeck:
        if playerCard < index:
            winRate +=1
        elif playerCard == index:
            drawRate +=1

    print("com 베팅확률", winRate,"/",len(comDeck)-drawRate)

indianDeck = shuffleDeck()
comDeck = indianDeck

while indianPlaying:
    print("--------------------------------------")
    print("상대 돈 : ", comPoint)
    print("플레이어 돈 : ", playerPoint)
    print("스킬 포인트 : ", skillPoint)
    print("--------------------------------------")

    indianIndex = int(input("1. 카드 뽑기 \n2. 끝내기\n : "))
    if indianIndex == 1:
        drawCard()
        print("상대의 수는 : ", comCard)
        print("test용 ", playerCard)
        indianCom()
    elif indianIndex == 2:
        indianPlaying=False
    elif indianIndex == 3:
        print(indianDeck)

