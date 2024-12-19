# funkcja wewnętrzna, zagnieżdzona
# dekorator wykorzystuyje zasade funkcji wew
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # referencja, adres funkcji


xFun = fun1()  # wpisujemy wynik działania funkcji fun1() czyli adres fun2
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000024160058A40>
print(type(xFun))  # <class 'function'>
xFun()
