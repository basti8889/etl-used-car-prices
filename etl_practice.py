import pandas as pd 
import glob 
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def extract_from_csv(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe

def extract_from_json(file_path):
    dataframe = pd.read_json(file_path,lines=True)
    return dataframe

def extract_from_xml(file_path):
    root = ET.parse(file_path).getroot()
    rows = []
    for car in root:
        rows.append({
        "car_model": car.find("car_model").text,
        "year_of_manufacture": int(car.find("year_of_manufacture").text),
        "price": float(car.find("price").text),
        "fuel": car.find("fuel").text
             })
    return pd.DataFrame(rows)


def extract():
    frames = []
    for csvfile in glob.glob("*.csv"):
        if csvfile != target_file:
           frames.append(extract_from_csv(csvfile))
    for jsonfile in glob.glob("*.json"):
           frames.append(extract_from_json(jsonfile))
    for xmlfile in glob.glob("*.xml"):
           frames.append(extract_from_xml(xmlfile))
    return pd.concat(frames, ignore_index=True)


def transform(data):
    data["price"] = data["price"].round(2)
    return data


def load_data(data, file_path):
    data.to_csv(file_path, index=False)

def log_progress(message):
    timestamp_format = '%Y-%b-%d %H:%M:%S'
    with open(log_file, "a") as f:
     f.write(f"[{datetime.now().strftime(timestamp_format)}] {message}\n")



log_progress("ETL Job start")
log_progress("ETL job extract started")
extracted_data = extract()
log_progress("ETL job extract completed")
log_progress("ETL job transform started")
transformed_data = transform(extracted_data)
log_progress("ETL job transform completed")
log_progress("ETL job load started")
load_data(transformed_data, target_file)
log_progress("ETL job load completed")
log_progress("ETL Job completed")