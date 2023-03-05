# Instructions to run the code.

## Scrapping crypto data from the internet

Firstly we need to run the *crypto_scrapping.py* file
To run this file make sure you have chrome webdriver installed in your device and the python selenium module installed.
If you don't have selenium module installed. Run the code provided below in your terminal.

  ***pip install -U selenium***
  
Install the chrome webdriver from the link given below
  https://chromedriver.chromium.org/


After making sure your device is ready run the cryptoscrapping.py file.
This will create a file called crypto_data.json containing the opening and closing value of btc and eth alongside their dates.

## Analysing the code.

We have performed our analysis in the file *crypto_analysis.ipynb* file
To perform our analysis we have assumed that the closing price of the day is the price of bitcoin/ethereum coin for the day.
Make sure you have the **pandas** and **matplotlib** package installed in your environment
Running the cells of the files will give you the analysis done on them.

## Uploading to GCS

Make sure you have google api package installed in your environment.
If you don't run these commands in the terminal

***pip install --upgrade google-api-python-client***

***pip install --upgrade google-cloud-storage***

After installing these make sure to add your security key json file to your working directory and change the file name.
Make sure to update the bucket name to your google bucket name.
Running the cells of this file will upload your data to your cloud storage.
