import pandas as pd


def launched(obj, info):
    value = obj["launched"]
    if not pd.isnull(value):
        return value
    return None