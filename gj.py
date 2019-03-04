# 生成字典参数
from WECHAT.cl import WORDS
class DICT:
    def allwords(self,LINE,LIST):
        LINES=[]
        LISTS=[]
        CSLB=dict(LINE)
        LISTS.append(LINE)
        CS=list(LIST.keys())
        for i in CS:
            cs=LIST[i]
            for j in cs:
                LINES.append(j)
        CSLBkey=list(CSLB.keys())
        for i in CSLBkey:
            C=CSLB[i]
            for j in LINES:
                CSLB[i]=j
                LISTS.append(str(CSLB))
            CSLB[i]=C
        return LISTS