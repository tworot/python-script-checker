def nwd(aa, bb):
	a = 0
	b = 0
	if bb > aa:
		a = bb
		b = aa
	else:
		a = aa
		b = bb

	while True:
		a = a-b
		if b > a:
			temp = a
			a = b
			b = temp
		if b == 0:
			return a
	return None

ile = int(input())
for i in range(0,ile):
	aa, bb = input().split()
	print(str(nwd(int(aa),int(bb))))