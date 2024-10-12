import function

#List of Dictionary
daftar_kontak = [
    {
    "nama" : "Mashu",
    "email" : "federicomatthewpratamaa@gmail.com",
    "telepon" : "00000"
    },
    {
    "nama" : "Arthur",
    "email" : "arthur@gmail.com",
    "telepon" : "2221112"
    },
    {
    "nama" : "Badut",
    "email" : "anjingkaubadutbeban@gmail.com",
    "telepon" : "12121131"
    }
]

while True:

    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")

    menu = input("Pilih menu : ")
    if menu == "0":
        break
    # if menu == "1":
    #     function.take_name(daftar_kontak)
    #     menu_kontak = input("Pilih Nama Kontak : ")
    #     if menu_kontak == "1":
    #         function.display_kontak(daftar_kontak)
    if menu == "1":
        function.take_name(daftar_kontak)
        menu_kontak = input("Pilih Nama Kontak : ")
        function.display_kontak(daftar_kontak, int(menu_kontak) - 1)

print("Program telah selesai")