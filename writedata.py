import pandas as pd
 
data = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]
 
newdata = pd.DataFrame(data)
newdata.to_csv('newdata.csv',sep=',',index=False)
