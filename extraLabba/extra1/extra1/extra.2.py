############################################################
# Write a program (function!) that takes a list and 
# returns a new list that contains all the
# elements of the first list minus all the duplicates.
# ?? 需要順序一樣嗎
############################################################
def dulpilist(listor):
    listorSet = set(listor)
    return list(listorSet)

print(dulpilist([3,5,6,4,3,7,88,5,7]))