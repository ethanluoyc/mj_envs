import gym
import pytest
import mj_envs

@pytest.mark.parametrize("env_name", [
    "door-v0",
    "door-binary-v0",
    "door-sparse-v0",
    'hammer-v0',
    "hammer-binary-v0",
    "hammer-sparse-v0",
    'relocate-v0',
    "relocate-binary-v0",
    "relocate-sparse-v0",
    'pen-v0',
    'pen-binary-v0',
    'pen-sparse-v0',
])
def test_eval(env_name):
    env = gym.make(env_name)
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())
