import random
list_1 = []
i = 0

while i < 10:
    num = random.randint(0, 99)
    list_1.append(int(num))
    i = i + 1

print("Every other element of the random list (keep the first element):", end=" ")
for i in range(len(list_1)):
    if list_1[i] % 2 != 0:
        print(list_1[i], end=" ")
print()

print("The value of elements that are even:", end=" ")
for i in list_1:
    if i % 2 == 0:
        print(i, end=" ")
print()

print("Elements in reverse order:", end=" ")
for i in list_1[::-1]:
    #range(len(len(list_1)-1,-1,-1) is another way to do it
    print(i, end=" ")
print()

list_1.sort()
print("Elements sorted:", end=" ")
for i in list_1:
    print(i, end=" ")




