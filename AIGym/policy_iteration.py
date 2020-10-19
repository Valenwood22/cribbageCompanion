# Policy Iteration (using Iterative Policy Evaluation)
# Sutton and Barto, Chapter 4.3

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


def policy_iteration(policy, env):
    num_states = env.nS
    num_actions = env.nA
    transitions = env.P

    policy_stable = True

    while policy_stable:
        # step 2: policy evaluation
        V = policy_evaluation(policy, env)
        # for each s in S:
        for state in range(num_states):
            # old_action = pi_s
            old_action = np.argmax(policy[state])
            # update rule is: pi_s = argmax_a(sum(p(s',r|s,a) * [r + gamma * V(s')]))
            new_action_values = np.zeros(num_actions)
            for action in range(num_actions):
                for probability, nextstate, reward, _ in transitions[state][action]:
                    new_action_values[action] += probability * (reward + GAMMA * V[nextstate])
            new_action = np.argmax(new_action_values)
            # update policy: policy[state] is pi_s
            # if policy_stable, then stop and return optimal policies and value, else go to step 2
            policy_stable = (new_action == old_action)
            policy[state] = np.eye(num_actions)[new_action]
        
        # If the policy is stable we've found an optimal policy. Return it
        if policy_stable:
            return policy, V


env = gym.make('GridWorld-v0').unwrapped
random_policy = np.ones([env.nS, env.nA]) * 0.25
v_k = policy_evaluation(random_policy, env)
print(v_k.reshape(env.shape))

optimal_policy, optimal_value = policy_iteration(random_policy, env)
print(optimal_policy)
