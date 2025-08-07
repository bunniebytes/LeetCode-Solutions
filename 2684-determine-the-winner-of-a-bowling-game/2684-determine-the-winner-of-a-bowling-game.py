class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        player1_score = self.findScore(player1)
        player2_score = self.findScore(player2)

        if player1_score > player2_score:
            return 1
        elif player1_score < player2_score:
            return 2
        else:
            return 0


    def findScore(self, scores: List[int]):
        _sum = scores[0]
        for idx, score in enumerate(scores):
            if idx >= 2:
                if scores[idx - 1] == 10 or scores[idx - 2] == 10:
                    _sum += score * 2
                else:
                    _sum += score
            elif idx == 1:
                if scores[idx - 1] == 10:
                    _sum += score * 2
                else:
                    _sum += score
        return _sum