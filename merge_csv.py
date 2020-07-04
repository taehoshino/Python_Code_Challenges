import pandas as pd


def merge_csv(input_csv_list, out_csv):
    df_in_list = []
    for csv in input_csv_list:
        df_in = pd.read_csv(csv, index_col="Name")
        df_in_list.append(df_in)
    out_df = pd.concat(df_in_list)
    print(out_df)
    out_df.to_csv(out_csv)


merge_csv(["in1.csv","in2.csv"], "out.csv")

