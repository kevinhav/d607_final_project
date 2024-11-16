import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import tomli
import re
from io import StringIO

with open("config.toml", "rb") as f:
    config = tomli.load(f)


def get_innova_data(url=config['paths']['innova_url'], table_id=config['paths']['innova_table']):
    """
    Scrape an HTML table by its ID from a given URL and convert it into a Pandas DataFrame.
    
    Parameters:
        url (str): The URL containing the HTML table.
        table_id (str): The ID of the HTML table to scrape.
        
    Returns:
        pd.DataFrame or None: A Pandas DataFrame containing the table data,
        or None if the table with the specified ID is not found.
    """
    try:
        # Send an HTTP GET request to fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table with the specified ID
        table = soup.find('table', {'id': table_id})
        
        if table:
            # Convert the table to a Pandas DataFrame
            df = pd.read_html(str(table))[0]
            return df
        else:
            print(f"Table with ID '{table_id}' not found on the page.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_pdga_data(url=config['paths']['pdga_url']):
    """
    Read PDGA disc data from their CSV export URL into a pandas dataframe
    """
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    req = requests.get(url, headers=header)
    data = StringIO(req.text)

    return  pd.read_csv(data)


def normalize_column_names(df):
    """
    Normalize the column names (headers) of a Pandas DataFrame by making them lowercase,
    removing whitespaces, special characters, and "cm" (case-insensitive) only if it's
    found at the end of the column name.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame with potentially non-standard column names.
        
    Returns:
        pd.DataFrame: A new DataFrame with normalized column names.
    """
    # Define a function to clean and normalize a single column name
    def clean_column_name(column_name):
        # Remove special characters and replace spaces with underscores
        cleaned_name = re.sub(r'[^a-zA-Z0-9_ ]', '', column_name)
        # Convert to lowercase
        cleaned_name = cleaned_name.lower()
        # Remove "cm" (case-insensitive) only if it's at the end of the string
        cleaned_name = re.sub(r'cm$', '', cleaned_name)
        # Remove "gr" (case-insensitive) only if it's at the end of the string
        cleaned_name = re.sub(r'gr$', '', cleaned_name)
        # Remove "kg" (case-insensitive) only if it's at the end of the string
        cleaned_name = re.sub(r'kg$', '', cleaned_name)
        # Remove extra spaces
        cleaned_name = cleaned_name.strip().replace(' ', '_')
        return cleaned_name

    # Apply the cleaning function to all column names
    normalized_columns = [clean_column_name(col) for col in df.columns]

    # Rename the DataFrame columns with the normalized names
    df.columns = normalized_columns

    return df

# TODO 

def clean_innova_data():
    ...

def clean_pdga_data():
    ...

def create_processed_data():
    ...

def cache_processed_data():
    # TODO feather or parquet?
    ...