import pandas as pd
#import numpy as np
#import requests
#from mechanism import *

# ON PRODUCTION REPLACE THIS
#url=open("/storage/emulated/0/AProjects/Api/currency/tra.html","rt") 
# TO THIS
#url=requests.get("https://www.tra.go.tz/index.php/exchange-rates")

class tra():
    
    def ForeignExhange():
        url=open("/storage/emulated/0/AProjects/Api/currency/tra.html","rt")
        dfs=pd.read_html(url)
     
        for df in dfs:
            
            if len(df) == 34:
                the_one = df
                clone=the_one.rename(columns={0:"COUNTRY",1:"CURRENCY",2:"SELLING RATES",3:"BUYING RATES"})
                pure=clone[1:]
                test=pure.T
                
                database={
                    "USD": dict(test[1]),
                    "UK": dict(test[2]),
                    "EUR": dict(test[3]),
                    "CND": dict(test[4]),
                    "SWZ": dict(test[5]),
                    "JPN": dict(test[6]),
                    "SWD": dict(test[7]),
                    "NRW": dict(test[8]),
                    "DNM": dict(test[9]),
                    "AUS": dict(test[10]),
                    "IND": dict(test[11]),
                    "PKS": dict(test[12]),
                    "ZAM": dict(test[13]),
                    "MAL": dict(test[14]),
                    "MOZ": dict(test[15]),
                    "KNY": dict(test[16]),
                    "UGN": dict(test[17]),
                    "RWD": dict(test[18]),
                    "BUR": dict(test[19]),
                    "ZIM": dict(test[20]),
                    "SAF": dict(test[21]),
                    "UAE": dict(test[22]),
                    "SNP": dict(test[23]),
                    "HNK": dict(test[24]),
                    "SAR": dict(test[25]),
                    "KWT": dict(test[26]),
                    "BTS": dict(test[27]),
                    "CHN": dict(test[28]),
                    "MLS": dict(test[29]),
                    "SKR": dict(test[30]),
                    "NZL": dict(test[31]),
                    "SDR": dict(test[32]),
                    "GOLD": dict(test[33]),
                }
                
                return database
                
            else:
                raise FileNotFound(f"Error:: {url.sttus_code} file not found")
                

# T E S T I N G   A P I
results=tra.ForeignExhange()
print(results["USD"])
