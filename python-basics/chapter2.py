"""
スッキリわかるPython入門
"""

"""
コード2-1  点数管理プログラム
"""
"""
network = 88
database = 95
security = 90
sum = network + database + security

avg = sum / 3

print('合計点:{}'.format(sum))
print('平均点:{}'.format(avg))
"""



"""
コード2-2  リストの作成
コード2-3  リストの要素を参照
コード2-4  リストの要素を参照(エラー)
"""
"""
members = ['工藤', '松田', '浅木']
print(members)
print(members[0])
#print(members[3])
"""



"""
コード2-5  試験の合計と平均を求める
コード2-6  sum関数を用いて合計を求める
"""
"""
scores = [88, 90, 95]
total = sum(scores)
print('合計{}点'.format(total))
"""



"""
コード2-7  リストの合計値と平均値を求める
"""
"""
scores = [88, 90, 95]
total = sum(scores)
avg = total / len(scores)

print('合計{}点、平均{}点'.format(total,avg))
"""



"""
コード2-8  リストに要素を追加
"""
"""
members = ['工藤', '松田', '浅木']
members.append('菅原')
members.append('湊')
members.append('朝香')

print(members)
"""



"""
コード2-9  リストから要素を削除
"""
"""
members = ['工藤', '松田', '浅木']
members.remove('松田')
print(members)
"""



"""
コード2-10  リストの要素を変更
"""
"""
members = ['工藤', '松田', '浅木']
members[0] = '菅原'
print(members)
"""



"""
コード2-11  スライスによる範囲指定
"""
"""
a = [10, 20, 30, 40, 50]
print(a[1:3])
print(a[2:])
print(a[:3])
"""



"""
コード2-12  負の数による指定
"""
"""
a = [10, 20, 30, 40, 50]
print(a[-1])
print(a[-2])
"""



"""
コード2-13  ディクショナリの作成
"""
"""
scores = {'network':60, 'database':80, 'security':50}
print(scores)
"""



"""
コード2-14  ディクショナリの要素を参照
"""
"""
scores = {'network':60, 'database':80, 'security':50}
print(scores['database'])
"""



"""
コード2-15  ディクショナリの要素の追加と変更
"""
"""
scores = {'network':60, 'database':80, 'security':50}
scores['programming'] = 65
scores['security'] = 55
print(scores)
"""



"""
コード2-16  ディクショナリの要素を削除
"""
"""
scores = {'network':60, 'database':80, 'security':55}
del scores['security']
print(scores)
"""



"""
Column  ディクショナリの合計
"""
"""
scores = {'network':60, 'database':80, 'security':50}
total = sum(scores.values())
print(total)
"""



"""
コード2-17  タプルの利用
"""
"""
scores = (70, 80, 55)
print(scores)
print(scores[0])
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))
"""



"""
コード2-18  タプルの要素を変更(エラー)
"""
"""
scores = (70, 80, 55)
scores[0] = 80
"""



"""
コード2-19  要素数が1つのリストとディクショナリ
"""
"""
members = ['松田']
scores = {'network':82}
print(members)
print(scores)
"""



"""
コード2-20
"""
"""
members = ('松田')
print(type(members))
"""



"""
コード2-21  要素数のタプル
"""
"""
members = ('松田',)
print(type(members))
"""



"""
コード2-22  セットの応用
"""
"""
scores = {70, 80, 55, 80}
scores.add(80);
print(scores)
print('要素数は{}'.format(len(scores)))
print('合計点は{}'.format(sum(scores)))
"""



"""
コード2-23  コレクションの相互変換
"""
"""
scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))
"""



"""
コード2-24  ディクショナリの中にディクショナリをネスト
"""

"""
matsuda_scores = {'network':60, 'database':80, 'security':50}
asagi_scores = {'network':80, 'database':75, 'security':92}
members_scores = {
  '松田': matsuda_scores,
  '浅木': asagi_scores
}
"""


"""
コード2-25  ディクショナリの中にセットをネスト
"""

"""
members_hobbies = {
  '松田': {'SNS', '麻雀', '自転車'},
  '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}

# 全員の趣味一覧を表示する
print(members_hobbies)
print(members_hobbies['松田'])
print(members_hobbies['浅木'])
"""



"""
コード2-26  2次元リストの例
"""
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c)
print(c[0])
print(c[1][2])
"""



"""
コード2-27  セットの&演算
"""
"""
member_hobbies = {
  '松田': {'SNS', '麻雀', '自転車'},
  '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)
"""



"""
コード2-28  4つの集合演算
"""
"""
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
"""



"""
練習2-2
"""
"""
scores = []
scores.append(int(input('国語の点数 >>')))
scores.append(int(input('算数の点数 >>')))
scores.append(int(input('理科の点数 >>')))
scores.append(int(input('社会の点数 >>')))
scores.append(int(input('英語の点数 >>')))

print(f'合計点 {sum(scores)}点 / 平均 {sum(scores) / len(scores)}点')
"""



"""
練習2-3
"""
"""
player1 = {'読書', '昼寝', '映画鑑賞', '散歩', '料理'}
player2 = {'テニス', '将棋', '料理', '読書', '旅行'}
input('心の準備ができたらEnterキーを押してください')
common = player1 & player2
total = player1 | player2

compatibility_rate = (len(common) / len(total)) * 100
print(f'相性度は{compatibility_rate}パーセントでした')
"""


