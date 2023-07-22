import pandas as pd

# df = [['No. of valid combinations','Max degree','Valid Combinations','Selected Bundle','No. of iterations']]
df = pd.read_excel("/home/raj/Desktop/4 setups experiment_Ursynow/No scaled rewards_No random degree/analysis.xlsx")
i=0
for k in range(5,76,5):
    for j in range(2, 25, 2):
        with open('Max'+str(j)+'_comb'+str(k), 'r') as file:
            lines = file.readlines()
        valid=[]
        flag = 0
        flag1 = 0
        i+=1
        for line in lines:
            words = line.strip().split()    
            if words[0]=='Concensus':
                df.at[i, 'No. of iterations'] = words[3]
            if words[0]=='Max':
                df.at[i, 'Max degree'] = words[2]
            if words[0]=='Max':
                df.at[i, 'No. of valid combinations'] = words[7]
            if flag1==1:
                df.at[i, 'Selected bundle'] = line
                substring = line[:line.index(")")]
                projects1 = substring.replace("(", "")
                projects = projects1.replace(")", "")
                flag1 = 0
            if words[0]=='There':
                flag1 = 1
            if words[0]=='Valid':
                flag = 1
            if words[0]=='Initial':
                flag = 0
            if flag==1:
                valid.append(line)
        df.at[i, 'Valid combinations'] = valid
        projectids = projects.split(',')
        cost = 0
        popularity = 0
        for project in projectids:
            # print(project.strip())
            if project.strip()=='1024.0':
                cost+=175000    
                popularity+=1.0
            elif project.strip()=='1061.0':
                cost+=149000
                popularity+=0.89
            elif project.strip()=='1034.0':
                cost+=102600
                popularity+=0.78
            elif project.strip()=='210.0':
                cost+=650000
                popularity+=0.67
            elif project.strip()=='635.0':
                cost+=110180
                popularity+=0.56
            elif project.strip()=='264.0':
                cost+=257030
                popularity+=0.44
            elif project.strip()=='300.0':
                cost+=131100
                popularity+=0.33
            elif project.strip()=='346.0':
                cost+=120000
                popularity+=0.22
            elif project.strip()=='1806.0':
                cost+=235200
                popularity+=0.11
            elif project.strip()=='1644.0':
                cost+=252000
                popularity+=0.00
        df.at[i, 'Total cost'] = cost
        df.at[i, 'Budget utilization'] = cost/954900
        df.at[i, 'Popularity index'] = popularity/len(projectids)
        greedy_cost = 924910
        equal_cost = 787880
        phragmen_cost = 667880
        if df.at[i, 'Total cost']==greedy_cost:
            df.at[i, 'Match'] = 'greedy'
        elif df.at[i, 'Total cost']==equal_cost:
            df.at[i, 'Match'] = 'equal shares'
        elif df.at[i, 'Total cost']==phragmen_cost:
            df.at[i, 'Match'] = 'phragmen'
        else:
            df.at[i, 'Match'] = 'None'

df.to_excel('/home/raj/Desktop/4 setups experiment_Ursynow/No scaled rewards_No random degree/analysis1.xlsx', index=False)
        