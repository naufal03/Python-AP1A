nama = str(input("masukan nama karyawan :"))
gaji_pokok = float(input("masukan gaji pokok :"))

tunjangan = 0.2*gaji_pokok
pajak = 0.15*(gaji_pokok+tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

print(10*"=")

print("nama = ",nama)
print("tunjangan = ",tunjangan)
print("pajak = ",pajak)
print("gaji berih =" ,gaji_bersih)