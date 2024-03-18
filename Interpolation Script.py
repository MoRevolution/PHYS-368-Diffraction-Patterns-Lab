import pandas as pd
import numpy as np

data = pd.read_csv('file_name.csv')


data['interpolated_column'] = np.interp(
    data.iloc[:, 3], data.iloc[:, 1].dropna(), data.iloc[:, 0].dropna()
    )

data.to_csv('output_file_name.csv', index=False)
