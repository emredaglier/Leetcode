
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort = sorted(score, reverse=True)

        for index in range(len(score)):
            if index == 0:
                score[score.index(sort[0])] = 'Gold Medal'

            elif index == 1:
                score[score.index(sort[1])] = 'Silver Medal'
        
            elif index == 2:
                score[score.index(sort[2])] = 'Bronze Medal'

            else:
                score[score.index(sort[index])] = str(index + 1)

        return score




_ = Solution()

print(_.findRelativeRanks([5,4,3,2,1]))