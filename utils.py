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
    dict or None
        A Python dictionary representing the JSON data, or `None` if an error occurs.
    '''
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {data_path}")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in {data_path}")
    except Exception as e: #pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {str(e)}")
    return None

def save_data(data_path, update_data):
    '''
    Save JSON data to a file.

    Parameters
    ----------
    data_path : str
        The path to the JSON file.
    update_data : dict
        The data to be saved as JSON.

    Returns
    -------
    bool
        `True` representing successfully saved, or `False` if an error occurs.
    '''
    with open(data_path, 'w', encoding='utf-8') as file:
        json.dump(update_data, file)
