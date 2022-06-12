import pandas as pd
def solve(res_df):
    #dates=res_df[0]
    #RID=res_df[1]
    #phy=res_df[2]
    #chem=res_df[3]
    #math=res_df[4]
    df=res_df
    #df = pd.DataFrame({'dates':dates,'RID':RID, 'Phy':phy, 'Chem':chem, 'Math':math})
    #df=pd.DataFrame(res_df,columns=['dates', 'RID', 'Phy', 'Chem', 'Math'])
    df['dates']=pd.to_datetime(df['dates'],format='%Y/%m/%d')
    df_2014=df.loc[df['dates'].dt.year==2014]
    df_2014=df_2014.loc[df_2014['dates'].dt.month>=5]

    df_2015on=df.loc[df['dates'].dt.year>2014 ]
    df=pd.concat([df_2014,df_2015on],axis=0)
    rid=df.RID
    df.drop(['dates','RID'],axis=1,inplace=True)
    avg=df.mean(axis=1)
    df=pd.DataFrame({'RID':rid,'avg':avg})
    df=df.sort_values('avg',axis=0)


    return df.RID.tolist()
