#TFT Calc

def goldAmount():
    currentGold = 0
    winStreak = 0
    winStreakGold = 0
    lossStreak = 0
    lossStreakGold = 0
    interestGold = 0
    roundGold = 5
    
    currentGold = int(input('How much Gold do you have?'))
    print(currentGold)
    winStreak = int(input('Win Streak amount?'))
    print(winStreak)
    lossStreak = int(input('Loss Streak amount?'))
    print(lossStreak)

    if currentGold >= 10 and currentGold < 20:
        interestGold = 1
    elif currentGold >= 20 and currentGold < 30:
        interestGold = 2
    elif currentGold >= 30 and currentGold < 40:
        interestGold = 3
    elif currentGold >= 40 and currentGold < 50:
        interestGold = 4
    elif currentGold >= 50:
        interestGold = 5
    else:
        interestGold = 0
    
    if winStreak == 1:
        winStreakGold = 1
    elif winStreak == 2:
        winStreakGold = 2
    elif winStreak == 3:
        winStreakGold = 3
    elif winStreak == 4:
        winStreakGold = 4
    elif winStreak >= 5:
        winStreakGold = 5
    else:
        winStreakGold = 0

    if lossStreak == 1:
        lossStreakGold = 1
    elif lossStreak == 2:
        lossStreakGold = 2
    elif lossStreak == 3:
        lossStreakGold = 3
    elif lossStreak == 4:
        lossStreakGold = 4
    elif lossStreak >= 5:
        lossStreakGold = 5
    else:
        lossStreakGold = 0
    

    newGoldAmount = currentGold + interestGold + winStreakGold + lossStreakGold + roundGold
    print(newGoldAmount)
goldAmount()
