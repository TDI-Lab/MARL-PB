import pandas as pd

# df = [['No. of valid combinations','Max degree','Valid Combinations','Selected Bundle','No. of iterations']]
df = pd.read_excel("/home/raj/Desktop/4 setups experiment_Ruda/No scaled rewards_No random degree/analysis.xlsx")
i=0
for k in range(3,13,1):
    for j in range(2, 26, 2):
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
            if project.strip()=='1142.0':
                cost+=40000
                popularity+=1.000
            elif project.strip()=='2296.0':
                cost+=20800
                popularity+=0.875
            elif project.strip()=='2263.0':
                cost+=50000
                popularity+=0.750
            elif project.strip()=='1867.0':
                cost+=81330
                popularity+=0.625
            elif project.strip()=='2037.0': 
                cost+=250000
                popularity+=0.500
            elif project.strip()=='518.0':
                cost+=10000
                popularity+=0.375
            elif project.strip()=='248.0':
                cost+=9000
                popularity+=0.250
            elif project.strip()=='1226.0':
                cost+=183000
                popularity+=0.125
            elif project.strip()=='2205.0':
                cost+=12400
                popularity+=0.000
        df.at[i, 'Total cost'] = cost
        df.at[i, 'Budget utilization'] = cost/550000
        df.at[i, 'Popularity index'] = popularity/len(projectids)
        greedy_cost = 473530
        equal_cost = 223530
        phragmen_cost = 473530
        if df.at[i, 'Total cost']==greedy_cost:
            df.at[i, 'Match'] = 'greedy plus phragmen'
        elif df.at[i, 'Total cost']==equal_cost:
            df.at[i, 'Match'] = 'equal shares'
        else:
            df.at[i, 'Match'] = 'None'

df.to_excel('/home/raj/Desktop/4 setups experiment_Ruda/No scaled rewards_No random degree/analysis1.xlsx', index=False)
        