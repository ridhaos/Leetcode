class ListNode():
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new = self
        while new.next:
            new = new.next
        new.next = ListNode(val)
        self = new
    
def printAllnode(head:ListNode):
    element = []
    while head:
        element.append(str(head.val))
        head = head.next
    print(" -> ".join(element))

def sumOftList(l1:ListNode, l2:ListNode, carry=0):
    

    if l1 == None and l2 == None and carry==0:
        return None
    
    sum = l1.val + l2.val + carry
    newcarry = sum // 10
    newdigit = sum % 10

    lSum = ListNode(newdigit)
    
    lSum.next = sumOftList(l1.next, l2.next, newcarry)
    
    return lSum



num1 = ListNode(1)
num1.append(1)
num1.append(1)

num2 = ListNode(2)
num2.append(2)
num2.append(2)

summ = sumOftList(num1,num2)
printAllnode(num1)
printAllnode(num2)
printAllnode(summ)