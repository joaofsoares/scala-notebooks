import pandas as pd


df = pd.read_csv("../../files/fakefriends.csv")

young_people_df = df[df["age"] < 25]

young_people_df.to_csv("../../files/young_fakefriends.csv")
