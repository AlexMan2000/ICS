
import sys
sys.path.append('./lec7')
import random
# import dice_helper

class Dice:
    def __init__(self, sides=2):
        self.n_sides = sides # default 2, like a coin
        self.bounds = [x/sides for x in range(0, sides)] # default[0, 0.5]. bounds[i] give Prob(sides<i)
        self.bounds.append(1.0)
        self.point = None
        self.lands = 0 # int, with 2 sides, could be 0 or 1

    def set_bounds(self, r):
        assert len(r) == len(self.bounds)
        self.bounds = r

    def get_bounds(self):
        return self.bounds

    def roll(self):
# replace the following line with you code
# it should set self.point as a random var in [0, 1]
# return which side the dice lands on
        res = random.uniform(0,1)
        self.point = res
        for i in range(self.n_sides):
            if self.point > self.bounds[i] and self.point <= self.bounds[i+1]:
                return i



if __name__ == "__main__":
    d = Dice()
    ''' make a biased dice '''
    d.set_bounds([0.0, 0.5, 1.0])
    ones = 0
    num_rolls = 1000
    for i in range(num_rolls):
        ones += d.roll()
    print("the dice is:", ones/float(num_rolls))