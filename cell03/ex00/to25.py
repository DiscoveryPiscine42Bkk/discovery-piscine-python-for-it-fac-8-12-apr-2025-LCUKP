"""Exercise 00: Up to 25"""
def main() :
    num = int(input("Enter a number less than 25\n"))
    if num > 25 :
        print("Error")
    else :
        for i in range(6) :
            print("Inside the loop, my variable is" , (num+i))
main()
