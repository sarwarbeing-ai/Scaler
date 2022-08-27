def bill(unit):
    ans = None
    if unit<=50:
        ans= 0.50*unit
    elif unit>50 and unit<=150:
        ans=50*0.50+(unit-50)*0.75
    elif unit>150 and unit<=250:
        ans=50*0.50+100*0.75+(unit-150)*1.20
    else:
        ans=50*0.50+100*0.75+100*1.20+1.50*(unit-250)
    ans=ans+(ans*20/100)




    return int(ans)
