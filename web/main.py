# coding=utf-8
def temp_convert(var):
    try:
        a= int(var)
        print "in try"

    #异常发生时不会被执行
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument
        print "in func there is somthing wrong:" + str(Argument)

temp_convert("god")