"""
スッキリわかるPython入門
"""

"""
コード5-3 hello関数の定義
コード5-4 hello関数の呼び出し
"""
"""
def hello():
    print('こんにちは。工藤です。')

hello()
"""


"""
コード5-7 引数を受け取るhello関数
コード5-8 引数を渡しながらhello関数を呼び出す
"""
"""
def hello(name):
    print('こんにちは。{}です。'.format(name))

hello('浅木')
hello('松田')
"""



"""
コード5-9 複数の引数を受け取るprofile関数
コード5-10 複数の引数を渡しながらprofile関数を呼び出す
"""
"""
def profile(name, age, hobby):
    print('私の名前は{}です'.format(name))
    print('年齢は{}歳です'.format(age))
    print('趣味は{}です'.format(hobby))

profile('浅木', 24, 'カフェ巡り')
"""



"""
コード5-11 リストの平均を求める calc_average関数
"""
"""
def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}です'.format(avg))

scores = [88, 78, 94, 79, 85]
calc_average(scores)
"""

"""
コード5-14 足し算の結果を返すplus関数
コード5-15 plus関数の呼び出し
"""
"""
def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)
print('足し算の答えは{}です'.format(answer))
"""

"""
コード5-12 input_scores関数とcalc_average関数
コード5-13 さまざまな機能を担当する関数の定義
"""
"""
def input_scores(name):
    print('{}さんの試験結果を入力してください'.format(name))
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print('{}さんの平均点は{}です'.format(name, avg))


#浅木と松田の得点入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

#平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

#結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)
"""



"""
コード5-18  2つの戻り値を返す?
"""
"""
def plus_and_minus(a, b):
    return a+b, a-b          #戻り値は一つ → タプルになる

next, prev =plus_and_minus(1978, 1)
"""



"""
コード5-19  戻り値のタプルをアンパック代入
"""
"""
def plus_and_minus(a, b):
    return (a+b, a-b)

(next, prev) = plus_and_minus(1978, 1)
"""



"""
コード5-20  指定された3食を表示するeat関数
コード5-21  松田くんの食生活を出力する
"""
"""
def eat(breakfast, lunch, dinner):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))

print('8月1日')
eat('トースト', 'おにぎり', 'カレー')
print('8月2日')
eat('納豆ごはん', 'ラーメン', 'カレー')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当', 'カレー')
"""


"""
コード5-22  指定された3食を表示するeat関数(デフォルト値を利用)
"""
"""
def eat(breakfast, lunch, dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))

print('8月1日')
eat('トースト', 'おにぎり')
print('8月2日')
eat('納豆ごはん', 'ラーメン')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当')
"""



"""
コード5-24  松田くんの基本なeat関数
"""
"""
def eat(breakfast, lunch='ラーメン', dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))

#以下、4行は同じ意味
eat('納豆ごはん', 'ラーメン', 'カレーうどん')
eat(breakfast='納豆ごはん', dinner='カレーうどん')
eat(dinner='カレーうどん', breakfast='納豆ごはん')
eat('納豆ごはん', dinner='カレーうどん')
"""



"""
コード5-29  おやつも出力できるeat関数(可変長引数を利用)
コード5-30  おやつも食べた日のeat函数の呼び出し(可変長引数を利用)
"""

"""
def eat(breakfast, lunch, dinner='カレー', *desserts):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました'.format(d))

eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')
"""



"""
Column  ディクショナリを用いた可変長引数
"""

"""
def eat(**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key, kwargs[key]))

eat(朝食='納豆', 遅めの昼食='パスタ', 夕方のおやつ='カレーパン')
"""



"""
コード5-34  関数の中からグローバル変数への代入を試みる
コード5-35  global変数を用いてグローバル変数に代入する
"""
"""
name = '松田'
def change_name():
    global name
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')

change_name()
hello()
"""



"""
練習5-2
"""
"""
def is_leapyear(y):
    return (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))

current_year = int(input('現在の西暦を入力してください >>'))
if is_leapyear(current_year):
    print('西暦{}年は、うるう年です'.format(current_year))
else:
    print('西暦{}年は、うるう年ではありません'.format(current_year))
"""



"""
練習5-3
"""
"""
def take_bus():
    print('バスに乗ります')
def walk():
    print('ちょっと歩きます')
def run():
    print('走ります')
    walk()

print('行ってきます!')
walk();take_bus();run();run()
print('ただいま')
"""



"""
練習5-5
"""
"""
def int_input(msg):
    return int(input('{}を入力してください >>'.format(msg)))

def calc_payment(amount, people=2):
    dnum = amount / people       #総額を人数で割る(端数も保持)
    pay = (dnum // 100) * 100    #100円未満を切り捨てる
    if dnum > pay:               #元の値と比較して
        pay = int(pay + 100)     #小さければ100円未満であったので上乗せ
    payorg = amount - pay * (people - 1)   #幹事の支払額の計算
    return [int(pay), int(payorg)]

def show_payment(pay, payorg, people=2):
    print('***支払額***')
    print('1人あたり{}円({}人)、幹事は{}円です'.format(pay, people - 1, payorg))

#計算データの入力
amount = int_input('支払総額')
people = int_input('参加人数')

#割り勘の計算
[pay, payorg] = calc_payment(amount, people)

#結果の表示
show_payment(pay, payorg, people)
""
