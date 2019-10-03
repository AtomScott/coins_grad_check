import sys

sys.path.append("./")
import check
import check2
import pandas as pd

major = int(sys.argv[2])
csv_file = sys.argv[1]

senko = ["ソフトウェアサイエンス","情報システム","知能情報メディア"][major-2]
print("専攻 : "+senko+" GB"+str(major))


df = pd.read_csv(csv_file)

df = check.f(df, senko=senko)
df = check.g(df)
#df = check.h(df)

df = check2.spots2(df, major=major)
df = check2.spots1(df)


print("体育3, 自由単位5.5, 総合I 2, 総合II 5, 総合III 1")

for i,row in df.iterrows():
	print((row["科目番号"],row["単位"],row["科目名"]))