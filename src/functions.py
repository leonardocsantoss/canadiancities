import pandas as pd
import random

"""
This is the "Canadian Cities" module.

The example module supplies functions to calculate properties from Canadian Cities.  
For example, Life Quality, Cost of Living, Environmental Factors and Lifestyle.
"""


def normalize(index: str, df: pd.core.frame.DataFrame):
    """
        Return normalized values ​​using the extremes of the scale.

    :param index:
    :param df:
    :return:
    """
    result = df.copy()
    max_value = df[index].max()
    min_value = df[index].min()
    result[index] = (df[index] - min_value) / (max_value - min_value)
    return result


def quality(city: str, df: pd.core.frame.DataFrame):
    """
        Return the Quality of Life for the City, an exact float in [0,1].

        The calculation of the Human Development Index (HDI) is produced from
        three main aspects of the population: income, education and health.

    :param city:
    :param df:
    :return:
    """

    # Normalize df
    normalized_df = normalize('Quality of Life Index', df)

    city_row = normalized_df[(normalized_df.City == city)]

    return city_row['Quality of Life Index'].values


def cost(city: str, df: pd.core.frame.DataFrame):
    """
         Return the Cost of Living for the City, an exact float in [0,1].

    :param city:
    :param df:
    :return:
    """

    city_row = df[(df.City == city)]
    cost_value = random.uniform(0, 1)

    return cost_value


def environment(city: str, df: pd.core.frame.DataFrame):
    """
        Return the Environmental Factors for the City, an exact float in [0,1].

    :param city:
    :param df:
    :return:
    """

    city_row = df[(df.City == city)]
    env_value = random.uniform(0, 1)

    return env_value


def lifestyle(city: str, df: pd.core.frame.DataFrame):
    """
        Return the Lifestyle for the City, an exact float in [0,1].

        The calculation of the Life Style is produced from a mean of
        two aspects: Traffic Index and Climate Inedex.

        Traffic Index is a composite index of time consumed in traffic
        due to job commute, estimation of time consumption dissatisfaction,
        CO2 consumption estimation in traffic and overall inefficiencies
        in the traffic system.

        Climate Index is an estimation of the climate likability of a given 
        city or a country. It is in the range [-100, +100] (higher is better). 
        Cities with climate index 100 have moderate temperatures and low 
        humidity and no other major weather condition which is usually not 
        preferred by most people. However, some persons prefer colder 
        climate while others prefer warmer climates and some people are 
        fine with humid conditions, so this index is general guidance, 
        which shall not be blindly considered.

    :param city:
    :param df:
    :return:
    """

    # Normalize df
    normalized_df = normalize('Traffic Index', df)
    normalized_df = normalize('Climate Index', normalized_df)

    city_row = normalized_df[(normalized_df.City == city)]

    style_value = (city_row['Traffic Index'].values+city_row['Climate Index'].values)/2

    return style_value
