#using Expection keyword in except class
try:
    a=10
    b="Hello"
    print(a+b)
except Exception as e:
    print(e)
    print(type(e))
    print(type(e).__name__)
    print("error")
finally:
    print("completed")
print("=============================")
#using typeerror in except class
try:
    a=10
    b="Hello"
    print(a+b)
except TypeError:
    print("error")
finally:
    print("completed")

