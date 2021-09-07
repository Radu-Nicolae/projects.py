from samples import madlibs1, madlibs2, madlibs3
import random

if __name__ == "__main__":
    m = random.choice([madlibs1, madlibs2, madlibs3])
    m.madlib()

