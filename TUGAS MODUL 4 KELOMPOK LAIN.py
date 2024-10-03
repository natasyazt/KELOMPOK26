# Daftar global untuk menyimpan transaksi
transaksi = []

# Fungsi untuk menambah pemasukan
def tambah_pemasukan(jumlah, deskripsi):
    transaksi.append({"jenis": "pemasukan", "jumlah": jumlah, "deskripsi": deskripsi})
    return f"Pemasukan sebesar {jumlah} berhasil ditambahkan."

# Fungsi untuk menambah pengeluaran
def tambah_pengeluaran(jumlah, deskripsi):
    transaksi.append({"jenis": "pengeluaran", "jumlah": jumlah, "deskripsi": deskripsi})

# Method untuk menampilkan semua transaksi
def tampilkan_transaksi():
    for t in transaksi:
        print(f"{t['jenis'].capitalize()}: {t['jumlah']}, {t['deskripsi']}")

# Method untuk menghitung total pemasukan/pengeluaran
def hitung_total(jenis):
    total = 0
    for t in transaksi:
        if t['jenis'] == jenis:
            total += t['jumlah']
    return total

# Main Program
while True:
    print("Menu Pengelolaan Keuangan Pribadi")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Tampilkan Semua Transaksi")
    print("4. Tampilkan Total Pemasukan/Pengeluaran")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        deskripsi = input("Masukkan deskripsi pemasukan: ")
        print(tambah_pemasukan(jumlah, deskripsi))
        
    elif pilihan == '2':
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        deskripsi = input("Masukkan deskripsi pengeluaran: ")
        tambah_pengeluaran(jumlah, deskripsi)
        
    elif pilihan == '3':
        tampilkan_transaksi()
        
    elif pilihan == '4':
        jenis = input("Ingin menghitung total apa (pemasukan/pengeluaran)? ")
        print(f"Total {jenis}: {hitung_total(jenis)}")
        
    elif pilihan == '5':
        break
    
    else:
        print("Pilihan tidak valid.")
