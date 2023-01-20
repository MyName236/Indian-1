import random

skillPoint = 2  # 테스트용 스킬포인트 부여(횟수)
cardOrder = 0  # 카드순서 변수
playerCard = 0  # 플레이어 카드 초기화
comCard = 0  # 컴퓨터 카드 초기화
indianPlaying = True  # 게임진행 변수
indianIndex = 0  # 테스트용 변수
indianDeck = []  # 카드덱
comPoint = 10  # 컴퓨터 돈
playerPoint = 10  # 플레이어 돈
winRate = 0  # 컴퓨터 승률계산
drawRate = 0  # 컴퓨터 승률계산
betAmount = 0  # 베팅액
betNum = 1  # 베팅 순환
comFollow = True
nowBet = 0

def shuffleDeck():
    list = [card1 for card1 in range(1, 11)]  # 1~10 카드넣기
    list += list  # 1~10 덱 복사
    random.shuffle(list)  # 덱 셔플
    for jungbok in range(0, 19):
        if list[jungbok] == list[jungbok + 1]:
            list = shuffleDeck()
    return list

def drawCard():
    global cardOrder
    global playerCard, comCard
    global indianDeck, comDeck

    if cardOrder == 9:  # 카드 다썼을경우 셔플
        indianDeck = shuffleDeck()
        cardOrder = 0
        comDeck = indianDeck
    playerCard = indianDeck[cardOrder]  # 플레이어 카드배분
    comCard = indianDeck[cardOrder + 1]  # 컴퓨터 카드배분
    cardOrder += 1

def indianCom():
    global comDeck
    global winRate, drawRate
    winRate, drawRate = 0, 0
    if playerCard in comDeck:
        comDeck.remove(playerCard)
    for index in comDeck:
        if playerCard < index:
            winRate += 1
        elif playerCard == index:
            drawRate += 1

def comBet():
    global winRate, drawRate
    global combetAmount, comFollow, comBetting
    comBetting = [1] * winRate
    comBetting += [0] * (len(comDeck) - winRate-1)
    random.shuffle(comBetting)
    if comBetting[0] == 1:
        comFollow = True
    elif comBetting[0] == 0:
        comFollow = False

def boardPan():
    print("--------------------------------------")
    print("상대 돈 : ", comPoint)
    print("플레이어 돈 : ", playerPoint)
    print("스킬 포인트 : ", skillPoint)
    print("--------------------------------------")

indianDeck = shuffleDeck()
comDeck = indianDeck
comBetting = []

while indianPlaying:
    if playerPoint <=0 or comPoint <=0 :
        if playerPoint <= 0:
            print("player 사망")
            break
        elif comPoint <= 0:
            print("com 사망")
            break
    drawCard()
    boardPan()
    while betNum > 0:
        indianCom()
        comBet()
        if playerPoint <= 0 or comPoint <= 0:
            if playerPoint <= 0:
                break
            elif comPoint <= 0:
                break
        if betNum == 1:
            print("상대 카드는 :", comCard)
            print("내카드 ", playerCard)
            betAmount = int(input("베팅값 입력(0 입력시 포기) : "))
        else:
            betAmount = int(input("베팅값 입력(0 입력시 포기, 99입력시 패까기) : "))
        if betAmount > 0 and betAmount!=99:
            nowBet += betAmount
            print("현재 베팅액 : ", nowBet)
            if comFollow == True:
                betNum += 1
                continue
            elif comFollow == False:
                print("컴퓨터 베팅 포기")
                print("내카드는 ", playerCard, "였습니다")
                if betNum == 1:
                    comPoint -=1
                    playerPoint +=1
                else:
                    comPoint -= nowBet
                    playerPoint += nowBet
                nowBet = 0
                betNum = 1
                break

        elif betAmount == 99:
            if comCard > playerCard:
                playerPoint -= nowBet
                comPoint += nowBet
                print("패배하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
            elif comCard < playerCard:
                playerPoint += nowBet
                comPoint -= nowBet
                print("승리하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
            nowBet = 0
            betNum = 1
            break

        elif nowBet + betAmount > playerPoint:
            print("베팅액 초과")

        elif nowBet +betAmount == playerPoint and nowBet+betAmount<comPoint:
            if comCard > playerCard:
                playerPoint -= nowBet+betAmount
                comPoint += nowBet+betAmount
                print("패배하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
                boardPan()
            elif comCard < playerCard:
                playerPoint += nowBet+betAmount
                comPoint -= nowBet+betAmount
                print("승리하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
                boardPan()
            nowBet = 0
            betNum = 1

        elif nowBet + betAmount >= comPoint:
            if comCard > playerCard:
                playerPoint -= nowBet+betAmount
                comPoint += nowBet+betAmount
                print("패배하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
                boardPan()
            elif comCard < playerCard:
                playerPoint += nowBet+betAmount
                comPoint -= nowBet+betAmount
                print("승리하셨습니다.")
                print("내카드는 ", playerCard, "였습니다")
                boardPan()
            nowBet = 0
            betNum = 1

        elif betAmount == 0:
            print("베팅을 포기하셨습니다. \n")
            playerPoint -= 1
            comPoint += 1
            print("내카드는 ", playerCard, "였습니다")
            nowBet = 0
            betNum = 1
            break
