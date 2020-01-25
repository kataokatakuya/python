"""
スッキリわかるPython入門
"""


"""
コード1-20  割り勘計算プログラムの修正
"""
"""
price = input('料金を入力 >>')
price = int(price)
number = input('人数を入力 >>')
number = int(number)

payment = price/number
payment = int(payment)

print('お支払いは' + str(payment) + '円です')
"""


"""
コード1-22  format関数で文字列に数値を埋め込む
"""
"""
name = '松田光太'
age = 23
height = 175.6
print('私の名前は{}で、年齢は{}で、年齢は身長は{}cmです'.format(name, age, height))
"""


"""
コード1-23  割り勘計算プログラムの修正
"""
"""
price = int(input('料金を入力 >>'))
number = int(input('人数を入力 >>'))

payment = int(price/number)

print('お支払いは{}円です'.format(payment))
"""



"""
練習1-3  BMIの計算
"""
"""
h = int(input('身長(cm)は? >>')) / 100
w = int(input('体重(kg)は? >>'))
bmi = w / h / h

print('BMIは{}です。'.format(bmi))
"""







