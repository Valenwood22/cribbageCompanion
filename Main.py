import itertools
import math
import random
from collections import defaultdict

class CribCompanion:
    def __init__(self):
        self.deck = [(1,'A','H'), (2,'2','H'), (3,'3','H'), (4,'4','H'), (5,'5','H'), (6,'6','H'), (7,'7','H'), (8,'8','H'), (9,'9','H'), (10,'10','H'), (10,'J','H'), (10,'Q','H'), (10,'K','H'),
                     (1,'A','D'), (2,'2','D'), (3,'3','D'), (4,'4','D'), (5,'5','D'), (6,'6','D'), (7,'7','D'), (8,'8','D'), (9,'9','D'), (10,'10','D'), (10,'J','D'), (10,'Q','D'), (10,'K','D'),
                     (1,'A','C'), (2,'2','C'), (3,'3','C'), (4,'4','C'), (5,'5','C'), (6,'6','C'), (7,'7','C'), (8,'8','C'), (9,'9','C'), (10,'10','C'), (10,'J','C'), (10,'Q','C'), (10,'K','C'),
                     (1,'A','S'), (2,'2','S'), (3,'3','S'), (4,'4','S'), (5,'5','S'), (6,'6','S'), (7,'7','S'), (8,'8','S'), (9,'9','S'), (10,'10','S'), (10,'J','S'), (10,'Q','S'), (10,'K','S') ]
        self.deckMap = {"AH":(1,'A','H'), "2H":(2,'2','H'), "3H":(3,'3','H'), "4H":(4,'4','H'), "5H":(5,'5','H'), "6H":(6,'6','H'), "7H":(7,'7','H'), "8H":(8,'8','H'), "9H":(9,'9','H'), "0H":(10,'10','H'), "JH":(10,'J','H'), "QH":(10,'Q','H'), "KH":(10,'K','H'),
                        "AD":(1,'A','D'), "2D":(2,'2','D'), "3D":(3,'3','D'), "4D":(4,'4','D'), "5D":(5,'5','D'), "6D":(6,'6','D'), "7D":(7,'7','D'), "8D":(8,'8','D'), "9D":(9,'9','D'), "0D":(10,'10','D'), "JD":(10,'J','D'), "QD":(10,'Q','D'), "KD":(10,'K','D'),
                        "AC":(1,'A','C'), "2C":(2,'2','C'), "3C":(3,'3','C'), "4C":(4,'4','C'), "5C":(5,'5','C'), "6C":(6,'6','C'), "7C":(7,'7','C'), "8C":(8,'8','C'), "9C":(9,'9','C'), "0C":(10,'10','C'), "JC":(10,'J','C'), "QC":(10,'Q','C'), "KC":(10,'K','C'),
                        "AS":(1,'A','S'), "2S":(2,'2','S'), "3S":(3,'3','S'), "4S":(4,'4','S'), "5S":(5,'5','S'), "6S":(6,'6','S'), "7S":(7,'7','S'), "8S":(8,'8','S'), "9S":(9,'9','S'), "0S":(10,'10','S'), "JS":(10,'J','S'), "QS":(10,'Q','S'), "KS":(10,'K','S')}


        self.shuffleDeck()
        self.hand1 = self.dealCards(6) #self.dealCertainCards([(10, 'J', 'D'),(10, 'J', 'H'),(10, 'J', 'S'), (10, 'J', 'C')])
        self.hand2 = self.dealCards(6) #self.dealCertainCards([(1, 'A', 'D'), (1, 'A', 'S'), (10, 'Q', 'D'), (10, 'Q', 'S')])
        self.cut = self.cutDeck()
        print("p1 hand", self.hand1)
        print("p2 hand", self.hand2)
        print("cut", self.cut)




    def shuffleDeck(self):
        random.shuffle(self.deck)




    def dealCards(self, nDeal):
        hand = self.deck[:nDeal]
        self.deck = self.deck[nDeal:]
        return hand


    def cutDeck(self):
        return self.deck.pop(0)



    def dealCertainCards(self, cards):
        for card in cards:
            self.deck.remove(card)
        return cards



    def chooseBestHand(self, hand, cut, hand2, throw):
        combinationsObj = itertools.combinations(hand, len(hand)-throw)
        combList = list(combinationsObj)
        tempDeck = self.deck.copy()
        tempDeck.extend(hand2)
        tempDeck.append(cut)
        deckLen = len(tempDeck)
        bestAvg = -1
        bestHand = None
        for combo in combList:
            modifierMap = defaultdict(int)
            baseHand = self.countHand(list(combo))

            for card in tempDeck:
                modifierMap[self.countHand(list(combo), cut=card)] += 1
            # key = numpts, val = hands that will get you those points
            s= ""
            avg = 0
            itemList = sorted(modifierMap.items(), key=lambda x:x[0])
            for key, val in itemList:
                avg += (key*val/deckLen)
                # s += f" pts {key}:{val/deckLen:.2f}"
            avg = round(avg,4)
            if bestAvg < avg:
                bestAvg = avg
                bestHand = combo
        print(bestHand, "Best Avg pts", bestAvg)



    def countHand(self, hand, cut=None, isCrib=False):
        # 15's
        def count15s(hand):
            num15s = 0
            for r in range(2, len(hand) + 1):
                combinationsObj = itertools.combinations(hand, r)
                combList = list(combinationsObj)
                for combo in combList:
                    if sum([x[0] for x in combo]) == 15:
                        num15s += 1
            return num15s*2


        # pairs
        def countPairs(hand):
            pairMap = defaultdict(int)
            pairPts = 0
            for card in hand:
                pairMap[card[1]] += 1
            for val in pairMap.values():
                if val == 0 or val == 1:
                    continue
                elif val == 2:
                    pairPts += 2
                elif val == 3:
                    pairPts += 6
                elif val == 4:
                    pairPts += 12
            return pairPts

        # runs
        def countRuns(hand):
            def numDup(card, duplicate, interpreter):
                ans = 1
                for dupCard in duplicates:
                    if interpreter[card[1]] == interpreter[dupCard[1]]:
                        ans += 1
                return ans

            interpreter = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
            runPts = 0
            hand.sort(key=lambda x:interpreter[x[1]])
            i = 0
            duplicates = []
            while i < len(hand)-1:
                if interpreter[hand[i + 1][1]] == interpreter[hand[i][1]]:
                    duplicates.append(hand.pop(i+1))
                else:
                    i += 1

            runIndexes = []
            i = 0
            while i < len(hand)-2:
                if interpreter[hand[i+1][1]] == interpreter[hand[i][1]]+1 and interpreter[hand[i+2][1]] == interpreter[hand[i+1][1]]+1:
                    runIndexes.append([i])
                    i += 2
                    while i < len(hand)-1:
                        if interpreter[hand[i+1][1]] == interpreter[hand[i][1]]+1:
                            i += 1
                        else:
                            break
                    runIndexes[-1].append(i)
                i += 1
            for runs in runIndexes:
                dupTracker = []
                for i in range(runs[0],runs[1]+1):
                    dupTracker.append(numDup(hand[i], duplicates, interpreter))
                runPts += math.prod(dupTracker) * (runs[1] - runs[0] + 1)
            return runPts

        # flushes
        def countFlush(hand, cut, isCrib):
            suit = hand[0][2]
            for card in hand[1:]:
                if card[2] != suit:
                    return 0
            if isCrib:
                if cut[2] == suit:
                    return len(hand) + 1
                return 0
            else:
                if cut:
                    if cut[2] == suit:
                        return len(hand) + 1
                return len(hand)

        # knobs
        def countKnobs(hand, cut):
            if cut != None:
                for card in hand:
                    if card[1] == 'J' and cut[2] == card[2]:
                        return 1
            return 0
        if cut:
            fullhand = hand.copy()
            fullhand.append(cut)
            pts15 = count15s(fullhand)
            ptsFlush = countFlush(hand, cut, isCrib)
            ptsPairs = countPairs(fullhand)
            ptsRuns = countRuns(fullhand)
            ptsknobs = countKnobs(hand, cut)
        else:
            pts15 = count15s(hand)
            ptsFlush = countFlush(hand, None, isCrib)
            ptsPairs = countPairs(hand)
            ptsRuns = countRuns(hand)
            ptsknobs = 0
        return pts15 + ptsFlush + ptsPairs + ptsRuns + ptsknobs





    def pegging(self, hand1, hand2, cut=None, turn="p1"):
        def findBestPlay(options, playOrder, totalPts, interpreter):
            mx = -1
            ans = None
            for i, card in enumerate(options):
                playOrder.append(card)
                tempScore = score(playOrder, totalPts+card[0], interpreter)
                playOrder.pop()
                if tempScore > mx:
                    mx = tempScore
                    ans = card
            return ans

        def formatHand(hand):
            ans = []
            for card in hand:
                ans.append(card[1]+card[2])
            return ans

        def legalPlays(hand, totalPts):
            ans = []
            for card in hand:
                if totalPts + card[0] <= 31:
                    ans.append(card)
            return ans

        def getLastC(lastCard, p1pts, p2pts):
            if lastC == "p1":
                return p1pts+1, p2pts
            else:
                return p1pts, p2pts+1

        def score(playOrder, totalPts, interpreter):
            ans = 0
            # 15's
            if totalPts == 15:
                ans += 2
            elif totalPts == 31:
                ans += 2

            # runs there is a small bug here
            if len(playOrder) >= 3:
                last3 = [interpreter[card[1]] for card in playOrder[-3:]]
                last3.sort()
                if last3[0] == last3[1]-1 and last3[1] == last3[2]-1:
                    ans += 3
                    i = 4
                    gate = True
                    while i<=len(playOrder):
                        last = [interpreter[card[1]] for card in playOrder[-i:]]
                        last.sort()
                        j=0
                        while j<len(last)-1:
                            if last[j] != last[j+1] -1:
                                gate = False
                                break
                            j+=1
                        if not gate:
                            break
                        ans += 1
                        i += 1

            # pairs
            if len(playOrder) == 2:
                if playOrder[-1][1] == playOrder[-2][1]:
                    ans += 2

            if len(playOrder) == 3:
                if playOrder[-1][1] == playOrder[-2][1] and playOrder[-2][1] == playOrder[-3][1]:
                    ans += 6
                elif playOrder[-1][1] == playOrder[-2][1]:
                    ans += 2

            if len(playOrder) >= 4:
                if playOrder[-1][1] == playOrder[-2][1] and playOrder[-2][1] == playOrder[-3][1] and playOrder[-3][1] == playOrder[-4][1]:
                    ans += 12
                elif playOrder[-1][1] == playOrder[-2][1] and playOrder[-2][1] == playOrder[-3][1]:
                    ans += 6
                elif playOrder[-1][1] == playOrder[-2][1]:
                    ans += 2
            return ans

        # ===== Driver Code =====
        interpreter = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        player1Pts = 0
        player2Pts = 0
        if cut[1] == 'J':
            if turn == "p1": player2Pts += 2
            if turn == "p2": player1Pts += 2
        hand1Temp = hand1.copy()
        hand2Temp = hand2.copy()
        playOrder = []
        totalPts = 0
        stateP1 = "P"
        stateP2 = "P"
        lastC = ""
        while len(hand1Temp) > 0 or len(hand2Temp) > 0:
            print(totalPts, player1Pts, player2Pts, playOrder)
            if turn == "p1":
                turn = "p2"
                playCard = input("Play a card Hand "+ str(formatHand(hand1Temp)) + ": ")
                if playCard == "GO":
                    if stateP2 == "GO":
                        stateP1 = "P"
                        stateP2 = "P"
                        totalPts = 0
                        player1Pts, player2Pts = getLastC(lastC, player1Pts, player2Pts)
                    else:
                        stateP1 = "GO"
                    continue
                playCard = self.deckMap[playCard]
                playOrder.append(playCard)
                totalPts += playCard[0]
                hand1Temp.remove(playCard)
                lastC = "p1"
                player1Pts += score(playOrder, totalPts, interpreter)
                if totalPts == 31:
                    stateP1 = "P"
                    stateP2 = "P"
                    totalPts = 0
                    if len(hand2Temp) == 0 and len(hand1Temp) == 0:
                        totalPts = 31
            else:
                turn = "p1"
                t = legalPlays(hand2Temp, totalPts)
                if len(t) == 0:
                    if stateP1 == "GO":
                        stateP1 = "P"
                        stateP2 = "P"
                        totalPts = 0
                        player1Pts, player2Pts = getLastC(lastC, player1Pts, player2Pts)
                    else:
                        stateP2 = "GO"
                    continue

                playCard = findBestPlay(t, playOrder, totalPts, interpreter)# random.choice(t)
                playOrder.append(playCard)
                totalPts += playCard[0]
                hand2Temp.remove(playCard)
                lastC = "p2"
                player2Pts += score(playOrder, totalPts, interpreter)
                if totalPts == 31:
                    stateP1 = "P"
                    stateP2 = "P"
                    totalPts = 0
                    if len(hand2Temp) == 0 and len(hand1Temp) == 0:
                        totalPts = 31

        if totalPts != 31:
            player1Pts, player2Pts =  getLastC(lastC, player1Pts, player2Pts)
        print(totalPts, player1Pts, player2Pts, playOrder)
        return player1Pts, player2Pts



if __name__ == '__main__':
    c = CribCompanion()
    # print(c.hand1)
    print(c.pegging(c.hand1, c.hand2, cut=c.cut))
    # print(c.chooseBestHand(c.hand1, c.cut, c.hand2, 2))
