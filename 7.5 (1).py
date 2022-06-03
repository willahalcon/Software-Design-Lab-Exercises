#Represents the node of the list.    
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;    
     
class CreateList:    
    #Declaring head and tail pointer as null.    
    def __init__(self):    
        self.count = 0;    
        self.head = Node(None);    
        self.tail = Node(None);    
        self.head.next = self.tail;    
        self.tail.next = self.head;    
        
    #This function will add the new node at the end of the list.    
    def add(self,data):    
        newNode = Node(data);    
        #Checks if the list is empty.    
        if self.head.data is None:    
            #If list is empty, both head and tail would point to new node.    
            self.head = newNode;    
            self.tail = newNode;    
            newNode.next = self.head;    
        else:    
            #tail will point to new node.    
            self.tail.next = newNode;    
            #New node will become new tail.    
            self.tail = newNode;    
            #Since, it is circular linked list tail will point to head.    
            self.tail.next = self.head;    
                
    #This function will count the nodes of circular linked list    
    def countNodes(self):    
        current = self.head;    
        self.count=self.count+1;    
        while(current.next != self.head):    
            self.count=self.count+1;    
            current = current.next;    
        print("Count of nodes present in circular linked list: "),    
        print(self.count);    
        
     
class CircularLinkedList:    
    cl = CreateList();    
    #Adds data to the list    
    cl.add(1);    
    cl.add(2);    
    cl.add(4);    
    cl.add(1);    
    cl.add(2);    
    cl.add(3);    
    #Displays all the nodes present in the list    
    cl.countNodes();