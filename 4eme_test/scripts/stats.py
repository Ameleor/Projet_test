import pandas as pd

def main():
    # Retrieving the csv with pandas
    df = pd.read_csv("../data/list_with_taxonomy.csv")

    # General informations of the df
    print("General informations:")
    print(df.info())

    # Print of the general statistics of the df
    print("\n Descriptive statistics for each numeric columns :")
    print(round(df.describe(), 0))

    # Print of the number of unique number for each column of the df
    print("\nHow much unique number ther is for each column :")
    print(df.nunique())

    print("\nThe 10 first lines of the list :")
    print(df.head(10))

if __name__ == "__main__":
    # Launching of the code
    main()
