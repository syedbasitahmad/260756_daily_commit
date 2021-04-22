#price of pizzas problem
error_msg="plz type correct input"
def take_input():
    no_of_pizzas=int(input())
    return no_of_pizzas
def price(no_of_pizzas):
    if (no_of_pizzas<=0):
        return error_msg
    if (no_of_pizzas%2==0):
        return no_of_pizzas*120
    else:
        return no_of_pizzas*130
        
if __name__=="__main__":
    no_of_pizzas=take_input()
    ans=price(no_of_pizzas)
    print(ans)