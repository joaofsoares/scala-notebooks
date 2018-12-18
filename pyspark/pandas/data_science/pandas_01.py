import pandas as pd


csv_path = "../../files/fakefriends.csv"

df = pd.read_csv(csv_path)

print(df.head())

songs = {"album": ["Thriller", "Back in Black",
                   "The Dark Side of the Moon", "The Bodyguard", "Bat Out of Hell"],
         "released": [1982, 2980, 1973, 1992, 1977],
         "length": ["00:42:19", "00:42:11", "00:42:49", "00:57:44", "00:46:33"]}

songs_frame = pd.DataFrame(songs)

print(songs_frame)

x = songs_frame[["length"]]

print(x)
