def main():
    var_str = "This Repository will be All About Tkinter , Some a Little projects For Beginners !"
    print(var_str)

    def collatz(n):
        if n % 2 == 0:
            r = n // 2
            print(r)
            return r
        elif n % 2 != 0:
            r = 3 * n + 1
            print(r)
            return r

    try:
        inp = int(input("Enter a number : "))
        if inp == 0 :
            print("You cant use 0 !")
        while inp != 1 and inp != 0:
            inp = collatz(inp)
    except ValueError:
        print("Please Enter a valid number")
    except:
        print("Error , You have to enter a valid number .")


if __name__ == '__main__':
    main()
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[0:2])

# Created by Malek1Dev
