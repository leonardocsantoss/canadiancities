
import pandas as pd

from functions import quality, cost, environment, lifestyle


def main():
    """
        Prints "Canadian Cities!" to the display. And call the lifeQuality function.
    """

    df = pd.read_csv("../data/numeo.csv")

    print("Canadian Cities!\n")

    print("Quality of Life:")
    quality_value = quality(df.City[0], df)
    print(quality_value)
    print()

    print("Cost of Living:")
    cost_value = cost(df.City[0], df)
    print(cost_value)
    print()

    print("Environmental Factors")
    env_value = environment(df.City[0], df)
    print(env_value)
    print()

    print("Lifestyle")
    style_value = lifestyle(df.City[0], df)
    print(style_value)
    print()

    print("End Test!!!")


main()
