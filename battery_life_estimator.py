"""
Script for importing data, and calculating energy consumption and battery-lifetime

Author: Rohit Kulkarni
Date: August 11th, 2023

"""
# import libraries
import pandas as pd
import logging
import numpy

logging.basicConfig(
    filename="battery_life_estimator_results.log", 
    level=logging.INFO,
    filemode='w+',
    format='%(name)s - %(levelname)s - %(message)s',
    force=True)


def import_data(pth):
    """
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            dataframe: pandas dataframe
    """
    dataframe = pd.read_csv(pth)
    dataframe.columns = ['Timestamp', 'Current(A)']

    return dataframe


def calc_power(dataframe):
    """
    returns dataframe with added column for time interval calculated in hours from UTC timestamp and Power column in Ampere hours

    input:
            dataframe: dataframe containing UTC timestamp and current consumption in Amperes
    output:
            dataframe: pandas dataframe with new column for time interval and power consumed in ampere hours
    """
    #assuming the timestamp has a precision of nanoseconds
    dataframe['time_interval_hours'] = (dataframe['Timestamp'] - dataframe['Timestamp'].shift(1)) / 1e9 / 3600.0
    dataframe['Power-Ah'] = dataframe['Current(A)'] * dataframe['time_interval_hours']

    return dataframe


def calc_battery_life(dataframe, batt_capacity):
    """
    returns battery life,
    input:
            dataframe: dataframe containing current consumed, power consumed in Ampere hours, and battery capacity in mAh
    output:
            dataframe: expected battery life in hours
    """
    max_current = dataframe['Current(A)'].abs().max()
    min_current = dataframe['Current(A)'].abs().min()
    logging.info("Maximum current drawn in Amperes by device is: %f", max_current)
    logging.info("Minimum current drawn in Amperes by device is: %f", min_current)


    # Calculating time interval for total energy consumption 
    time_interval = (dataframe['Timestamp'].max() - dataframe['Timestamp'].min()) / 1e9 / 3600.0

    if time_interval <= 0.0:
        logging.warning("Time interval is zero or negative, cannot calculate battery life.")
        return None
    # Calculating total energy consumed in mAh per hour
    total_energy = (dataframe['Power-Ah'].sum()) * 1000.0 / time_interval
    logging.info("Total Energy Consumed in mAh: %f", total_energy)

    # Calculating expected battery life in hours by dividing battery capacity (assumed) in mAh by total energy
    # consumed in mAh per hour
    battery_life = batt_capacity / total_energy
    logging.info("Expected Battery life in hours is: %f", battery_life)

    return battery_life


if __name__ == "__main__":
    df = import_data("./data/sampleData.csv")
    df_power = calc_power(df)
    batt_cap = 1000.0  # battery capacity assumed 1000 mAh
    exp_batt_life = calc_battery_life(df_power, batt_cap)
