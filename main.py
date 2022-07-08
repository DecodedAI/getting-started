"""
An example for the Decoded.AI preview.
"""

from typing import Any, Callable

def get_obs():
    """
    Returns some observations
    """
    # a short story about the world as seen by the AI
    return "The world is a big red square with a big red circle inside it. But you wouldn't know that because they are both red and you are not a computer." 

def get_model() -> Callable[..., Any]:
    """
    Returns a model of the universe.
    """
    return lambda obs: "Journal entry:" + obs

def get_env():
    """
    Returns an environment
    """
    return lambda: get_obs()

def train_step(model: Callable[..., Any], env: Callable[..., str]):
    """
    Trains the model for one step
    """
    model(
        env()
    )

def other_train_loop(model: Callable[..., Any], i: int, env: Any):
    """
    Train the model for i episodes. If the environment is solved/failed before the ith episode, 
    then it is reset and the agent continues until the ith episode.
    """
    for _i in range(i):
        train_step(model, env)

def train_loop(model: Callable[..., Any], i: int, env: Any):
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
    train_loop(get_model(), 2000, get_env())
    other_train_loop(get_model(), 2000, get_env())

if __name__ == '__main__':
    main()
    #! decoded export: decoded_logs
