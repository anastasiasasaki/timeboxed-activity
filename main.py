


i = 10
r = 2
d = 3
sum_score = 0
score = i

while d > 1:
    score += r * i*(d-1)
    sum_score += score
    d = d - 1

print("Total score:", score)