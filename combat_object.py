

class CombatObject(object):
	def __init__(self, statsDictionary):
		self.__stats = statsDictionary
		self.hp = self.__stats["hpMax"]

	def setStat(self, name, value):
		if name in self.__stats:
			self.__stats[name] = value
		else:
			raise KeyError("No key " + name + " in __stats.")

	def damage(self, attackPower):
		self.hp -= attackPower
		return isDead()

	def isDead():
		if self.hp <= 0:
			return True
		return False