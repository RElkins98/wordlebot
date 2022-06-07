import pymongo
import pickle

class wordleServer:
  def __init__(self, server_name)
    self.client = MongoClient()
    self.db = client[server_name]

  def __del__(self):
    self.db.close()

class wordleUser:
  def __init__(self, info):
    self.user = info[0]
    self.wins = int(info[1])
    self.high_score = int(info[2])
    self.avg_score = float(info[3])
    self.all_scores = info[4]

  def print_user_stats(self):
    try:
      return self.user + " has a high score of " + str(self.high_score) + ", an average scor$
    except TypeError:
      return self.user + " has a high score of " + str(self.high_score) + ", an average scor$

  def add_new_score(self, new_score):
    self.all_scores.append(new_score)
    scores = 0
    tot_score = 0
    if(new_score < self.high_score):
      self.high_score = new_score
    for score in self.all_scores:
      tot_score += score
      scores += 1
    self.avg_score = tot_score/scores

  def return_user_list(self):
    return [self.user, self.wins, self.high_score, self.avg_score, self.all_scores]

