import pandas as pd

#for mac users, run '/Applications/Python\ 3.12/Install\ Certificates.command' in terminal

url = "https://raw.githubusercontent.com/wonjun-seo/cosmos/master/static_files/presentations/lecture_five/code%26data/coding(anddata)/movie_cluster_data.csv"
movie_data = pd.read_csv(url)

