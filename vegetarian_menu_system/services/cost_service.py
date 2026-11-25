import math
def suggested_price(cost, ratio):
    return math.ceil(cost / ratio / 5) * 5
