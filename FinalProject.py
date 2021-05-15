import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os


folderExists = os.path.exists("Deliverables")
if folderExists == False:
    os.makedirs("Deliverables")
elif folderExists == True:
    pass
    
#PG COUNTY 2019
class PGJanuaryFebuary19:
    def __init__(self):
        self.jan = pd.read_csv("Data/2019NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("Data/2019NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        self.janfeb1=pd.read_csv("Data/2019PGJANFEB.csv")
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary19")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/")
        elif folderExists == True:
            pass
        # POPULAR ROUTES
        
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'20"]
        routes=self.janfeb1.groupby('route')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janbest_bestroutes.csv",encoding="utf-8")

        bymonth=self.janfeb1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.loc[0,'month']=monthlist[0]
        bymonth.loc[1,'month']=monthlist[1]
        bymonth.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered[0:5], x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Most Popular Routes Jan-Feb 2019")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Jan-Feb 2019")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=self.janfeb1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index()
        stops=stops.nlargest(len(stops),'boardings')

        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_popularstops.png")
        boardingsStops=stops.nlargest(len(stops),'boardings')
        alightingsStops=stops.nlargest(len(stops),'alightings')
        boardingsStops.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardingsstops.csv",encoding="utf-8")
        alightingsStops.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightingsstops.csv",encoding="utf-8")
        
        # TIME OF DAY

        todroutes=self.janfeb1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Jan-Feb 2019")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes.iloc[0:20], x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topstops_byhour.png")

        boardingHours=todroutes.nlargest(len(todroutes),'boardings')
        alightingHours=todroutes.nlargest(len(todroutes),'alightings')
        boardingHours.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardingshours.csv",encoding="utf-8")
        alightingHours.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightingshours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings=self.janfeb1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings=self.janfeb1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightinglocations.csv",encoding="utf-8")

    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary19", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGJanuaryFebuary19/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')
              
