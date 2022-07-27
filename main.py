"""
An example for the Decoded.AI preview.
"""

import time

from typing import Any

def get_obs():
    """
    Returns some observations
    """
    # a short story about the world as seen by the AI
    return "The world is a big red square with a big red circle inside it. But you wouldn't know that because they are both red and you are not a computer." 

def get_model() -> Any:
    """
    Returns a model of the universe.
    """
    return "21309123123019"

def get_env():
    """
    Returns an environment
    """
    return get_obs()

def train_step(model: Any, env: Any):
    """
    Trains the model for one step
    """
    time.sleep(1)
    return model + env

def other_train_loop(model: Any, i: int, env: Any):
    """
    Train the model for i episodes. If the environment is solved/failed before the ith episode, 
    then it is reset and the agent continues until the ith episode.
    """
    for _i in range(i):
        train_step(model, env)

def train_loop(model: Any, i: int, env: Any):
    """
    Train the model for i episodes. If the environment is solved/failed before the ith episode, 
    then it is reset and the agent continues until the ith episode.
    """
    for _i in range(i):
        train_step(model, env)

def main():
    """
    Entrypoint for the program
    """
    train_loop(get_model(), 5, get_env())
    other_train_loop(get_model(), 5, get_env())

if __name__ == '__main__':
    main()
