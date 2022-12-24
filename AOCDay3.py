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

#Create a list of the numbers that are duplicated in the first and second half of each line
List_of_Duplicates = []

for list in Number_Lines:
    midpoint = len(list) // 2
    first_half = set(list[:midpoint])
    second_half = set(list[midpoint:])
    duplicates = first_half.intersection(second_half)

    List_of_Duplicates.append(duplicates)

total = sum([s.pop() for s in List_of_Duplicates])

print(total)















