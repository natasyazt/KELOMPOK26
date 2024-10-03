# Daftar belanja akan disimpan di sini
daftar_belanja = []

# Function dengan return type dan tanpa parameter
def lihat_daftar_belanja():
    if len(daftar_belanja) == 0:
        return "Daftar belanja kosong."
    else:
        return "\n".join(daftar_belanja)

# Function tanpa return type dan berparameter
def tambah_item(item):
    daftar_belanja.append(item)
    print(f"Item '{item}' berhasil ditambahkan ke daftar belanja.")

# Method (sebagai bagian dari class) tanpa return type
class DaftarBelanja:
    def hapus_item(self, item):
        if item in daftar_belanja:
            daftar_belanja.remove(item)
            print(f"Item '{item}' berhasil dihapus dari daftar belanja.")
        else:
            print(f"Item '{item}' tidak ditemukan di daftar belanja.")
    
    # Method dengan return type
    def total_item(self):
        return len(daftar_belanja)

# Program utama
def main():
    daftar = DaftarBelanja()
    
    while True:
        print("\n=== Sistem Pengelolaan Daftar Belanja ===")
        print("1. Lihat daftar belanja")
        print("2. Tambah item ke daftar belanja")
        print("3. Hapus item dari daftar belanja")
        print("4. Lihat total item dalam daftar")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            print("\nDaftar Belanja:")
            print(lihat_daftar_belanja())
        
        elif pilihan == '2':
            item = input("Masukkan nama item: ")
            tambah_item(item)
        
        elif pilihan == '3':
            item = input("Masukkan nama item yang ingin dihapus: ")
            daftar.hapus_item(item)
        
        elif pilihan == '4':
            print(f"Total item dalam daftar: {daftar.total_item()}")
        
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem ini!")
            break
        
        else:
            print("Opsi tidak valid, coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
