# raspberrypi-monitoring

# Project Description
This project aims to monitor the performance of a Raspberry Pi by tracking CPU temperature and CPU utilization. The data is collected using a Python script, stored in an InfluxDB database, and visualized through a Grafana dashboard.

# Problems Encountered
During the development of this project, several challenges were encountered and resolved:

Docker Installation Issues: Initial difficulties in installing Docker on the Raspberry Pi were resolved by using the official Docker installation script.
InfluxDB Setup: Configuring InfluxDB to run correctly in a Docker container and ensuring it was accessible by Grafana required setting up a custom Docker network and adjusting configuration settings.
Data Collection Script: Ensuring the Python script collected accurate CPU temperature and utilization data and successfully pushed it to InfluxDB involved troubleshooting and refining the script.
Grafana Configuration: Connecting Grafana to InfluxDB and setting up the dashboard required careful configuration of data sources and queries.
# Team Contribution
This project was initially planned as a collaborative effort between two students. However, my partner David decided to leave the "Labs and Production" course to pursue "Digital Health". As a result, I completed this project independently.

# Files Created
Dockerfile: This file contains the instructions to build a Docker image for running the Python data collection script. It includes the necessary installations and setups to ensure the script runs correctly inside a Docker container.

monitor.py: This Python script collects CPU temperature and utilization data from the Raspberry Pi and sends it to the InfluxDB database. It runs continuously, collecting data at regular intervals.

grafana_dashboard.json: This JSON file contains the configuration for the Grafana dashboard, including the panels for visualizing CPU temperature and utilization data.
