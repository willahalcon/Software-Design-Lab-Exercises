x=5
y=3

def recursive_multiply(x,y):

    if y ==0:
        return 0
    return x + recursive_multiply(x,y-1)

print(x + y)


