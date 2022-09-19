gamma = 0.8
def take_action(current_state, reward_matrix, gamma):
    action = get_action(current_state, reward_matrix)
    current_sa_reward = reward_matrix[current_state, action]
    print(current_sa_reward)
    q_sa_value = max(q_matrix [action, ])
    print(q_sa_value)
    q_current_state = current_sa_reward+(gamma*q_sa_value)
    print (q_current_state)
    q_matrix[current_state, action] = q_current_state
    print("q_matrix", "\n", q_matrix)
    new_state = action









    