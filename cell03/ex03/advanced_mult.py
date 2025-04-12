"""Exercise 03: advanced_mult"""
def main() :
    for i in range(11) :
        print(f"Table de {i}: ",end="")
        for j in range(11) :
            print(i*j, end=" ")
        print()
main()
