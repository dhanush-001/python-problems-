a = 1030
b = 2000

print(f"before swapping: a = {a},b ={b}")

#swapping without using the temp

a = a+b
b = a-b
a = a-b

print(f"after swapping : a={a},b ={b}")
