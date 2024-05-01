# TODO


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        first, second, third = sorted(score, reverse=True)[:3]
        score[score.index(first)] = 'Gold Medal'
        score[score.index(second)] = 'Silver Medal'
        score[score.index(third)] = 'Bronze Medal'

        return [str(x) for x in score if type(x)]

    

_ = Solution()

print(_.findRelativeRanks([10,3,8,9,4]))