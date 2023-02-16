# Program for fighting wizards
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/14/2023

import heapq

# Spell constants
MM_CST = 53
MM_DMG = 4
DR_CST = 73
DR_DMG = 2
SH_CST = 113
SH_ARM = 7
SH_TNS = 6
PO_CST = 173
PO_DMG = 3
PO_TNS = 6
RC_CST = 229
RC_RNW = 101
RC_TNS = 5

# Constants for the player/boss starting stats
P_HP = 50
P_MANA = 500
B_HP = 71
B_DMG = 10

#--------------------- Function Definitions---------------
# On each player turn, can choose not to cast or cast any of the 5 spells
def min_mana_boss_kill(p_state, b_state):
    # Create the initial state tuple
    init_state = create_state_str(p_state, b_state, 0)
    p_queue = [(0, id(init_state), init_state, p_state, b_state, [])]
    # Create the priority queue
    heapq.heapify(p_queue)
    # Create the set of visited locations
    searched_set = set()
    # Set first turn flag
    f_turn = True
    # While the priority queue still has elements in it
    curr_min_boss_hp = 100
    while (len(p_queue) > 0):
        # Pop the first element off the priority queue
        first_el = heapq.heappop(p_queue)
        mana_spent = first_el[0]
        state = first_el[2]
        curr_p_state = first_el[3]
        curr_b_state = first_el[4]
        turn_guide = first_el[5]

        if curr_b_state.get("hp") < curr_min_boss_hp:
            curr_min_boss_hp = curr_b_state.get("hp")
        # If we have already visited it, skip this iteration, otherwise, add it
        if state in searched_set:
            continue
        else:
            searched_set.add(state)
        # If we killed the boss, return the answer
        if curr_b_state.get("hp") <= 0:
            return mana_spent
        # Perform a boss turn (after 1st turn), followed by applying effects for player's turn
        # This is OK because we will check player health first and player can't die on their turn
        if not f_turn:
            boss_turn(curr_p_state, curr_b_state)
        else:
            f_turn = False
        if curr_b_state.get("hp") <= 0:
            return mana_spent

        # Hard mode, comment out for pt1
        curr_p_state.update({"hp":curr_p_state.get("hp") - 1})
        if curr_p_state.get("hp") <= 0:
            continue

        apply_effects(curr_p_state,curr_b_state)
        # If the boss killed us, skip this iteration
        if curr_p_state.get("hp") <= 0:
            continue
        # Elif we killed the boss, return the mana spent
        elif curr_b_state.get("hp") <= 0:
            return mana_spent
        # Generate new states for each possibility and add to the priority queue
        # Cast MM
        if curr_p_state.get("mana") > MM_CST:
            mm_p = curr_p_state.copy()
            mm_b = curr_b_state.copy()
            cast_mm(mm_p, mm_b)
            mm_mana = mana_spent + MM_CST
            state = create_state_str(mm_p, mm_b, mm_mana)
            mm_turn = turn_guide.copy()
            mm_turn.append(("MM", state))
            heapq.heappush(p_queue, (mm_mana, id(state), state, mm_p, mm_b, mm_turn))
        # Cast Drain
        if curr_p_state.get("mana") > DR_CST:
            dr_p = curr_p_state.copy()
            dr_b = curr_b_state.copy()
            cast_drain(dr_p, dr_b)
            dr_mana = mana_spent + DR_CST
            state = create_state_str(dr_p, dr_b, dr_mana)
            dr_turn = turn_guide.copy()
            dr_turn.append(("DR", state))
            heapq.heappush(p_queue, (dr_mana, id(state), state, dr_p, dr_b, dr_turn))
        # Cast Shield
        if curr_p_state.get("mana") > SH_CST and curr_p_state.get("sh_rem") == 0:
            sh_p = curr_p_state.copy()
            sh_b = curr_b_state.copy()
            cast_shield(sh_p)
            sh_mana = mana_spent + SH_CST
            state = create_state_str(sh_p, sh_b, sh_mana)
            sh_turn = turn_guide.copy()
            sh_turn.append(("SH", state))
            heapq.heappush(p_queue, (sh_mana, id(state), state, sh_p, sh_b, sh_turn))
        # Cast Poison
        if curr_p_state.get("mana") > PO_CST and curr_b_state.get("po_rem") == 0:
            po_p = curr_p_state.copy()
            po_b = curr_b_state.copy()
            cast_poison(po_p, po_b)
            po_mana = mana_spent + PO_CST
            state = create_state_str(po_p, po_b, po_mana)
            po_turn = turn_guide.copy()
            po_turn.append(("PO", state))
            heapq.heappush(p_queue, (po_mana, id(state), state, po_p, po_b, po_turn))
        # Cast Recharge
        if curr_p_state.get("mana") > RC_CST and curr_p_state.get("rc_rem") == 0:
            rc_p = curr_p_state.copy()
            rc_b = curr_b_state.copy()
            cast_recharge(rc_p)
            rc_mana = mana_spent + RC_CST
            state = create_state_str(rc_p, rc_b, rc_mana)
            rc_turn = turn_guide.copy()
            rc_turn.append(("RC", state))
            heapq.heappush(p_queue, (rc_mana, id(state), state, rc_p, rc_b, rc_turn))
    return False

