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

def shuffleDeck():
    list=[card1 for card1 in range(1,11)] # 1~10 카드넣기
    list += list # 1~10 덱 복사
    random.shuffle(list) # 덱 셔플
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

indianDeck = shuffleDeck()

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
    elif indianIndex == 2:
        indianPlaying=False

