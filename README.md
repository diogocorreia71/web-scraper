# Car Listings Scraper

This project is a web scraper for car listings from [Standvirtual](https://www.standvirtual.com). The scraper allows you to search for multiple car makes and models, within a specified price range, and sends you an email with the latest listings.

## Features

- Scrapes car listings based on user-provided make, model, and price.
- Stores previously seen listings to avoid sending duplicate results.
- Sends an email with new listings every morning at 9 AM via a cron job.
- Allows multiple email recipients.

## Prerequisites

- Python 3.x
- BeautifulSoup4
- Requests
- smtplib
- json

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/car-listings-scraper.git
    cd car-listings-scraper
    ```

2. Install required packages:
    ```sh
    pip install beautifulsoup4 requests
    ```

## Configuration

1. Open the `web-scraper.py` file and configure your email settings:
    ```python
    sender_email = "your_email"
    sender_password = "your_password"
    receiver_email = "receiver_email"
    ```

2. Update the `data_file` variable if you want to use a different file name for storing seen listings:
    ```python
    data_file = "scraped_data.json"
    ```

## Usage

1. Run the scraper script:
    ```sh
    python3 web-scraper.py
    ```

2. Follow the prompts to enter the make, model, and maximum price for each search.

## Automate with Cron

To run the script every day at 9 AM, create a cron job:

1. Open your crontab file:
    ```sh
    crontab -e
    ```

2. Add the following line to schedule the script:
    ```sh
    0 9 * * * /path/to/your/scraper_script.sh
    ```

    Make sure your `scraper_script.sh` contains:
    ```sh
    #!/bin/bash
    cd /path/to/your/project
    python3 web-scraper.py << EOF
    1
    marca
    modelo
    valor
    EOF
    ```

## Note

- Ensure your `scraped_data.json` file is created and properly updated after each run to avoid receiving duplicate listings.
- Replace "your_email", "your_password", and "receiver_email" with actual email addresses and password before running the script. Adjust the crontab and bash script paths as per your environment.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, please feel free to contact me at diogo_correia7@hotmail.com.
