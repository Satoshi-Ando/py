# coding: utf-8

#������ key value

# ���Ϸ�̤Υ��󥰥륯�����ơ������ϼ��񷿤�key�򼨤����ڤ�ʸ���Ǥ���


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
