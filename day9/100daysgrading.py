#Grading
#Outstanding    91 - 100
#Excellent      81 - 90
#Acceptable     71 - 80
#Fail           0 - 70

scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

grades = {}
#Tranfer all scores into grades

for student in scores :
    if scores[student] > 90 :
        grades[student] = "Outstanding"
    elif scores[student] > 80 :
        grades[student] = "Outstanding"
    elif scores[student] > 70 :
        grades[student] = "Acceptable"
    else : 
        grades[student] = "Fail"

print(grades)