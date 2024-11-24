import pandas as pd
from pandas import DataFrame
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import tomli
import re
from io import StringIO
import sys
import os

# TODO figure out how to do relative path with Quarto
with open("/Users/kevinhav/projects/d606_final_project/config.toml", "rb") as f:
    config = tomli.load(f)


def get_innova_data(
    url=config["paths"]["innova_url"], table_id=config["paths"]["innova_table"]
) -> DataFrame:
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
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table with the specified ID
        table = soup.find("table", {"id": table_id})

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


def get_pdga_data(url=config["paths"]["pdga_url"]) -> DataFrame:
    """
    Read PDGA disc data from their CSV export URL into a pandas dataframe
    """
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    req = requests.get(url, headers=header)
    data = StringIO(req.text)

    return pd.read_csv(data)


def clean_innova_data(innova_df) -> DataFrame:
    """
    Drop uncessary columns and clean up column names for Innova disc data
    """
    innova_df.drop(columns="ABBR.", inplace=True)
    innova_df.rename(columns=str.lower, inplace=True)

    return innova_df


def clean_pdga_data(pdga_df) -> DataFrame:

    pdga_df_clean = pdga_df.rename(columns=lambda x: x.lower().replace(" ", "_"))
    pdga_df_clean.drop(
        columns=[
            "max_weight_(gr)",
            "max_weight_vint_(gr)",
            "last_year_production",
            "class",
            "certification_number",
            "approved_date",
        ],
        inplace=True,
    )

    return pdga_df_clean


def create_processed_data(innova_df, pdga_df) -> DataFrame:
    """
    Join Innova and PDGA data as the final processed dataset, dropping nulls
    """
    df = pd.merge(
        how="left", left=innova_df, right=pdga_df, left_on="disc", right_on="disc_model"
    )

    # Some discs are missing measurements so we'll ignore them
    df.dropna(subset="rim_thickness_(cm)", inplace=True)

    return df


def cache_processed_data():
    # TODO feather or parquet?
    ...


def get_data() -> DataFrame:
    """
    Returns processed and combined Innova and PDGA data
    """

    innova_df = get_innova_data()
    innova_df = clean_innova_data(innova_df)

    pdga_df = get_pdga_data()
    pdga_df = clean_pdga_data(pdga_df)

    return create_processed_data(innova_df, pdga_df)


if __name__ == "__main__":
    get_data()
