class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def length(self):
        count = 0
        if self.head is not None:
            node = self.head
            while node:
                count += 1
                node = node.next
        return count    
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < self.length():
            current_node = self.head
            idx = 0
            result = -1

            while current_node:

                if idx == index:
                    return current_node.val
                    break
                else:
                    current_node = current_node.next
                    idx += 1
        return -1
        
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is not None:
            NewNode = ListNode(val)
            NewNode.next = self.head
            self.head = NewNode
        else:
            self.head = ListNode(val = val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is not None:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = ListNode(val = val)
        else:
            self.head = ListNode(val = val)


        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            #addAtHead
            node = ListNode(val = val)
            if self.head is not None:
                node.next = self.head
                self.head = node
            else:
                self.head = node
            return
        if index < self.length():
            count = 0
            node = self.head
            while count != index - 1:
                node = node.next
                count += 1
            next_node = node.next
            Node_1 = ListNode(val = val)
            node.next = Node_1
            Node_1.next = next_node
        elif index == self.length():
            #addAtTail
            node = self.head
            while node.next is not None:
                node = node.next
            Node1 = ListNode(val = val)
            node.next = Node1



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        DummyNode = ListNode(None)
        DummyNode.next = self.head
        idx = 0

        current_node = DummyNode.next
        previous_node = DummyNode

        while current_node:
            if index == 0:
                self.head = self.head.next
                return
            elif idx == index:
                previous_node.next = current_node.next
                current_node = current_node.next
                break
          
            idx += 1
            previous_node = current_node
            current_node = current_node.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)