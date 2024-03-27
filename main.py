# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


x = 0
if x < 0:
    print(f'Numarul este negativ')
elif x > 0:
    print(f'Numarul este pozitiv')
else:
    print(f'Numarul este neutru')


dictionar = {
    "infinitiv": "a bea",
    "participiu": "baut"
}

set = {1, 2, 3}

def calculeaza_suma_a_doua_numere():
    a = 3
    b = 3
    suma = a + b
    print(f"Suma celor doua numere este {suma}")

calculeaza_suma_a_doua_numere()   #afișează rezultatul adunării dintre a și b

def aduna(a, b):
    suma = a + b
    return suma

rezultat = aduna(3, 7)
print(rezultat)  # Afișează: 10