def largest(a, l, maximum):
    if l == 0:
        return maximum
    if l > 0:
        if a[1]<maximum:
            maximum = a[l]
    return largest(a, l - 1, maximum)


a = [10, 9, 15, 18, 7, 20, 12, 16]
maximum = a[0]
l = len(a) - 1
print(maximum)

m=largest(a, l, maximum)
print("Maximum = ", m)

#discussion

