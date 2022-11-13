# unemployment_inclass2022

## Setup 

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemplyment-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the unemployment report:

```sh

python app/unemployment.py

## Configuration

Obtain an API Key from AlphaVantage

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file ...

ALPHAVANTAGE_API_KEY="__________"

```


