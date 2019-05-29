def int_float(n): # Coonvert integers and floats in string properly
    if "." in n:  # If there is a period, it is a float
        return float(n)
    else:
        return int(n)
def do(w,n1,n2): # A fuction to subtract, add, multiply and divide
    if w=="add":
        return n1+n2
    elif w=="sub":
        return n1-n2
    elif w=="div":
        return "Quotient is: "+str(int(n1//n2))+", remainder is: "+str(int_float(str(n1%n2)))
    elif w=="mul":
        return n1*n2
    else:
        raise "Error"
def calc():
    print("Welcome to calculator")
    while 1: # Keep the calculator running
        ainput=input("")
        if ainput=="q": # Quit if q is passed as an input
            return None
        else:
            try:
                print(do(ainput.split()[0].lower(),int_float(ainput.split()[1]),int_float(ainput.split()[2]))) # Pass correct parameters to do fuction
            except:
                print("Error")
calc()