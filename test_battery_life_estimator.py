import logging
import pytest
import pandas as pd
import numpy
from battery_life_estimator import import_data, calc_battery_life, calc_power

logging.basicConfig(
    filename="test_battery_life_estimator.log", 
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    force=True)


@pytest.fixture
def sample_data_path():
    return "./data/sampleData.csv"


def test_import_data_returns_dataframe(sample_data_path):
    try:
        df = import_data(sample_data_path)
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_data: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't appear to have rows and columns")
        raise err


def test_import_data_columns(sample_data_path):
    df = import_data(sample_data_path)
    assert set(df.columns) == {'Timestamp', 'Current(A)'}


def test_calc_power_valid_input():
    # You can create a small DataFrame with known values for testing this function.
    # Test the calculated columns and other expected behaviors.
    pass


def test_calc_battery_life_valid_input():
    # Similar to the previous test, create a DataFrame with known values and test the function.
    pass

# Add more test cases to cover edge cases, exceptions handling, etc.
