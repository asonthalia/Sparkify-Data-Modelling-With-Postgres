# 🫀 Data Modelling in Postgres


This project is part of the Udacity Nanodegree® on Data Engineering. 

It aims to demonstrate database creation from a JSON store by creating appropriate database structures and populating correct data post ETL.

## Core Technologies
![Shield](https://img.shields.io/badge/Database-Postgres-lightgrey) 
![Shield](https://img.shields.io/badge/Language-Python-lightgrey)
![Shield](https://img.shields.io/badge/RawData-JSON-lightgrey)
## Usage

Start by creating the database using,
```bash
python create_tables.py
```
Start the ETL process using,
```bash
python etl.py
```

The data will then be loaded to the tables created and can be tested using the ```test.ipynb``` notebook present in the repository.

## Database Architecture
> “Data that is loved tends to survive.” - _Kurt Bollacker_
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
