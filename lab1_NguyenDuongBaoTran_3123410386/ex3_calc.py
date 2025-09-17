# ex3_calc.py
print("Calculator Basic")

a = int(input("Moi ban nhap so a: "))
b = int(input("Moi ban nhap so b: "))

print("Ket qua cac phep tinh la:")
print("a + b = %d + %d = %d" % (a, b, a + b))
print("a - b = %d - %d = %d" % (a, b, a - b))
print("a * b = %d * %d = %d" % (a, b, a * b))

if b != 0:
    print("a / b = %d / %d = %.2f" % (a, b, a / b))
else:
    print("Khong the chia cho 0")
