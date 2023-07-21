import random
import string

q_values = random.randint(6, 12) # длина пароля
print(q_values)
all = string.ascii_letters + string.digits + string.punctuation # массив символов для сборки пароля

password = ''
for i in range(q_values): # цикл посимвольной сборки парольной строки
    random_letter = all[random.randint(0, len(all) - 1)]
    password += random_letter

print(password)
print(len(password))

# нужно как-то приспособить программу под разные требования серверов