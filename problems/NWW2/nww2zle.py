def nwd(a,b):
	if b > a:
		temp = b
		b = a
		a = temp
	while True:
		if b == 0:
			break
		temp = a % b
		a = b
		b = temp
	return b

ile = int(input())
for test in range(0,ile):
	ile2 = int(input())
	a = input().split()
	if ile2 ==1:
 		print(a[0])
	else:
 		wynik = int(a[0])
 		for i in range(1, ile2):
 			ii = int(a[i])
 			wynik *= (ii//nwd(wynik,ii))
 		print(str(wynik))