# Environment setup
import os
import requests
from datetime import datetime
import glob

def get_csv_from_url(url):
    
    # Download file
    r = requests.get(url, allow_redirects=True)
    
    return r.content

def save_file_to_csv(content, output_folder, filename_prefix):
    
    # Generate filename
    ## Get current datetime
    dt = str(datetime.now())

    ## Reformat datetime string
    dt = dt.split(".")[0].replace(" ", "_").replace("-", "").replace(":", "")
    filename = filename_prefix + "_" +  dt + ".csv"
    
    # Create CSV file
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), output_folder, filename)
    open(filepath, 'wb').write(content)
    
def get_latest_file(path, file_format='*csv'):
    list_of_files = glob.glob(path + file_format) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    return latest_file