import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

    
class PGJanuaryFebuary19:
    def __init__(self):
        self.jan = pd.read_csv("2019NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("2019NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        os.mkdir("Deliverables")
              
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
            #print("ROUTE",alljanfeb['route'].iloc[num])
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route)
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/Route"+num+".csv", index=False, encoding='utf-8')
            
            
class PGMarchMay19:
    def __init__(self):
        self.mar=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("2019NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
    
    def route_analysis(self):
        allmarmay=self.marmay.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        allmarmay=allmarmay.iloc[[4,5,6,7,0,8,1,9,10,11,2,12,13,14,15,16,17,18,19,20,21,22,23,3,24,25,26,27]]
        allmarmay.sort_values(by='late %')
        x=range(0, len(allmarmay))
        for num in x:
            print("ROUTE",allmarmay['route'].iloc[num])
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]])
                    
class PGAugustJanuary19:
    def __init__(self):
        self.aug=pd.read_csv("2019NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("2019NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("2019NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2020NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
    
    def route_analysis(self):
        allaugjan=self.augjan.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allaugjan['total']=allaugjan['early']+allaugjan['on_time']+allaugjan['late']
        allaugjan['early %']=round(allaugjan['early']/allaugjan['total'],2)
        allaugjan['on_time %']=round(allaugjan['on_time']/allaugjan['total'],2)
        allaugjan['late %']=round(allaugjan['late']/allaugjan['total'],2)
        allaugjan=allaugjan.iloc[4:]
        allaugjan.sort_values(by='late %')
        x=range(0, len(allaugjan))
        for num in x:
            print("ROUTE",allaugjan['route'].iloc[num])
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]])
                
        
def makepies(number,filling, count, name):
        labels = number
        sizes = filling
        explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(name)
        
        x = plt.savefig("Deliverables/"+name+".png")
        return x 

    
def main():
    county = input("Welcome, please choose a county (Moco or PG):  ")
    if county.upper() == "MOCO":
        pass
    elif county.upper() == "PG":
        timeframe = int(input("Great. What timeframe are you interested in? \n"
                          "(1)January to Febuary \n"
                          "(2)March to May \n"
                          "(3)August to January\n"))
        if timeframe == 1:
            pg = PGJanuaryFebuary19()
            pg.route_analysis()
            
            #moco = MOCOJanuaryFebuary19()
            #moco.route_analysis()
        

    
main()