import random
import string

q_values = random.randint(6, 12) # длина пароля
option_symbols = "_-" # разрешённые спецсимволы. Отличаются на разных серверах
all = string.ascii_letters + string.digits + option_symbols # массив символов для сборки пароля
password = ''
for i in range(q_values): # цикл посимвольной сборки парольной строки
    random_letter = all[random.randint(0, len(all) - 1)]
    password += random_letter
print(password)
