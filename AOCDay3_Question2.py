#import data from text file
with open ('AOC_Day3_Data.txt') as file:
    Letter_Lines = [line.strip() for line in file.readlines()]

#Dictonary for converting letters to numbers
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_Conversion = {}
for x in range(len(characters)):
    alphabet_Conversion[characters[x]] = x+1

#Create a list of letters converted to numbers
Number_Lines = [
    [alphabet_Conversion.get(ch, ch) for ch in word]
    for word in Letter_Lines
]
Number_Lines_Sets =[]
#Convert lists of numbers to sets of numbers
for lists in Number_Lines:
    lists = set(lists)
    Number_Lines_Sets.append(lists)

Badges = []
x = 0

for sets in Number_Lines_Sets:
    GroupBadge = Number_Lines_Sets[x].intersection(Number_Lines_Sets[x+1], Number_Lines_Sets[x+2])
    Badges.append(GroupBadge)
    x += 3

    if x == 300:
        break

BadgeTotal = 0
for num in Badges:
    badge = num.pop()
    BadgeTotal += badge

print(BadgeTotal)


























