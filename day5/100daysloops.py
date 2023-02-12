
#fruits = ["Apple", "Pie", "Banana"]
#for fruit in fruits : print(fruit)

#Average Height - Calculate average height from a list of heights

heights = [180, 124, 165, 173, 189, 169, 146]
index = 0
sum_ = 0

for height in heights:
    index += 1
    sum_ += height

average = round(sum_ / index, 2)
print(average)

print(round(sum(heights) / len(heights)))

#Highest Scores
inp =  input("Enter numbers, separated by space").split()
scores = [] #[78, 65, 89, 55, 91, 64, 89]
count = 0
for iput in inp : 
    scores.append(int(iput))
    count += 1


for score in scores:
    if score > count : count = score
print(f"The highest score in the class is: {count}")

count = scores[0]

for score in scores:
    if score < count : count = score

print(f"The lowest score in the class is: {count}")
