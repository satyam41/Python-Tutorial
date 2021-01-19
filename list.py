# list is ordered data sequence. 

# l = ["Satyam", 1021]
# l[1] = 294782

# index is length of list - 1  n-1

# functions of list:
    # 1.append()
    # 2.extend()
    # 3.pop(), pop(index number)
    # 4.remove()
    # 5.index()
    # 6.clear()
    # 7.sort() 
    # 8.reverse sort()
    # 9.reverse()
    # 10.len()
    # 11.max()
    # 12.min()
    # 13.sum()

lst = [1,2,3,4,5,6,7,8,9,10]
# pop()
# print(lst.pop())
# print(lst.pop(4))
# print(lst)

# remove()
lst.remove(7)
# print(lst)

# append()
lst.append(12)
# print(lst)

# extend()
l = ['a','b','c',True,2.4]
lst.extend(l)
# print(lst)

# len()
# print(len(lst))
# print(lst)
lst.clear()
# print(lst)

l1 = [2,41,25,6,0,9]
# sort()
l1.sort()
# print(l1)
# reverse sort
l2 = [3,12,6,3,1,2]
l2.sort(reverse=True)
# print(l2)

l3 = [1,2,3,4,5]
# [5,4,3,2,1]
l3.reverse()
# print(l3)

# index()
# print(l3.index(5))

# max()
# print(max(l3))
# min()
# print(min(l3))
# sum()
# print(sum(l3))

l4 = [1,2,3,4,5,6,7,8,9,10]
# print(l4[0])
# print(l4[1])
# [start:stop:step]
# print(l4[0:11:2])
# print(l4[1:11:2])
