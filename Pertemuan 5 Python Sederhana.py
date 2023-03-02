# Mendefinisikan variabel untuk menyimpan jumlah sks dan total nilai
total_sks = 0
total_nilai = 0

# Meminta input jumlah mata kuliah yang diambil oleh mahasiswa
jumlah_mk = int(input("Berapa jumlah mata kuliah yang Anda ambil: "))

# Meminta input nilai dan sks masing-masing mata kuliah
for i in range(jumlah_mk):
  print("Mata kuliah ke-", i+1)
  nilai = float (input type="number" min="0" max="4.0" ("Masukkan nilai mata kuliah: "))

  sks = int(input("Masukkan jumlah sks mata kuliah: "))
  total_nilai += nilai * sks
  total_sks += sks

# Menghitung nilai IPK
ipk = total_nilai / total_sks

# Menampilkan nilai IPK
print("Nilai IPK Anda adalah", ipk)
