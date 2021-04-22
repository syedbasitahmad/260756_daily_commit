#second smallest
n = int(input("Enter number of elements : "))

a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
a.sort()
if(n<=1):
    print("only one element is present")
else:
    print(a[1])