#!/bin/bash
# Define files location
FILES_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Activate virtual environment
source $FILES_PATH/venv/bin/activate

# Execute Python script
python3 $FILES_PATH/"downloader_country_data.py"
python3 $FILES_PATH/"etl_country_data.py"

# Deactivate the virtual environment
deactivate
