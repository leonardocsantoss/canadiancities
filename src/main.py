
from src.functions import quality
from src.functions import cost
from src.functions import environment
from src.functions import lifestyle
import pandas as pd


def main():
    """
        Prints "Canadian Cities!" to the display. And call the lifeQuality function.
    """

    data = pd.read_csv("../data/numeo.csv")

    print("Canadian Cities!\n")

    print("Quality of Life:")
    quality_value = quality(data.City[0], data)
    print(quality_value)
    print()

    print("Cost of Living:")
    cost_value = cost(data.City[0], data)
    print(cost_value)
    print()

    print("Environmental Factors")
    env_value = environment(data.City[0], data)
    print(env_value)
    print()

    print("Lifestyle")
    style_value = lifestyle(data.City[0], data)
    print(style_value)
    print()

    print("End Test!!!")

main()
