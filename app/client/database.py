from pymongo import MongoClient
from pprint import pprint

class Database:
  def __init__(self, host, port, username, password):
    self.host = host
    self.port = port
    self.username = username
    self.password = password

    try:
      # client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/?readPreference=primary')
      client = MongoClient('mongodb://localhost:27017/?readPreference=primary&ssl=false')
      self.db = client.gelatinous
    except Exception as e:
      pprint(f'Something happened connecting to mongo: {e}')

  def get_server_status(self):
    # Issue the serverStatus command and print the results
    if self.db is not None:
      serverStatusResult = self.db.admin.command("serverStatus")
      pprint(serverStatusResult)
  
  def get_enemy_by_id(self, id):
    return self.db.enemy.find_one({"_id": id})

  def get_weapon_by_id(self, id):
    return self.db.weapon.find_one({"_id": id})
  
  def get_armor_by_id(self, id):
    return self.db.armor.find_one({"_id": id})
  
  def get_character_class_by_id(self, id):
    return self.db.character_class.find_one({"_id": id})
  
