# suma los n primeros numeros
# n+n-1+n-2+......+1
def sumaN(n):
    if n !=1:
        return n+sumaN(n-1)
    else:
        return 1

def factorial(n):
    if n !=1:
        return n*factorial(n-1)
    else:
        return 1

print(sumaN(100))

# fx(100)= 100+ fx(99)
# fx(100) = 100 + 99 + fx(98)+ ...... 1