import numpy as np
import random

num_actions = 4
num_rows = 4
num_columns = 5
lr=0.2
gamma=0.8
q_table = np.zeros((num_rows * num_columns, num_actions))
r_table = [-8, -8, -8, -8, -8, -8, 0, 0, 0, 8, -8, 0, 0, 0, -8, -8, -8, -8, -8, -8]
start = 11
end = 9
epsilon = 0.1

episode = 0
while(episode != 3000):
    state = start
    while(state != end):
        flag = 1
        if random.uniform(0, 1) < epsilon:
            """ Explore: select a random action    """
            while(flag == 1):
                action = random.randint(0,4)
                if (action == 1):
                    if (state+5 in range(20)):
                        next_state = state + 5
                        flag = 0
                    else:
                        flag = 1
                if (action == 0):
                    if (state - 5 in range(20)):
                        next_state = state - 5
                        flag = 0
                    else:
                        flag = 1
                if (action == 2):
                    if (state+1 in range(20)):
                        next_state = state + 1
                        flag = 0
                    else:
                        flag = 1
                if (action == 3):
                    if (state-1 in range(20)):
                        next_state = state - 1
                        flag = 0
                    else:
                        flag = 1




        else:
            """ Exploit: select the action with max value (future reward)    """
            max_reward=-10000
            if((state+1 in range(20)) and r_table[state+1]>max_reward):
                max_reward= r_table[state+1]
                action=2
                next_state=state+1
            if((state-1 in range(20)) and r_table[state-1] > max_reward):
                max_reward= r_table[state-1]
                action =3
                next_state=state-1
            if((state-5 in range(20)) and r_table[state-5] > max_reward):
                max_reward= r_table[state-5]
                action =0
                next_state=state-5
            if((state+5 in range(20)) and r_table[state+5] > max_reward):
                max_reward= r_table[state+5]
                action =1
                next_state=state+5
        q_table[state, action] = q_table[state, action] + lr * (r_table[next_state] + gamma * np.max(q_table[next_state, :]) - q_table[state, action])
        state = next_state
    episode += 1
print(" up          down        right       left")
print(q_table)
print("Optimal Pathes from A to B:")
print("1- Up, Right, Right, Right")
print("2- Right, Right, Up, Right")
