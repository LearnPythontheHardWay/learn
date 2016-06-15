# 将 There are %d types of people. 赋值给 x ，这句话当中包含有一个格式化字符，值为10
# 接着给两个变量进行赋值
# 然后给 y 赋值，y中包含有前两个变量
# 然后将 x、y 输出
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said %r." % x
print "I also said:'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?!" % r

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e