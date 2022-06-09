import pymongo
import pickle
import discord

class wordleServer:
  def __init__(self)
    self.client = MongoClient()
    self.db = client["wordle-server"]

  def make_new_wordle_guild(self, guild)
    new_guild = {"guild": guild.name, "current_winners": [], "old_winners": [], "users": [], "todays_high": 7}
    self.db.guilds.insert_one(new_guild)

  def add_new_wordler(self, guild, member)
    to_add = new WordleUser([member, 0, 7, 0, []])
    self.db.guilds.update_one({"guild": guild.name}, {'$push': {"users": pickle.dumps(to_add)})
    del(to_add)

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
    if(self.all_scores == []):
      try:
        return self.user.nick + " has no scores yet!  Play some wordle first! :)"
      except TypeError:
        return self.user.name + " has no scores yet!  Play some wordle first! :)"
    else:
      try:
        return self.user.nick + " has a high score of " + str(self.high_score) + ", an average scor
      except TypeError:
        return self.user.name + " has a high score of " + str(self.high_score) + ", an average scor

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

