# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play,
          opponent_history=[],
          play_order=[{"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0,
              "SR": 0, "SP": 0, "SS": 0,}],
          our_history = []
          ):

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  if not prev_play:
    prev_play = 'R'
  
  opponent_history.append(prev_play) 
  if our_history == []:
    our_history.append("R")
  
  last_two = "".join(our_history[-2:])
  if len(last_two) == 2:
    play_order[0][last_two] += 1
  
  score_R = 0
  score_P = 0
  score_S = 0
  
  def pred_quincy(prev_play, opponent_history):
    if prev_play == "P" and opponent_history[-3:-1] == ["R", "P"]:
      return "S"
    elif prev_play == "S" and opponent_history[-3:-1] == ["P", "P"]:
      return "R"
    elif prev_play == "R" and opponent_history[-3:-1] == ["P", "S"]:
      return "R"
    elif prev_play == "R" and opponent_history[-3:-1] == ["S", "R"]:
      return "P"
    elif prev_play == "P" and opponent_history[-3:-1] == ["R", "R"]:
      return "P"
  
  def pred_mrugesh(prev_play, our_history, ideal_response):
    last_ten = our_history[-10:]

    if last_ten ==[]:
      last_ten = ['R', 'P', 'S']

    max_frequent = max(set(last_ten), key = last_ten.count)
    return ideal_response[max_frequent]
  
  def pred_kris(our_history, ideal_response):
    return ideal_response[our_history[-1]]
  
  def pred_abbey(our_history, play_order, ideal_response):
    potential_plays = [
        our_history[-1] + "R",
        our_history[-1] + "P",
        our_history[-1] + "S",
    ]

    sub_order = {
          k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
      }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    return ideal_response[prediction]

  options = ["R", "P", "S"]
  next_opp_turns = [pred_quincy(prev_play, opponent_history),
                    pred_mrugesh(prev_play, our_history, ideal_response),
                    pred_kris(our_history, ideal_response),
                    pred_abbey(our_history, play_order, ideal_response)]

  for opt in options:
    for opp in next_opp_turns:
      if opt == "R":
        if opp == "P":
          score_R -= 1
        elif opp == "S":
          score_R += 1
      elif opt == "P":
        if opp == "R":
          score_P += 1
        elif opp == "S":
          score_P -= 1
      elif opt == "S":
        if opp == "P":
          score_S += 1
        elif opp == "R":
          score_S -= 1
  
  options_dict = dict()
  options_dict["R"] = score_R
  options_dict["P"] = score_P
  options_dict["S"] = score_S
  
  guess = max(options_dict, key=options_dict.get)
  our_history.append(guess)
  return guess


