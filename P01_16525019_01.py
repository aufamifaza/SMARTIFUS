#Nama : Aufa Muhammad Izzan Faza
#NIM : 16525019

B = int(input("Masukkan Jawaban Benar: "))                      #Masukkan jawaban benar
N = int(input("Masukkan Jumlah Soal: "))                        #Masukkan jumlah soal
T = int(input("Masukkan Waktu Yang Digunakan (Dalam Detik): ")) #Masukkan waktu pengerjaan

Skor = float                        #Skor dalam bilangan real
Skor = ((B*100)/N)+((3600-T)/60)    #Pengoprasian untuk mencari Skor

Akurasi = float                     #Akurasi dalam bilangan real
Akurasi = (B/N)*100                 #Pengoperasian untuk mencari Akurasi

print("Skor yang didapatkan Nona Sal adalah", Skor, "dengan akurasi", Akurasi, "%") #Hasil Akhir