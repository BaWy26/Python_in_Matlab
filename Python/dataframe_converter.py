import pandas as pd

def convert_to_dataframe(data, columns):
    df = pd.DataFrame(data, columns=columns)
    return df.to_dict('list')  # Convert the DataFrame to a dictionary