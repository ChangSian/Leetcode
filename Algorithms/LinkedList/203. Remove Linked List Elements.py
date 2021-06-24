# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 直接使用原来的鏈表来進行刪除操作
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        # move head until its value is not val
        while head and head.val == val:
            head = head.next

        else:
            previous_node = None
            current_node = head

            while current_node:


                # remove all consequitive vals
                while current_node and current_node.val == val:
                    previous_node.next = current_node.next
                    current_node = current_node.next

                # or move pointers
                else:

                    if current_node:
                        previous_node = current_node
                        current_node = current_node.next
        return head

## 設置一個虛擬頭節點在進行刪除操作
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        DummyNode = ListNode()
        DummyNode.next = head

        previous_node = DummyNode
        current_node = DummyNode.next

        while current_node:
            
            # remove all consequitive vals
            while current_node and current_node.val == val:
                
                previous_node.next = current_node.next
                current_node = current_node.next

             # or move pointers
            else:
                if current_node:
                    previous_node = current_node
                    current_node = current_node.next
                        
        return DummyNode.next


