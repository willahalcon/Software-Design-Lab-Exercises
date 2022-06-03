# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class LinkedList
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Delete first node of the list
  def pop_front(self):
    if(self.head != None):
      temp = self.head
      self.head = self.head.next
      temp = None

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code
MyList = LinkedList()

#Add four elements in the list.
MyList.push_back("Mon")
MyList.push_back("Tue")
MyList.push_back("Wed")
MyList.push_back("Thur")
MyList.PrintList()

#Delete the first node
MyList.pop_front()
MyList.PrintList()