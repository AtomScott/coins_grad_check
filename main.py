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

df = check2.spots2(df, major=major)
df = check2.spots1(df)