import pandas as pd
import glob
import clean_data

PARQUET_FILES = "monthly_data_releases/*.parquet"

def main():
    list_dfs = []

    files = sorted(glob.glob(PARQUET_FILES))
    for file_name in files:
        print(f"Load data from : ", file_name, "\n")
        df = pd.read_parquet(file_name, columns= ['station', 'delay_in_min' , 'time', 'is_canceled', 'train_type'])
        list_dfs.append(clean_data.clean_df(df))
        
    
    final_df = pd.concat(list_dfs, ignore_index=True)
    # Write final_df to csv file
    first_month_str = files[0][-15:-8] 
    last_month_str = files[-1][-15:-8]
    final_csv_file_name = "deutsche_bahn_" + first_month_str + "-" + last_month_str + ".csv"
    final_df.to_csv(final_csv_file_name, index=False)

if __name__ == "__main__":
    main()