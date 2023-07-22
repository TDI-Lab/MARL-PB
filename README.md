# MARL-PB


Participatory Budgeting (PB) using Reinforcement Learning - Code Repository
=================================================================

This document describes the initial release of the code to simulate
the PB process and reach a consensus in real-world datasets from <br>
http://pabulib.org/ for three areas - Ursynow, Ruda and Rembertow<br>



File Organization
=================================================================


The code repository <br>

The code repository contains three folders pertaining to each area.<br>
This division was done as the rewards are different based on the past preference of projects in previous PBs of each area.<br>


In a PB process, a set of projects with descriptions and costs is listed. <br>
The voters can select multiple projects subject to a constraint that the total cost <br>
of the projects is within the total budget of the PB. To incorporate this knapsack constraint,<br>
 we create a combinatorial mode to formulate bundles from the available list of projects.<br>
This is the action space of the RL model<br>


Each folder contains the following:<br>
Code: RL_varying_parameters.ipynb<br>
Input: The .pb instance (input format of participatory budgeting datasets released<br>
 in Pabulib, more details of the data format is in the link http://pabulib.org/format)<br>
Output: Folder - RL_varying_parameters<br>
Contains  .txt files for each experiment settings - <br>
different action spaces and different indegree of the communication graph<br>



Running the code
=================================================================

In every area based folder, open the RL_varying_parameters.ipynb and run each cell<br>

You may change the parameters and run<br>



Changing parameters
=================================================================
The code contains the following sections for setting the hyperparameters<br>

The last block of code in the .ipynb notebook contains two loops<br>
1st - deciding the number of bundles to be used as the action space for the experiments <br>
(should be less than the maximum possible )<br>
2nd - for a decided action space, the indegrees used for the random graph generated for<br>
 information exchange (should be less than the total number of agents (voters)<br>
 
 ------------------------------------------------------------------------------------

Finally the Q_learn call in the last block can be edited for different parameters<br>

Q=Q_learn(count,sample_voter,0.1,sample_projects,np.array(edge_list),total_budget,<br>
 output_file=OutputFile, num_iter=10000,is_complete_graph=0, communicated=random_find,epsilon=0.01,<br>
  randomised_communication=1,max_degree=maxdegree)<br>

The following parameters can be configured
------------------------------------------------------------------------------------

count = number of action spaces<br>
total_budget = Add the budget in integer form<br>
communicated = reward communicated in the information exchange - bundles with minimum (min_find) reward, maximum (max_find) or any random bundle (random_find)<br>
maxdegree =  maximum indegree<br>



Output Format
=================================================================

The output text files are named as MaxN_CombY where N is the maximum indegree 
allowed for the communication and Y is the number of bundles (Combinations) used as action space
An output text file contains the following 

    project id    reward
0       1211.0 -0.444988<br>
1       2141.0 -0.057202<br>
2       1356.0  0.331482<br>
3       2183.0  0.343395<br>
4        433.0 -0.263659<br>
5        192.0  0.232709<br>
6       1889.0  0.302624<br>
7        193.0  0.251523<br>
8       1347.0  0.192139<br>
9       1905.0  0.121838<br>
10      2092.0  0.245409<br>
11      2121.0 -0.136063<br>
12       191.0  0.215283<br>

Action Space used for the experiment<br>

Valid Combinations are:<br>
(2141.0, 1356.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 191.0)<br>
(2141.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0)<br>
(1356.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0)<br>
(1211.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1905.0, 2092.0, 191.0)<br>
(1211.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 191.0)<br>
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2121.0)<br>
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 2092.0, 2121.0)<br>
(2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1347.0, 2121.0, 191.0)<br>

The choices of each agent after each iteration<br>

After Iteration 1 :<br>
Voter 1: ID 521; Choice (2141.0, 2183.0, 433.0, 1889.0, 1347.0, 1905.0, 2092.0, 2121.0) <br>
Voter 2: ID 231; Choice (2141.0, 2183.0, 433.0, 192.0, 1889.0, 193.0, 1905.0, 2121.0, 191.0) <br>
Voter 3: ID 390; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 1905.0, 2121.0, 191.0) <br>
Voter 4: ID 417; Choice (1211.0, 1356.0, 2183.0, 192.0, 193.0, 1347.0, 1905.0, 2092.0) <br>
Voter 5: ID 352; Choice (1211.0, 1356.0, 2183.0, 192.0, 193.0, 1347.0, 1905.0, 2092.0) <br>
Voter 6: ID 712; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 1905.0, 2092.0, 2121.0) <br>
Voter 7: ID 160; Choice (2141.0, 1356.0, 433.0, 192.0, 193.0, 1905.0, 2121.0, 191.0) <br>
Voter 8: ID 704; Choice (2141.0, 1356.0, 2183.0, 433.0, 193.0, 2092.0, 2121.0, 191.0) <br>

Consensus Details<br>

Consensus reached after 56 iterations.<br>
Max degree: 6 Number of valid combinations: 49 Using random reward sending strategy.<br>
There is 1 opinion after all iterations.<br>
(2141.0, 1356.0, 2183.0, 192.0, 1889.0, 193.0, 1347.0, 1905.0, 2092.0, 2121.0, 191.0) count: 50<br>









































