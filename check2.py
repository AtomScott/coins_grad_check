# coding: utf-8




import pandas as pd
import re




def check(bag, thr):
	total = 0
	for kamoku in bag:
		print(kamoku)
		total += kamoku[1]

	if total >= thr:
		print("\tクリア : " + str(total)+"/"+str(thr))
	else:
		print("\t卒業できません" + str(total)+"/"+str(thr))


	print("===================")


def spots1(df):


	# 単位の大きい順にソート　この枠の単位は最大2という前提
	df = df.sort_values("単位", ascending=False)

	spot1 = ["解析学III","複素関数論","コンピュータ数学","確率論","力学","技術英語","情報特別演習I","情報特別演習II","Mathematics for Computer Science"]
	spot1_scores = []


	bag1 = []
	bag2 = []
	bag3 = []

	thr1 = 8
	thr2 = 12
	thr3 = 4

	total1 = 0
	total2 = 0
	total3 = 0

	for i,row in df.iterrows():
		if str(row["科目名"]) in spot1:
			if total1 < thr1:
				total1 += row["単位"]
				bag1.append((row["科目番号"],row["単位"],row["科目名"]))
			else:
				total2 += row["単位"]
				bag2.append((row["科目番号"],row["単位"],row["科目名"]))

			df = df[df['科目番号'] != row["科目番号"]]

	# spot1終了


	for i,row in df.iterrows():
		if str(row["科目番号"])[:3] == "GB1" or str(row["科目番号"])[:3] == "GA1":
			if total2 < thr2:
				total2 += row["単位"]
				bag2.append((row["科目番号"],row["単位"],row["科目名"]))
				df = df[df['科目番号'] != row["科目番号"]]


	# spot2終了


	for i,row in df.iterrows():
		if (str(row["科目番号"])[:2] == "GB" and str(row["科目番号"])[:3] != "GB0") or str(row["科目番号"])[:3] == "GA1":
			total3 += row["単位"]
			bag3.append((row["科目番号"],row["単位"],row["科目名"]))
			df = df[df['科目番号'] != row["科目番号"]]




	print("専門基礎科目 選択科目")
	check(bag1, thr1)


	check(bag2, thr2)

	print("専門科目 自由科目")
	check(bag3, thr3)


	return df




def spots2(df, major):



	# 単位の大きい順にソート　この枠の単位は最大2という前提
	df = df.sort_values("単位", ascending=False)


	bag1 = []
	bag2 = []
	bag3 = []

	thr1 = 10
	thr2 = 12
	thr3 = 8

	total1 = 0
	total2 = 0
	total3 = 0



	for i,row in df.iterrows():
		if str(row["科目番号"])[:3] == "GB"+str(major) and str(row["科目番号"])[:4] != "GB"+str(major)+"0" and str(row["科目番号"]) != "GB42101":
			if total1 < thr1:
				total1 += row["単位"]
				bag1.append((row["科目番号"],row["単位"],row["科目名"]))
				df = df[df['科目番号'] != row["科目番号"]]



	for i,row in df.iterrows():
		if str(row["科目番号"])[:4] == "GB"+str(major)+"0" or (major == 4 and str(row["科目番号"]) == "GB42101"):
			if total1 < thr1:
				total1 += row["単位"]
				bag1.append((row["科目番号"],row["単位"],row["科目名"]))
			else:
				total2 += row["単位"]
				bag2.append((row["科目番号"],row["単位"],row["科目名"]))

			df = df[df['科目番号'] != row["科目番号"]]

	### ここまででspot1終了




	for i,row in df.iterrows():
		if str(row["科目番号"])[:4] == "GB20" or str(row["科目番号"])[:4] == "GB30" or str(row["科目番号"])[:4] == "GB40" or str(row["科目番号"]) == "GB42101":
			if total2 < thr2:
				total2 += row["単位"]
				bag2.append((row["科目番号"],row["単位"],row["科目名"]))
			else:
				total3 += row["単位"]
				bag3.append((row["科目番号"],row["単位"],row["科目名"]))

			df = df[df['科目番号'] != row["科目番号"]]

	### ここまででspot2終了



	for i,row in df.iterrows():
		if str(row["科目番号"])[:3] == "GB2" or str(row["科目番号"])[:3] == "GB3" or str(row["科目番号"])[:3] == "GB4":
			if total3 < thr3:
				total3 += row["単位"]
				bag3.append((row["科目番号"],row["単位"],row["科目名"]))

				df = df[df['科目番号'] != row["科目番号"]]




	print("GB"+str(major))
	check(bag1, thr1)


	print("GB20, GB30, GB40, 情報セキュリティ")
	check(bag2, thr2)
	print("GB2, GB3, GB4")
	check(bag3, thr3)



	return df



