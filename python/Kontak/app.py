import function

# List of Dictionary
daftar_kontak = [
    {
        "nama": "Mashu",
        "email": "federicomatthewpratamaa@gmail.com",
        "telepon": "00000"
    },
    {
        "nama": "Arthur",
        "email": "arthur@gmail.com",
        "telepon": "2221112"
    },
    {
        "nama": "Badut",
        "email": "anjingkaubadutbeban@gmail.com",
        "telepon": "12121131"
    },
    {
        "nama": "Jefferey",
        "email": "jeffereymonyet@gmail.com",
        "telepon": "12345"
    }
]

while True:
    print("===========================")
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")
    print("===========================")

    # Exit from Program
    menu = input("Pilih menu : ")
    if menu == "0":
        break

    # Display All Contact
    elif menu == "1":
        function.take_name(daftar_kontak)
        menu_kontak = input("Pilih Nama Kontak : ")
        function.display_kontak(daftar_kontak, int(menu_kontak) - 1)

    # Add New Contact (Temporary) because its only python not using db
    elif menu == "2":
        kontak = function.kontak_baru()
        daftar_kontak.append(kontak)

    # Delete Contact by Number Telp or Name
    elif menu == "3":
        kontak = function.hapus_kontak(daftar_kontak)

    # Search Contact
    elif menu == "4":
        kontak = function.cari_kontak(daftar_kontak)

    else:
        print("Data Harus Integer !")

# Print when the program is done
print("Program telah selesai")