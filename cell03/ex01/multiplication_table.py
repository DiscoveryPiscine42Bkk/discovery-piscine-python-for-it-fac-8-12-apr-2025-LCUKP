"""Exercise 01: multiplication_table"""
def main() :
    num = int(input("Enter a number\n"))
    for i in range(10) :
        print(i,"x",num,"=",i*num)
main()
