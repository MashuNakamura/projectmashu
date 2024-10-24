def take_name(daftar_kontak):
    # Easy to Understand
    for i, kontak in enumerate(daftar_kontak, start=1):
        print(f"{i}. {kontak['nama']}")
    # Hard to Understand
    # for i in enumerate(daftar_kontak, start=1):
    #     print(f"{i[0]}. {i[1]['nama']}")

# def display_kontak(daftar_kontak):
#     for kontak in daftar_kontak:
#         print("============================")
#         for nomor in kontak:
#             print(f"Nama : {kontak[nomor]}")

def display_kontak(daftar_kontak, index: int):
    selected = daftar_kontak[index]
    print("===========================")
    print(f"Nama    : {selected["nama"]}")
    print(f"Email   : {selected["email"]}")
    print(f"Telepon : {selected["telepon"]}")
    print("===========================")

def kontak_baru():
    nama = input("Masukkan Nama : ")
    email = input("Masukkan Email : ")
    telepon = input("Masukkan No Telp :")
    tmp_kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return tmp_kontak

def hapus_kontak(daftar_kontak):
    index = -1
    check = int(input("Pilih mode 1. Nomor 2. Nama"))
    if check == 1:
        telepon = input("No Telepon yang akan dihapus: ")
        for i in range(0, len(daftar_kontak)):
            kontak = daftar_kontak[i]
            if telepon == kontak["telepon"]:
                index = i
                break
    if check == 2:
        nama = input("Nama Kontak yang ingin dihapus : ").lower()
        for i in range(0, len(daftar_kontak)):
            kontak = daftar_kontak[i]
            if nama.lower() == kontak["nama"].lower():
                index = i
                print(i)
                break

    if index == -1:
        print("Tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil dihapus")