from math import sqrt

#### Fonction secondaire
def isprime(p):
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale
def main():
    # Test les 100 premiers nombres
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
