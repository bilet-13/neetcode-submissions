from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def play(i, j, alice_turn):
            if i > j:
                return (0, 0)

            a1, b1 = play(i + 1, j, not alice_turn)
            a2, b2 = play(i, j - 1, not alice_turn)

            if alice_turn:
                left = (a1 + piles[i], b1)
                right = (a2 + piles[j], b2)
                return max(left, right, key=lambda x: x[0])
            else:
                left = (a1, b1 + piles[i])
                right = (a2, b2 + piles[j])
                return max(left, right, key=lambda x:x[1])
        
        alice, bob = play(0, len(piles) - 1, True)
        return alice > bob
