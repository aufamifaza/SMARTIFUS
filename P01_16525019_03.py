#Nama : Aufa Muhammad Izzan Faza
#NIM : 16525019

J = int(input("Jarak (Km): "))                      #Masukkan Jarak
N = int(input("Masukkan nilai n: "))                #Masukkan nilai N
X = int(input("Masukkan nilai x: "))                #Masukkan nilai X 
Y = int(input("Masukkan nilai y: "))                #Masukkan nilai Y
A = int(input("Kecepatan ayah Tuan Vin (km/h): "))  #Masukkan Kecepatan Ayah Tuan Vin
V = int(input("Kecepatan Tuan Vin (Km/h): "))       #Masukkan Kecepatan Tuan Vin

Vx = J//(V*X/60)        #berapa kali Tuan Vin istirahat

T_A = int               #Waktu Ayah Tuan Vin
T_A = (J/A)*60          #Mencari Waktu Ayah Tuan Vin

T_V = int                   #Waktu Tuan Vin
T_V = N + (J/V)*60 + Y*Vx   #Mencari Waktu Tuan Vin

S = int             #Selisih waktu
S = T_A - T_V       #Mencari Selisih Waktu

K_1 = bool
K_1 = T_A>T_V 
K_1 = True (print("Tuan Vin Menang dengan Jarak Waktu", S, "menit"))

K_2 = bool
K_2 = T_A==T_V
K_2 = True (print("Hasil Seri"))

K_3 = bool
K_3 = T_A<T_V 
K_3 = True (print("Ayah Tuan Vin Menang dengan Jarak waktu", S, "menit"))
