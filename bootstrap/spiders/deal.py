# -*- coding:utf-8 -*-
# !usr/bin/env python
import pandas as pd


def open_file():
    df = pd.read_csv("app_details.csv")
    df = pd.DataFrame(df, columns=["App Package Name","Play Store Name","Category","Average Rating","Number of Ratings"])
    fl = df["Category"].unique()
    for i in fl:
        tmp_data = df[df["Category"].isin([i])]
        tmp_data.sort_values("Average Rating")
        result_data = tmp_data.head(150)
        print(result_data["Average Rating"])
        result_data.to_csv("re.csv", mode="a", header=False)



if __name__ == "__main__":
    open_file()