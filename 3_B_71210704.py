#input
Bil1 = float(input("Masukkan bilangan pertama: "))
Bil2 = float(input("Masukkan bilangan kedua: "))
kalimat = str(input("Masukkan kalimat: "))

#kondisi dan output
Jumlah_Kali = Bil1 * Bil2
Jumlah_Bagi = Bil1 / Bil2
Jumlah = Bil1 + Bil2
Kurang = Bil1 - Bil2

if ("kali" in kalimat):
 print ("Hasil perkalian",Bil1,"dengan",Bil2,"adalah",Jumlah_Kali)
elif ("bagi" in kalimat):
 print ("Hasil pembagian",Bil1,"dengan",Bil2,"adalah",Jumlah_Bagi)
elif ("tambah" in kalimat):
 print ("Hasil penjumlahan",Bil1,"dengan",Bil2,"adalah",Jumlah)
elif ("kurang" in kalimat):
 print ("Hasil pengurangan",Bil1,"dengan",Bil2,"adalah",Kurang)
else :
 print ("Tidak ada")
