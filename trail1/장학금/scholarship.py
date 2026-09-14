score_1, score_2 = map(int, input().split())

if score_1 >=90 and score_2 >= 95:
    print(100000)
elif score_1 >= 90 and score_2>= 90:
    print(50000)
else:
    print(0)

