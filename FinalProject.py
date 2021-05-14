import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os


folderExists = os.path.exists("Deliverables")
if folderExists == False:
    os.makedirs("Deliverables")
elif folderExists == True:
    pass
    
    
class PGJanuaryFebuary19:
    def __init__(self):
        self.jan = pd.read_csv("2019NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("2019NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary19")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        alljanfeb=self.janfeb.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        alljanfeb=alljanfeb.iloc[[4,5,6,7,0,8,1,9,10,11,2,12,13,14,15,16,17,18,19,20,21,22,23,3,24,25,26,27]]
        alljanfeb.sort_values(by='late %')
        x=range(0, len(alljanfeb))
        routelist = ["Route11", "Route12", "Route13", "Route14", "Route15X", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route21X", "Route22",
             "Route23", "Route24", "Route25", "Route26", "Route27", "Route28",
             "Route30", "Route32", "Route33", "Route34", "Route35", "Route35s",
             "Route36", "Route37", "Route51", "Route53"]
        numlist = ["11", "12", "13", "14", " 15 Express", "16", " 17 (Route 1 Ride)", "18",
                   "20", "21", " 21 Express", "22", "23", "24", "25", "26", "27", "28",
                   "30", "32", "33", "34", "35", " 35s", "36", "37", "51", "53"]
        
        segments=self.janfeb.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary19", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGJanuaryFebuary19/Route"+num+".csv", index=False, encoding='utf-8')
              
class PGMarchMay19:
    def __init__(self):
        self.mar=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("2019NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay19")
        elif folderExists == True:
            pass
        
    
    def route_analysis(self):
        allmarmay=self.marmay.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        allmarmay=allmarmay.iloc[[4,5,6,7,0,8,1,9,10,11,2,12,13,14,15,16,17,18,19,20,21,22,23,3,24,25,26,27]]
        allmarmay.sort_values(by='late %')
        
        x=range(0, len(allmarmay))
        routelist = ["Route11", "Route12", "Route13", "Route14", "Route15X", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route21X", "Route22",
             "Route23", "Route24", "Route25", "Route26", "Route27", "Route28",
             "Route30", "Route32", "Route33", "Route34", "Route35", "Route35s",
             "Route36", "Route37", "Route51", "Route53"]
        numlist = ["11", "12", "13", "14", " 15 Express", "16", " 17 (Route 1 Ride)", "18",
                   "20", "21", " 21 Express", "22", "23", "24", "25", "26", "27", "28",
                   "30", "32", "33", "34", "35", " 35s", "36", "37", "51", "53"]
        segments=self.marmay.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay19", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGMarchMay19/Route"+num+".csv", index=False, encoding='utf-8')
    
class PGAugustJanuary19:
    def __init__(self):
        self.aug=pd.read_csv("2019NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("2019NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("2019NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2020NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary19")
        elif folderExists == True:
            pass

    
    def route_analysis(self):
        allaugjan=self.augjan.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allaugjan['total']=allaugjan['early']+allaugjan['on_time']+allaugjan['late']
        allaugjan['early %']=round(allaugjan['early']/allaugjan['total'],2)
        allaugjan['on_time %']=round(allaugjan['on_time']/allaugjan['total'],2)
        allaugjan['late %']=round(allaugjan['late']/allaugjan['total'],2)
        allaugjan=allaugjan.iloc[4:]
        allaugjan.sort_values(by='late %')
        x=range(0, len(allaugjan))
        routelist = ["Route11", "Route12", "Route13", "Route14", "Route15X", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route21X", "Route22",
             "Route23", "Route24", "Route25", "Route26", "Route27", "Route28",
             "Route30", "Route32", "Route33", "Route34", "Route35", "Route35s",
             "Route36", "Route37", "Route51", "Route53"]
        numlist = ["11", "12", "13", "14", " 15 Express", "16", " 17 (Route 1 Ride)", "18",
                   "20", "21", " 21 Express", "22", "23", "24", "25", "26", "27", "28",
                   "30", "32", "33", "34", "35", " 35s", "36", "37", "51", "53"]
        
        segments=self.augjan.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary19", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGAugustJanuary19/Route"+num+".csv", index=False, encoding='utf-8')
    
   
