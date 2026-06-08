class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)

        for card in sorted(count):
            while count[card] > 0:
                for next_card in range(card, card + groupSize):
                    if count[next_card] == 0:
                        return False
                    count[next_card] -= 1
        return True