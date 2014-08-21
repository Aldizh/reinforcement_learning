######################
# ANALYSIS QUESTIONS #
######################

def question2():
  answerDiscount = 0.9
  answerNoise = 0.01
  return answerDiscount, answerNoise
  
def question3a():
  answerDiscount = 0.9
  answerNoise = .01
  answerLivingReward = -5
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.8
  answerNoise = 0.5
  answerLivingReward = -1.7
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 0.9
  answerNoise = .01
  answerLivingReward = -2
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.8
  answerNoise = 0.5
  answerLivingReward = -1
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 0.5
  answerNoise = 1
  answerLivingReward = -5
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = None
  answerLearningRate = None
  #best option is to stay closer to the beginning so it doesn't end up exploring a whole lot
  return "NOT POSSIBLE"
  # If not possible, return 'NOT POSSIBLE'
  
if __name__ == '__main__':
  print 'Answers to analysis questions:'
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print '  Question %s:\t%s' % (q, str(response))
