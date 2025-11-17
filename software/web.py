import csv
from flask import Flask, render_template_string

CSV_PATH = "/home/pi/solthrive/solar_log.csv"

TEMPLATE = """<!doctype html>
<title>SolThrive Monitor V1</title>
<h1>SolThrive – Solar Monitoring V1</h1>
<p><b>Solar now:</b> {{ p_solar }} W</p>
<p><b>Home load:</b> {{ p_load }} W</p>
<p><b>Grid:</b> {{ p_grid }} W (positive = import, negative = export)</p>
"""


def get_latest():
    try:
        with open(CSV_PATH) as f:
            rows = list(csv.reader(f))
        if len(rows) < 2:
            return 0.0, 0.0, 0.0
        ts, p_solar, p_load, p_grid = rows[-1]
        return float(p_solar), float(p_load), float(p_grid)
    except FileNotFoundError:
        return 0.0, 0.0, 0.0

app = Flask(__name__)

@app.route("/")
def index():
    p_solar, p_load, p_grid = get_latest()
    return render_template_string(TEMPLATE, p_solar=p_solar, p_load=p_load, p_grid=p_grid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)