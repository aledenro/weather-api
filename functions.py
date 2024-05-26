import pandas as pd


def parse_filename(station):
    """Parses the correct filename when passed a station ID"""
    station_id = str(station).zfill(6)
    filename = f"data/TG_STAID{station_id}.txt"

    return filename


def get_temp_by_station_date(station, date):
    """Reads the csv file for a specific station and returns its temperature from a specific date"""
    filename = parse_filename(station)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    return temperature


def get_stations():
    df = pd.read_csv("data/stations.txt", skiprows=17)
    df = df[["STAID", "STANAME                                 "]]

    return df


def get_all_data_by_station(station):
    """Reads the csv file for a specific station and returns all the data"""
    filename = parse_filename(station)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")

    return result


def get_all_data_by_station_year(station, year):
    """Reads the csv file for a specific station and returns all the data for a year"""
    filename = parse_filename(station)
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")

    return result
