#simulation.py
#vera


#Init
tortoise_wins = 0
hare_wins = 0
finish_line = 50
tortoise_pos = 0
hare_pos = 0
is_hare_asleep = False
import random
#functions
def main():
    tortoise_wins = 0
    hare_wins = 0
    finish_line = 50
    tortoise_pos = 0
    hare_pos = 0
    is_hare_asleep = False
    for i in range(100000):
        tortoise_pos = 0
        hare_pos = 0
        while tortoise_pos < finish_line and hare_pos < finish_line:
            #Tortoise always moves a short distance between 1 - 3 meters at random
            move  = random.randint(1, 3)
            tortoise_pos = tortoise_pos + move
            #Hare has a 30% chance of falling a sleep for a turn
            chance = random.randint(1,100)
            move_hare = random.randint(1,10)
            if chance > 80:
                hare_pos = hare_pos + move_hare
            elif chance < 80:
                hare_pos = hare_pos
        if tortoise_pos >= finish_line:
            tortoise_wins = tortoise_wins + 1
        else:
            hare_wins = hare_wins + 1
    print(f"🐢 Tortoise Wins: {tortoise_wins}")
    print(f"🐇 Hare Wins: {hare_wins}")
#main
main()
