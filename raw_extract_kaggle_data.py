import kagglehub
from kagglehub import KaggleDatasetAdapter

def getkaggle_data(csv_name):
    # Load the latest version of the dataset
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "sumitrodatta/nba-aba-baa-stats",
        csv_name,
        # Provide any additional arguments like
        # sql_query or pandas_kwargs. See the
        # documentation for more information:
        # https://github.com/Kaggle/kagglehub#kaggledatasetadapterpandas
    )
    return df