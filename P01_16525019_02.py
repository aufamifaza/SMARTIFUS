#Nama : Aufa Muhammad Izzan Faza
#NIM :16525019

a = int(input("Jumlah barang A: "))             #Masukkan jumlah barang A
b = int(input("Jumlah barang B: "))             #Masukkan jumlah barang B
c = int(input("Jumlah barang C: "))             #Masukkan jumlah barang C

k = int(input("Jumlah bundle identik: "))       #Masukkan jumlah bundle identik
H_b = int(input("Harga bundle identik: "))      #Masukkan harga bundle identik
H_s = int(input("Harga spesial per item: "))    #Masukkan harga spesial per item

A = a % k       #Mencari sisa barang A
B = b % k       #Mencari sisa barang B
C = c % k       #Mencari sisa barang C

T = H_b*k + H_s*(A+B+C)     #Pengoperasian data untuk mendapatkan total pendapatan

print("Total pendapatan: ", T)      #Hasil Akhir