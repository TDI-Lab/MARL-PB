import pandas as pd

# df = [['No. of valid combinations','Max degree','Valid Combinations','Selected Bundle','No. of iterations']]
df = pd.read_excel("/home/raj/Desktop/4 setups experiment/No scaled rewards_No random degree/overlap.xlsx")

j = 2
k = 2
for l in range(5,101,5):
    for i in range(6, 25, 2):
        with open('Max'+str(i)+'_comb100', 'r') as file:
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
                        if project=='193.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1356.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2183.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='192.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1211.0':
                            greedy+=1
                        elif project=='2141.0':
                            greedy+=1
                        elif project=='1889.0':
                            equal+=1
                            phragmen+=1
                        elif project=='1905.0':
                            equal+=1
                            phragmen+=1
                        elif project=='2092.0':
                            equal+=1
                            phragmen+=1
                        elif project=='191.0':
                            equal+=1
                            phragmen+=1
                        elif project=='1347.0':
                            equal+=1
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
                        if project=='193.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1356.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='2183.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='192.0':
                            greedy+=1
                            equal+=1
                            phragmen+=1
                        elif project=='1211.0':
                            greedy+=1
                        elif project=='2141.0':
                            greedy+=1
                        elif project=='1889.0':
                            equal+=1
                            phragmen+=1
                        elif project=='1905.0':
                            equal+=1
                            phragmen+=1
                        elif project=='2092.0':
                            equal+=1
                            phragmen+=1
                        elif project=='191.0':
                            equal+=1
                            phragmen+=1
                        elif project=='1347.0':
                            equal+=1
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
    
df.to_excel('/home/raj/Desktop/4 setups experiment/No scaled rewards_No random degree/overlap1.xlsx', index=False)