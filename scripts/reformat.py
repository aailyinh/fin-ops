#!/usr/bin/python3

import pandas as pd
import numpy as np
import glob
import os


def main():
    path = './downloader-data'
    extension = 'csv'
    os.chdir(path)
    all_files = glob.glob('*.{}'.format(extension))

    columns = ['Date', 'Close', 'Volume']
    for i, file in enumerate(all_files):
        print(f'[{i}/{len(all_files)}] - {file}')
        dataframe = pd.read_csv(file)
        updated = pd.DataFrame(data=[], columns=[])

        for col in columns:
            updated[col] = dataframe[col]

        updated.to_csv(file, index=False)





if __name__ == "__main__":
    main()
