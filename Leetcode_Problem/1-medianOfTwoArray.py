class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1 + nums2
        a.sort()
        
        if len(a)%2 != 0:
            return float(a[len(a) // 2])
        else:
            m1 = len(a) // 2
            m2 = m1-1
            return (a[m1]+ a[m2]) / 2
   

s = Solution()
print(s.findMedianSortedArrays([1, 3, 4, 8], [2,3]))
