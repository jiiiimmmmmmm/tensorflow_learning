import math
print("It's math! It has type {}".format(type(math)))

# help(math)
# print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))


# help(list)
hand = ['Q', '3', '8']
A_count = 0
sum = 0
for h in hand:
    if h == 'A':
        A_count+=1
        sum+=11
    elif h.isnumeric():
        sum+=int(h)
    else:
        sum+=10
while sum>21 and A_count != 0:
    sum-=10
    A_count-=1
print(sum)
