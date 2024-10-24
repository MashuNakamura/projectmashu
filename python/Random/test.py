# # Dari GPT Update data , bukan input data

# # Dictionary awal
# data = {'nama': 'Alice', 'usia': 25}

# # Meminta input dari user
# kunci_baru = input("Masukkan kunci baru: ")
# nilai_baru = input("Masukkan nilai baru: ")

# # Menambahkan data baru ke dictionary
# data[kunci_baru] = nilai_baru

# # Menampilkan dictionary yang sudah diperbarui
# print(data)

# Contoh daftar kontak disimpan dalam bentuk dictionary
contacts = {
    "John Doe": "123-456-7890",
    "Jane Smith": "987-654-3210",
    "Alice Johnson": "555-123-4567"
}

# Fungsi untuk mencari kontak berdasarkan nama
def search_contact_by_name(contacts, name):
    if name in contacts:
        return f"Kontak ditemukan: {name} - {contacts[name]}"
    else:
        return "Kontak tidak ditemukan."

# Fungsi untuk mencari kontak berdasarkan nomor telepon
def search_contact_by_number(contacts, number):
    for name, contact_number in contacts.items():
        if contact_number == number:
            return f"Kontak ditemukan: {name} - {contact_number}"
    return "Kontak tidak ditemukan."

# Mencari kontak berdasarkan nama
name_to_search = "Jane Smith"
print(search_contact_by_name(contacts, name_to_search))

# Mencari kontak berdasarkan nomor telepon
number_to_search = "555-123-4567"
print(search_contact_by_number(contacts, number_to_search))