class PGMarchMay19:
    def __init__(self):
        self.mar=pd.read_csv("Data/2019NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("Data/2019NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("Data/2019NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        self.marmay1=pd.read_csv("Data/2019PGMARMAY.csv")
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay19")
        elif folderExists == True:
            pass
        
    def first_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/")
        elif folderExists == True:
            pass
        # POPULAR ROUTES
        
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'20"]
        routes=self.marmay1.groupby('route')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_bestroutes.csv",encoding="utf-8")

        bymonth=self.marmay1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.loc[0,'month']=monthlist[2]
        bymonth.loc[1,'month']=monthlist[3]
        bymonth.loc[2,'month']=monthlist[4]
        bymonth.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[2:5]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered[0:5], x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Most Popular Routes Mar-May 2019")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Mar-May 2019")
        plt.savefig("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=self.marmay1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index()
        stops=stops.nlargest(len(stops),'boardings')

        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_popularstops.png")
        boardingsStops=stops.nlargest(len(stops),'boardings')
        alightingsStops=stops.nlargest(len(stops),'alightings')
        boardingsStops.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topboardingstops.csv",encoding="utf-8")
        alightingsStops.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topalightingstops.csv",encoding="utf-8")
        
        # TIME OF DAY

        todroutes=self.marmay1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Mar-May 2019")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes.iloc[0:20], x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topstops_byhour.png")
        boardingHours=todroutes.nlargest(len(todroutes),'boardings')
        alightingHours=todroutes.nlargest(len(todroutes),'alightings')
        boardingHours.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topboardingshours.csv",encoding="utf-8")
        alightingHours.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topalightingshours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings=self.marmay1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings=self.marmay1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGMarchMay19/BoardingAlightingTrends/2019marmay_topalightinglocations.csv",encoding="utf-8")    
    
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay19", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGMarchMay19/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')
    
class PGAugustJanuary19:
    def __init__(self):
        self.aug=pd.read_csv("Data/2019NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("Data/2019NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("Data/2019NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("Data/2020NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        self.augjan1=pd.read_csv("Data/2019PGAUGJAN.csv")
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary19")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary19")
        elif folderExists == True:
            pass
        
    def first_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/")
        elif folderExists == True:
            pass
        # POPULAR ROUTES
        
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","DEC","JAN'21"]
        routes=self.augjan1.groupby('route')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_bestroutes.csv",encoding="utf-8")

        bymonth=self.augjan1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.loc[1,'month']=monthlist[5]
        bymonth.loc[2,'month']=monthlist[6]
        bymonth.loc[3,'month']=monthlist[7]
        bymonth.loc[0,'month']=monthlist[8]
        bymonth.iloc[[1,2,3,0]]
        bymonth.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[5:]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered[0:5], x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Most Popular Routes Aug'19-Jan'20")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Aug'19-Jan'20")
        plt.savefig("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=self.augjan1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index()
        stops=stops.nlargest(len(stops),'boardings')

        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_best_stops.png")
        boardingsStops=stops.nlargest(len(stops),'boardings')
        alightingsStops=stops.nlargest(len(stops),'alightings')
        boardingsStops.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topboardingstops.csv",encoding="utf-8")
        alightingsStops.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topalightingstops.csv",encoding="utf-8")
        
        # TIME OF DAY

        todroutes=self.augjan1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Jan-Feb 2019")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes.iloc[0:20], x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_toproutes_byhours.png")

        boardingHours=todroutes.nlargest(len(todroutes),'boardings')
        alightingHours=todroutes.nlargest(len(todroutes),'alightings')
        boardingHours.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topboardinghours.csv",encoding="utf-8")
        alightingHours.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topalightinghours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings=self.augjan1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings=self.augjan1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGAugustJanuary19/BoardingAlightingTrends/2019augjan_topalightinglocations.csv",encoding="utf-8")

    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary19", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGAugustJanuary19/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')
    
#PG COUNTY 2020   
class PGJanuaryFebuary20:
    def __init__(self):
        self.jan = pd.read_csv("Data/2020NEWJAN_scheduled-ad.csv")
        self.feb=pd.read_csv("Data/2020NEWFEB_scheduled-ad.csv")
        for title in [self.jan, self.feb]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.janfeb=pd.concat([self.jan,self.feb])
        self.janfeb3 = pd.read_csv("Data/2020janfeb3.csv")
        self.janfeb1=pd.read_csv("Data/2020PGJANFEB.csv")
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary20")
        elif folderExists == True:
            pass
    
    def first_del(self):
        # POPULAR ROUTES
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/")
        elif folderExists == True:
            pass
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.janfeb1.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janbest_bestroutes.csv",encoding="utf-8")

        bymonth=round(self.janfeb1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[0]
        bymonth.loc[1,'month']=monthlist[1]
        bymonth.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered[0:5], x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Most Popular Routes Jan-Feb 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Jan-Feb 2020")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=round(self.janfeb1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index(),2)
        stops=stops.nlargest(len(stops),'boardings')
        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_popularstops.png")
        boardings=stops.nlargest(len(stops),'boardings')
        alightings=stops.nlargest(len(stops),'alightings')
        boardings.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topboardings.csv",encoding="utf-8")
        alightings.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topalightings.csv",encoding="utf8")
        
        # TIME OF DAY
        
        todroutes=round(self.janfeb1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_tophours.csv",encoding="utf-8")

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Jan-Feb 2020")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes[0:10], x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topstops_byhour.png")
        boardings2=todroutes.nlargest(len(todroutes),'boardings')
        alightings2=todroutes.nlargest(len(todroutes),'alightings')
        boardings2.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topboardinghours.csv",encoding="utf-8")
        alightings2.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topalightinghours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings3=self.janfeb1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings3.nlargest(len(boardings3),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings=self.janfeb1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGJanuaryFebuary20/BoardingAlightingTrends/2020janfeb_topalightinglocations.csv",encoding="utf-8")

    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "PGJanuaryFebuary20", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGJanuaryFebuary20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

    def third_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGJanuaryFebuary20/ServiceEnhancments")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGJanuaryFebuary20/ServiceEnhancments/")
        elif folderExists == True:
            pass
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.janfeb3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGJanuaryFebuary20/ServiceEnhancments/2020janfeb_bestroutes.csv",encoding="utf-8")
        bymonth=round(self.janfeb3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[0]
        bymonth.loc[1,'month']=monthlist[1]
        bymonth.to_csv("Deliverables/PG/PGJanuaryFebuary20/ServiceEnhancments/2020janfeb_boardings.csv",encoding="utf-8")
        
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGJanuaryFebuary20/ServiceEnhancments/2020janfeb_bestroutes.png")   
    
class PGMarchMay20:
    def __init__(self):
        self.mar=pd.read_csv("Data/2020NEWMAY_scheduled-ad.csv")
        self.apr=pd.read_csv("Data/2020NEWAPR_scheduled-ad.csv")
        self.may=pd.read_csv("Data/2020NEWMAY_scheduled-ad.csv")
        for title in [self.mar, self.apr, self.may]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        self.marmay=pd.concat([self.mar,self.apr,self.may])
        self.marmay3=pd.read_csv("Data/2020marmay3.csv")
        self.marmay1=pd.read_csv("Data/2020PGMARMAY.csv")
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay20")
        elif folderExists == True:
            pass
        
    def first_del(self):
        # POPULAR ROUTES MAR-MAY
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/")
        elif folderExists == True:
            pass

        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=self.marmay1.groupby('route')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_bestroutes.csv",encoding="utf-8")

        bymonth=self.marmay1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.loc[0,'month']=monthlist[2]
        bymonth.loc[1,'month']=monthlist[3]
        bymonth.loc[2,'month']=monthlist[4]
        bymonth.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[2:5]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered[0:5], x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Most Popular Routes Mar-May 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Mar-May 2020")
        plt.savefig("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=self.marmay1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index()
        stops=stops.nlargest(len(stops),'boardings')
        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_popularstops.png")
        boardings=stops.nlargest(len(stops),'boardings')
        alightings=stops.nlargest(len(stops),'alightings')
        boardings.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topboardingstops.csv",encoding="utf-8")
        alightings.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topalightingstops.csv",encoding="utf-8")
        
        #TOD

        todroutes=self.marmay1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_tophours.csv",encoding="utf-8")

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Jan-Feb 2020")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes[0:10], x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topstops_byhour.png")

        boardingHours=todroutes.nlargest(len(todroutes),'boardings')
        alightingHours=todroutes.nlargest(len(todroutes),'alightings')
        boardingHours.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topboardinghours.csv",encoding="utf-8")
        alightingHours.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topalightinghours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings2=self.marmay1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings2.nlargest(len(boardings2),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings2=self.marmay1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings2.nlargest(len(alightings2),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGMarchMay20/BoardingAlightingTrends/2020marmay_topalightinglocations.csv",encoding="utf-8")

    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "PGMarchMay20", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGMarchMay20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')
            
    def third_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGMarchMay20/ServiceEnhancments")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGMarchMay20/ServiceEnhancments")
        elif folderExists == True:
            pass
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.marmay3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGMarchMay20/ServiceEnhancments/2020marmay_bestroutes.csv",encoding="utf-8")

        bymonth=round(self.marmay3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[2]
        bymonth.loc[1,'month']=monthlist[3]
        bymonth.loc[2,'month']=monthlist[4]
        bymonth.to_csv("Deliverables/PG/PGMarchMay20/ServiceEnhancments/2020marmay_boardings.csv",encoding="utf-8")

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[2:5]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGMarchMay20/ServiceEnhancments/2020marmay_bestroutes.png")
         
class PGAugustJanuary20:
    def __init__(self):
        self.aug=pd.read_csv("Data/2020NEWAUG_scheduled-ad.csv")
        self.sep=pd.read_csv("Data/2020NEWSEP_scheduled-ad.csv")
        self.dec=pd.read_csv("Data/2020NEWDEC_scheduled-ad.csv")
        self.jan20=pd.read_csv("2021NEWJAN_scheduled-ad.csv")
        for title in [self.aug, self.sep, self.dec, self.jan20]:
            title.columns=["route","stops","direction","early","on_time","late"]
        self.augjan=pd.concat([self.aug,self.sep,self.dec,self.jan20])
        self.augjan3=pd.read_csv("Data/2020augjan3.csv")
        self.augjan1=pd.read_csv("Data/2020PGAUGJAN.csv")
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary20")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary20")
        elif folderExists == True:
            pass

    def first_del(self):
        # POPULAR ROUTES MAR-MAY
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=self.augjan1.groupby('route')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_bestroutes.csv",encoding="utf-8")

        bymonth=self.augjan1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.loc[0,'month']=monthlist[5]
        bymonth.loc[1,'month']=monthlist[6]
        bymonth.loc[2,'month']=monthlist[7]
        bymonth.loc[3,'month']=monthlist[8]
        bymonth.loc[4,'month']=monthlist[9]
        bymonth.loc[5,'month']=monthlist[10]
        bymonth.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_popular_routes.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[5:]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Aug'20-Jan'21")
        plt.savefig("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_bestroutes.png")
        
        # POPULAR STOPS
        
        stops=self.augjan1.groupby('stop')[['boardings','alightings']].agg('sum').reset_index()
        stops=stops.nlargest(len(stops),'boardings')
        sns.barplot(data=stops[0:10],x="boardings",y="stop")
        plt.savefig("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_popularstops.png")
        boardings=stops.nlargest(len(stops),'boardings')
        alightings=stops.nlargest(len(stops),'alightings')
        boardings.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topboardingstops.csv",encoding="utf-8")
        alightings.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topalightingstops.csv",encoding="utf-8")
        
        #TOD

        todroutes=self.augjan1.groupby(['hour','route'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_tophours.csv",encoding="utf-8")

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        axes[0]=sns.barplot(ax=axes[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes[0].set_title("Boarding by the Hour Jan-Feb 2020")
        axes[1]=sns.barplot(ax=axes[1],data=todroutes, x='route',y='boardings',ci=None)
        plt.savefig("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topstops_byhour.png")
        boardingHours=todroutes.nlargest(len(todroutes),'boardings')
        alightingHours=todroutes.nlargest(len(todroutes),'alightings')
        boardingHours.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topboardinghours.csv",encoding="utf-8")
        alightingHours.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topalightinghours.csv",encoding="utf-8")
        
        # BOARDING LOCATIONS

        boardings2=self.augjan1.groupby('stop')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings2.nlargest(len(boardings2),'boardings')
        boardingsordered.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topboardinglocations.csv",encoding="utf-8")
        
        # ALIGHTING LOCATIONS

        alightings2=self.augjan1.groupby('stop')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings2.nlargest(len(alightings2),'alightings')
        alightingsordered.to_csv("Deliverables/PG/PGAugustJanuary20/BoardingAlightingTrends/2020augjan_topalightinglocations.csv",encoding="utf-8")

    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
                   "30", "32", "33", "34", "35", "36", "37", "51", "51A", "51B", "51X"]
        
        segments=self.augjan.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allaugjan['early %'].iloc[num],allaugjan['on_time %'].iloc[num],allaugjan['late %'].iloc[num]], num, route, "PGAugustJanuary20", "PG", "RoutePerfAnalysis")
        for num in numlist:
            x = segments[segments["route"]==num]
            x.to_csv("Deliverables/PG/PGAugustJanuary20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

    def third_del(self):
        folderExists = os.path.exists("Deliverables/PG/PGAugustJanuary20/ServiceEnhancments")
        if folderExists == False:
            os.makedirs("Deliverables/PG/PGAugustJanuary20/ServiceEnhancments")
        elif folderExists == True:
            pass
        monthlist=["JAN","FEB","MAR","APR","MAY","AUG","SEP","OCT","NOV","DEC","JAN'21"]
        routes=round(self.augjan3.groupby('route')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/PG/PGAugustJanuary20/ServiceEnhancments/2020augjan_bestroutes.csv",encoding="utf-8")

        bymonth=round(self.augjan3.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.loc[0,'month']=monthlist[5]
        bymonth.loc[1,'month']=monthlist[6]
        bymonth.loc[2,'month']=monthlist[7]
        bymonth.loc[3,'month']=monthlist[8]
        bymonth.loc[4,'month']=monthlist[9]
        bymonth.loc[5,'month']=monthlist[10]
        bymonth.to_csv("Deliverables/PG/PGAugustJanuary20/ServiceEnhancments/2020augjan_boardings.csv",encoding="utf-8")
            
        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[5:]})

        fig, axes = plt.subplots(2, figsize=(20,15))
        plt.subplots_adjust(hspace = 0.5)
        sns.barplot(ax=axes[0],data=routesordered, x='route',y="boardings")
        axes[0].set_ylim(0,routesordered['boardings'].max()+(routesordered['boardings'].max()*0.35))
        axes[0].set_title("Best Performing Enhanced Routes 2020")
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        axes[1].set_title("Total Boardings for Enhanced Routes 2020")
        plt.savefig("Deliverables/PG/PGAugustJanuary20/ServiceEnhancments/2020augjan_bestroutes.png")


#MOCO COUNTY 2019
class MOCOJanuaryFebuary19:
    def __init__(self):
        self.janfeb1=pd.read_csv("Data/2019MOCOJANFEB.csv")
        self.janfeb2 = pd.read_csv("Data/2019JANFEBSEG.csv")
        for title in [self.janfeb2]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary19")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES
        
        monthlist = ["JANUARY", "FEBRUARY"]
        routes=self.janfeb1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index()
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_popular_routes.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=self.janfeb1.groupby('month')[['boardings','alightings']].agg('sum').reset_index()
        bymonth.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_best_routes.csv")

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_best_routes.png")
        
        # TOP STOPS
        stops=self.janfeb1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index()
        stops = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=stops[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_best_stops.png")
        a=stops.nlargest(len(stops),'boardings')
        b=stops.nlargest(len(stops),'alightings')
        a.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardingstops.csv")
        b.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightingstops.csv")
        
        #TOD
        todroutes=self.janfeb1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index()
        todroutes=todroutes.nlargest(len(todroutes),'boardings')

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings')
        d=todroutes.nlargest(len(todroutes),'alightings')
        c.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardingshours.csv")
        d.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightinghours.csv")
        
        # BOARDING LOCATIONS
        boardings=self.janfeb1.groupby('stops')['boardings'].agg('sum').reset_index()
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topboardingslocations.csv")
        
        # ALIGHTING LOCATIONS
        alightings=self.janfeb1.groupby('stops')['alightings'].agg('sum').reset_index()
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/BoardingAlightingTrends/2019janfeb_topalightinglocations.csv")
        
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
        alljanfeb=self.janfeb2.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        
        alljanfeb=alljanfeb.iloc[0:]
        
        alljanfeb.sort_values(by='late %')
       
        x=range(0, len(alljanfeb))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.janfeb2.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "MOCOJanuaryFebuary19", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary19/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOMarchMay19:
    def __init__(self):
        self.marmay1 = pd.read_csv("Data/2019MOCOMARMAY.csv")
        self.marmay2 = pd.read_csv("Data/2019MARMAYSEG.csv")
        for title in [self.marmay2]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay19")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES/SEGMENTS JAN-FEB
        monthlist = ["MARCH", "APRIL", "MAY"]
        routes=round(self.marmay1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/AllRoutesBoarding.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=round(self.marmay1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/BoardingbyMonth.csv") # to_csv to make record

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:3]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/AllRoutesBoarding.png")
        
        #STATIONS
        stops=round(self.marmay1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index(),2)
        dataa = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=dataa[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/TopStopsBoarding.png")
        a=stops.nlargest(len(stops),'boardings') # to_csv to make record
        b=stops.nlargest(len(stops),'alightings') # to_csv to make record
        a.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/StopsBoarding.csv")
        b.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/StopsAlighting.csv")
        
        #TOD
        todroutes=round(self.marmay1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes # to_csv to make record

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings') # to_csv to make record
        d=todroutes.nlargest(len(todroutes),'alightings') # to_csv to make record
        c.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/TODRoutesBoardings.csv")
        d.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/TODRoutesAlighting.csv")
        
        # BOARDING LOCATIONS
        boardings=round(self.marmay1.groupby('stops')['boardings'].agg('sum').reset_index(),2)
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/BoardingLocations.csv") # to_csv to make record
        
        # ALIGHTING LOCATIONS
        alightings=round(self.marmay1.groupby('stops')['alightings'].agg('sum').reset_index(),2)
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOMarchMay19/BoardingAlightingTrends/AlightingLocations.csv") # to_csv to make record
    
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
        allmarmay=self.marmay2.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        
        allmarmay=allmarmay.iloc[0:]
        
        allmarmay.sort_values(by='late %')
       
        x=range(0, len(allmarmay))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.marmay2.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "MOCOMarchMay19", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOMarchMay19/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOAugustJanuary19:
    def __init__(self):
        self.augjan1 = pd.read_csv("Data/2019MOCOAUGJAN.csv")
        self.sepjan = pd.read_csv("Data/2019SEPJANSEG.csv")
        for title in [self.sepjan]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary19")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary19")
        elif folderExists == True:
            pass
        
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES/SEGMENTS JAN-FEB
        monthlist = ["AUGUST", "SEPTEMBER", "OCTOBER", "NOVERMBER", "DECEMBER", "JANUARY"]
        routes=round(self.augjan1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/AllRoutesBoarding.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=round(self.augjan1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/BoardingbyMonth.csv") # to_csv to make record

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:6]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/AllRoutesBoarding.png")
        
        #STATIONS
        stops=round(self.augjan1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index(),2)
        dataa = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=dataa[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/TopStopsBoarding.png")
        a=stops.nlargest(len(stops),'boardings') # to_csv to make record
        b=stops.nlargest(len(stops),'alightings') # to_csv to make record
        a.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/StopsBoarding.csv")
        b.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/StopsAlighting.csv")
        
        #TOD
        todroutes=round(self.augjan1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes # to_csv to make record

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings') # to_csv to make record
        d=todroutes.nlargest(len(todroutes),'alightings') # to_csv to make record
        c.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/TODRoutesBoardings.csv")
        d.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/TODRoutesAlighting.csv")
        
        # BOARDING LOCATIONS
        boardings=round(self.augjan1.groupby('stops')['boardings'].agg('sum').reset_index(),2)
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/BoardingLocations.csv") # to_csv to make record
        
        # ALIGHTING LOCATIONS
        alightings=round(self.augjan1.groupby('stops')['alightings'].agg('sum').reset_index(),2)
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary19/BoardingAlightingTrends/AlightingLocations.csv") # to_csv to make record
    
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary19/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary19/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[allsepjan['early %'].iloc[num],allsepjan['on_time %'].iloc[num],allsepjan['late %'].iloc[num]], num, route, "MOCOAugustJanuary19", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOAugustJanuary19//RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

#MOCO COUNTY 2020
class MOCOJanuaryFebuary20:
    def __init__(self):
        self.janfeb1 = pd.read_csv("Data/2020MOCOJANFEB.csv")
        self.janfeb2 = pd.read_csv("Data/2020JANFEBSEG.csv")
        for title in [self.janfeb2]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary20")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES/SEGMENTS JAN-FEB
        monthlist = ["JANUARY", "FEBRUARY"]
        routes=round(self.janfeb1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/AllRoutesBoarding.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=round(self.janfeb1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/BoardingbyMonth.csv") # to_csv to make record

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:2]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/AllRoutesBoarding.png")
        
        #STATIONS
        stops=round(self.janfeb1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index(),2)
        dataa = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=dataa[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/TopStopsBoarding.png")
        a=stops.nlargest(len(stops),'boardings') # to_csv to make record
        b=stops.nlargest(len(stops),'alightings') # to_csv to make record
        a.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/StopsBoarding.csv")
        b.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/StopsAlighting.csv")
        
        #TOD
        todroutes=round(self.janfeb1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes # to_csv to make record

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings') # to_csv to make record
        d=todroutes.nlargest(len(todroutes),'alightings') # to_csv to make record
        c.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/TODRoutesBoardings.csv")
        d.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/TODRoutesAlighting.csv")
        
        # BOARDING LOCATIONS
        boardings=round(self.janfeb1.groupby('stops')['boardings'].agg('sum').reset_index(),2)
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/BoardingLocations.csv") # to_csv to make record
        
        # ALIGHTING LOCATIONS
        alightings=round(self.janfeb1.groupby('stops')['alightings'].agg('sum').reset_index(),2)
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/BoardingAlightingTrends/AlightingLocations.csv") # to_csv to make record
    
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOJanuaryFebuary20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOJanuaryFebuary20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
        alljanfeb=self.janfeb2.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        alljanfeb['total']=alljanfeb['early']+alljanfeb['on_time']+alljanfeb['late']
        alljanfeb['early %']=round(alljanfeb['early']/alljanfeb['total'],2)
        alljanfeb['on_time %']=round(alljanfeb['on_time']/alljanfeb['total'],2)
        alljanfeb['late %']=round(alljanfeb['late']/alljanfeb['total'],2)
        
        alljanfeb=alljanfeb.iloc[0:]
        
        alljanfeb.sort_values(by='late %')
       
        x=range(0, len(alljanfeb))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.janfeb2.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[alljanfeb['early %'].iloc[num],alljanfeb['on_time %'].iloc[num],alljanfeb['late %'].iloc[num]], num, route, "MOCOJanuaryFebuary20", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOJanuaryFebuary20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOMarchMay20:
    def __init__(self):
        self.marmay1 = pd.read_csv("Data/2020MOCOMARMAY.csv")
        self.marmay2 = pd.read_csv("Data/2020MARMAYSEG.csv")
        for title in [self.marmay2]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay20")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES/SEGMENTS JAN-FEB
        monthlist = ["MARCH", "APRIL", "MAY"]
        routes=round(self.marmay1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/AllRoutesBoarding.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=round(self.marmay1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/BoardingbyMonth.csv") # to_csv to make record

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:3]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/AllRoutesBoarding.png")
        
        #STATIONS
        stops=round(self.marmay1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index(),2)
        dataa = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=dataa[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/TopStopsBoarding.png")
        a=stops.nlargest(len(stops),'boardings') # to_csv to make record
        b=stops.nlargest(len(stops),'alightings') # to_csv to make record
        a.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/StopsBoarding.csv")
        b.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/StopsAlighting.csv")
        
        #TOD
        todroutes=round(self.marmay1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes # to_csv to make record

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings') # to_csv to make record
        d=todroutes.nlargest(len(todroutes),'alightings') # to_csv to make record
        c.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/TODRoutesBoardings.csv")
        d.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/TODRoutesAlighting.csv")
        
        # BOARDING LOCATIONS
        boardings=round(self.marmay1.groupby('stops')['boardings'].agg('sum').reset_index(),2)
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/BoardingLocations.csv") # to_csv to make record
        
        # ALIGHTING LOCATIONS
        alightings=round(self.marmay1.groupby('stops')['alightings'].agg('sum').reset_index(),2)
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOMarchMay20/BoardingAlightingTrends/AlightingLocations.csv") # to_csv to make record20
        
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOMarchMay20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOMarchMay20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
        allmarmay=self.marmay2.groupby('route')[['early','on_time','late']].agg('sum').reset_index()
        allmarmay['total']=allmarmay['early']+allmarmay['on_time']+allmarmay['late']
        allmarmay['early %']=round(allmarmay['early']/allmarmay['total'],2)
        allmarmay['on_time %']=round(allmarmay['on_time']/allmarmay['total'],2)
        allmarmay['late %']=round(allmarmay['late']/allmarmay['total'],2)
        
        allmarmay=allmarmay.iloc[0:]
        
        allmarmay.sort_values(by='late %')
       
        x=range(0, len(allmarmay))
        routelist = ["Route46", "Route55", "Route100"]
        numlist = ["46", "55", "100"]
        
        segments=self.marmay2.groupby(['route', "stops"])[['early','on_time','late']].agg('sum').reset_index()
        segments['total']=segments['early']+segments['on_time']+segments['late']
        segments['early %']=round(segments['early']/segments['total'],2)
        segments['on_time %']=round(segments['on_time']/segments['total'],2)
        segments['late %']=round(segments['late']/segments['total'],2)
        segments=segments.nlargest(len(segments), 'on_time %')
        
        for num,route in zip(x,routelist):
            makepies(('early','on_time','late'),[allmarmay['early %'].iloc[num],allmarmay['on_time %'].iloc[num],allmarmay['late %'].iloc[num]], num, route, "MOCOMarchMay20", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOMarchMay20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')

class MOCOAugustJanuary20:
    def __init__(self):
        self.augjan1 = pd.read_csv("Data/2020MOCOAUGJAN.csv")
        self.sepjan = pd.read_csv("Data/2020OCTJANSEG.csv")
        for title in [self.sepjan]:
            title.columns=["indices", "stops", "route", "early", "on_time", "late"]
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary20")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary20")
        elif folderExists == True:
            pass
    
    def first_del(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends")
        elif folderExists == True:
            pass
        # POPULAR ROUTES/SEGMENTS JAN-FEB
        monthlist = ["AUGUST", "SEPTEMBER", "OCTOBER", "NOVERMBER", "DECEMBER", "JANUARY"]
        routes=round(self.augjan1.groupby('route_id')[['boardings','alightings']].agg('sum').reset_index(),2)
        routesordered=routes.nlargest(len(routes),'boardings').reset_index()
        routesordered=routesordered.drop(labels='index',axis=1)
        routesordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/AllRoutesBoarding.csv") # to_csv to make record
        topfive = routesordered.iloc[0:]

        bymonth=round(self.augjan1.groupby('month')[['boardings','alightings']].agg('sum').reset_index(),2)
        bymonth.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/BoardingbyMonth.csv") # to_csv to make record

        df=pd.DataFrame({"bymonth":bymonth['boardings'],"month":monthlist[0:6]})

        fig1, axes = plt.subplots(2, figsize=(20,10))
        sns.barplot(ax=axes[0],data=topfive, x='route_id',y="boardings")
        axes[0].set_ylim(0,topfive['boardings'].max()+(topfive['boardings'].max()*0.35))
        sns.barplot(ax=axes[1],data=df,x='month',y='bymonth')
        axes[1].set_ylim(0,bymonth['boardings'].max()+(bymonth['boardings'].max()*0.35))
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/AllRoutesBoarding.png")
        
        #STATIONS
        stops=round(self.augjan1.groupby('stops')[['boardings','alightings']].agg('sum').reset_index(),2)
        dataa = stops.nlargest(len(stops),'boardings')
        fig2, axes1 = plt.subplots(1, figsize=(20,10))

        sns.barplot(data=dataa[0:10], x="boardings", y="stops")
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/TopStopsBoarding.png")
        a=stops.nlargest(len(stops),'boardings') # to_csv to make record
        b=stops.nlargest(len(stops),'alightings') # to_csv to make record
        a.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/StopsBoarding.csv")
        b.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/StopsAlighting.csv")
        
        #TOD
        todroutes=round(self.augjan1.groupby(['hour','route_id'])[['boardings','alightings']].agg('sum').reset_index(),2)
        todroutes=todroutes.nlargest(len(todroutes),'boardings')
        todroutes # to_csv to make record

        fig3, axes2 = plt.subplots(2, figsize=(20,15))
        axes2[0]=sns.barplot(ax=axes2[0],data=todroutes, x='hour',y="boardings",ci=None)
        axes2[1]=sns.barplot(ax=axes2[1],data=todroutes, x='route_id',y='boardings',ci=None)
        plt.savefig("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/BoardingbyHour.png")
        c=todroutes.nlargest(len(todroutes),'boardings') # to_csv to make record
        d=todroutes.nlargest(len(todroutes),'alightings') # to_csv to make record
        c.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/TODRoutesBoardings.csv")
        d.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/TODRoutesAlighting.csv")
        
        # BOARDING LOCATIONS
        boardings=round(self.augjan1.groupby('stops')['boardings'].agg('sum').reset_index(),2)
        boardingsordered=boardings.nlargest(len(boardings),'boardings')
        boardingsordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/BoardingLocations.csv") # to_csv to make record
        
        # ALIGHTING LOCATIONS
        alightings=round(self.augjan1.groupby('stops')['alightings'].agg('sum').reset_index(),2)
        alightingsordered=alightings.nlargest(len(alightings),'alightings')
        alightingsordered.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/BoardingAlightingTrends/AlightingLocations.csv") # to_csv to make record
    
    def route_analysis(self):
        folderExists = os.path.exists("Deliverables/MOCO/MOCOAugustJanuary20/RoutePerfAnalysis")
        if folderExists == False:
            os.makedirs("Deliverables/MOCO/MOCOAugustJanuary20/RoutePerfAnalysis")
        elif folderExists == True:
            pass
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
            makepies(('early','on_time','late'),[allsepjan['early %'].iloc[num],allsepjan['on_time %'].iloc[num],allsepjan['late %'].iloc[num]], num, route, "MOCOAugustJanuary20", "MOCO", "RoutePerfAnalysis")
        
        for num in numlist:
            x = segments[segments["route"]==int(num)]
            x.to_csv("Deliverables/MOCO/MOCOAugustJanuary20/RoutePerfAnalysis/Route"+num+".csv", index=False, encoding='utf-8')
    
    
def makepies(number,filling, count, name, folder, county, deliverable):
        labels = number
        sizes = filling
        explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(name)
        
        x = plt.savefig("Deliverables/"+county+"/"+folder+"/"+deliverable+"/"+name+".png")
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
                pg.first_del()
                pg.route_analysis()
            elif timeframe==2:
                pg = PGMarchMay19()
                pg.first_del()
                pg.route_analysis()
            elif timeframe==3:
                pg = PGAugustJanuary19()
                pg.first_del()
                pg.route_analysis()
        elif year == 2020:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                pg = PGJanuaryFebuary20()
                pg.first_del()
                pg.route_analysis()
                pg.third_del()
            elif timeframe==2:
                pg = PGMarchMay20()
                pg.first_del()
                pg.route_analysis()
                pg.third_del()
            elif timeframe==3:
                pg = PGAugustJanuary20()
                pg.first_del()
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
                            "(3)August to January\n"))
            if timeframe == 1:
                moco = MOCOJanuaryFebuary19()
                moco.first_del()
                moco.route_analysis()
            elif timeframe==2:
                moco = MOCOMarchMay19()
                moco.first_del()
                moco.route_analysis()
            elif timeframe==3:
                moco = MOCOAugustJanuary19()
                moco.first_del()
                moco.route_analysis()
        elif year == 2020:
            timeframe = int(input("Great. What timeframe are you interested in? \n"
                            "(1)January to Febuary \n"
                            "(2)March to May \n"
                            "(3)August to January\n"))
            if timeframe == 1:
                moco = MOCOJanuaryFebuary20()
                moco.first_del()
                moco.route_analysis()
            elif timeframe==2:
                moco = MOCOMarchMay20()
                moco.first_del()
                moco.route_analysis()
            elif timeframe==3:
                moco = MOCOAugustJanuary20()
                moco.first_del()
                moco.route_analysis()
    


main()