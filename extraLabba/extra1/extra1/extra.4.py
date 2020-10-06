#############################################################
# Mid string
# Given a string of odd length greater 7
# return a string made of the middle three chars of a
# given String
# Original String is JhonDipPeta
# Middle three chars are Dip
# ?? 是指大於7嗎
#############################################################

while True:
    inputstr = input("Write a string of odd length more than 7 tecken -> ")
    if len(inputstr)<=7 or len(inputstr)%2 == 0: print("Wrong string, try again -> ")
    else: break
midindex=int((len(inputstr)-1)/2)
start=midindex-1
end=midindex+2
print(inputstr[start:end])