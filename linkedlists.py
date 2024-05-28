'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj0=node(71)
obj1=node(72)
obj2=node(73)
obj3=node(74)
obj4=node(75)
obj5=node(76)
obj6=node(77)
obj7=node(78)
obj8=node(79)
obj9=node(80)
obj0.next=obj1
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
currentnode=obj0
while currentnode!=None:
    print(currentnode.data,end=" ")
    currentnode=currentnode.next'''

#insertionattail
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end=" ")
        currentnode=currentnode.next
    print()
def insertattail(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertattail(head,ele)
    printlinkedlist(head)
print("Final linked list is:")
printlinkedlist(head)'''
            
#insertionathead
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end=" ")
        currentnode=currentnode.next
    print()
def insertathead(head,ele):
    temp=node(ele)
    temp.next=head
    return temp
nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertathead(head,ele)
    printlinkedlist(head)
print("Final linked list is:")
printlinkedlist(head)'''

#insertionatspecificposition
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinkedlist(head):
    currentNode=head
    while currentNode!=None:
        print(currentNode.data,end=" ")
        currentNode=currentNode.next
    print()
def insertattail(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def insertatspecificposition(head,position,ele):
    if position==0:
        return insertatspecificposition(head,ele)
    temp=node(ele)
    index=0
    currentNode=head
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertattail(head,ele)
print("Final linked list is:")
printlinkedlist(head)
head =insertatspecificposition(head, 3, 101)
printlinkedlist(head)
    





















