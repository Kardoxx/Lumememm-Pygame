# See funktsioon lisab kaks numbrit
def add(x, y):
    return x + y


# See funktsioon lahutab kaks arvu
def subtract(x, y):
    return x - y


# See funktsioon korrutab kaks numbrit
def multiply(x, y):
    return x * y


# See funktsioon jagab kaks arvu
def divide(x, y):
    return x / y

# Konsool annab valikut mis toimingut teha soovid
print("Valige toiming.")
print("1.Liitmine")
print("2.Lahutamine")
print("3.Korrutamine")
print("4.Jagamine")

while True:
    # võtab kasutajalt sisendi vastu
    choice = input("Sisestage valik(1/2/3/4): ")

    # kontrollib, kas valik on üks neljast valikust
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Sisesta esimene number: "))
            num2 = float(input("Sisesta teine number: "))
        except ValueError:
            print("Vigane sisestus. Palun sisestage number.")
            continue
        # Iga arv tähendab eri arvutusviisi (Nt korrutamine, liitmine jne, ning sa saad valida millise valid)
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # kontrollib, kas kasutaja soovib teist arvutust
        # katkestab while-tsükkel, kui vastus on eitav
        next_calculation = input("Teeme järgmise arvutuse? (jah/ei): ")
        if next_calculation == "ei":
            break
    else: #Prindib terminali Vigane sisend
        print("Vigane sisend")
        # See funktsioon ümardab arvud
def round_off():
    num = float(input("Sisesta number: "))
    decimals = int(input("Sisestage ümardatavate kümnendkohtade arv: "))
    return round(num, decimals)

print(round_off())
 # Küsib kas tahad teha järgmist arvutust
next_calculation = input("Tahad ruutjuurt sellest arvust saada? (jah/ei): ")
 # See funktsioon arvutab ruutjuure välja
def find_square_root():
    num = float(input("Sisesta number: "))
    return num ** 0.5

print(find_square_root())
 # Küsib kas tahad teha järgmist arvutust
next_calculation = input("Kas soovid astendada?(jah/ei): ")
 # See funktsioon astendab sisestatud arve
def find_exponentiation():
    base = float(input("Sisestage alus: "))
    exponent = float(input("Sisesta astendaja: "))
    return base ** exponent

print(find_exponentiation())


