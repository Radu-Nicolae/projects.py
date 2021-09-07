from samples import madlibs1, madlibs2, madlibs3
import random

print(
'''
 _______ _______ ______         _____ ______  _______
 |  |  | |_____| |     \ |        |   |_____] |______
 |  |  | |     | |_____/ |_____ __|__ |_____] ______|
                                                     
'''
)

if __name__ == "__main__":
    m = random.choice([madlibs1, madlibs2, madlibs3])
    m.madlib()

