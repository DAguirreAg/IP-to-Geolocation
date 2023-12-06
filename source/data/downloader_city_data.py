# Environment setup
from config import Config
from utils import get_csv_from_url, save_file_to_csv

# Main
if __name__ == "__main__":
    
    # Get CSV data
    content = get_csv_from_url(Config.URL_CITY_DATA)
    
    # Save file as CSV
    save_file_to_csv(content, Config.RAW_FOLDER_CITY_DATA, Config.FILENAME_PREFIX_CITY_DATA)