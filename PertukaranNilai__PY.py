GarisJudul = 48 * "-"
BarisBaru = "\n"
Judul1 = "Inisialisasi Variabel A & B (Sebelum Pertukaran)"
Judul2 = "Hasil Variabel A & B (Setelah Pertukaran)"
Judul3 = "Inisialisasi Variabel Awal"
Judul4 = "Hasil Pertukaran Nilai"

#Inisialisasi (Assignment) Awal
a = 10
b = 20

# CARA 1 (Tidak Disarankan)
print(GarisJudul)
print("Cara I (Tidak Disarankan)")
print(GarisJudul, BarisBaru)
print(Judul1)
print(f'=> A: {a}')
print(f'=> B: {b}', BarisBaru)
c = a
a = b
b = c
print(Judul2)
print(f'=> A: {a}')
print(f'=> B: {b}', 3 * BarisBaru)

# CARA 2 (Disarankan)
print(GarisJudul)
print("Cara II (Disarankan)")
print(GarisJudul, BarisBaru)
print(Judul1)
print(f'=> A: {a}')
print(f'=> B: {b}', BarisBaru)
a, b = b, a
print(Judul2)
print(f'=> A: {a}')
print(f'=> B: {b}', 3 * BarisBaru)

#Contoh Pertukaran Nilai Dengan Banyak Variabel
print(GarisJudul)
print("Pertukaran Nilai Dengan Banyak Variabel")
print(GarisJudul, BarisBaru)

a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7 

print(Judul3)
print(f'A: {a}, B: {b}, C: {c}, D: {d}, E: {e}, F: {f}, G: {g}', BarisBaru)

a, b, c, d, e, f, g = d, f, b, g, c, a, e

print(Judul4)
print(f'A: {a}, B: {b}, C: {c}, D: {d}, E: {e}, F: {f}, G: {g}', 6 * BarisBaru)



