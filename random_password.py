import random
import string

print('Please enter the Password length you want to generate: ')
length=int(input())

password=''
choice=[lambda: random.randint(0,9),
        lambda: random.choice(string.ascii_letters),
        lambda: random.choice(string.punctuation)]
    
for i in range(length):
    password+=str(choice[i%3]())

print('Your generated password is: ',password)   
   

































