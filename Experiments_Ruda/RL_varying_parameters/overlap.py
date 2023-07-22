import pandas as pd

# df = [['No. of valid combinations','Max degree','Valid Combinations','Selected Bundle','No. of iterations']]
df = pd.read_excel("/home/raj/Desktop/4 setups experiment_Ruda/No scaled rewards_No random degree/overlap.xlsx")

j = 2
k = 2
for l in range(3,13,1):
    for i in range(2, 25, 2):
        with open('Max'+str(i)+'_comb'+str(l), 'r') as file:
            lines = file.readlines()
        consensus = lines[-1]   
        consensus_projects = consensus[consensus.index("(")+1:consensus.index(")")].split(',')
        max_line = lines[-3]
        word = max_line.strip().split()
        max = word[2]
        combinations = word[7]
        for line in lines:
            words = line.strip().split()
            if words[0]=="Initial":
                initial = lines[lines.index(line)+2:lines.index(line)+52]
                # print(initial)
                for voters in initial:
                    df.at[j, 'Voter'] = voters[:voters.index(":")]
                    df.at[j, 'Max degree'] = max
                    df.at[j, 'No. of valid combinations'] = combinations
                    df.at[j, 'Initial Choice'] = voters[voters.index("(")+1:voters.index(")")]
                    df.at[j, 'Consensus'] = consensus[consensus.index("(")+1:consensus.index(")")]
                    projectids = df.at[j, 'Initial Choice'].split(',')
                    greedy = 0
                    phragmen = 0
                    equal = 0
                    con = 0
                    for projects in projectids:
                        project = projects.strip()
                        if project=='1142.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2296.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2263.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='518.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='248.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2205.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1867.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2037.0':
                            greedy+=1
                            phragmen+=1
                        for consensus_project in consensus_projects:
                            consen = consensus_project.strip()
                            if project==consen:
                                con+=1
                    length = len(projectids)
                    df.at[j, 'Overlap with greedy(initial)'] = greedy/length
                    df.at[j, 'Overlap with phragmen(initial)'] = phragmen/length
                    df.at[j, 'Overlap with equal shares(initial)'] = equal/length
                    df.at[j, 'Overlap with consensus(initial)'] = con/length
                    j+=1
                iteration = lines[lines.index(line)+54:lines.index(line)+104]
                for voter in iteration:
                    df.at[k, 'Iteration 1'] = voter[voter.index("(")+1:voter.index(")")]
                    projectids = df.at[k, 'Iteration 1'].split(',')
                    greedy = 0
                    phragmen = 0
                    equal = 0
                    con = 0
                    for projects in projectids:
                        project = projects.strip()
                        if project=='1142.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2296.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2263.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='518.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='248.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2205.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1867.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2037.0':
                            greedy+=1
                            phragmen+=1
                        for consensus_project in consensus_projects:
                            consen = consensus_project.strip()
                            if project==consen:
                                con+=1
                    length = len(projectids)
                    df.at[k, 'Overlap with greedy(iteration 1)'] = greedy/length
                    df.at[k, 'Overlap with phragmen(iteration 1)'] = phragmen/length
                    df.at[k, 'Overlap with equal shares(iteration 1)'] = equal/length
                    df.at[k, 'Overlap with consensus(iteration 1)'] = con/length
                    k+=1
    
df.to_excel('/home/raj/Desktop/4 setups experiment_Ruda/No scaled rewards_No random degree/overlap1.xlsx', index=False)