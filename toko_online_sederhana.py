# --- 1. Definisi Kelas Produk ---
class Produk:
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"ID: {self.id_produk}, Nama: {self.nama}, Harga: Rp{self.harga:,.2f}, Stok: {self.stok}"

# --- 2. Definisi Kelas Item Pesanan (untuk menyimpan produk dan kuantitas dalam pesanan) ---
class ItemPesanan:
    def __init__(self, produk, kuantitas):
        self.produk = produk
        self.kuantitas = kuantitas
        self.subtotal = produk.harga * kuantitas

    def __str__(self):
        return f"{self.produk.nama} (x{self.kuantitas}) - Subtotal: Rp{self.subtotal:,.2f}"

# --- 3. Definisi Kelas Pesanan ---
class Pesanan:
    def __init__(self, id_pesanan, nama_pelanggan, alamat_pengiriman):
        self.id_pesanan = id_pesanan
        self.nama_pelanggan = nama_pelanggan
        self.alamat_pengiriman = alamat_pengiriman
        self.item_pesanan = [] # Daftar ItemPesanan yang ada dalam pesanan ini
        self.total_harga = 0.0
        self.status = "Pending" # Contoh status: Pending, Diproses, Dikirim, Selesai

    def tambah_item(self, produk, kuantitas):
        if produk.stok >= kuantitas:
            item = ItemPesanan(produk, kuantitas)
            self.item_pesanan.append(item)
            self.total_harga += item.subtotal
            produk.stok -= kuantitas # Kurangi stok produk
            print(f"'{produk.nama}' sejumlah {kuantitas} ditambahkan ke pesanan.")
        else:
            print(f"Maaf, stok '{produk.nama}' tidak mencukupi. Tersedia: {produk.stok}")

    def tampilkan_detail_pesanan(self):
        print(f"\n--- Detail Pesanan #{self.id_pesanan} ---")
        print(f"Pelanggan: {self.nama_pelanggan}")
        print(f"Alamat: {self.alamat_pengiriman}")
        print("Item:")
        for item in self.item_pesanan:
            print(f"  - {item}")
        print(f"Total Harga: Rp{self.total_harga:,.2f}")
        print(f"Status: {self.status}")
        print("----------------------------")

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membuat beberapa produk
    baju = Produk("P001", "Kaos Polos", 50000, 100)
    celana = Produk("P002", "Celana Jeans", 150000, 50)
    sepatu = Produk("P003", "Sepatu Sneakers", 250000, 20)

    print("Daftar Produk Awal:")
    print(baju)
    print(celana)
    print(sepatu)

    # Membuat pesanan baru
    pesanan1 = Pesanan("ORD001", "Budi Santoso", "Jl. Merdeka No. 10, Jakarta")

    # Menambahkan item ke pesanan
    pesanan1.tambah_item(baju, 2)
    pesanan1.tambah_item(celana, 1)
    pesanan1.tambah_item(sepatu, 1)
    pesanan1.tambah_item(baju, 5) # Menambahkan baju lagi
    pesanan1.tambah_item(sepatu, 25) # Mencoba memesan melebihi stok

    # Menampilkan detail pesanan
    pesanan1.tampilkan_detail_pesanan()

    print("\nStok Produk Setelah Pesanan:")
    print(baju)
    print(celana)
    print(sepatu)
