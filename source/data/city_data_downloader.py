# Environment setup
from utils import get_csv_from_url, save_file_to_csv

# Settings
## Input/Output
URL = "https://github.com/sapics/ip-location-db/raw/master/geolite2-city/geolite2-city-ipv4-num.csv.gz"
FILENAME_PREFIX = "geolite2-city-ipv4-num"
OUTPUT_FOLDER = "city_level_files"

# Main
if __name__ == "__main__":
    
    # Get CSV data
    content = get_csv_from_url(URL)
    
    # Save file as CSV
    save_file_to_csv(content, OUTPUT_FOLDER, FILENAME_PREFIX)