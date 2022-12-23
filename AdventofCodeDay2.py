# --- Day 2: Rock Paper Scissors ---

# 1 for Rock
# 2 for Paper
# 3 for Scissors
#
# 0 if you lost
# 3 if the round was a draw
# and 6 if you won

# with open ('DataforAOCDay2') as file:
#    lines = [line.strip() for line in file.readlines()]
#
# matches = [(a, b) for a, b in (line.split() for line in lines)]
#
# translating = {
#    'A':'Rock',
#    'B':'Paper',
#    'C':'Scissors',
#    'X':'Rock',
#    'Y':'Paper',
#    'Z':'Scissors'
# }
#
# translated_Matches = [(translating.get(a, a), translating.get(b, b)) for a, b in matches]
#
# myScore = 0
#
# for (a, b) in translated_Matches:
#    if a == 'Rock' and b == "Rock":
#       myScore += 4
#
#    elif a == 'Rock' and b == 'Paper':
#       myScore += 8
#
#    elif a == 'Rock' and b == 'Scissors':
#       myScore += 3
#
#    if a == 'Paper' and b == "Rock":
#       myScore += 1
#
#    elif a == 'Paper' and b == 'Paper':
#       myScore += 5
#
#    elif a == 'Paper' and b == 'Scissors':
#       myScore += 9
#
#    if a == 'Scissors' and b == "Rock":
#       myScore += 7
#
#    elif a == 'Scissors' and b == 'Paper':
#       myScore += 2
#
#    elif a == 'Scissors' and b == 'Scissors':
#       myScore += 6
#
# print(myScore)

# For the Second Part of the problem
with open ('DataforAOCDay2') as file:
   lines = [line.strip() for line in file.readlines()]

matches = [(a, b) for a, b in (line.split() for line in lines)]

translating = {
   'A':'Rock',
   'B':'Paper',
   'C':'Scissors',
   'X':'lose',
   'Y':'draw',
   'Z':'win'
}

translated_Matches = [(translating.get(a, a), translating.get(b, b)) for a, b in matches]

myScore = 0

for (a, b) in translated_Matches:
   if a == 'Rock' and b == "lose":
      myScore += 3

   elif a == 'Rock' and b == 'draw':
      myScore += 4

   elif a == 'Rock' and b == 'win':
      myScore += 8

   elif a == 'Paper' and b == "lose":
      myScore += 1

   elif a == 'Paper' and b == 'draw':
      myScore += 5

   elif a == 'Paper' and b == 'win':
      myScore += 9

   elif a == 'Scissors' and b == "lose":
      myScore += 2

   elif a == 'Scissors' and b == 'draw':
      myScore += 6

   elif a == 'Scissors' and b == 'win':
      myScore += 7

print(myScore)






