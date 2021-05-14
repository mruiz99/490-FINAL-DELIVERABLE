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
    
    
#SECOND DELIVERABLE
class PGJanuaryFebuary19:
    def __init__(self):
        self.jan = pd.read_csv("2019NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("2019NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        os.mkdir("Deliverables/PGJanuaryFebuary19")
    
    def second_deliv(self):
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
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary19")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGJanuaryFebuary19/Route"+num+".csv", index=False, encoding='utf-8')

class PGJanuaryFebuary20:
    def __init__(self):
        self.jan = pd.read_csv("2020NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("2020NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        os.mkdir("Deliverables/PGJanuaryFebuary20")
    
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
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary20")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGJanuaryFebuary20/Route"+num+".csv", index=False, encoding='utf-8')
    
          
class PGMarchMay19:
    def __init__(self):
        self.mar=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("2019NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("2019NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        os.mkdir("Deliverables/PGMarchMay19")
    
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
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay19")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGMarchMay19/Route"+num+".csv", index=False, encoding='utf-8')
    
class PGMarchMay20:
    def __init__(self):
        self.mar=pd.read_csv("2020NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("2020NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("2020NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        os.mkdir("Deliverables/PGMarchMay20")
        
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
        numlist = ["13", "16", " 17 (Route 1 Ride)", "18",
                   "20", "21", "24", "26", "28",
                   "30", "32", "33", "35", " 35s", "36", "37"]
        segments=self.marmay.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay20")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGMarchMay20/Route"+num+".csv", index=False, encoding='utf-8')


class PGAugustJanuary19:
    def __init__(self):
        self.aug=pd.read_csv("2019NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("2019NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("2019NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2020NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        os.mkdir("Deliverables/PGAugustJanuary19")

    
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
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary19")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGAugustJanuary19/Route"+num+".csv", index=False, encoding='utf-8')

class PGAugustJanuary20:
    def __init__(self):
        self.aug=pd.read_csv("2020NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("2020NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("2020NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2021NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        os.mkdir("Deliverables/PGAugustJanuary20")
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
             "Route36", "Route37", "Route51", "Route51A", "Route51B", "Route51X"]
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
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary20")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PGAugustJanuary20/Route"+num+".csv", index=False, encoding='utf-8')


class MOCOJanuaryFebuary19:
    def __init__(self):
        self.janfeb = pd.read_csv("2019JANFEBSEG.csv")
        for title in [self.janfeb]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        os.mkdir("Deliverables/MOCOJanuaryFebuary19")
    
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
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "MOCOJanuaryFebuary19")
            a = (segments[segments["route"]=="46", segments["route"]=="55", segments["route"]=="100"])
            (a).to_csv("Deliverables/MOCOJanuaryFebuary19/Route"+num+".csv", index=False, encoding='utf-8')
                
def makepies(number,filling, count, name, folder):
        labels = number
        sizes = filling
        explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(name)
        
        x = plt.savefig("Deliverables/"+folder+"/"+name+".png")
        return x 

    
def main():
    county = input("Welcome, please choose a county (Moco or PG):  ")
    if county.upper() == "MOCO":
        year = int(input("What year would you like to take a look at? (2019 or 2020)\n"))
        if year == 2019:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                moco = MOCOJanuaryFebuary19()
                moco.route_analysis()
            elif timeframe==2:
                moco = MOCOMarchMay19()
                moco.route_analysis()
            elif timeframe==3:
                moco = MOCOAugustJanuary19()
                moco.route_analysis()
        elif year == 2020:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                pg = PGJanuaryFebuary20()
                pg.route_analysis()
            elif timeframe==2:
                pg = PGMarchMay20()
                pg.route_analysis()
            elif timeframe==3:
                pg = PGAugustJanuary20()
                pg.route_analysis()
        
    elif county.upper() == "PG":
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
            elif timeframe==2:
                pg = PGMarchMay20()
                pg.route_analysis()
            elif timeframe==3:
                pg = PGAugustJanuary20()
                pg.route_analysis()
        


main()