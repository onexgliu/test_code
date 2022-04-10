import string
s1='{:0>5}'
formatter = string.Formatter()
data={'订单编号':[1,2,3],'会员名':['mrsoft','mingri','mr']}
list1=data['订单编号']
for i in list1:
  val = formatter.format(s1, i)
  print(val)
