# coding=utf-8

#login
LOGIN_LOC={
    "LoginSub":"com.pitaya.daokoudai:id/login_submit",

    "Tel":"com.pitaya.daokoudai:id/auto_tv_account",

    "LoginPwd":"com.pitaya.daokoudai:id/et_pwd",

    "LoginBtn":"com.pitaya.daokoudai:id/bt_login",

    "PwdMiss":"com.pitaya.daokoudai:id/bt_forget_psw",

    "RegiBtn":"com.pitaya.daokoudai:id/bt_regist",

    "cachelayout":"android.widget.LinearLayout",

    "GesturPwd":"com.pitaya.daokoudai:id/gestureLockView"

}

PORTAL_LOC={
    "Navigator":"android.widget.LinearLayout",

    "More":'new UiSelector().classNameMatches(".*TextView$").text("更多")',

    "Myaccount":'new UiSelector().classNameMatches(".*TextView$").text("我的账户")',

    "Project":'new UiSelector().classNameMatches(".*TextView$").text("投资项目")',

    "DKD":'new UiSelector().classNameMatches(".*TextView$").text("道口贷")'

}

MYACCOUNT_LOC={
    "CapAccount":"com.pitaya.daokoudai:id/rl_bank"

}

CAPACCOUNT_LOC={
    "RealName":"com.pitaya.daokoudai:id/et_name",

    "ID":"com.pitaya.daokoudai:id/et_id",

    "BankCard":"com.pitaya.daokoudai:id/et_card",

    "BankList":"com.pitaya.daokoudai:id/tv_bank_name",
    
    "Tel":"com.pitaya.daokoudai:id/et_phone",

    "NextStep":"com.pitaya.daokoudai:id/bt_confirm",

    "ImgLeft":"com.pitaya.daokoudai:id/iv_left",

    "ImgRight":"com.pitaya.daokoudai:id/iv_right",

    "PictureList":"com.pitaya.daokoudai:id/folder_list",

    "Picture":"com.pitaya.daokoudai:id/picture",

    "OpenAccountBtnSubmit":"com.pitaya.daokoudai:id/bt_confirm"
}

AccountInfo_LOC={
    "Name":"com.pitaya.daokoudai:id/tv_name",
    "Id":"com.pitaya.daokoudai:id/tv_id",
    "Account":"com.pitaya.daokoudai:id/tv_account",
    "Bank":"com.pitaya.daokoudai:id/tv_account",
    "BankLocation":"com.pitaya.daokoudai:id/tv_province"

}

BankList_LOC={
    "BOC":'new UiSelector().classNameMatches(".*TextView$").text("中国银行")',

    "CCB":'new UiSelector().classNameMatches(".*TextView$").text("中国建设银行")',

    "ABC": 'new UiSelector().classNameMatches(".*TextView$").text("中国农业银行")',

    "ICBC": 'new UiSelector().classNameMatches(".*TextView$").text("中国工商银行")',

    "BCM": 'new UiSelector().classNameMatches(".*TextView$").text("中国交通银行")'

}

LMOpen_LOC={
    "VerifyCodeBtn":u"获取验证码",
    "RegisterBtn":u"同意协议确定注册",
    "Know":u"知道了 Link",
    "VerifyCodeText":"android.widget.EditText",
    "TradePwd":"android.widget.EditText",
    "TradePwdConfirm":"android.widget.EditText"

}