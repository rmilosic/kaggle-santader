# unzip
from zipfile import ZipFile
import os
import pandas as pd

# export files
files_dir = os.path.join(os.getcwd(), "files")
files = os.listdir(files_dir)
for i in files:
    z = ZipFile(os.path.join(files_dir, i), mode="r")
    z.extractall(path=files_dir)


def load_data():
    train_data = pd.read_csv(os.path.join(files_dir, "train.csv"), sep=",", header=True)
    train_data = train_data.drop(['ID_code'], axis=1)

    return train_data