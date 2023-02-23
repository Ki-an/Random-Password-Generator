import random
alpha ="abcdef!£$%^&*(#@1234567890?><,._-';:\/')ghijklmnopqrstuvwxyz"

len = list(range(0,13))
password =""
for i in len:
 password+=random.choice(alpha)
print(password)