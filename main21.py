x={'Just':9,'Fifty-two':9,'days':9,'till':5,'CHRISTMAS':9}
searching=9
frequency=0
for key in x:
    if x[key]==searching:
        frequency=frequency+1
        
print("The number of times that 9 occured is", frequency,":)")