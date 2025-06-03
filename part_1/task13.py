daycount, penalties, amount = *map(float, input("").split())    
for i in range(daycount):
    amount -= 3;
    if amount <= 0:
        print( f"Вы успешно оплатите кредит за {i+1} дня(-ей)!")
    amount *= (100 + penalties)/100;
print(f"К сожелению, вы не уплатите долг за такой срок с такой суммой ежедневного платежа. Ваш долг, по истечении этого срока, составит {amount} рублей(?)")
