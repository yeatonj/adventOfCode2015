# did not do any real programming to solve this, used algebra

# Equation 1: (p_dmg - b_armor)*(p_turns) >= b_health
# Equation 2: (b_dmg - p_armor)*(p_turns-1) < p_health
# Note that b_dmg, b_armor, b_health, and p_health are constants, allowing quick checking
# and simulation of outcome

import math

# CONSTS
B_HEALTH = 104
P_HEALTH = 100
B_ARMOR = 1
B_DMG = 8

# change
p_dmg = 7 # 108g
p_armor = 2 # 40g

p_turns = math.ceil(B_HEALTH / (p_dmg - B_ARMOR))
print("Player needs " + str(p_turns) + " turns to kill boss.")
if (B_DMG - p_armor) * (p_turns -1) >= P_HEALTH:
    print("Boss kills player")
else:
    print("Player kills boss")
