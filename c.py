a="pots&pans&hello&hi"
b=a.split("&")

def reverse(lis):

    if not lis:
        return ""

    if type(lis) == list and len(lis) == 1:
        return reverse(lis[0])

    if type(lis) == str:
        return reverse(lis[1:]) + lis[0]

    if type(lis) == list:
        return reverse(lis[1:]) + "&" + reverse(lis[0])

print(reverse(b))