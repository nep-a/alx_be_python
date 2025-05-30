#prompting a user to enter a number
number = int(input("Enter a number: "))
#generating a multiplication table
for numb in range(1,11):
    result = numb * number
    print(result)