class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        if head is None:
            return Node(data)

        current = head
        while current.next:
            current = current.next

        current.next = Node(data)

        return head

def main():
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head);   

if __name__ == '__main__':
    main()