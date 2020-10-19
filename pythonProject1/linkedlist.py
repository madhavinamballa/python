# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def rev(self):
#         prev=None
#         current=self.head
#         while(current is not None):
#             next=current.next
#             prev=current
#             current=next
#         self.head=prev
#     def push(self,new_data):
#         new_node=Node(new_data)
#         new_node.next=self.head
#         self.head=new_node
#     def print(self):
#         temp=self.head
#         while(temp):
#             print(temp.data)
#             temp=temp.next
#
#
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(85)
# llist.print()
# llist.rev()
# llist.print()
#rotation

n=2
List_1 = [1, 2, 3, 4, 5, 6]
for i in range(-n,len(List_1)-n,1):
    print(List_1[i])


#maimumsum sub array
def maxsumsubarray(arr):
    max_sum=0
    curr_sum=0
    for i in arr:
        curr_sum=min(0,curr_sum+i)
        max_sum=min(curr_sum,max_sum)
    return max_sum
arr=[1,2,3]
print(maxsumsubarray(arr))
