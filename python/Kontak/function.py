def take_name(daftar_kontak):
    for i, kontak in enumerate(daftar_kontak, start=1):
        print(f"{i}. {kontak['nama']}")

def display_kontak(daftar_kontak, index: int):
    selected = daftar_kontak[index]
    print("===========================")
    print(f"Nama    : {selected["nama"]}")
    print(f"Email   : {selected["email"]}")
    print(f"Telepon : {selected["telepon"]}")

def kontak_baru():
    nama = input("Masukkan Nama : ")
    email = input("Masukkan Email : ")
    telepon = input("Masukkan No Telp : ")
    tmp_kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return tmp_kontak

def hapus_kontak(daftar_kontak):
    index = -1
    check = int(input("Pilih mode 1. Nama 2. Number : "))

    if check == 1:
        nama = input("Nama Kontak yang ingin dihapus : ").lower()
        for i in range(0, len(daftar_kontak)):
            kontak = daftar_kontak[i]
            if nama.lower() == kontak["nama"].lower():
                index = i
                break

    if check == 2:
        telepon = input("No Telepon yang akan dihapus: ")
        for i in range(0, len(daftar_kontak)):
            kontak = daftar_kontak[i]
            if telepon == kontak["telepon"]:
                index = i 
                break

    if index == -1:
        print("===========================")
        print("Tidak ditemukan")
        
    else:
        del daftar_kontak[index]
        print("===========================")
        print("Berhasil dihapus")

def cari_kontak(daftar_kontak):
    while True:
        try:
            print("1. Nama")
            print("2. Number")
            check = int(input("Search mode : "))
            check_boolean = False
            
            if check == 1:
                search = input("Cari kontak dengan nama : ")
                for kontak in daftar_kontak:
                    nama = kontak["nama"].lower()
                    if nama.find(search) != -1:
                        print("===========================")
                        print(f"Nama    : {kontak["nama"]}")
                        print(f"Email   : {kontak["email"]}")
                        print(f"Telepon : {kontak["telepon"]}")
                        check_boolean = True
                    break
                if check_boolean == False:
                    print("===========================")
                    print("Tidak ditemukan")
                    print("===========================")
                    continue
                break

            if check == 2:
                search = input("Cari kontak dengan nomor : ")
                for kontak in daftar_kontak:
                    number = kontak["telepon"]
                    if number.find(search) != -1:
                        print("===========================")
                        print(f"Nama    : {kontak["nama"]}")
                        print(f"Email   : {kontak["email"]}")
                        print(f"Telepon : {kontak["telepon"]}")
                        check_boolean = True
                    break
                if check_boolean == False:
                    print("===========================")
                    print("Tidak ditemukan")
                    print("===========================")
                    continue
                break
        except:
            print("===========================")
            print("Data harus Integer !")
            continue        