"""
スッキリわかるPython入門
"""

"""
コード4-2  ひつじを数えるのを3回繰り返す
"""
"""
count = 0
while count < 3:
    count += 1
    print('ひつじが{}匹'.format(count))
print('おやすみなさい・・・')
"""



"""
コード4-3  無限ループ
"""
"""
count = 0
while count < 3:
    print('ひつじが{}匹'.format(count))
print('おやすみなさい・・・')
"""



"""
コード4-4  ひつじを数えるの眠るまで繰り返す
"""
"""
is_awake = True
count = 0

while is_awake == True:
    count += 1
    print('ひつじが{}匹・・・'.format(count))
    key = input('もう眠りそうですか?(y/n) >>')
    if key == 'y':
        is_awake = False
print('おやすみなさい・・・')
"""



"""
コード4-5  繰り返しを使って得点リストを作成する
"""
"""
count = 0
student_num = int(input('学生の数を入力 >>'))
score_list = list()

while count < student_num:
    count += 1
    score = int(input('{}人目の試験の得点を入力 >>'.format(count)))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print('平均点は{}点です'.format(total / student_num))
"""



"""
コード4-6  リストの全要素を繰り返し参照する
"""
"""
scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1
"""



"""
コード4-7  for文でリストの全要素を参照する
"""
"""
scores = [80, 20, 75, 60]
for data in scores:
    if data >= 60:
        print('合格')
    else:
        print('不合格')
"""



"""
コード4-8  for文で決まった回数を繰り返す
"""
"""
for num in range(3):
    print('Pythonは楽しい')
"""



"""
コード4-9  データのまとまりからサンプルを抽出する
"""
"""
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
samples = list()

for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)
"""



"""
コード4-10  目標数に達したら繰り返しを終了する
"""
"""
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
samples = list()

for data in ages:
    if 20 <= data <30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)
"""



"""
コード4-11  不要な回のループをスキップする
"""
"""
ages = [28, 50, 'ひみつ', 20, 78, 25, 22, 10, '無回答', 33]
samples = list()
for data in ages:
    if not isinstance(data, int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)
"""



"""
練習4-2
"""
"""
count = 1
ans = True

print('カレーを召し上がれ')
print('{}皿のカレーを食べました'.format(count))

while ans:
    key = input('おかわりはいかがですか? (y/n) >>')

    if key == 'y':
        count += 1
    else:
        ans = False

print('ごちそうさまでした')
"""



"""
練習4-3
"""
"""
for n in range(10):
    print('{}、'.format(10 - n), end = '')
print('List off!')
"""



"""
練習4-4 (1)
"""
"""
for i in range(9):
    for j in range(9):
        print('{}×{}={}'.format(i+1, j+1, (i+1)*(j+1)))
"""



"""
練習4-4 (2)
"""
"""
for i in range(9):
    if (i + 1) % 2 == 0:
        continue
    for j in range(9):
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')
"""



"""
練習4-4 (3)
"""
"""
for i in range(9):
    if (i +1) % 2 == 0:
        continue
    for j in range(9):
        if (i+1)*(j+1) > 50:
            break
        print('{}×{}={}'.format(i+1, j+1, (i+1)*(j+1)))
"""



"""
練習4-5
"""
"""
temp = list()
for n in range(10):
    data = float(input('{}個目のデータを入力 >>'.format(n+1)))
    temp.append(data)

for count in range(len(temp)):
    print('{}時 {}度'.format(count+8, temp[count]))


temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

total = 0
for data in temp_new:
    if isinstance(data, float):
        total = total + data
print(total / len(temp_new) -1)
"""



"""
練習4-6
"""
"""
numbers = [1, 1]
data = sum(numbers)
count = 2

while count <= 10:
    numbers.append(data)
    data = data + numbers[count-1]
    count += 1
print(numbers)


ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratios.append(numbers[count+1] / numbers[count])
print(ratios)


for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)
"""



