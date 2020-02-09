"""
スッキリわかるPython入門
"""

"""
コード6-3 strオブジェクトのメソッドを活用した血液型占い
"""
"""
userinfo = input('名前と血液型をカンマで区切って1行で入力 >>')
[name, blood] = userinfo.split(',')
blood = blood.upper().strip()

print('{}さんは{}型なので大吉です'.format(name, blood))
"""



"""
Column
"""
"""
def add(x, y):
    return x+y

type(add)
print(type(add))
newadd = add
print(newadd(4, 5))
"""



"""
コード6-4 リテラルやクラス名関数を用いたオブジェクトの生成
"""
"""
int_value1 = 0
int_value2 = int()
int_value3 = int(9)
list_value1 = []
list_value2 = list()
list_value3 = list(('松田', '浅木'))

print(int_value1)
print(int_value2)
print(int_value3)
print(list_value1)
print(list_value2)
print(list_value3)
"""



"""
コード6-5  RPGの勇者を表すクラスの定義と利用
"""
"""
class Hero:
    name = '松田'
    hp = 100
    def sleep(self, hours):
        print('{}は{}時間寝た!'.format(self.name, hours))
        self.hp += 100

#ゲーム開始
print('スッキリファンタジーXII  ~金色の理想郷~')
h = Hero()
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name, h.hp))
"""



"""
コード6-6  オブジェクトのidentityの確認
"""
"""
scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print('scores1のidentity: {}'.format(id(scores1)))
print('scores2のidentity: {}'.format(id(scores2)))

if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')
"""



"""
コード6-7  リストオブジェクトのコピーによる不可解な動作
"""
"""
scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print('scores1の先頭要素は{}'.format(scores1[0]))
print('scores2の先頭要素は{}'.format(scores2[0]))

print('変数scores2の中身を変数scores1に代入(コピー)します')
scores1 = scores2

print('scores1の先頭要素を90に書き換えます')
scores1[0] = 90

print('90を代入したscores1の先頭要素は{}'.format(scores1[0]))
print('90を代入していないscores2の先頭要素は{}'.format(scores2[0]))
"""



"""
コード6-8  関数に渡すと変数の内容を書き換えられてしまう
"""
"""
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
after_names = add_suffix(before_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])
"""



"""
コード6-9  防御的コピーを用いて悪影響を防ぐ
"""
"""
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
copied_names = list()
for n in before_names:
    copied_names.append(n)
after_names = add_suffix(copied_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])
"""



"""
コード6-10  文字列を引き渡しても悪影響が起きない
"""
"""
def add_suffix(name):
    name = name + 'さん'
    return name

before_name = '松田'
after_name = add_suffix(before_name)
print('さん付け後:' + after_name)
print('さん付け前:' + before_name)
"""



"""
コード6-11  リストと文字列による書き換え時のidentity値の変化
"""
"""
names = list()     #リストの場合
print('変更前のlistのidentity: {}'.format(id(names)))
names.append('松田')
print('変更後のlistのidentity: {}'.format(id(names)))

name = '松田'     #文字列の場合
print('変更前のstrのidentity: {}'.format(id(name)))
name = 'スーパー' + name
print('変更後のstrのidentity: {}'.format(id(name)))
"""



"""
練習6-3
"""
"""
def welcome(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] = u['age'] + 1
    print('あなたは来年{}歳だから大吉です!'.format(u['age']))

username = input('名前を入力してください >>')
userage = int(input('年齢を入力してください >>'))
user = {'name': username, 'age': userage}

copied_user = user.copy()
welcome(copied_user)

print('{}歳の{}さん、またプレイしてくださいね'.format(user['age'], user['name']))
"""


