def bes_yil():
	i = float(input("İskonto oranı girin : "))
	# i : iskonto
	k = 10**3
	yil1 = 300*k
	yil2 = 400*k
	yil3 = 450*k
	yil4 = 800*k
	yil5 = 900*k
	yatirim_tutari = 2500*k
	ngbd = yil1/(1+i) + yil2/(1+i)**2 + yil3/(1+i)**3 + yil4/(1+i)**4 + yil5/(1+i)**5
	print("iskonto oranı : " , i)
	print("NGBD : ", ngbd)
	print("Sonuç : " , ngbd - yatirim_tutari)
	bes_yil()

bes_yil()
	