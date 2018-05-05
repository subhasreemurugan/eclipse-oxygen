def bintodeci(n):
    if n==0:
        return 0
    return n % 10 * (int) Math.pow(2, size) + binaryToDecimal((int) binary / 10, size - 1)
n=eval(input("enter a no to be "))
no=bintodeci(n)