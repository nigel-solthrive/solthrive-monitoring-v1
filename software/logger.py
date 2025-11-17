import csv
import datetime
import os

CSV_PATH = "/home/pi/solthrive/solar_log.csv"

def _open_writer():
    exists = os.path.exists(CSV_PATH)
    f = open(CSV_PATH, "a", newline="")
    writer = csv.writer(f)
    if not exists:
        writer.writerow(["timestamp_utc", "p_solar_w", "p_load_w", "p_grid_w"])
    return f, writer

def log_sample(p_solar, p_load, p_grid):
    f, writer = _open_writer()
    ts = datetime.datetime.utcnow().isoformat()
    writer.writerow([ts, p_solar, p_load, p_grid])
    f.flush()
    f.close()