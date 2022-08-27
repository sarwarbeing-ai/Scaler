def data_distribute(input_data):
    '''
    input:
    input_data -> the input data in the form of a string, such as "_,10,_"
    output:
    filled_data -> the output python list with the missing data filled up in place of the blanks
    rules:
    1.left of a number is filled by the number distributed equally
    into number of blanks to the left, along with the number position itself
    2.middle blanks of two numbers are filled by their sum equally distrubuted,
     along with their two positions
     3.right blanks of a number is again distributed equally by that number,
      along with the position of the number itself.
    '''
    input_data=input_data.split(",")
    filled_data =input_data
    data=[]
    for a in input_data:
        if a!="_":
            data.append(int(a))
    if len(data)==1:
        for i in range(len(filled_data)):
            filled_data[i]=int(data[0]//(len(filled_data)))
        return filled_data

    if input_data[0]=="_":
        c=0
        for a in input_data:
            if a=="_":
                c+=1
            else:
                break
        for i in range(c+1):
            filled_data[i]=int(data[0]//(c+1))
        data[0]=data[0]//(c+1)
        i=0
        j=1
        while j<len(data):
            count=0
            s=data[i]+data[j]
            for i in range(c+1,len(input_data)):
                if filled_data[i]=="_":
                    count+=1
                else:
                    break
            for i in range(c,c+count+2):
                filled_data[i]=int(s//(count+2))
            c=c+count+1
            data[j]=s//(count+2)
            i+=1
            j+=1
        sc=0
        for i in range(c+1,len(filled_data)):
            sc+=1
        if sc!=0:
            for i in range(c,len(filled_data)):
                filled_data[i]=int(data[-1]//(sc+1))

    else:
        i=0
        j=1
        c=0
        while j<len(data):
            count=0
            s=data[i]+data[j]
            for i in range(c+1,len(input_data)):
                if filled_data[i]=="_":
                    count+=1
                else:
                    break
            for i in range(c,c+count+2):
                filled_data[i]=int(s//(count+2))
            c=c+count+1
            data[j]=s//(count+2)
            i+=1
            j+=1
        sc=0
        for i in range(c+1,len(filled_data)):
            sc+=1
        if sc!=0:
            for i in range(c,len(filled_data)):
                filled_data[i]=int(data[-1]//(sc+1))



    return filled_data
    
