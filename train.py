import gym

env = gym.make('Breakout-ram-v0').unwrapped
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(env.render())