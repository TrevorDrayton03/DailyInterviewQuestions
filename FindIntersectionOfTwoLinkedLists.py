# Hi, here's your problem today. This problem was recently asked by Apple:

# You are given two singly linked lists. The lists intersect at some node.
# Find, and return the node. Note: the lists are non-cyclical.

# Example:

# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4

# This should return 3 (you may assume that any nodes with the same value are the same node).

# This is the easy way because I know the difference in length is only 1 between the two linked lists (which is key).
# Otherwise, you'd need to make a loop that determines the length of each node and then chooses which one has the larger
# length, then remove the difference in lengths off the larger list then compare like how I did.
def intersection(a, b):
    cur_a, cur_b = a,b
    for i in range(1):
        cur_a = cur_a.next
    while(cur_a != cur_b):
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a


class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
