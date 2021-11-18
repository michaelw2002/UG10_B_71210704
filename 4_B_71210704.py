#input
angka = int(input("Masukkan angka: "))

#kondisi dan output
if (angka%2 == 0) and (angka%3 != 0):
 print ("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA")
else:
 print ("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3? Program dihentikan")

if (angka%5 != 0 ==True) or (angka%10 == 0 ==False):
  print ("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
elif (angka%2 !=0) and (angka%3 == 0):
  print ()
else:
  print ("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
