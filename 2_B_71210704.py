#input
r = int(input("Masukkan besar RSI: "))
macd = str(input("Masukkan kondisi MACD: "))
#kondisi
if (r>=70) and (macd=='death-cross'):
 print ("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")
elif (r<=30) and (macd=='golden-cross'):
 print ("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")
elif (r>=70) and (macd=='golden-cross'):
 print ("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")
elif (r<=30) and (macd=='death-cross'):
 print ("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai golden-cross")
else :
 print ("RSI berada di area 31-69, bukan saatnya membeli maupun menjual")
