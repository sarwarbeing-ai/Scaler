import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def preprocess(df):

  """
    Takes df as input, do the preprocessing as asked.
    Return the preprocessed dataframe
  """
  #
  boolean=((df['Roll_ID']=="0") | (df['Roll_ID']==np.nan)) & ((df['Name']=="0") | (df['Name']==np.nan))& ((df['Marks']=="0") | (df['Marks']==np.nan))
  df.drop(df.index[boolean],axis=0,inplace=True)
  df.fillna("Anonymous")
  df['Name']=df['Name'].replace("0","Anonymous")
  df['Roll_ID']=df['Roll_ID'].replace(["0",np.nan],df['Roll_ID'].median()).astype('int')
  df['Marks']=df['Marks'].replace(["0",np.nan],df['Marks'].median()).astype('int')



  return df
