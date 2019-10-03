import pandas as pd

senko = 'ソフトウェアサイエンス'

def f(df0, senko):
    df0.columns = df0.columns.str.strip()
    df0 = df0.dropna(subset=['科目名'])

    # 不合格単位を落とす
    df1 = df0[~df0['成績'].isin(['D'])]

    # 専門科目必修科目
    senmon_hisshu = ['コンピュータリテラシ', 'プログラミング入門A', 'プログラミング入門B', '情報科学概論I', '情報科学概論II', 'データ構造とアルゴリズム','データ構造とアルゴリズム実験', '情報科学基礎実験', '論理回路', '論理回路実験', '{0}実験A'.format(senko), '{0}実験B'.format(senko),'卒業研究A', '卒業研究B']

    df2 = df1[~df1['科目名'].isin(senmon_hisshu)]

    # 専門基礎科目必修科目
    senmonkiso_hisshu = ['線形代数I', '線形代数II', '解析学I', '解析学II', '離散構造', '電磁気学', 'シミュレーション物理', '専門語学A', '専門語学B']

    df3 = df2[~df2['科目名'].isin(senmonkiso_hisshu)]

    # 専門基礎科目選択科目 （残す）
    senmonkiso_sentaku = ['解析学Ⅲ', '複素環数論', 'コンピュータ数学', '確率論', '力学', '技術英語', '情報特別演習Ⅰ', '情報特別演習Ⅱ', 'Mathematics for Computer Science']

    print("必修")
    if len(df3)==len(df1) - len(senmon_hisshu) -len(senmonkiso_hisshu):
        print("\tクリア")
    else:
        print("\t卒業できません")
    #print('正しくできていたらTrue: ', len(df3)==len(df1) - len(senmon_hisshu) -len(senmonkiso_hisshu))

    #print(df3['科目名'])

    return df3

# eigo check
def g(df):
    kamoku = df[df['科目名'].str.startswith('English')]
    df = df[~df['科目名'].str.startswith('English')]
    tannisu = kamoku['単位'].sum()
    print("英語")

    for i, row in kamoku.iterrows():
        print((row["科目番号"],row["単位"],row["科目名"]))

    if tannisu > 5.5:
        print("\tクリア", end=': ')
    else:
        print("\t卒業できません", end=': ')
    print(str(tannisu)+"/"+str(5.5))

    return df

# taiku hajiku
def h(df):
    df = df[~df['科目番号'].str.startswith('2')]
    return df
