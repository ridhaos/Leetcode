# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if len(list1) == 0 and len(list2) == 0:
            return []

        elif len(list1) == 0 and len(list2) > 0:
            return list2
        
        elif len(list1) > 0 and len(list2) == 0:
            return list1

        globalList = []
        while(len(list1) != 0 and len(list2) != 0):
            if list1[0] >= list2[0]:
                globalList.append(list2.pop(0))
            else:
                globalList.append(list1.pop(0))
        
        if len(list1) > 0:
            globalList.extend(list1)
        elif len(list2) > 0:
            globalList.extend(list2)
            
        return globalList

s = Solution()
print(s.mergeTwoLists([1,2,4], [1,3,4]))
        # while(list2.next == None or list2.next == None):
        #     if list1.val <= list2.val:
        #         list1 = list1.next
        #     elif list1.val > list2.val:
        #         list1.next = list2
        #         list1 = list1.next
        
        # return list1
                

        