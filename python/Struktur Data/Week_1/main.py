## Week 1

import function

## Temporary List Barang
daftar_barang = [
    {"Nama": "Laptop", "Harga": 15000000},
    {"Nama": "Mouse", "Harga": 250000}
]

## Looping until Exit
while True:
    print("===========================")
    print("Toko UKDC")
    print("1. Tambah Data")
    print("2. Tampil Data")
    print("3. Hapus Data")
    print("4. Keluar")
    print("===========================")

    ## Select Menu Option
    menu = input("Pilih menu : ")

    ## Checking the Menu
    if menu == "1":
        barang = function.tambah_barang()
        daftar_barang.append(barang)

    elif menu == "2":
        function.display_barang(daftar_barang)

    elif menu == "3":
        function.hapus_barang(daftar_barang)

    elif menu == "4":
        print("Sampai Jumpa !")
        break

    else:
        print("Harap memasukkan nomor yang benar !")