def apply_effects(p_state, b_state):
    if p_state.get("sh_rem") > 0:
        p_state.update({"armor":SH_ARM})
        p_state.update({"sh_rem":p_state.get("sh_rem") - 1})
    else:
        p_state.update({"armor":0})
    if p_state.get("rc_rem") > 0:
        p_state.update({"mana":p_state.get("mana") + RC_RNW})
        p_state.update({"rc_rem":p_state.get("rc_rem") - 1})
    if b_state.get("po_rem") > 0:
        b_state.update({"hp":b_state.get("hp") - PO_DMG})
        b_state.update({"po_rem":b_state.get("po_rem") - 1})

def create_state_str(p_state,b_state,m_spent):
    p_hp = p_state.get("hp")
    p_ma = p_state.get("mana")
    p_sh = p_state.get("sh_rem")
    p_rc = p_state.get("rc_rem")
    b_hp = b_state.get("hp")
    b_po = b_state.get("po_rem")
    return (p_hp, p_ma, p_sh, p_rc, m_spent, b_hp, b_po)

def cast_mm(p_state, b_state):
    p_state.update({"mana":p_state.get("mana") - MM_CST})
    b_state.update({"hp":b_state.get("hp") - MM_DMG})

def cast_drain(p_state, b_state):
    p_state.update({"mana":p_state.get("mana") - DR_CST})
    p_state.update({"hp":p_state.get("hp") + DR_DMG})
    b_state.update({"hp":b_state.get("hp") - DR_DMG})

def cast_shield(p_state):
    p_state.update({"mana":p_state.get("mana") - SH_CST})
    p_state.update({"sh_rem":SH_TNS})

def cast_poison(p_state, b_state):
    p_state.update({"mana":p_state.get("mana") - PO_CST})
    b_state.update({"po_rem":PO_TNS})

def cast_recharge(p_state):
    p_state.update({"mana":p_state.get("mana") - RC_CST})
    p_state.update({"rc_rem":RC_TNS})

def boss_turn(p_state, b_state):
    # Apply effects
    apply_effects(p_state, b_state)
    # If boss dies, boss cannot attack
    if (b_state.get("hp") <= 0):
        return
    # Otherwise, it attacks
    dmg_dealt = B_DMG - p_state.get("armor")
    p_state.update({"hp":p_state.get("hp") - dmg_dealt})
        
    

# ------------------- Main Program -----------------------

# Set initial states
boss_state = {"hp":B_HP, "dmg":B_DMG, "po_rem":0}
player_state = {"hp":P_HP, "armor":0, "mana":P_MANA, "sh_rem":0, "rc_rem":0}

# print(create_state_str(player_state,boss_state,0))

soln = min_mana_boss_kill(player_state, boss_state)
print(soln)
# Answer of 1263 is too low
# Answer of 1800 also too low
