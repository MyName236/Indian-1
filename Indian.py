import random

skillPoint=2 # 테스트용 스킬포인트 부여(횟수)
cardOrder=0 # 카드순서 변수
playerCard = 0 # 플레이어 카드 초기화
comCard = 0 # 컴퓨터 카드 초기화
indianPlaying = True # 게임진행 변수
indianIndex = 0 #
indianDeck = []

def shuffleDeck():
    list=[card1 for card1 in range(1,11)] # 1~10 카드넣기
    list += list # 1~10 덱 복사
    random.shuffle(list) # 덱 셔플
    return list

def drawCard():
    global cardOrder
    global playerCard, comCard
    global indianDeck
    if cardOrder == 20:
        indianDeck = shuffleDeck()
        cardOrder = 0
    playerCard = indianDeck[cardOrder]
    comCard = indianDeck[cardOrder+1]
    cardOrder += 2

indianDeck = shuffleDeck()

while indianPlaying:
    indianIndex = int(input("1. 카드 뽑기 \n2. 끝내기\n : "))
    if indianIndex == 1:
        drawCard()
    elif indianIndex == 2:
        indianPlaying=False

