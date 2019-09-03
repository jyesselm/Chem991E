nums = input("Enter your list: ")
smallest = 10000000000
for n in nums.split(","):
    if int(n) < smallest:
        smallest = int(n)
print(smallest)
