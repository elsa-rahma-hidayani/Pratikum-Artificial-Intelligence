import random

# Fungsi untuk melempar dadu
def lempar_dadu():
    return random.randint(1, 6)

# Meminta input dari pengguna
jumlah_lemparan = int(input("Masukkan jumlah lemparan dadu: "))

# Melakukan lemparan dadu sebanyak yang diminta
for i in range(jumlah_lemparan):
    hasil_lempar = lempar_dadu()
    print("Hasil lemparan ke-", i+1, "adalah:",hasil_lempar)