# 常量信息
from WECHAT.csxx import *
for i in range(1):
     no=INT()
     flno = FLOAT()
     uppercase = UPPERCASE()
     lowercase = LOWERCASE()
     fh = FH()
     zfq=ZFC()
     # ch=GB2312()
objects1 = 'xxxx'
WORDS = {'整数':no,
         '小数':flno,
         '大写':uppercase,
         '小写':lowercase,
         '符号':fh,
         '字符串':zfq,
         '为空': '',
         '空格': '   ',
         'object':objects1,
         '过短':'1',
         '超长':'11111111111111111111111111111111111111111111111111111111111111111111111111111111',
         'sql注入1':"and 1=(select IS_SRVROLEMEMBER('sysadmin'))",
         'sql注入2':'and(select count(*) from sysobjects)>0 mssql',
         'sql注入3':"'and 1=2",
         'sql注入4':"'and 1=1",
         'sql注入5':"'or 1=1 --",}
URL = "http://172.17.12.66/ocm-info-webin/rest"
API={'会员快速注册':{'number':'1','url':URL,'querystring':{'ent_id':'0','method':'efuture.ocm.info.main.fastregister'}},
    '会员身份认证':{'number':'2','url':URL,'querystring':{'ent_id':'0','method':'efuture.ocm.info.main.auth'}}}