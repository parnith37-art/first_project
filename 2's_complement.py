def to_binary(n):
    return format(n & 0xFF, "08b")


def from_binary(binary):
    value = int(binary, 2)

    if value >= 128:
        value -= 256

    return value


def add_8bit(a, b):
    result = (a + b) & 0xFF
    binary_result = format(result, "08b")

    overflow = (a + b < -128 or a + b > 127)

    print("First operand :", to_binary(a), "=", a)
    print("Second operand:", to_binary(b), "=", b)
    print("Binary result :", binary_result)
    print("Decimal result:", from_binary(binary_result))
    print("Overflow      :", "Yes" if overflow else "No")
    print("-" * 35)


print("(a) (+20) + (+15)")
add_8bit(20, 15)

print("(b) (-20) + (-15)")
add_8bit(-20, -15)
