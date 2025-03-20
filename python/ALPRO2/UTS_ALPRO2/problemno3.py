import problemno1, problemno2

def Template():
    print("====================================================================================================")
    print("1. Menjalankan jawaban soal 1")
    print("2. Menjalankan jawaban soal 2")
    print("====================================================================================================")

if __name__ == "__main__":
    while True:
        try:
            Template()
            n = int(input("pilihan anda (1 / 2) : "))

            if n == 1:
                start = problemno1.Nomor_1(5, 89)
                while True:
                    start.InputUser()
                    if start.Valid():
                        start.Bilangan()
                        break
                    else:
                        print("Nilai ketentuan : 5 <= n <= 89 dan Nilai harus Ganjil")

            elif n == 2:
                start = problemno2.Nomor_2(5, 89)
                while True:
                    start.InputUser()
                    if start.Valid():
                        start.Bilangan()
                        break
                    else:
                        print("Nilai ketentuan : 5 <= n <= 89 dan Nilai harus Ganjil")

            else:
                print(f"Pilihan anda harus (1 / 2).")
                continue
        except Exception:
            print("Data harus integer !")
            continue
        looping = input("Program selesai. Apakah anda ingin mengulang menu lagi (y/n) : ")
        if looping.lower() == "y":
            continue
        else:
            break
