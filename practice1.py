def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر مجاز نیست!"
    return x / y

print("ماشین حساب ساده 🧮")
print("1. جمع")
print("2. تفریق")
print("3. ضرب")
print("4. تقسیم")

choice = input("لطفاً شماره عملیات مورد نظر را وارد کنید (1/2/3/4): ")

try:
    num1 = float(input("عدد اول را وارد کنید: "))
    num2 = float(input("عدد دوم را وارد کنید: "))

    if choice == '1':
        print("نتیجه:", add(num1, num2))
    elif choice == '2':
        print("نتیجه:", subtract(num1, num2))
    elif choice == '3':
        print("نتیجه:", multiply(num1, num2))
    elif choice == '4':
        print("نتیجه:", divide(num1, num2))
    else:
        print("ورودی نامعتبر است!")
except ValueError:
    print("لطفاً فقط عدد وارد کنید.")
