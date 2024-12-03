players = ["Alex", "Jake", "Trevor", "Matias", "aJ", "Leonardo"]

def sorting():
    for i in range(0, len(players)-1): # we only range till 5, we dont have to go to 6
        for a in range(0,len(players)-1):
            if players[a] > players[a+1]:# here it goes till 6, but we need to stop at 5
                players[a], players[a+1] = players[a+1], players[a]
    print(players)

sorting()