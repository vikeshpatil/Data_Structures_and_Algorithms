class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def Is_List_empty(self):
        if self.head is None:
            return True
        
        return False


    def printList(self):
        if self.Is_List_empty():
            print('List is empty')
            return

        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        
        print()

    def insertAtStart(self, new_data):      # time complexity = O(1)
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    
    def append(self, new_data):             #time complexity = O(n)
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertAfterNode(self, prev_node, new_data):      #time complexity = O(1)
        new_node = Node(new_data)

        if prev_node is Node:
            print("Previous node must be in Linked List")
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAfterValue(self, desiredValue, new_data):
        temp = self.head

        while temp != None and temp.data != desiredValue:
            temp = temp.next

        if temp is None:
            print('Element '+ str(desiredValue) +' is not in list')
            return
        else:
            new_node = Node(new_data)
            new_node.next = temp.next
            temp.next = new_node



if __name__ == '__main__':
    
    linkeList = LinkedList()
    
    linkeList.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    linkeList.head.next = second
    second.next = third

    linkeList.printList()   # 1 -> 2 -> 3

    linkeList.insertAtStart(4)
    linkeList.printList()   # 4 -> 1 -> 2 -> 3

    linkeList.append(5)
    linkeList.printList()   # 4 -> 1 -> 2 -> 3 -> 5

    linkeList.insertAfterNode(second, 6)
    linkeList.printList()   # 4 -> 1 -> 2 -> 6 -> 3 -> 5

    linkeList.insertAfterValue(3, 7)
    linkeList.printList()   # 4 -> 1 -> 2 -> 6 -> 3 -> 7 -> 5

