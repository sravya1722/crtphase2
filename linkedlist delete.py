#deletetail

'''class node:
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
def deletetailnode(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentnode=head
    while currentnode.next != None:
        previous=currentnode
        currentnode=currentnode.next
    previous.next=None
    return head
nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertattail(head,ele)
    printlinkedlist(head)
print("Final linked list is:")
printlinkedlist(head)
deletetailnode(head)
printlinkedlist(head)'''

#deletehead

'''class node:
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
def insertathead(head,ele):
    temp=node(ele)
    temp.next=head
    return temp
def deleteheadnode(head):
    if head==None:
        return head
    secondnode=head.next
    head.next=None
    return secondnode
nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertattail(head,ele)
    printlinkedlist(head)
print("Final linked list is:")
printlinkedlist(head)
head=deleteheadnode(head)
printlinkedlist(head)'''

#deletespecificposition




















