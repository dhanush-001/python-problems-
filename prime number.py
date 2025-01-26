def is_prime(num):

    if num < 2:
        return false

    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

number = int(input("enter the number:"))
if is_prime(number):
    print("it is prime number",number)
else:
    print("it is not a prime number",number)
    
          
