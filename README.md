# Monte Carlo Tree Search for OpenAI gym framework

General Python implementation of Monte Carlo Tree Search for the use with Open AI Gym environments.

The MCTS Algorithm is based on the one from [muzero-general](https://github.com/PatrickKorus/muzero-general) which is 
forked from [here](https://github.com/werner-duvaud/muzero-general).

This code was part of my Bachelor Thesis:

#### [An Evaluation of MCTS Methods for Continuous Control Tasks](https://www.dropbox.com/s/9acbtihfmagn7el/Bachelor_Thesis___An_Evaluation_of_MCTS_Methods_for_Continuous_Control_Tasks_FINAL.pdf?dl=0) 

The source code of the experiments covered by the thesis can be found [here](https://github.com/PatrickKorus/MCTSOC).

## Dependencies

Python 3.8 is used. Dependencies are mainly numpy and gym. Simply run:

```shell script
pip install -r requirements.txt
```

## How to use

This implementation follows the common agent-environment scheme. The environment is Wrapped by the Game class defined,
in `game.py`, which ensures that the game's state can be deep copied. The main Game implementations for usage with 
OpenAI gym environments are `DiscreteGymGame` and `ContinuousGymGame`. 

A simple example would be:

```python
import gymnasium as gym
from mcts_general.agent import MCTSAgent
from mcts_general.config import MCTSAgentConfig
from mcts_general.game import DiscreteGymGame


# configure agent
config = MCTSAgentConfig()
config.num_simulations = 200
agent = MCTSAgent(config)

# init game
env=gym.make('CartPole-v0')
game = DiscreteGymGame(env=gym.make('CartPole-v0'))
state=env.reset(seed=0)
state = game.reset(seed=0)
done = False
reward = 0

# run a trajectory
while not done:
    action = agent.step(game, state, reward, done)
    state, reward, done = env.step(action)
    
    # game.render()     # uncomment for environment rendering

game.close()
``` 

