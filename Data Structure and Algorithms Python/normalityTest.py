def normality_test(arr):
    '''
    Input:
    arr: a python list denoting the input distribution of floating point values
    Output:
    res: return "yes" or "no" as per required, of type string
    Normality test:Test whether the given array of data is normaly distributed or not
    within an error of margin plus-minus 2%
    '''
    res = ""
    # Your code goes here
    import numpy as np
    sd=np.std(arr)
    mu=np.mean(arr)
    count3=0
    count2=0
    count1=0
    for a in arr:
        if a<(mu+3*sd) and a>(mu-3*sd):
            count3+=1
        if a<(mu+2*sd) and a>(mu-2*sd):
            count2+=1
        if a<(mu+sd) and a>(mu-sd):
            count1+=1


    per3=(count3/len(arr))*100
    per2=(count2/len(arr))*100
    per1=(count1/len(arr))*100
    if abs(per1-68)<=2 and abs(per2-95)<=2 and abs(per3-99.7)<=2:
        return "yes"
    return "no"
