""" name = "Alice"
age = 25
message = f"Hello, {name}. You are {age} years old."
print(message)  # Output: Hello, Alice. You are 25 years old. """

def calsec(h,m,s):
    h = h * 60 * 60
    m = m * 60
    s = s
    return h + m + s


def sumsec():
    h = int(input("Hour: "))
    m = int(input("Minute: "))
    s = int(input("Second: "))

    print("Summary:", calsec(h, m, s))

sumsec()