class PGJanuaryFebuary20:
    def __init__(self):
        self.jan = pd.read_csv("2020NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("2020NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        self.janfeb3 = pd.read_csv("2020janfeb3.csv")
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary20")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        alljanfeb=self.janfeb.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        alljanfeb=alljanfeb.iloc[[4,5,6,7,0,8,1,9,10,11,2,12,13,14,15,16,17,18,19,20,21,22,23,3,24,25,26,27]]
        alljanfeb.sort_values(by='late %')
        x=range(0, len(alljanfeb))
        routelist = ["Route11", "Route12", "Route13", "Route14", "Route15X", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route21X", "Route22",
             "Route23", "Route24", "Route25", "Route26", "Route27", "Route28",
             "Route30", "Route32", "Route33", "Route34", "Route35", "Route35s",
             "Route36", "Route37", "Route51", "Route53"]
        numlist = ["11", "12", "13", "14", " 15 Express", "16", " 17 (Route 1 Ride)", "18",
                   "20", "21", " 21 Express", "22", "23", "24", "25", "26", "27", "28",
                   "30", "32", "33", "34", "35", " 35s", "36", "37", "51", "53"]
        
        segments=self.janfeb.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary20", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGJanuaryFebuary20/Route"+num+".csv", index=False, encoding='utf-8')

    def third_del(self):
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.janfeb3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGJanuaryFebuary20/2020janfeb_bestroutes.csv",encoding="utf-8")
        bymonth=round(self.janfeb3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[0]
        bymonth.loc[1,'month']=monthlist[1]
        bymonth.to_csv("Deliverables/PG/PGJanuaryFebuary20/2020janfeb_boardings.csv",encoding="utf-8")
        
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary20/2020janfeb_bestroutes.png")   
    
class PGMarchMay20:
    def __init__(self):
        self.mar=pd.read_csv("2020NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("2020NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("2020NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        self.marmay3=pd.read_csv("2020marmay3.csv")
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay20")
        elif folderExists == True:
            pass
        
        
    def route_analysis(self):
        allmarmay=self.marmay.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        allmarmay=allmarmay.iloc[[4,5,6,7,0,8,1,9,10,11,2,12,13,14,15]]
        allmarmay.sort_values(by='late %')
        
        x=range(0, len(allmarmay))
        routelist = ["Route13", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route24", "Route26", "Route28",
             "Route30", "Route32", "Route33", "Route35", "Route35s",
             "Route36", "Route37"]
        numlist = ["13", "16", "17 (Route 1 Ride)", "18",
                   "20", "21", "24", "26", "28",
                   "30", "32", "33", "35", "35s", "36", "37"]
        segments=self.marmay.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay20", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGMarchMay20/Route"+num+".csv", index=False, encoding='utf-8')
            
    def third_del(self):
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.marmay3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGMarchMay20/2020marmay_bestroutes.csv",encoding="utf-8")

        bymonth=round(self.marmay3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[2]
        bymonth.loc[1,'month']=monthlist[3]
        bymonth.loc[2,'month']=monthlist[4]
        bymonth.to_csv("Deliverables/PG/PGMarchMay20/2020marmay_boardings.csv",encoding="utf-8")

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[2:5]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGMarchMay20/2020marmay_bestroutes.png")
         
class PGAugustJanuary20:
    def __init__(self):
        self.aug=pd.read_csv("2020NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("2020NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("2020NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2021NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        self.augjan3=pd.read_csv("2020augjan3.csv")
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary20")
        elif folderExists == True:
            pass
        
        
    def route_analysis(self):
        allaugjan=self.augjan.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allaugjan['total']=allaugjan['early']+allaugjan['on_time']+allaugjan['late']
        allaugjan['early %']=round(allaugjan['early']/allaugjan['total'],2)
        allaugjan['on_time %']=round(allaugjan['on_time']/allaugjan['total'],2)
        allaugjan['late %']=round(allaugjan['late']/allaugjan['total'],2)
        allaugjan=allaugjan.iloc[4:]
        allaugjan.sort_values(by='late %')
        x=range(0, len(allaugjan))
        routelist = ["Route13", "Route16",
             "Route17", "Route18", "Route20", "Route21", "Route24", "Route26", "Route28",
             "Route30", "Route32", "Route33", "Route34", "Route35",
             "Route36", "Route37", "Route51", " Route51A", " Route51B", "Route51X"]
        numlist = ["13", "16", "17 (Route 1 Ride)", "18",
                   "20", "21", "24", "26", "28",
                   "30", "32", "33", "34", "35", "36", "37", "51", "51 Loop A", "51 Loop B", "51 Loop X"]
        
        segments=self.augjan.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary20", "PG")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGAugustJanuary20/Route"+num+".csv", index=False, encoding='utf-8')

    def third_del(self):
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.augjan3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGAugustJanuary20/2020augjan_bestroutes.csv",encoding="utf-8")

        bymonth=round(self.augjan3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[5]
        bymonth.loc[1,'month']=monthlist[6]
        bymonth.loc[2,'month']=monthlist[7]
        bymonth.loc[3,'month']=monthlist[8]
        bymonth.loc[4,'month']=monthlist[9]
        bymonth.loc[5,'month']=monthlist[10]
        bymonth.to_csv("Deliverables/PG/PGAugustJanuary20/2020augjan_boardings.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[5:]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGAugustJanuary20/2020augjan_bestroutes.png")



class MOCOJanuaryFebuary19:
    def __init__(self):
        self.janfeb = pd.read_csv("2019JANFEBSEG.csv")
        for title in [self.janfeb]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary19")
        elif folderExists == True:
            pass
        
    
    def route_analysis(self):
        alljanfeb=self.janfeb.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        
        alljanfeb=alljanfeb.iloc[0:]
        
        alljanfeb.sort_values(by='late %')
       
        x=range(0, len(alljanfeb))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.janfeb.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "MOCOJanuaryFebuary19", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOMarchMay19:
    def __init__(self):
        self.marmay = pd.read_csv("2019MARMAYSEG.csv")
        for title in [self.marmay]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay19")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        allmarmay=self.marmay.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        
        allmarmay=allmarmay.iloc[0:]
        
        allmarmay.sort_values(by='late %')
       
        x=range(0, len(allmarmay))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.marmay.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "MOCOMarchMay19", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOMarchMay19/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOSeptemberJanuary19:
    def __init__(self):
        self.sepjan = pd.read_csv("2019SEPJANSEG.csv")
        for title in [self.sepjan]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOSeptJanuary19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOSeptJanuary19")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        allsepjan=self.sepjan.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allsepjan['total']=allsepjan['early']+allsepjan['on_time']+allsepjan['late']
        allsepjan['early %']=round(allsepjan['early']/allsepjan['total'],2)
        allsepjan['on_time %']=round(allsepjan['on_time']/allsepjan['total'],2)
        allsepjan['late %']=round(allsepjan['late']/allsepjan['total'],2)
        
        allsepjan=allsepjan.iloc[0:]
        
        allsepjan.sort_values(by='late %')
       
        x=range(0, len(allsepjan))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.sepjan.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allsepjan['early %'].iloc[num],allsepjan['on_time %'].iloc[num],allsepjan['late %'].iloc[num]], num, route, "MOCOSeptJanuary19", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOSeptJanuary19/Route"+num+".csv", index=False, encoding='utf-8')


class MOCOJanuaryFebuary20:
    def __init__(self):
        self.janfeb = pd.read_csv("2020JANFEBSEG.csv")
        for title in [self.janfeb]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary20")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        alljanfeb=self.janfeb.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        
        alljanfeb=alljanfeb.iloc[0:]
        
        alljanfeb.sort_values(by='late %')
       
        x=range(0, len(alljanfeb))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.janfeb.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "MOCOJanuaryFebuary20", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOMarchMay20:
    def __init__(self):
        self.marmay = pd.read_csv("2020MARMAYSEG.csv")
        for title in [self.marmay]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay20")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        allmarmay=self.marmay.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        
        allmarmay=allmarmay.iloc[0:]
        
        allmarmay.sort_values(by='late %')
       
        x=range(0, len(allmarmay))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.marmay.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "MOCOMarchMay20", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOMarchMay20/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOSeptemberJanuary20:
    def __init__(self):
        self.sepjan = pd.read_csv("2020OCTJANSEG.csv")
        for title in [self.sepjan]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOOctoberJanuary20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOOctoberJanuary20")
        elif folderExists == True:
            pass
    
    def route_analysis(self):
        allsepjan=self.sepjan.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allsepjan['total']=allsepjan['early']+allsepjan['on_time']+allsepjan['late']
        allsepjan['early %']=round(allsepjan['early']/allsepjan['total'],2)
        allsepjan['on_time %']=round(allsepjan['on_time']/allsepjan['total'],2)
        allsepjan['late %']=round(allsepjan['late']/allsepjan['total'],2)
        
        allsepjan=allsepjan.iloc[0:]
        
        allsepjan.sort_values(by='late %')
       
        x=range(0, len(allsepjan))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.sepjan.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allsepjan['early %'].iloc[num],allsepjan['on_time %'].iloc[num],allsepjan['late %'].iloc[num]], num, route, "MOCOOctoberJanuary20", "MOCO")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOOctoberJanuary20/Route"+num+".csv", index=False, encoding='utf-8')
    
    
    
    
def makepies(number,filling, count, name, folder, county):
        labels = number
        sizes = filling
        explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(name)
        
        x = plt.savefig("Deliverables/"+county+"/"+folder+"/"+name+".png")
        return x 

def main():
    county = int(input("Welcome, please choose a county: \n"
                   "(1)Prince George's County \n"
                   "(2)Montgomery County\n"))
    if county == 1:
        folderExists = os.path.exists("Deliverables/PG")
        if folderExists == False:
            os.makedirs("Deliverables/PG")
        elif folderExists == True:
            pass
        year = int(input("What year would you like to take a look at? (2019 or 2020)\n"))
        if year == 2019:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                pg = PGJanuaryFebuary19()
                pg.route_analysis()
            elif timeframe==2:
                pg = PGMarchMay19()
                pg.route_analysis()
            elif timeframe==3:
                pg = PGAugustJanuary19()
                pg.route_analysis()
        elif year == 2020:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                pg = PGJanuaryFebuary20()
                pg.route_analysis()
                pg.third_del()
            elif timeframe==2:
                pg = PGMarchMay20()
                pg.route_analysis()
                pg.third_del()
            elif timeframe==3:
                pg = PGAugustJanuary20()
                pg.route_analysis()
                pg.third_del()
    
    elif county == 2:
        folderExists = os.path.exists("Deliverables/MOCO")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO")
        elif folderExists == True:
            pass
        year = int(input("What year would you like to take a look at? (2019 or 2020)\n"))
        if year == 2019:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)September to January\n"))
            if timeframe == 1:
                moco = MOCOJanuaryFebuary19()
                moco.route_analysis()
            elif timeframe==2:
                moco = MOCOMarchMay19()
                moco.route_analysis()
            elif timeframe==3:
                moco = MOCOSeptemberJanuary19()
                moco.route_analysis()
        elif year == 2020:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                pg = MOCOJanuaryFebuary20()
                pg.route_analysis()
            elif timeframe==2:
                pg = MOCOMarchMay20()
                pg.route_analysis()
            elif timeframe==3:
                pg = MOCOSeptemberJanuary20()
                pg.route_analysis()
        
    


main()