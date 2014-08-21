import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
    states = self.mdp.getStates()
    updated_util = util.Counter()
    for _ in range(self.iterations):
        for state in states:
            actions = self.mdp.getPossibleActions(state)
            utilitiesList = []
            for action in actions:
                transitionStates = self.mdp.getTransitionStatesAndProbs(state, action)
                totalSum = 0
                for (nextState, probNextState) in transitionStates:
                    """Callculate the possible utilities for each of the following states"""
                    totalSum = totalSum + probNextState * (self.mdp.getReward(state, action, nextState) + self.discount * self.values[nextState])
                utilitiesList.append(totalSum)
                if not self.mdp.isTerminal(state):
                    updated_util[state] = max(utilitiesList)
            newStateDict = updated_util.keys()
        for s in newStateDict:
            newValue = updated_util[s]
            self.values[s] = newValue
            
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    transitionStates = self.mdp.getTransitionStatesAndProbs(state, action)
    totalSum = 0
    for (nextState, probNextState) in transitionStates:
            totalSum = totalSum + probNextState * (self.mdp.getReward(state, action, nextState) + self.discount * self.values[nextState])
    return totalSum

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.
    """
    Actions = []
    if self.mdp.isTerminal(state):
        return
    for action in self.mdp.getPossibleActions(state):
        Actions.append(self.getQValue(state, action))
    "Return the action with the maximum Qvalue"
    return self.mdp.getPossibleActions(state)[Actions.index(max(Actions))]

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  