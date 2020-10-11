# Iterative Policy Evaluation

import gym
import lib
import numpy as np

GAMMA = 1.0
THETA = 1e-5


def policy_evaluation(policy, env):
    num_states = env.nS
    num_actions = env.nA
    transitions = env.P
    # initialize an array V(s) = 0, for all s in S+
    V = np.array(np.zeros(num_states))
    # repeat
    while True:
        # delta = 0
        delta = 0
        # for each s in S:
        for state in range(num_states):
            # v = V(s)
            new_value = 0
            # update rule is: V(s) = sum(pi(a|s) * sum(p(s, a) * [r + gamma * V(s')]))
            # sum over a
            for action, p_action in enumerate(policy[state]):
                # sum over s', r
                for probability, nextstate, reward, _ in transitions[state][action]:
                    new_value += p_action * probability * (reward + GAMMA * V[nextstate])
            # delta = max(delta, abs(v - V(s)))
            delta = max(delta, np.abs(new_value - V[state]))
            V[state] = new_value
        # until delta < theta
        if delta < THETA:
            break
    # return V ~ v_pi
    return V

env = gym.make('GridWorld-v0').unwrapped
random_policy = np.ones([env.nS, env.nA]) * 0.25
v_k = policy_evaluation(random_policy, env)
print(v_k.reshape(env.shape))
