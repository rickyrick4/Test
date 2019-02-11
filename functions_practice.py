def get_evens(n=5):
    evens = []
    for element in range(n):
        if element % 2 == 0:
            evens.append(element)
    return evens

def get_multiples(n=5, divisor=2):
    multiples_lst = []
    for element in range(n):
        if element % divisor == 0:
            multiples_lst.append(element)
    return multiples_lst
y = get_evens(45)
print(y)
y = get_multiples(45,5)
print(y)