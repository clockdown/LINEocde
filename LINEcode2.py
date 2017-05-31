s = "hwnujaotcktxjuvahk"
alphabet = [chr(i) for i in range(97, 97+26)]
number = [i for i in range(26)]

a_to_n = dict(zip(alphabet, number))
n_to_a = dict(zip(number, alphabet))

ans = []
for i in range(26):
	t = list(s)
	for j in range(len(t)):
		x = (a_to_n[t[j]] + i) % 26
		t[j] = n_to_a[x]
	t.insert(8, ' ')
	t.insert(15, ' ')
	t = "".join(t)
	ans.append(t)
	print(s, "->", t)
	print(str(i+1)+"sentence convert")

print(ans)