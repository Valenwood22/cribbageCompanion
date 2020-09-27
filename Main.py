import itertools
import math
import random
from collections import defaultdict

class CribCompanion:
    def __init__(self):
        self.deck = [(1,'A','H'), (2,'2','H'), (3,'3','H'), (4,'4','H'), (5,'5','H'), (6,'6','H'), (7,'7','H'), (8,'8','H'), (9,'9','H'), (10,'10','H'), (10,'J','H'), (10,'Q','H'), (10,'K','H'),
                     (1,'A','D'), (2,'2','D'), (3,'3','D'), (4,'4','D'), (5,'5','D'), (6,'6','D'), (7,'7','D'), (8,'8','D'), (9,'9','D'), (10,'10','D'), (10,'J','D'), (10,'Q','D'), (10,'K','D'),
                     (1,'A','C'), (2,'2','C'), (3,'3','C'), (4,'4','C'), (5,'5','C'), (6,'6','C'), (7,'7','C'), (8,'8','C'), (9,'9','C'), (10,'10','C'), (10,'J','C'), (10,'Q','C'), (10,'K','C'),
                     (1,'A','S'), (2,'2','S'), (3,'3','S'), (4,'4','S'), (5,'5','S'), (6,'6','S'), (7,'7','S'), (8,'8','S'), (9,'9','S'), (10,'10','S'), (10,'J','S'), (10,'Q','S'), (10,'K','S'),]

        self.shuffleDeck()
        self.hand1 = self.dealCards(6)
        self.hand2 = self.dealCards(6)
        # print(self.hand1)






    def shuffleDeck(self):
        random.shuffle(self.deck)






    def dealCards(self, nDeal):
        hand = self.deck[:nDeal]
        self.deck = self.deck[nDeal:]
        return hand





    def countHand(self, hand, cut=None, isCrib=False):
        # 15's
        def count15s(hand, cut):
            if cut: hand.append(cut)
            num15s = 0
            for r in range(2, len(hand) + 1):
                combinationsObj = itertools.combinations(hand, r)
                combList = list(combinationsObj)
                for combo in combList:
                    if sum([x[0] for x in combo]) == 15:
                        num15s += 1
            return num15s*2


        # pairs
        def countPairs(hand, cut):
            if cut: hand.append(cut)
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
            if cut: hand.append(cut)
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
        return count15s(hand, cut) + countFlush(hand, cut) + countPairs(hand,cut) + countRuns(hand,cut) + countKnobs(hand, cut)



if __name__ == '__main__':
    c = CribCompanion()
    print(c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))

