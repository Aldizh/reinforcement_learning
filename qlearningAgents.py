from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math
          
class QLearningAgent(ReinforcementAgent):
  """

    Q-Learning Agent
    
    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update
      
    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.gamma (discount rate)
    
    Functions you should use
      - self.getLegalActions(state) 
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)
    self.values = util.Counter()
    
  def getQValue(self, state, action):
    """

      Returns Q(state,action)    
      Should return 0.0 if we never seen
      a state or (state,action) tuple 
    """
    return self.values[(state, action)];
  
    
  def getValue(self, state):
    """
      Returns max_action Q(state,action)        
      where is max is over legal actions
    """
    qValues = []
    for action in self.getLegalActions(state):
        qValues.append(self.getQValue(state, action))
    if len(qValues) == 0:
        return 0.0
    return max(qValues)
    
  def getPolicy(self, state):
    """
    What is the best action to take in a state
    """
    if len(self.getLegalActions(state)) == 0:
        return None
    else:
        bestAction = None
        optimalQVal = -1000
        for action in self.getLegalActions(state):
            if self.getQValue(state, action) > optimalQVal:
                bestAction = action
                optimalQVal = self.getQValue(state, action)
            elif self.getQValue(state, action) == optimalQVal:
                if util.flipCoin(self.epsilon):
                    bestAction = action
        return bestAction

  def getAction(self, state):
    """
      What action to take in the current state. With
      probability self.epsilon, we should take a random
      action and take the best policy action otherwise.
    
      After you choose an action make sure to
      inform your parent self.doAction(state,action) 
      This is done for you, just don't clobber it
       
      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """  
    # Pick Action
    legalActions = self.getLegalActions(state)
    action = None
    if util.flipCoin(self.epsilon):
        action = random.choice(legalActions)
    else:
        action = self.getPolicy(state)
    
    # Need to inform parent of action for Pacman (do not delete this line)
    self.doAction(state,action)    
    
    return action
  
  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a 
      state = action => nextState and reward transition.
      You should do your Q-Value update here
      
      NOTE: You should never call this function,
      it will be called on your behalf
    """
    sample = reward + self.discount * self.getValue(nextState)
    self.values[(state, action)] = (1-self.alpha)*self.values[(state, action)] + self.alpha*sample
    
class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"
  
  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
    
    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    QLearningAgent.__init__(self, **args)
    
class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.
    self.weight = util.Counter()

  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    featureVector = self.featExtractor.getFeatures(state, action)
    QVal = 0.0
    for key in featureVector:
        QVal = QVal + self.weight[key] * featureVector[key]
    return QVal

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    correction = reward + self.discount * self.getValue(nextState) - self.getQValue(state, action)
    featureVector = self.featExtractor.getFeatures(state, action)
    for key in featureVector:
        self.weight[key] = self.weight[key] + self.alpha * correction * featureVector[key]
    
    
  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      "*** YOUR CODE HERE ***"
      pass

