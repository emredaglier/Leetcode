class Solution:
    def merge_sort(self, l:list):
        arr = l[::]
        if len(arr) < 2:
            return arr
        mid = len(arr)//2;
        left = arr[:mid]
        right = arr[mid:]
        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self, l, r):
        arr = []
        i = j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr.append(l[i])
                i += 1
            else:
                arr.append(r[j])
                j += 1
        while i < len(l):
            arr.append(l[i])
            i += 1
        while j < len(r):
            arr.append(r[j])
            j += 1
        return arr
    
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = nums1 + nums2
        
        arr = self.merge_sort(arr)

        if len(arr) % 2 == 0:
            return (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2 - 1)]) / 2
        
        return arr[int(len(arr) / 2)]
        
        
        
_ = Solution()

print(_.findMedianSortedArrays([1,2], [3,4]))
        