'''A set of utility functions
'''
import json


def load_data(data_path):
    '''
    Load JSON data from a file.

    Parameters
    ----------
    data_path : str
        The path to the JSON file.

    Returns
    -------
    dict
        A Python dictionary representing the JSON data.
    '''
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)
