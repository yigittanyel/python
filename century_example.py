def century2Year(year):
    str_year=str(year)
    if(len(str_year)<3): #100
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"):
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4]=="00"): #1900
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1

print(century2Year(1453))
    
    