#!/bin/bash
# Activate virtual environment
source /home/daniel/Documents/GitHub/IP-to-Geolocation/source/data/venv/bin/activate

# Execute Python script
python3 ${PWD}/"country_data_downloader.py"
python3 ${PWD}/"city_data_downloader.py"
#python3 ${PWD}/"country_data_uploader.py"

# Deactivate the virtual environment
deactivate