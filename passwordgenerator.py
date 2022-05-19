import random
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters=uppercase_letters.lower()
digits="0123456789"
symbols=",./?!@#$%^&*()"
uppercase,lowercase,digs,syms=True,True,True,True

all=""
if uppercase:
    all+=uppercase_letters
if lowercase:
        all+=lowercase_letters
if digs:
        all+=digits
if syms:
        all+=symbols



length=10
amount=20
for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)
   
            

 