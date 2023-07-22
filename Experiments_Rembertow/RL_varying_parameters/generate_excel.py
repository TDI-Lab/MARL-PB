import pandas as pd

# df = [['No. of valid combinations','Max degree','Valid Combinations','Selected Bundle','No. of iterations']]
df = pd.read_excel("/home/raj/Desktop/4 setups experiment_Rembertow/No scaled rewards_No random degree/analysis.xlsx")
i=0
for k in range(5,101,5):
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
            if project.strip()=='1211.0':
                cost+=229500
                popularity+=1.000
            elif project.strip()=='2141.0':
                cost+=80000
                popularity+=0.917
            elif project.strip()=='1356.0':
                cost+=40000
                popularity+=0.833
            elif project.strip()=='2183.0':
                cost+=3800
                popularity+=0.750
            elif project.strip()=='433.0':
                cost+=120000
                popularity+=0.667
            elif project.strip()=='192.0':
                cost+=11200
                popularity+=0.583
            elif project.strip()=='1889.0':
                cost+=20000
                popularity+=0.500
            elif project.strip()=='193.0':
                cost+=4200
                popularity+=0.417
            elif project.strip()=='1347.0':
                cost+=31500
                popularity+=0.333
            elif project.strip()=='1905.0':
                cost+=17300
                popularity+=0.250
            elif project.strip()=='2092.0':
                cost+=22150
                popularity+=0.167
            elif project.strip()=='2121.0':
                cost+=77000
                popularity+=0.083
            elif project.strip()=='191.0':
                cost+=20000
                popularity+=0.00
        df.at[i, 'Total cost'] = cost
        df.at[i, 'Budget utilization'] = cost/372063
        df.at[i, 'Popularity index'] = popularity/len(projectids)
        greedy_cost = 368700
        equal_cost = 170150
        phragmen_cost = 138650
        if df.at[i, 'Total cost']==greedy_cost:
            df.at[i, 'Match'] = 'greedy'
        elif df.at[i, 'Total cost']==equal_cost:
            df.at[i, 'Match'] = 'equal shares'
        elif df.at[i, 'Total cost']==phragmen_cost:
            df.at[i, 'Match'] = 'phragmen'
        else:
            df.at[i, 'Match'] = 'None'
df.to_excel('/home/raj/Desktop/4 setups experiment_Rembertow/No scaled rewards_No random degree/analysis1.xlsx', index=False)
        
