# EVolution
This is a project developed for the ECE NTUA course Software Engineering, during the academic year 2020-2021.

## Project Overview
The goal of this project was to develop a full-stack website that focuses on **electric vehicles (EVs)**. The platform provides a secure sign-up and login functionality for different user roles, including **car owners**, **energy suppliers**, and **car manufacturers**, providing valuable insights, statistics, and functionality tailored to their specific needs.

This web application is designed to enhance the EV experience by offering a comprehensive range of features for each user type. Below is a detailed overview of the functionalities available for each user group.

### 1. Car Owners
- **Nearby Charging Stations**: The platform helps EV owners locate nearby charging stations based on their location.
- **Charging Session Scheduling**: Owners can schedule charging sessions and manage their payments directly through the site.
- **Usage Statistics**: Owners receive detailed statistics on their energy consumption, charging sessions, and other metrics.
- **Point System**: A point system is integrated into the platform, allowing owners to accumulate points during their usage. They also have the flexibility to delay payments using this system.

### 2. Energy Suppliers
- **Demand Forecasting**: Energy suppliers have access to demand forecasts to help them plan better for energy distribution.
- **Consumption Statistics**: Detailed consumption data is provided to suppliers, helping them optimize their resources for energy distribution and future forecasts.

### 3. Car Manufacturers
- **Charging Session Reports**: Manufacturers can view detailed reports on the charging sessions of their electric vehicle models.
- **Energy Consumption Reports**: These reports provide insights into the energy consumption of each model, helping manufacturers make improvements.
- **Average Energy Costs**: Manufacturers can see the average energy costs associated with their vehicles. This information is aggregated to ensure no sensitive information is shared with competitors.
- **Cross-Manufacturer Insights**: High-level statistics are provided on energy consumption across manufacturers, allowing for benchmarking while ensuring data privacy.


## Presentation of the EVolution website:

https://user-images.githubusercontent.com/63066416/137513209-474f8c5e-f07b-4158-8802-98ff725f89c7.mp4


## Technologies
* JavaScript
* Python
* CSS
* HTML

## Configuration and Setup
To install and run the software, follow these steps:

1. **Clone this GitHub Repository** using the command:
   ```bash
   git clone https://github.com/LiagkaAikaterini/EVolution.git
   ```
2. **Import the Database:** Load the data from the [Database Files](back-end/Database%20Files) folder into a relational database of your choice.
3. **Configure the Database Connection:** Modify the [db.config.js](back-end/REST_API/config/db.config.js) file by adding your own database credentials for establishing the connection.
4. **Set Up a Secure Environment:** Follow the instructions in the [certificationGuide](certificationGuide.md) to create a secure environment before launching the application.
5. **Install Dependencies:** Inside both the `back-end/REST_API` and `front-end/react_code` directories run the command:
   ```bash
   npm install
   ```
6. **Start the Application:** After the dependencies are installed, use the command npm start in both of these directories to start the backend and frontend services.
7. **CLI and Testing:** For command-line interface (CLI) operations and testing, follow the [instructions](cli-client/README.md) provided.


## Our Team
* [Alexandropoulos Stamatis](https://github.com/stamatisalex)
* [Giorgoulakis Nikolaos](https://github.com/nikosgio)
* [Gkotsi Polytimi-Anna](https://github.com/PolyannaG)
* [Kaparou Alexandra](https://github.com/alexandrakapa)
* [Liagka Aikaterini](https://github.com/LiagkaAikaterini)
* [Zhara Stela](https://github.com/stelazr)
