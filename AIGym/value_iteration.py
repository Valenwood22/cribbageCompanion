# Value Iteration
# Sutton and Barto, Chapter 4.4

import gym
import lib
import numpy as np

GAMMA = 1.0
THETA = 1e-5


def value_iteration(env):
    num_states = env.nS
    num_actions = env.nA
    transitions = env.P
    # initialize array V arbitarily
    V = np.zeros(num_states)
    # repeat
    while True:
        # initialize delta to zero
        delta = 0
        # for each s in S
        for state in range(num_states):
            # v = V(s)
            old_value = V[state]
            new_action_values = np.zeros(num_actions)
            # update rule is: V(s) = max_a(sum(p(s',r|s,a) * [r + gamma * V(s')]))
            for action in range(num_actions):
                for probability, nextstate, reward, _ in transitions[state][action]:
                    new_action_values[action] += probability * (reward + GAMMA * V[nextstate])
            V[state] = np.max(new_action_values)
            # calculate delta = max(delta, |v - V(s)|)
            delta = max(delta, np.abs(V[state] - old_value))
        # until delta is smaller than theta
        if delta < THETA:
            break

    # output a deterministic policy (the optimal one)
    optimal_policy = np.zeros([num_states, num_actions])
    for state in range(num_states):
        action_values = np.zeros(num_actions)
        for action in range(num_actions):
            for probability, nextstate, reward, _ in transitions[state][action]:
                action_values[action] += probability * (reward + GAMMA * V[nextstate])
        optimal_policy[state] = np.eye(num_actions)[np.argmax(action_values)]

    return optimal_policy, V


env = gym.make('GridWorld-v0').unwrapped
optimal_policy, optimal_value = value_iteration(env)

print("Policy Probability Distribution:")
print(optimal_policy)

print("Value Function:")
print(optimal_value.reshape(env.shape))
