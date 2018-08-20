#coding=utf-8
def check_accountinfo(name ,id):

    # accountinfo =self.get_accountinfo()
    accountinfo=[u'六*',u'411325****0522****']



    namestr =accountinfo[0].strip('*')
    idstr_one =accountinfo[1][0:5]
    idstr_two =accountinfo[1][10:14]

    print idstr_two
    return namestr in name and idstr_one in id and idstr_two in id

name=u'六谁'
id='411325198005221234'
print check_accountinfo(name,id)
