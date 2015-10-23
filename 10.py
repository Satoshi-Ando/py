# coding: utf-8

# 集合体
# 論理計算ができる⇒データ抽出など


a = set([1, 2, 3, 4])
b = set([3, 4, 5])
print a
print b

print a - b
print a | b
print a & b
print a ^ b

c = a - b
print c | a
