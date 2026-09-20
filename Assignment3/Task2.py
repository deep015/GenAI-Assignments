
def factorial(num):
    if num == 0 or num ==1 :
        return 1
    if num < 0 :
        return "Number cannot be negative"
    return num * factorial(num - 1) 


print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(-1))
