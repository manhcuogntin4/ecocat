This project contains the following files:

    - eco_act.ipynb: A Jupyter notebook for viewing the main characteristics of the EcoAct dataset.
    - analyse_ecoact.py: Contains a Dash web application that allows users to interactively explore and visualize data from an Excel file. The application includes features for       selecting a column from the dataset and displaying corresponding visualizations (e.g., histograms for numerical columns or bar charts for categorical columns).
    - export_database.py: Defines an SQLAlchemy ORM model and a method to write data from a DataFrame to a PostgreSQL database.
    - ecoact_api.py: A Flask-based API for managing records in a PostgreSQL database. The API supports CRUD (Create, Read, Update, Delete) operations for elements, each containing a variety of attributes related to their type, identification, location, and other metadata.