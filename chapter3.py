"""
スッキリわかるPython入門
"""

"""
コード3-1  いつも同じことを言うチャットボット
"""
"""
name = input('あなたの名前を教えてください >>')
print('{}さん、こんにちは'.format(name))
food = input('{}さんの好きな食べ物を教えてください >>'.format(name))
print('私も{}が好きですよ'.format(food))
"""


"""
コード3-2  答えが分岐するチャットボット
"""
"""
name = input('あなたの名前を教えてください >>')
print('{}さん、こんにちはこんにちは!'.format(name))
food = input('{}さんの好きな食べ物を教えてください >>'.format(name))

if food == 'カレー':
    print('素敵です。カレーは最高ですよね!!')
else:
    print('私も{}が好きですよ!'.format(food))
"""



"""
コード3-3  常に追試を受けることになる判定プログラム
"""
"""
score = int(input('試験の点数を入力してください >>'))
if score >= 60:
    print('合格')
    print('よく頑張りましたね')
else:
    print('残念ながら不合格です')
print('追試を受けてください')
"""



"""
コード3-4  どんなカレーでも絶賛するチャットボット
"""
"""
name = input('あなたの名前を入力してください >>')
print('{}さん、こんにちは'.format(name))
food = input('{}さんの好きな食べ物を教えてください >>'.format(name))

if 'カレー' in food:
    print('素敵です。カレーは最高ですよね!!')
else:
    print('私も{}が好きですよ!'.format(food))
"""




"""
コード3-5  100点があるかどうかを調べる
"""
"""
scores = [80, 100, 20, 60]
if 100 in scores:
    print('100点満点の試験があったんですね。おめでとう!')
else:
    print('次はどれか1つでも100点満点を取ろう')
"""



"""
コード3-6  ディクショナリのキーをチェックする
"""
"""
scores = {'network': 60, 'database': 80, 'security': 50}

key = input('追加する科目名を入力してください >>')
if key in scores:
    print('すでに登録済みです')
else:
    data = int(input('得点を入力してください >>'))
    scores[key] = data
print(scores)
"""



"""
コード3-7  条件式の評価結果を確認する
"""
"""
score = int(input('試験の点数を入力 >>'))
print(score >= 60)
"""


"""
コード3-8  elseブロックのない処理
"""
"""
name = input('あなたの名前を教えてください >>')
print('{}さん、こんにちは'.format(name))

if name == '松田':
    print('松田さんに会えて嬉しいです')

food = input('{}さんの好きな食べ物を教えてください >>'.format(name))

if 'カレー' in food:
    print('素敵です。とにかくカレーは最高ですよね!!')
else:
    print('私も{}が好きですよ'.format(food))
"""



"""
コード3-9  多分岐するif文
"""
"""
score = int(input('試験の点数を入力してください >>'))
if score < 0 or score > 100:
    print('異常な得点です')
    print('入力し直してください')
elif score >= 60:
    print('合格!')
    print('よくがんばりましたね')
else:
    print('残念ながら不合格です')
    print('追試を受けてください')
"""



"""
コード3-10  晩ご飯をレコメンドするチャットボット
"""
"""
print('すべての質問に y または n で答えてください')
okane_aruka = input('お金に余裕はありますか? >>')

if okane_aruka == 'y':
    onaka_suiteruka = input('お腹がすごく空いてますか? >>')
    nomitai_kibunka = input('ビールを飲みたいですか? >>')

    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかがですか')
    elif onaka_suiteruka == 'y':
        print('カレーはいかがですか')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかがですか')
    else:
        print('パスタはいかがですか')
    yashoku_iruka = input('夜食は必要ですか? >>')

    if yashoku_iruka == 'y':
        print('コンビニのチキンはいかがですか')

else:
    print('家で食べましょう')
"""



"""
練習3-3 (1)
"""
"""
isError = False
n = 99
if isError == False and n < 100:
    print('正解です')
"""


"""
練習3-3 (2)
"""
"""
number = int(input('数値を入力してください >>'))
if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')
"""


"""
練習3-3 (3)
"""
"""
greeting = input('挨拶をどうぞ >>')
if greeting == 'こんにちは':
    print('ようこそ')
elif greeting == '景気は?':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で!')
else:
    print('どうしました?')
"""



"""
Column 三項条件演算子
"""
"""
number = int(input('数値を入力してください >>'))
div = '偶数' if number % 2 == 0 else '奇数'
print('{}です'.format(div))
"""







