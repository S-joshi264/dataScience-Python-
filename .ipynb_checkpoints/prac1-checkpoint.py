import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

players_data=pd.read_csv("C:\\Users\\sj81o\\Downloads\\archive (1)\\players.csv")

class pandaPractice:
    def initiate():
        print(players_data.info())
        print(players_data["player_id"].count())
        print(players_data.shape)
        print(players_data.dtypes)
        print(players_data["nationality"].value_counts())
        print(players_data["nationality"].unique())
        print(players_data["batting_style"].unique())
        print(players_data[(players_data["batting_style"].str.contains("left",case=False) )])
        print(players_data.sort_values("highest_auction_price_lakh",ascending=False).head(5))
        print(players_data.columns)
        print(players_data["is_capped_international"].unique())
        print(players_data.groupby("is_capped_international")["highest_auction_price_lakh"].mean())
        print(players_data.groupby("is_capped_international")["highest_auction_price_lakh"].median())
        print( players_data["playing_role"].unique())
        print(players_data.groupby("playing_role")["highest_auction_price_lakh"].mean())
        print(players_data.groupby("playing_role")["highest_auction_price_lakh"].median())
        print(players_data.groupby("playing_role")["highest_auction_price_lakh"].std())
        # print(players_data[(players_data["playing_role"]).str.contains("bat",case=False)]["highest_auction_price_lakh"].max())
        print(players_data.columns)
        sb.boxplot(x=players_data["playing_role"],y=players_data["highest_auction_price_lakh"],data=players_data)
        plt.show()
del_data=pd.read_csv("C:\\Users\\sj81o\\Downloads\\archive (1)\\deliveries.csv")
# print(del_data.info())
# print(del_data.isnull().sum())
# print(del_data["total_runs"].unique())
# print(del_data.groupby("striker")["batsman_runs"].sum().sort_values(ascending=False).head())
# print(del_data.groupby("striker")["delivery_id"].size())
print(del_data["extra_type"].unique())
