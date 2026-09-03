


i = 10
r = 2
d = int(input("Enter the rounds won: "))
sum_score = 0
score = i

while d > 1:
    score += r * i * (d - 1)
    sum_score += score
    d -= 1

print("Total score:", score)