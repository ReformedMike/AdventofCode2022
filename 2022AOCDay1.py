with open('Data.in') as file:
    data =[i for i in file.read().strip().split("\n")]

#print(data)

max = 0
count = 0

for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max = count
print("The greatest amount of calories that one elf is carrying is", max)

EachElfTotalCalories = []
total = 0
for snack in data:
    if snack != '':
        number = int(snack)
        total += number

    else:
        EachElfTotalCalories.append(total)
        total = 0

EachElfTotalCalories.sort(reverse=True)

TotalCaloriesofTop3Elves = EachElfTotalCalories[0]+EachElfTotalCalories[1]+EachElfTotalCalories[2]

print("The top 3 Elves combines Calories is ", TotalCaloriesofTop3Elves)


