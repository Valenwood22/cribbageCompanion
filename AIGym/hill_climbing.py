#import tensorflow as tf
import numpy as np
import gym
import logging

logger = logging.getLogger('rl')
logger.setLevel(logging.DEBUG)


class Harness:

    def run_episode(self, env, agent):
        observation = env.reset()
        total_reward = 0
        for _ in range(1000):
            action = agent.next_action(observation)
            observation, reward, done, info = env.step(action)
            total_reward += reward
            if done:
                break
        return total_reward


class LinearAgent:

    def __init__(self):
        self.parameters = np.random.rand(4) * 2 - 1

    def next_action(self, observation):
        return 0 if np.matmul(self.parameters, observation) < 0 else 1


def random_search():
    env = gym.make('CartPole-v0')
    best_params = None
    best_reward = 0
    agent = LinearAgent()
    harness = Harness()

    for step in range(10000):
        agent.parameters = np.random.rand(4) * 2 - 1
        reward = harness.run_episode(env, agent)
        if reward > best_reward:
            best_reward = reward
            best_params = agent.parameters
            if reward == 200:
                print('200 achieved on step {}'.format(step))

    print(best_params)


def hill_climbing():
    env = gym.make('CartPole-v0')
    noise_scaling = 0.1
    best_reward = 0
    reward = 0
    agent = LinearAgent()
    harness = Harness()

    for step in range(10000):
        old_params = agent.parameters # save the old parameters
        agent.parameters += noise_scaling * (np.random.rand(4) * 2 - 1) # add some noise to the new parameters
        run = harness.run_episode(env, agent) # run again
        if run > best_reward:
            best_reward = run # if the new parameters are better use them instead
            print('Step: {}, New Record: {}, Policy: {}'.format(step, best_reward, agent.parameters))
        else:
            agent.parameters = old_params # if they are not better try the old parameters

        if reward == 200:
            break


hill_climbing()