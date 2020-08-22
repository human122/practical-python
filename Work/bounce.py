# bounce.py
#
# Exercise 1.5

height = 100

def bounce(h):
    return h * 3 / 5

for i in range(10):
    height = bounce(height)
    print(round(height, 4))
