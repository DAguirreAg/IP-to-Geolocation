# Environment setup
from config import Config
from utils import get_csv_from_url, save_file_to_csv

# Main
def main():
    # Get CSV data
    content = get_csv_from_url(Config.URL_COUNTRY_DATA)
    
    # Save file as CSV
    save_file_to_csv(content, Config.RAW_FOLDER_COUNTRY_DATA, Config.FILENAME_PREFIX_COUNTRY_DATA)

if __name__ == "__main__":
    main()
