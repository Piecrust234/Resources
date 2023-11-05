#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Optional Print List function
def printList(resultList):
    print(resultList.val)
    if resultList.next:
        printList(resultList.next)

class Solution:
    def mergeTwoLists(self, list1, list2):

       
        dummy = ListNode()  # Set the dummy. This handles edge cases, like empty lists, etc.
        tail = dummy        # Set the tail to initially be the dummy, as a starting point. (We are moving "right to left")


        while list1 and list2: # When the current value of each list is not None/empty, iterate.
            if list1.val < list2.val: # if list1.val is less than list2.val, list1.val will be popped in first.
                tail.next = list1 # setting what follows after the current tail to be this next lowest value
                list1 = list1.next # get the next value of the list1 (ie if list is 1,2,4, move to '2')
            else: # Reverse of the logic above
                tail.next = list2
                list2 = list2.next
            tail = tail.next # for the next iteration, set the tail to be the end again.

        # we reach the following logic if either of the list1 or the list2 are empty (no more next); in this case, what remains (either list1 or list2), can be slapped on at the end
        if list1: 
            tail.next = list1
        elif list2:
            tail.next = list2
        
        #optional printing of list
        printList(dummy.next)
        
        return dummy.next # return the dummy.next, because dummy is a placeholder for us to start.
    
    
        
# Define two lists for a test solution.
l1 = ListNode(val = 1)
l1.next = ListNode(val=2)
l1.next.next = ListNode(val=4)


l2 = ListNode(val=1)
l2.next = ListNode(val=3)
l2.next.next = ListNode(val=4)

# Create test solution
testSolution = Solution()
testSolution.mergeTwoLists(list1=l1,list2=l2)