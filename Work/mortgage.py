# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months == 342:
        print(total_paid) # 929965.6199999959
    if months <= 12:
        total_paid += 1000
    months += 1

print('Total paid', total_paid)
print('Months', months)