# IP-to-Geolocation

The following repository contains code of a proof of concept of a IP-to-Geolocation web application. The main task of the application is to return the geographic location of a given IP address. It achieves this by downloading the data automatically and then uploading it to the database. Once available the user is able to extract this information via the frontend application. 

<div>
	<div align="middle">
		<img src="documentation/Main design.png" alt="Main design" width=600>
	</div>
	<div align="middle">
	  <i>Overview of architectural design.</i>
	</div>
</div>


## 1. Introduction

Some services require knowing the location of the users for providing location dependent services.

This repository aims at implementing a web service for users to identify where a given IP is coming from.

<div>
	<div align="middle">
		<img src="documentation/Frontend view.png" alt="Frontend view" height=250>
	  	<img src="documentation/Database table content view.png" alt="Database table content view" height=300>
	</div>
	<div align="middle">
	  <i>Overview of frontend and database.</i>
	</div>
</div>

## 2. How to use it

### 2.1. Option 1: Standard install
Follow the next steps:

* Prepare the database:
	* Open your favourite SQL database and create the database and the table using `setup.sql` helper script.
	* Open the `config.py` file and modify the `SQLALCHEMY_DATABASE_URL` to use the database you just created.

* Prepare the backend service:
	* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
	* Open a terminal window and type `uvicorn main:app --reload` to launch the application.
	* (Optional) Open a browser and type `http://127.0.0.1:8000/docs` in the address bar to open an interactive view of the backend service.

<div>
	<div align="middle">
		<img src="documentation/Running the backend service.png" alt="Running the backend service" width=900>
	</div>
	<div align="middle">
	  <i>Running the backend service.</i>
	</div>
</div>

* Prepare the frontend:
	* Run the `index.html` in a live server and open the provided URL. (I recommend using VScode's Live server plug-in due to its ease of use)

<div>
	<div align="middle">
		<img src="documentation/Running the frontend.png" alt="Running the frontend" height=300>
	</div>
	<div align="middle">
	  <i>Running the frontend.</i>
	</div>
</div>

* Upload data:
	* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
	* Open a terminal window and type `python downloader_country_data.py` to download the data.
	* In the same terminal window type `python etl_country_data.py` to process and upload the data.
	* (Optional) Schedule the script to run automatically on a weekly basis.

### 2.2. Option 2: Install via docker

Follow the next steps (note that you will require to have docker installed):

* Build the database docker image:
	* Open a terminal window and `cd` to database folder.
	* Type: `docker build -t ip-to-geo-db .`

* Build the backend docker image:
	* Open a terminal window and `cd` to backend folder.
	* Type: `docker build -t ip-to-geo-be .`

* Build the frontend docker image:
	* Open a terminal window and `cd` to frontend folder.
	* Type: `docker build -t ip-to-geo-fe .`

* Build the data-upload (data-engineering) docker image:
	* Open a terminal window and `cd` to data-engineering folder.
	* Type: `docker build -t ip-to-geo-de .`

* Launch the docker compose file
	* Open a terminal window and `cd` to source folder.
	* Type: `docker compose up`.
	* Visit [http://localhost:8002/](http://localhost:8002/)
	* Execute the `download_country_data` endpoint.
	* Execute the `etl_country_data` endpoint.

## 3. Technical details

### 3.1. Back-of-the-envelope calculations

Find below a rough estimation of database requirements.

Assumptions:

* Amount of IP ranges: 240k
* Hold historical records: Yes
* Data refresh rate: Weekly
* Data history retention: 5 years

Database size:

* Record size: 2*64 (BIGINT) + 13 (TIMESTAMP) + 4 (VARCHAR) = 145 bytes 
* Required database size: 145 * 240k * 52 (weeks/year) * 5 (years) = 9 Gb

### 3.2. Technology stack

* Vanilla JS and JQuery were selected due to the simple nature of the application.
* FastAPI was selected due to its performance and great community adoption.
* SQL was selected due the robustness of it and the structured nature of the data to be received.

### 3.3. How it works

The architecture of the code works in the following way:

* A HTML form allows the user to input his feedback and submit it via JQuery to the server.
* The server running the backend (implemented in FastAPI) will receive the form data and, if correct, it will add it to the database.
* In parallel, a service is running that updated the data in a

Note that a microservice architecture philosophy was followed, as this should allow the application to receive requests from users even when the other services are down (as long as they are not located in the same machines).

<div>
	<div align="middle">
		<img src="documentation/Main design.png" alt="Main design" width=700>
	</div>
	<div align="middle">
	  <i>Overview of architectural design.</i>
	</div>
</div>

### 3.4. Endpoints
The application structure is pretty simple. It is composed of three API endpoints (one in the backend side and two in the data-engineering side):

* Backend:
	* `/geolocation`: It expects an IP address as an input and outputs the country from which the given IP originated from.

<p align="middle">
  <img src="documentation/Backend endpoints.png" alt="Backend endpoints." width=800></br>
  <i>Backend endpoints.</i>
</p>

* Data-Engineering:
	* `/download_country_data`: It triggers the service to download the latest available IP-To-Geolocation data.
	* `/etl_country_data`: It triggers the service to process the latest available IP-To-Geolocation data and load it into the database.

<p align="middle">
  <img src="documentation/Data-engineering endpoints.png" alt="Data-engineering endpoints." width=800></br>
  <i>Data-engineering endpoints.</i>
</p>


## 4. Future functionalities/Considerations
As a proof of concept of a IP-to-Geolocation application, the source code doesn't implement all the functionalities that this kind of applications should have. On one hand, only the country of origin is being retrieved (no province or cities are being provided). On the other hand, the data in the database is expected to be manually uploaded, which can be time consuming as well as introduce human errors in the process. 

Find below a list of functionalities that will need to be considered implementing in the current repository to make it fully functional as well as some nice-to-have functionalities: 

* Province and city data should be added to the database to make the queries more complete and useful.
* Upload file's content should be sanitized to ensure no malicious code is placed in the database.
* For this small size database, it should be possible to implement a in-memory database, to speed up the queries.

## 5. Disclaimers
This is a proof of concept project that aims to shown how a IP-to-Geolocation service works. Bear in mind, that as many POC, it is not a final product and many points need to be considered before making the code production ready.

## References
* [Internet geolocation](https://en.wikipedia.org/wiki/Internet_geolocation)
* [IP-to-Geolocation Data](https://github.com/sapics/ip-location-db)
