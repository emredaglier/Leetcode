List = list

#happiness = [2,3,4,5], k = 1
#             5

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        return happiness
    
    
    
_ = Solution()
print(_.maximumHappinessSum([2,3,4,5], 1))
        
        
        
        