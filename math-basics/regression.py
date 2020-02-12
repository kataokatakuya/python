#回帰

"""
2-1  学習データの確認
"""
"""
import numpy as np
import matplotlib.pyplot as plt

# 学習データを読み込む
train = np.loadtxt('click.csv', delimiter=',', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]

# プロット
plt.plot(train_x, train_y, 'o')
plt.show()
"""




"""
2-2  1次関数として実装
"""

"""
import numpy as np
import matplotlib.pyplot as plt

# 学習データを読み込む
train = np.loadtxt('click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]

# 標準化
mu = train_x.mean()
sigma = train_x.std()
# z-score化(学習データの平均を0、分散を1に変換する)
def standardize(x):
    return (x - mu) / sigma

# 変換後のtrain_x
train_z = standardize(train_x)

# パラメータを初期化
theta0 = np.random.rand()
theta1 = np.random.rand()

# 予測関数
def f(x):
    return theta0 + theta1 * x

# 目的関数
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)

# 学習率
ETA = 1e-3

# 誤差の差分
diff = 1

# 更新回数
count = 1

# 誤差の差分が0.01以下になるまでパラメータ更新を繰り返す
error = E(train_z, train_y)
while diff > 1e-2:
    # 更新結果を一時変数に保存
    tmp_theta0 = theta0 - ETA * np.sum((f(train_z) - train_y))
    tmp_theta1 = theta1 - ETA * np.sum((f(train_z) - train_y) * train_z)

    # パラメータを更新
    theta0 = tmp_theta0
    theta1 = tmp_theta1

    # 前回の誤差との差分を計算
    current_error = E(train_z, train_y)
    diff = error - current_error
    error = current_error

    # ログの出力
    count += 1
    log = '{}回目: theta0 = {:.3f}, theta1 = {:.3f}, 差分 = {:.4f}'
    print(log.format(count, theta0, theta1, diff))

# プロットして確認
x = np.linspace(-3, 3, 100)
plt.plot(train_z, train_y, 'o')
plt.plot(x, f(x))
plt.show()
"""



"""
2-4  多項式回帰の実装
"""
import numpy as np
import matplotlib.pyplot as plt

# 学習データを読み込む
train = np.loadtxt('click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]

# 標準化
mu = train_x.mean()
sigma = train_x.std()
def standardize(x):
    return (x - mu) / sigma

train_z = standardize(train_x)

# 目的関数
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)

# 学習率
ETA = 1e-3

# 誤差の差分
diff = 1

# パラメータを初期化
theta = np.random.rand(3)

# 学習データの行列を作る
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]), x, x ** 2]).T

X = to_matrix(train_z)

# 予測関数
def f(x):
    return np.dot(x, theta)


# 学習を繰り返す
error = E(X, train_y)
while diff > 1e-2:
    # パラメータを更新
    theta = theta - ETA * np.dot(f(X) - train_y, X)
    # 前回の誤差との差分を計算
    current_error = E(X, train_y)
    diff = error - current_error
    error = current_error

# プロット
x = np.linspace(-3, 3, 100)
plt.plot(train_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()
