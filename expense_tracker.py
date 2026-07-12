total_expense=0
while True:
    print('please enter the expense amount:')
    expense_amount=int(input())
    total_expense+=expense_amount


    print('DO you want to add another expense? (YES/NO)')

    responce=input()
    if responce.upper()=='YES':
        continue
    if responce.upper()=='NO':
        break

print('YOUR TOTAL EXPENSE IS:', total_expense)    















































