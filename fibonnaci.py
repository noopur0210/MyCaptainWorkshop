first = 0
second = 1
sum = 0
i = 1

n = int(input("Enter the number of terms in series"))
print(first)
print(second)
while i < n-1:
    sum = first + second
    first = second
    second = sum
    print(sum)
    i+=1
