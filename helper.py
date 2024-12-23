import numpy as np
import pandas as pd

def filter_models(dataframe, brand, segment):
    filtered_df = dataframe[(dataframe['brand_name'] == brand) & (dataframe['segment'] == segment)]
    
    return filtered_df['model'].unique().tolist()

# Filter processor
def filter_pros(dataframe, brand, segment):
    filtered_df = dataframe[(dataframe['brand_name'] == brand) & (dataframe['segment'] == segment)]
    
    return filtered_df['processor_brand'].unique().tolist()

#Filter Operating system
def filter_OS(dataframe, brand, segment):
    filtered_df = dataframe[(dataframe['brand_name'] == brand) & (dataframe['segment'] == segment)]
    
    return filtered_df['os'].unique().tolist()

#width
def filter_width(dataframe, brand, segment):
    filtered_df = dataframe[(dataframe['brand_name'] == brand) & (dataframe['segment'] == segment)]
    
    return filtered_df['width'].unique().tolist()

#Height
def filter_height(dataframe, brand, segment):
    filtered_df = dataframe[(dataframe['brand_name'] == brand) & (dataframe['segment'] == segment)]
    
    return filtered_df['height'].unique().tolist()

#Filter Operating system
def filter_laos(dataframe, brand):
    filtered_df = dataframe[dataframe['Company'] == brand]
    
    return filtered_df['os'].unique().tolist()
