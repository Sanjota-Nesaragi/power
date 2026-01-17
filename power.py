import sys

def power(base, exp):
    return base ** exp

if __name__ == "__main__":
    try:
        base = int(sys.argv[1])
        exp = int(sys.argv[2])
    except IndexError:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))

    print("Result:", power(base, exp))