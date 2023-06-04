# Environment setup
from utils import get_csv_from_url, save_file_to_csv

# Settings
## Input/Output
URL = "https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country/geolite2-country-ipv4-num.csv"
FILENAME_PREFIX = "geolite2-country-ipv4-num"
OUTPUT_FOLDER = "country_level_files"

# Main
if __name__ == "__main__":
    
    # Get CSV data
    content = get_csv_from_url(URL)
    
    # Save file as CSV
    save_file_to_csv(content, OUTPUT_FOLDER, FILENAME_PREFIX)