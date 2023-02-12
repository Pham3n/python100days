# GitHub token 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
# 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
summ = 0

for answer in range(1, 101):
    if answer % 2 == 0 : summ += answer

print(summ)

summ = 0
for answer in range(2, 101, 2):
    summ += answer
print(summ)