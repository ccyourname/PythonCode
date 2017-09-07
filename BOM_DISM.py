#coding=gbk
#__author__ ="谢飞"
from tkinter import *
import dbcfg
class Bom_dsm:
    def dsmbom(self,date,partno):
        sql=("SELECT a.ComponentPartNo,b.PartDesc ,a.Qty,a.Type FROM  dbo.MFG_BOM a "
             "INNER JOIN dbo.MFG_PartDetail b ON a.ComponentPartNo=b.PartNo "
             "WHERE (a.EffStartTime<='%s' and a.EffExpireTime >='%s' )AND a.ParentPartNo = '%s' "
             "AND b.FactoryCode='1140' AND a.FactoryCode='1140'"%(date,date,partno))
        db_bom=dbcfg.cursor1.execute(sql)
        bom_str =[i for i in db_bom ]
        n=1
        if not bom_str:
            pass
        else:
            for bom in bom_str:
                # print(bom,len(bom))
                print(n, bom)

                self.dsmbom(date,bom[0])
                n += 1
    def gui(self):
        self.master=Tk()
        self.master.title("BOM查询")
        Label(text="父零件")

if __name__ == '__main__':
    b=Bom_dsm()
    b.dsmbom('2017-08-30','12004626')

