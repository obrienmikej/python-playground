class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to act as the starting point
    dummy = ListNode()
    tail = dummy
    
    # While both linked lists have nodes left to process
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    # If there are remaining nodes in list1 or list2, append them
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    # Return the merged list, starting from the node after dummy
    return dummy.next

# Helper functions for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# testing notes, keep for reference

# define first list
list1 = [1,3,5]
print(f"list1: {list1}")

# define second list
list2 = [2,4,6]
print(f"list2: {list2}")

# combine list, based on id in list
list_from_id = list1[0], list2[1]
print(f"list_from_id: {list_from_id}")

joinlist = list1 + list2
print(f"joinlist: {joinlist}")