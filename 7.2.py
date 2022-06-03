#Each node contain two parts...
#data part and pointer to point to next node
#Read all the elements in L list
#and then add the elements of M list into List L
class Node(object):
   def __init__(self, data = None, next_node = None ):
       self.data = data #data part
       self.next = next_node #pointer to point to next node
def MergeLists (headL, headM):#method that takes two linked lists
   head = tail = Node(' ',None)
   while headL or headM:
       if headL is not None: #checking whether headL is empty node or not
           if (headL and headL.data <= headM.data) or (headM is None):
               tail.next = headL
               tail = headL
               headL = headL.next
       if headM is not None: ##checking whether headL is empty node or not
           if ( headL and headM.data <= headL.data) or (headL is None):
               tail.next = headM
               tail = headM
               headM = headM.next
   return head.next