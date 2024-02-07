#array numbers[6]
numbers = [0] * 6

for i in range(0,6):
    numbers[i]=int(input("Enter a number: "))
 
print("Reverse order: ")
# for i = 5 to 0 do
for i in range (5, -1, -1):
    print(numbers[i])

total = sum(numbers)
average = total / len(numbers)

print(f"Total: {total}")
print(f"Average: {average}")