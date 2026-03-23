def load_data(df, output_path):

    df.to_parquet(output_path, index=False)

    print("Data saved successfully")