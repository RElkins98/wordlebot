import discord
import pickle
import json
import re

not_winner = 0
new_winner = 1
already_winner = 2


class wordleUser:
"""
User object, conatins information about the guild member and wordle stats
"""
  def __init__(self, member):
    self.member = member
    self.id = self.member.id
    self.wins = 0
    self.high_score = 7
    self.avg_score = 0
    self.all_scores = []


  def return_user_stats(self):
  """
  Returns wordle stats in the form of [
  """
    try:
      name = self.member.nick
    except TypeError:
      name = self.member.name
    if(self.all_scores == []):
      ret = []
    else:
      ret = [name, self.high_score, self.avg_score, self.wins]
    return ret

  def add_new_score(self, new_score):
  """
  Adds a new score to a user
  """
    self.all_scores.append(new_score)
    scores = 0
    tot_score = 0
    if(new_score < self.high_score):
      self.high_score = new_score
    scores = len(self.all_scores)
    self.avg_score = tot_score/scores
    return

class wordleGuild:
"""
Guild Object, contains information about the current wordle users for the guild and today's high score and winners
"""
  def __init__(self, guild):
    self.guild = guild
    self.current_winners = {}
    self.todays_high = 7
    self.users = {}
    self.id = guild.id
    self.cur_msgs = []
    
  def add_score(member, message):
    if member.id not in self.users:
      member = make_new_user(member)
      self.users.update(member.id: member)
    else:
      member = users[member.id]
    score = int(re.search("\d\/6", message.content).group(0)[0])
    member.add_new_score(score)
    if score == self.todays_high:
      if member.id not in self.current_winners:
        _add_winner(member, message)
    elif score < self.todays_high:
      if member.id not in self.current_winners:
        _new_high_score(member, message)
    else:
      return not_winner
      
  def add_user(self, member):
    if member.id not in self.users:
      member = make_new_user(member)
      self.users.update(member.id: member)
      return True
    else:
      return False
      
  def refresh(self):
    for winner in self.current_winners:
      winner.wins += 1
    self.current_winners = {}
    for msg in self.cur_msgs:
      await msg.clear_reaction("👑")
    self.cur_msgs = []
    self.todays_high = 7
      
  def _new_high_score(self, member, message):
    self.todays_high = score
    self.current_winners = {}
    self.current_winners.update({member.id, member})
    for msg in self.cur_msgs:
      await msg.clear_reaction("👑")
    self.cur_msgs = []
    self.cur_msgs.append("👑")
    
  def _add_winner(self, member, message):
    self.current_winners.update({member.id, member})
    self.cur_msgs.append(message)
    await message.add_reaction("👑")
    
  def check_high_score(self):
    return self.todays_high
  def guild_pickle(self):
    return pickle.dumps(self)
  def is_active_member(self, member):
    return member.id in self.users


def make_new_guild(guild):
  return wordleGuild(guild)
  
def depickle_guild(guild):
  return pickle.loads(guild)
