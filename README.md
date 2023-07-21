# MARL-PB

=================================================================
Participatory Budgeting (PB) using Reinforcement Learning - Code Repository
=================================================================

This document describes the initial release of the code to simulate
the PB process and reach a consensus in real-world datasets from 
http://pabulib.org/ for three areas - Ursynow, Ruda and Rembertow
=================================================================
File Organization
=================================================================


The code repository 



The code repository contains three folders pertaining to each area.
This division was done as the rewards are different based on the past preference of projects in previous PBs of each area.


In a PB process, a set of projects with descriptions and costs is listed. 
The voters can select multiple projects subject to a constraint that the total cost 
of the projects is within the total budget of the PB. To incorporate this knapsack constraint,
 we create a combinatorial mode to formulate bundles from the available list of projects.
This is the action space of the RL model


Each folder contains the following:
Code: RL_varying_parameters.ipynb
Input: The .pb instance (input format of participatory budgeting datasets released
 in Pabulib, more details of the data format is in the link http://pabulib.org/format)
Output: Folder - RL_varying_parameters
Contains  .txt files for each experiment settings - 
different action spaces and different indegree of the communication graph


=================================================================
Running the code
=================================================================

In every area based folder, open the RL_varying_parameters.ipynb and run each cell

You may change the parameters and run


=================================================================
Changing parameters
=================================================================
The code contains the following sections for setting the hyperparameters

The last block of code in the .ipynb notebook contains two loops
1st - deciding the number of bundles to be used as the action space for the experiments 
(should be less than the maximum possible )
2nd - for a decided action space, the indegrees used for the random graph generated for
 information exchange (should be less than the total number of agents (voters)
 
 ------------------------------------------------------------------------------------

Finally the Q_learn call in the last block can be edited for different parameters

Q=Q_learn(count,sample_voter,0.1,sample_projects,np.array(edge_list),total_budget,
 output_file=OutputFile, num_iter=10000,is_complete_graph=0, communicated=random_find,epsilon=0.01,
  randomised_communication=1,max_degree=maxdegree)

The following parameters can be configured
------------------------------------------------------------------------------------

count = number of action spaces
total_budget = Add the budget in integer form
communicated = reward communicated in the information exchange - bundles with minimum (min_find) reward, maximum (max_find) or any random bundle (random_find)
maxdegree =  maximum indegree


=================================================================
Output Format
=================================================================

The output text files are named as MaxN_CombY where N is the maximum indegree 
allowed for the communication and Y is the number of bundles (Combinations) used as action space
An output text file contains the following 

    project id    reward
0       1211.0 -0.444988
1       2141.0 -0.057202
2       1356.0  0.331482
3       2183.0  0.343395
4        433.0 -0.263659
5        192.0  0.232709
6       1889.0  0.302624
7        193.0  0.251523
8       1347.0  0.192139
9       1905.0  0.121838
10      2092.0  0.245409
11      2121.0 -0.136063
12       191.0  0.215283

Action Space used for the experiment

Valid Combinations are:
(2141.0, 1356.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 191.0)
(2141.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0)
(1356.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0)
(1211.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1905.0, 2092.0, 191.0)
(1211.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 191.0)
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2121.0)
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 2092.0, 2121.0)
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 2121.0, 191.0)

The choices of each agent after each iteration

After Iteration 1 :
Voter 1: ID 521; Choice (2141.0, 2183.0, 433.0, 1889.0, 1347.0, 1905.0, 2092.0, 2121.0) 
Voter 2: ID 231; Choice (2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1905.0, 2121.0, 191.0) 
Voter 3: ID 390; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 1905.0, 2121.0, 191.0) 
Voter 4: ID 417; Choice (1211.0, 1356.0, 2183.0, 192.0, 193.0, 1347.0, 1905.0, 2092.0) 
Voter 5: ID 352; Choice (1211.0, 1356.0, 2183.0, 192.0, 193.0, 1347.0, 1905.0, 2092.0) 
Voter 6: ID 712; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 1905.0, 2092.0, 2121.0) 
Voter 7: ID 160; Choice (2141.0, 1356.0, 433.0, 192.0, 193.0, 1905.0, 2121.0, 191.0) 
Voter 8: ID 704; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 2092.0, 2121.0, 191.0) 

Consensus Details

Concensus reached after 56 iterations.
Max degree: 6 Number of valid combinations: 49 Using random reward sending strategy.
There is 1 opinion after all iterations.
(2141.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0) count: 50









































