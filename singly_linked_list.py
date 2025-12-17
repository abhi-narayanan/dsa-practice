class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            print("Given key is not present in the list")
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            print("Given position is greater than number of elements in the list")
            return
        
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        cur_node = self.head
        count = 0
        while cur_node:
            count +=1
            cur_node = cur_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    # A -> B -> C -> D -> 0
    # D -> C -> B -> A -> 0
    # A <- B <- C <- D <- 0

    def reverse_iterative(self):

        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev

            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CUR")
            self.print_helper(nxt, "NEXT")
            print("\n")

            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        
        p = self.head
        q = llist.head

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head
    
    def remove_duplicates(self):
        """
        Original list:
        1 -> 6 -> 1 -> 4 -> 2 -> 2 -> 4

        Unique list:
        1 -> 6 -> 4 -> 2
        """
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Unique element encoutered
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        # # Method 1
        # total_len = self.len_iterative()

        # cur = self.head
        # while cur:
        #     if total_len == n:
        #         return cur.data
        #     total_len -= 1
        #     cur = cur.next
        
        # if cur is None:
        #     return

        # Method 2
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        if not q:
            print(str(n) + "greater than the number of nodes in list")

        while p and q:
            p = p.next
            q = q.next
        return p.data
    
    """
    1 -> 2 -> 1 -> 3 -> 1 -> 4 -> 1
    Number of ones - 4
    """
    def count_occurences_iterative(self, data):
        
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
        
    def rotate(self, k):
        
        p = self.head
        q = self.head

        prev = None
        count = 0 

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    # RACECAR, RADAR, TEST, ABC, HELLO
    def is_palindrome(self):
        # # Method 1
        # s = ""
        # p = self.head

        # while p:
        #     s += p.data
        #     p = p.next

        # return s == s[::-1]

        # # Method 2
        # p = self.head
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True

        # Method 3
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]

        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True
    
    def move_tail_to_head(self):
        """
        A -> B -> C -> D
        D -> B -> C -> A
        """
        last = self.head
        second_to_last = None

        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last
    
    def sum_two_lists(self, llist):
        """
        3 6 5
        2 4 8
        (+)
        6 1 3
        """
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()
            

llist_1 = LinkedList()
llist_1.append(5)
llist_1.append(6)
llist_1.append(3)

llist_2 = LinkedList()
llist_2.append(8)
llist_2.append(4)
llist_2.append(2)

# llist_1.rotate(4)

# llist_1.remove_duplicates()

# llist.prepend("X")

# llist.reverse_recursive()

# llist.swap_nodes("C", "X")

# llist.insert_after_node(llist.head.next, "E")

# llist.delete_node("B")
# print("-----------")
# print(llist_1.count_occurences_iterative("1"))
# print(llist_1.count_occurences_recursive(llist_1.head, "1"))

# print(llist.len_recursive(llist.head.next))

# print(llist_2.is_palindrome())

# llist_1.move_tail_to_head()

llist_1.sum_two_lists(llist_2)

# llist_1.print_list()

"""
Given a key (data field) delete node with this field. Assume elements in linked list are unique. Example: Delete node with data field "B".
"""
"""
Two cases - 
- Node to be deleted is head
- Node to be deleted is not head
"""

"""
Node Swap - Assume data entries are unique
"""
"""
Two cases - 
- Node_1 and Node_2 are not head nodes
- Either Node_1 or Node_2 are head nodes
"""