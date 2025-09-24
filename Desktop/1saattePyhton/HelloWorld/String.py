isim ='Özlem'
print(isim)
print(isim[0]) #ilk harfi yazdırır
print(isim[4])
print(isim[0:2]) #ilk iki harfi yazdıdr
print(isim[-1]) #son harfi yazdırır
print(isim[-4:-1]) #son 3 harfi yazdırır

print(len(isim)) #stringin uzunluğunu alır
print(isim.upper()) #bütün harfleri büyütür

print(isim.find("e")) #harfin oldugu indexi verir yokas -1 der
print(isim.replace("e","a")) #harf değiştirdik

isim= input("Adınızı girin :")
print(isim.title())