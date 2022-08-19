"""Prime numbers up to a given range of numbers"""
maxRange = int(input("Enter the maximum range you want: "))
print("prime numbers between ", 1, " and ", maxRange, " are: ")
for number in range(1, maxRange + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, end=' ')
