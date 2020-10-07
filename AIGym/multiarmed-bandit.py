import numpy as np
import tensorflow as tf


class MultiArmedBandit:

    def __init__(self):
        self.bandit = [0.2, 0.0, 0.1, -4.0]
        self.num_actions = 4

    def pull(self, arm):
        return 1 if np.random.randn(1) > self.bandit[arm] else -1


class Agent:

    def __init__(self, actions=4):
        self.num_actions = actions
        self.reward_in = tf.placeholder(tf.float32, [1], name='reward_in')
        self.action_in = tf.placeholder(tf.int32, [1], name='action_in')

        self.W = tf.get_variable('W', [self.num_actions])
        self.best_action = tf.argmax(self.W, axis=0)

        action_weight = tf.slice(self.W, self.action_in, [1])
        policy_loss = -(tf.log(action_weight) * self.reward_in)
        self.optimizer = tf.train.AdamOptimizer(
            learning_rate=1e-3).minimize(policy_loss)

    def predict(self, sess):
        return sess.run(self.best_action)

    def random_or_predict(self, sess, epsilon):
        if np.random.rand(1) < epsilon:
            return np.random.randint(self.num_actions)
        else:
            return self.predict(sess)

    def train(self, sess, action, reward):
        sess.run(self.optimizer, {
            self.action_in: [action],
            self.reward_in: [reward]
            })


env = MultiArmedBandit()
agent = Agent()
num_episodes = 50000
EPSILON = 0.1

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(num_episodes):
        action = agent.random_or_predict(sess, EPSILON)
        reward = env.pull(action)
        agent.train(sess, action, reward)
    
    # results time
    print(np.argmin(np.array(env.bandit)))
    print(agent.predict(sess))
        