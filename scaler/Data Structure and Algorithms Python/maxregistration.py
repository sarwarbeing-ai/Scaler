import pandas as pd
import numpy as np
def solve(df):
    """
    input: pandas dataframe with columns ['Date', 'R_id', 'Phy', 'Chem', 'Math']
    output: pandas series
    """

    # code for taking input and printing output is already taken care of just return the list with required elements.
    """
        You need to return a series where the elements will be the most occuring month,
        most occuring month's frequency, average chemistry,physics and maths marks in
        most occuring months upto two decimal places in this order.
    """
    # YOUR CODE GOES HERE

    df['Date']=df['Date'].astype("datetime64")
    df['month']=df['Date'].dt.month.map({1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',
                                     6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'})

    reg_freq=df['month'].value_counts().sort_values(ascending=False)
    max_number_reg=reg_freq[0]
    months_index=reg_freq[reg_freq==max_number_reg]
    months_index.sort_index(inplace=True)
    m=months_index.index[0] # month name
    avg=df.groupby("month")[['Chem','Phy','Math']].mean().round(2)
    average_marks=avg.loc[m,:].tolist()

    s=pd.Series([m,max_number_reg]+average_marks) # construct the series

    # YOUR CODE ENDS HERE
    return s
