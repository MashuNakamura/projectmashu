class Week_1:
    def __init__(self) -> None:
        self.n : int = 0

    # No 1
    def pola_1(self, n : int):
        for y in range (0, n):
            for _ in range (0, y + 1):
                print("*", end="")
            print()
        print()

    # No 2
    def pola_2(self, n : int):
        for y in range (0, n):
            for _ in range (y, n):
                print("*", end="")
            print()
        print()

    # No 3
    def check_prima(self, n : int):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    input_n = int(input("Masukkan nilai n : "))

    nomor_1 = Week_1()
    nomor_1.pola_1(input_n)

    nomor_2 = Week_1()
    nomor_2.pola_2(input_n)

    nomor_3 = Week_1()
    nomor_3.check_prima(input_n)
    if nomor_3.check_prima(input_n):
        print("Bilangan ini Prima")
    else:
        print("Bilangan ini Bukan Prima")
