t = (0,4,132.4222,10000,12345.67)
x=str(t[0])
y=str(t[1])
if(len(x)==1):
    x='0'+x
if(len(y)==1):
    y="0"+y
print("day_"+x+", ex_"+y+" : "+str(round(t[2],2))+", "+format(t[3],".2e")+", "+format(t[4],".2e"))
    
