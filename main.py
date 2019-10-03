import sys

sys.path.append("./")
import check
import check2
import pandas as pd

major = 4
senko = ["ソフトウェアサイエンス","情報システム","知能情報メディア"][major-2]
print("専攻 : "+senko+" GB"+str(major))


df = pd.read_csv('./data.csv')
df = check.f(df, senko=senko)

df = check2.spots1(df)
df = check2.spots2(df, major=major)