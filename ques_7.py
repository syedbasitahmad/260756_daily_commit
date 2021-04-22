#swap nTh value with n+1 th value in list
error_msg="plz type correct input"
def take_input():
    n = int(input("Enter number of elements : "))
    a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    return a
def swap(a):
    i = 0
    while i < a.__len__() - 1:
        t = a[i]
        a[i] = a[i + 1]
        a[i + 1] = t
        i = i + 2
    return a
        
if __name__=="__main__":
    list=take_input()
    ans=swap(list)
    print(ans)