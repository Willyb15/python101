import zombie_class
# from hero import Hero
import hero

zombie0 = zombie_class.Zombie('basic',5,12,'axe',23,9)
print zombie0.speed
hero1 = hero.Hero()
# print dir(hero1)
for key in dir(hero1):
	if not key.startswith('__'):
		print key
print hero1.name
hero.cheer()