# IP-to-Geolocation

The following repository contains code as a proof of concept of a IP-to-Geolocation application. The main task of the application is to return the geographic location of a given IP address.

<p align="middle">
  <img src="documentation/IP-to-Geolocation%20Main%20page.png" alt="IP-to-Geolocation Main page.png" height=500></br>
  <i>IP-to-Geolocation Main page.png</i>
</p>

## 1. How to use it
Follow the next steps:

* Open the `config.py` file and modify the `SQLALCHEMY_DATABASE_URL` to your favourite database.
* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
* Open a terminal window and type `uvicorn main:app --reload` to launch the application.
* Open a browser and type `http://127.0.0.1:8000/docs` in the address bar to open an interactive view of the App.
* Download the `geolite2-country-ipv4.csv` file from [here](https://github.com/sapics/ip-location-db) and upload it in the database.

<p align="middle">
  <img src="documentation/Running%20IP-to-Geolocation%20App.png" alt="Running IP-to-Geolocation App.png" height=200></br>
  <i>Running IP-to-Geolocation App</i>
</p>


## 2. Technical details
The application structure is pretty simple. It is composed of two API endpoints. 
* `/get_location`: It expects an IP address as an input and outputs the country from which the given IP originated from.
* `/upload`: It is a utility function to facilitate the refresh and upload of the database table that contains the mapping from IP ranges to countries. (Note that in production environments, this endpoint should be only accessible to authorized users, as it allows to upload any data in the database).

<p align="middle">
  <img src="documentation/Main%20design.png" alt="Main design.png" height=200></br>
  <i>Main design of the App.</i>
</p>

## 3. Future functionalities/Considerations
As a proof of concept of a IP-to-Geolocation application, the source code doesn't implement all the functionalities that this kind of applications should have. On one hand, only the country of origin is being retrieved (no province or cities are being provided). On the other hand, the data in the database is expected to be manually uploaded, which can be time consuming as well as introduce human errors in the process. Also, this operation is not done in the background, which causes a blocking issue (although it is not a big deal with such a small dataset).

Find below a list of functionalities that will need to be considered implementing in the current repository to make it fully functional as well as some nice-to-have functionalities: 

* Province and city data should be added to the database to make the queries more complete and useful.
* One of the endpoints is used to upload CSV data into the Database. In production settings, these endpoint should only be accessible to authorized people, to avoid people uploading erroneous data.
* Upload file's content should be sanitized to ensure no malicious code is placed in the database.
* For this small size database, it should be possible to implement a in-memory database, to speed up the queries. 
* It should be possible to implement a date dependant search option, to know from where a given IP come from in a given moment in time.

## 4. Disclaimers
This is a proof of concept project that aims to shown how a IP-toGeolocation service works. Bear in mind, that as many POC, it is not a final product and many points need to be considered before making the code production ready.

## References
* [Internet geolocation](https://en.wikipedia.org/wiki/Internet_geolocation)
* [IP-to-Geolocation Data](https://github.com/sapics/ip-location-db)