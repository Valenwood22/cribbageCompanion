import tensorflow as tf
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
    # implement this!

random_search()