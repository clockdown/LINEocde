import pandas as pd
import collections


def set_words(ds1=[]):
	"""
	それぞれの文字数のリストを作成
	引数 ds:pandasのデータフレーム
	戻り値 x,y,z 8,6,4文字の単語のリスト
	"""
	print("start set_words")
	x, y, z = [], [], []

	f1 = ds1.columns[0]
	print(f1)
	for i in range(len(str(ds1[f1]))):
		if len(str(ds1[f1].ix[i])) == 4:
			z.append(str(ds1[f1].ix[i]))
		elif len(str(ds1[f1].ix[i])) == 6:
			y.append(str(ds1[f1].ix[i]))
		elif len(str(ds1[f1].ix[i])) == 8:
			x.append(str(ds1[f1].ix[i]))
		else:
			pass
	print("set_words fin")
	return x, y, z


def judge(data):
	"""
	文字列に重なりがないか判定
	引数 data:単語のリスト
	戻り値 s:重なりがなかった単語のリスト
	"""
	print("start judge")
	s = []
	for i in data:
		size = collections.Counter(i)#要素数をカウント
		if size.most_common(1)[0][1] <= 1:#最も多い要素の要素数を抽出
			s.append(i)
		else:
			pass
	print("judge fin")
	return s


def make_pair(x, y, z):
	"""
	文字が同じなはずのところを検証
	"""
	print("start make_pair")
	pxy, pxz, pyz = [], [], []
	for i in range(len(x)):
		for j in range(len(y)):
			if (x[i][3] == y[j][5]) and (x[i][4] == y[j][4]) and (x[i][7] == y[j][2]):
				for k in range(len(z)):
					if (x[i][0] == z[k][2]) and (x[i][5] == z[k][1]):
						print(x[i], y[j], z[k])
					else:
						pass
			else:
				pass
	print("make_pair fin")


def main():
	ds = []
	ds.append(pd.read_csv('./csv/myDIC001.csv', encoding="SHIFT-JIS"))
	ds.append(pd.read_csv('./csv/myDIC002.csv', encoding="SHIFT-JIS"))
	x, y, z = [], [], []
	for i in ds:
		x1, y1, z1 = set_words(i)
		x.extend(x1)
		y.extend(y1)
		z.extend(z1)
	x = judge(x)
	y = judge(y)
	z = judge(z)
	make_pair(x, y, z)


if __name__ == '__main__':
	main()