paradigma=input("inserire il paradigma del verbo da coniugare. Es: 'amo,as,amavi,amatum,amare':\n")
#print(paradigma)#rimuovi
paradigma=paradigma.split(",")
#print(paradigma)

if paradigma[4].endswith("are"):
	#1 coniugazione
	
	temaDelPresente=paradigma[0].strip("o")
	
	print("\nIndicativo")
	print()
	
	#indicativo presente
	ip1p1c=temaDelPresente+"o"
	ip2p1c=temaDelPresente+"as"
	ip3p1c=temaDelPresente+"at"
	ip4p1c=temaDelPresente+"amus"
	ip5p1c=temaDelPresente+"atis"
	ip6p1c=temaDelPresente+"ant"
	
	indicativoPresente1c=[]
	for x in range(1,7):
		indicativoPresente1c.append(eval("ip"+str(x)+"p1c"))
	#stampa indicativo presente
	print("Presente",indicativoPresente1c) 
	
	
	#imperfetto
	ii1p1c=temaDelPresente+"abam"
	ii2p1c=temaDelPresente+"abas"
	ii3p1c=temaDelPresente+"abat"
	ii4p1c=temaDelPresente+"abamus"
	ii5p1c=temaDelPresente+"abatis"
	ii6p1c=temaDelPresente+"abant"
	
	indicativoImperfetto1c=[]
	for x in range(1,7):
		indicativoImperfetto1c.append(eval("ii"+str(x)+"p1c"))
	#stampa indicativo imperfetto
	print("Imperfetto",indicativoImperfetto1c)
	
	#futuro semplice
	if1p1c=temaDelPresente+"abo"
	if2p1c=temaDelPresente+"abis"
	if3p1c=temaDelPresente+"abit"
	if4p1c=temaDelPresente+"abimus"
	if5p1c=temaDelPresente+"abitis"
	if6p1c=temaDelPresente+"abunt"
	indicativoFuturoSemplice1c=[]
	for x in range(1,7):
		indicativoFuturoSemplice1c.append(eval("if"+str(x)+"p1c"))
	#stampa futuro semplice
	print("Futuro Semplice",indicativoFuturoSemplice1c)
	
	temaDelPerfetto=paradigma[2][:-1]
	
	#perfetto
	ipe1p1c=temaDelPerfetto+"i"
	ipe2p1c=temaDelPerfetto+"isti"
	ipe3p1c=temaDelPerfetto+"it"
	ipe4p1c=temaDelPerfetto+"imus"
	ipe5p1c=temaDelPerfetto+"istis"
	ipe6p1c=temaDelPerfetto+"erunt"
	indicativoPerfetto1c=[]
	for x in range(1,7):
		indicativoPerfetto1c.append(eval("ipe"+str(x)+"p1c"))
	#stampa perfetto
	print("Perfetto",indicativoPerfetto1c)
	#print(temaDelPresente)
	#print(temaDelPerfetto)
	
	ippf1c=[]
	DesIPPF=["eram","eras","erat","eramus","eratis","erant"]
	for x in DesIPPF:
		ippf1c.append(temaDelPerfetto+x)
	print("Piùccheperfetto",ippf1c)
	
	ifa1c=[]
	desifa=["ero","eris","erit","erimus","eritis","erint"]
	for x in desifa:
		ifa1c.append(temaDelPerfetto+x)
	print("Futuro Anteriore",ifa1c)
	
	#congiuntivo
	
	print("\n\nCongiuntivo\n")
	
	cp1c=[]
	descp1c=["em","es","et","emus","etis","ent"]
	for x in descp1c:
		cp1c.append(temaDelPresente+x)
	print("Presente",cp1c)