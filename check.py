import pandas as pd

senko = 'ソフトウェアサイエンス'

df0 = pd.read_csv('./data.csv')
df0.columns = df0.columns.str.strip()

# 不合格単位を落とす
df1 = df0[~df0['成績'].isin(['D'])]

# 専門科目必修科目
senmon_hisshu = ['コンピュータリテラシ', 'プログラミング入門A', 'プログラミング入門B', '情報科学概論I', '情報科学概論II', 'データ構造とアルゴリズム','データ構造とアルゴリズム実験', '情報科学基礎実験', '論理回路', '{0}実験A'.format(senko), '{0}実験B'.format(senko),'卒業研究A', '卒業研究B']

df2 = df1[~df1['科目名'].isin(senmon_hisshu)]

# 専門基礎科目必修科目
senmonkiso_hisshu = ['線形代数I', '線形代数II', '解析学I', '解析学II', '離散構造', '電磁気学', 'シミュレーション物理', '専門語学A', '専門語学B']

df3 = df2[~df2['科目名'].isin(senmonkiso_hisshu)]

# 専門基礎科目選択科目 （残す）
senmonkiso_sentaku = ['解析学Ⅲ', '複素環数論', 'コンピュータ数学', '確率論', '力学', '技術英語', '情報特別演習Ⅰ', '情報特別演習Ⅱ', 'Mathematics for Computer Science']

print('正しくできていたらTrue: ', len(df3)==len(df1) - len(senmon_hisshu) -len(senmonkiso_hisshu))

print(df3['科目名'])
