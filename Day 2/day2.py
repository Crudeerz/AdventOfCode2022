'''
w = 'A Y', 'B Z', 'C X'
l = 'A Z', 'B X', 'C Y'
d = 'A X', 'B Y', 'C Z'
'''


def RockPaperScissor():
  
    sPoints = {

        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    wPoints = {

        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3
    }

    
    with open("Day 2\strategyguide.txt") as f:
        games = f.readlines()
        tPoints = 0
        #print(games)

        for game in games:
            game = game.strip().split(" ")
            result = wPoints[game[0] + game[1]]
            tPoints += result + sPoints[game[1]]
        print(tPoints)


    





def main():
        RockPaperScissor()


if __name__ == "__main__":

    main()
