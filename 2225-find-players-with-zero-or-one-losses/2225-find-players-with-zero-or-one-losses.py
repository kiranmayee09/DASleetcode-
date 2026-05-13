class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losses = {}

        for winner, loser  in matches:

            if winner not in losses:
                losses[winner] = 0

            if loser not in losses:
                losses[loser] = 1
            else:
                losses[loser] += 1
        
        zero_loss = []
        one_loss = []

        for player in losses:

            if losses[player] == 0:
                zero_loss.append(player)

            elif losses[player] == 1:
                one_loss.append(player)

        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]