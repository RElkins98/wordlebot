from redis import Redis
import pickle
import discord
import wordleCast 
from wordleCast import wordleGuild, wordleUser


class wordleServer:
  def __init__(self):
    self.redis_server = Redis(host='localhost', port=6379, decode_responses=True, username="pi", password="TheRealSlimShady")
    

  def is_guild(self, guild):
    return self.redis_server.get(guild.id) is not None

  def is_wordler(self, guild, member):
    our_guild = self.redis_server.get(guild.id)
    if our_guild is None:
      return False
    our_guild = wordleCast.depickle_guild(our_guild)
    return member.id in our_guild.users

  def make_new_wordle_guild(self, guild):
    new_guild = make_new_wordle_guild(guild)
    redis_server.set(guild.id, new_guild.guild_pickle())
    return

  def add_new_wordler(self, guild, member):
    our_guild = self.redis_server.get(guild.id)
    if our_guild is None:
      our_guild = make_new_wordle_guild(guild)
    ret = our_guild.add_user(member)
    if ret:
      self.redis_server.set(guild.id, our_guild.guild_pickle())
    return ret

  def get_wordler(self, guild, member):
    our_guild = self.redis_server.get(guild.id)
    our_guild is None:
      return None
    our_guild = wordleCast.depickle_guild(our_guild)
    if member.id in our_guild.users:
      return our_guild.users[member.id]
    else
      return None

  def get_highest_score(self, guild):
    return wordleCast.depickle_guild(self.redis_server.get(guild.id)).todays_high

  def add_score_to_guild(self, guild, member, message):
    our_guild = self.redis_server.get(guild.id)
    if our_guild is None:
      our_guild = make_new_wordle_guild(guild)
    our_guild.add_score(member, message)
    self.redis_server.set(our_guild.id, our_guild.guild_pickle())
    return
    
  def calculate_winners(self):
    winners = {}
    for guild_id in self.redis_server.keys():
      our_guild = self.redis_server.get(guild_id)
      winners.update(our_guild, [our_guild.users, our_guild.current_winners, self.todays_high])
      our_guild.refresh()
    return winners

  def __del__(self):
    redis_server.close()
