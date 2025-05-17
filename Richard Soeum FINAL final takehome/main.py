import threading
from datetime import date, timedelta, datetime
import os
import time
import logging
import requests
import xmltodict
import json
import random
import calendar

BASE_DIR = r"C:\Users\rvsoe\OneDrive\Desktop\ETE4990\homeworkfolder-rsoeum-1\final take home"


DATA_DIR = os.path.join(BASE_DIR, "data_random")
LOG_DIR  = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'quest1_random.log')
THREAD_POOL_SIZE = 10
ALL_CURRENCIES =  ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
NUM_BASE_CURRENCIES_TO_SELECT = 10
START_YEAR = 2011
START_MONTH = 5
END_YEAR = 2023
END_MONTH = 10
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def fetch_rates(c_date, base, output=False): #fetches data
    date_str = c_date.strftime("%Y-%m-%d")
    filename = os.path.join(DATA_DIR, base, f"{date_str}_{base}.json")

    if os.path.exists(filename):
        logging.info(f"File exists: {filename}, skipping.")
        return
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date_str}&base_currency_code={base}&format_type=xml"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        xml_data = response.text
        data_dict = xmltodict.parse(xml_data)
        json_data = json.dumps(data_dict, indent=4)

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as json_file:
            json_file.write(json_data)
        logging.info(f"Saved: {filename}")

    except requests.exceptions.RequestException as e:
        logging.error(f"request Error for {base} on {date_str}: {e}")
    except xml.parsers.expat.ExpatError as e:
        logging.error(f"XML parse Error {base} on {date_str}: {e}. First 200 chars: {xml_data[:200]}")
    except Exception as e:
        logging.error(f"error processing {base} on {date_str}: {e}")


def threaded(start_date, end_date, base_currencies, output=False):#create threads to fetch data
    threads = []
    current_date = start_date
    delta = timedelta(days=1)
    while current_date <= end_date:
        for base_currency in base_currencies:
            thread = threading.Thread(target=fetch_rates, args=(current_date, base_currency, output))
            threads.append(thread)
            thread.start()
            if output:
                print(f"start thread for {base_currency} on {current_date}")
        current_date += delta
    for thread in threads:
        thread.join()
    if output:
        print("all threads finished.")

def main():
   
    start_time = time.time()
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

    #randomly select base currencies
    if len(ALL_CURRENCIES) >= NUM_BASE_CURRENCIES_TO_SELECT:
        random_base_currencies = random.sample(ALL_CURRENCIES, NUM_BASE_CURRENCIES_TO_SELECT)
        logging.info(f"randomly selected base currencies: {random_base_currencies}")
    else:
        random_base_currencies = ALL_CURRENCIES
        logging.warning("not enough currencies in ALL_CURRENCIES for the desired selection. using all available.")

    current_year = START_YEAR
    current_month = START_MONTH
    while current_year <= END_YEAR:
        month_range = calendar.monthrange(current_year, current_month)
        start_date = date(current_year, current_month, 1)
        end_date = date(current_year, current_month, month_range[1]) 

        logging.info(f"Processing: {start_date} to {end_date}")

        threaded(start_date, end_date, random_base_currencies, output=False)
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"execution time: {total_time:.2f} seconds")
    print(f"execution time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()