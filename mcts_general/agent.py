from mcts_general.config import MCTSAgentConfig, MCTSContinuousAgentConfig
from mcts_general.game import DeepCopyableGame
from mcts_general.mcts import MCTS, select_action, ContinuousMCTS


class MCTSAgent:

    def __init__(self, config: MCTSAgentConfig):
        self.config = config
        self.mcts = MCTS(self.config)
        self.result_node = None

    def step(self, game_state: DeepCopyableGame, observations, reward, done, output_info=False):
        self.result_node, info = self.mcts.run(
            observation=observations,
            reward=reward,
            game=game_state,
            add_exploration_noise=False,
            override_root_with=self.result_node if self.config.reuse_tree else None,
            done=done
        )
        action = select_action(self.result_node, temperature=self.config.temperature)
        return action, info if output_info else action


class ContinuousMCTSAgent(MCTSAgent):

    def __init__(self, config: MCTSContinuousAgentConfig):
        super(ContinuousMCTSAgent, self).__init__(config)
        self.mcts = ContinuousMCTS(config)
