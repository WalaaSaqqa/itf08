def pal(num:str):
    rev_str = num[::-1]
    return rev_str


def EO(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    print("1. Check if palindrome")
    print("2. Check if even or odd")
    print("Choose 1 or 2:  ")


    ch = int(input("Enter your num: "))

    if ch == 1:
        num = int(input("Enter a number: "))
        if pal(num):
            print("It's a palindrome!")
        else:
            print("It's not a palindrome.")
    elif ch == 2:
        num = int(input("Enter a number: "))
        result = EO(num)
        print(result})
    else:
        print("wrong")


main()

#########################


def X(num):
    num.sort()
    s= num[0]
    l = num[-1]
    return s, l

num = [10, 7, 1, 20, 100 , 35]
s, l = X(num)

print("Small number:", s)
print("Large number:", l)
