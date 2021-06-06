# Exercise
# House price is 1M pesos
# if the buyer has good credit lower the down payment to 10%
# if don't have good credit give the down payment to 20%
# then show the total down payment

price = int('1' + ('0' * 6))  # 1M
has_good = False

if has_good:
    downPayment = price * 0.10
else:
    downPayment = price * 0.20

print(f"Down payment is: P{downPayment}")

# if [expression]:
#   do this
# elif [expression]:
#   do this
# else
#   do this
