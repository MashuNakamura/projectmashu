from persegi_panjang import persegi_panjang
from lingkaran import lingkaran
from segitiga import segitiga

def main():
    while True:
        print("==================")
        print("0. Exit")
        print("1. Persegi Panjang")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("==================")
        menu = input("Pilih Menu : ")
        
        if menu == "1":
            Shape = persegi_panjang()

        elif menu == "2":
            Shape = lingkaran()

        elif menu == "3":
            Shape = segitiga()

        elif menu == "0":
            print("Terima Kasih telah menggunakan program ini")
            break
        else:
            print("Nomor Menu tidak valid")
                
        Shape.user_input()
        print(f"Luas : {Shape.hasil_luas()}")
        
if __name__ == "__main__":
    main()