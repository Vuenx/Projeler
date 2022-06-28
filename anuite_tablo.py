def faiz_tablosu(i,A,n):
	# i faiz oranı, A anapara, n dönem, a anülte
	d = 9 # sayı basamak görüntüleme
	formul = (((1+i)**n)-1)/(((1+i)**n)*i)
	a = A/formul
	print("A    Ö.t(A)       Ö.f.(B)      Ö.a.(C)      Anapara(D)")
	x = 1
	bosluk = "  "
	ott = 0 # Ödenen toplam tutar
	otf = 0 # Ödenen toplam faiz
	ota = 0 # Ödenen toplam anapara
	while A>0:
		B = A*i # B, ödenecek faiz
		C = a - B # C, ödenecek anapara
		A = A - C
		print(x, bosluk,  str(a)[:d], bosluk, str(B)[:d], bosluk, str(C)[:d], bosluk, str(A)[:d])
		x = x + 1
		ott = ott + a
		otf = otf + B
		ota = ota + C
	else:
		return print("Tablo tamamlandı" , "Ödenen toplam tutar :  " , str(ott)[:d], "Ödenen toplam faiz :  " , str(otf)[:d], "Ödenen toplam anapara : ", str(ota)[:d])


def faiz_input():
	Anapara = int(input("Anaparayı girin (TL) : "))
	Faiz = float(input("Faiz oranını girin (%5 için 0.05) : "))
	Donem = int(input("Dönem sayısını girin : "))
	return faiz_tablosu(Faiz, Anapara, Donem)

faiz_input()
	