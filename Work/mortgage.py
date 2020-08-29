# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 12*5
extra_payment_end_month = extra_payment_start_month + 4*12
extra_payment = 1000


while principal > 0:
    if principal * (1+rate/12) <= payment:
        payment = principal * (1+rate/12)
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid += extra_payment
    else:
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months += 1
    print(f'{months} {total_paid:0.2f} {principal:0.2f}')

print(f'Total paid {total_paid:0.2f}')
print(f'Months {months}')