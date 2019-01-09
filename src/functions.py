import pandas as pd
import random

"""
This is the "Canadian Cities" module.

The example module supplies functions to calculate properties from Canadian Cities.  
For example, Life Quality, Cost of Living, Environmental Factors and Lifestyle.
"""


def quality(city: str, data: pd.core.frame.DataFrame):
    """
        Return the Quality of Life for the City, an exact float in [0,1].

        The calculation of the Human Development Index (HDI) is produced from
        three main aspects of the population: income, education and health.

    :param city:
    :param data:
    :return:
    """

    city_row = data[(data.City == city)]

    city_quality = city_row['Quality of Life Index'].values

    quality_max = max(data['Quality of Life Index'].values)
    quality_min = min(data['Quality of Life Index'].values)

    # Normalized values ​​using the extremes of the scale.
    quality_value = (city_quality - quality_min) / (quality_max - quality_min)

    return quality_value


def cost(city: str, data: pd.core.frame.DataFrame):
    """
         Return the Cost of Living for the City, an exact float in [0,1].

    :param city:
    :param data:
    :return:
    """

    city_row = data[(data.City == city)]
    cost_value = random.uniform(0, 1)

    return cost_value


def environment(city: str, data: pd.core.frame.DataFrame):
    """
        Return the Environmental Factors for the City, an exact float in [0,1].

    :param city:
    :param data:
    :return:
    """

    city_row = data[(data.City == city)]
    env_value = random.uniform(0, 1)

    return env_value


def lifestyle(city: str, data: pd.core.frame.DataFrame):
    """
        Return the Lifestyle for the City, an exact float in [0,1].

    :param city:
    :param data:
    :return:
    """

    city_row = data[(data.City == city)]
    style_value = random.uniform(0, 1)

    return style_value
