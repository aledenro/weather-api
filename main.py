from flask import Flask, render_template
from functions import get_temp_by_station_date, get_stations, get_all_data_by_station, get_all_data_by_station_year


app = Flask(__name__)


@app.route("/")
def index():
    stations = get_stations()
    return render_template("index.html", data=stations.to_html(classes="table_style", index=False))


@app.route("/api/v1/<station>/<date>")
def api_by_station_date(station, date):
    temperature = get_temp_by_station_date(station, date)
    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def api_by_station(station):
    data = get_all_data_by_station(station)
    return data


@app.route("/api/v1/annual/<station>/<year>")
def api_by_station_year(station, year):
    data = get_all_data_by_station_year(station, year)
    return data


if __name__ == "__main__":
    app.run(debug=True)