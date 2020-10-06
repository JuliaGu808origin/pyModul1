#################################################
# Given a two list. 
# Create a third list by picking 
# an odd-index element from the first list
# and even index elements from second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# ?? 是從零開始算嗎
#################################################

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listlen = len(listOne)
listThree = [listTwo[i] if i % 2 == 0 else listOne[i] for i in range(listlen)]
print(listThree)