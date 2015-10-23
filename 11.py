# coding: utf-8

#　辞書 key value

# 出力結果のシングルクォーテーションは辞書型のkeyを示す区切り文字である


sales = {"taguchi":200 , "aaa":100, "bbbb":300}
# sales2 = {'taguchi':200 , 'aaa':100, 'bbb':300}


print sales
print "taguchi" in sales

print sales["taguchi"]

sales["taguchi"] = 500
print sales["taguchi"]

print sales.keys()
print sales.values()
print sales.items()

# print sales2
