# Internet Speed Twitter Bot

This project is a Python bot that checks your internet speed using [Speedtest](https://www.speedtest.net/) and tweets at your internet provider if your speed is lower than the promised rates. The bot uses Selenium to automate browser interactions and Python's smtplib to send email alerts.

This project is based on and inspired by the **100 Days of Code: The Complete Python Pro Bootcamp for 2023** course by Angela Yu. The course provides an excellent introduction to Python and was the foundation for this game. You can check out the course on [Udemy](https://www.udemy.com/course/100-days-of-code/?couponCode=ST14MT101024#reviews).

## Features

- Measure internet download and upload speeds using Speedtest.
- Compare the measured speeds with your internet provider's promised speeds.
- Automatically log in to Twitter and tweet at your provider if the speeds are below expectations.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Python-dotenv

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/angelikizoi/TwitterInternetSpeed.git
    cd TwitterInternetSpeed
    ```

2. Install dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory to store sensitive information:
    ```
    EMAIL=your_email@example.com
    USERNAME=your_twitter_username
    PASSWORD=your_twitter_password
    CHROME_DRIVER_PATH=/path/to/your/chromedriver
    ```

4. Make sure you have the Chrome WebDriver installed and add its path to the `.env` file.

5. Run the bot:
    ```bash
    python your_script.py
    ```

## How It Works

1. The bot launches a browser window and navigates to Speedtest.
2. It runs an internet speed test and records the download and upload speeds.
3. If the measured speeds are below the expected rates (which you can adjust in the script), the bot logs into Twitter and posts a tweet to your internet provider.
4. After the tweet is sent, the browser window closes.

## Customization

You can customize the following variables in the script to adjust how the bot works:

- `PROMISED_DOWN`: Set the expected download speed (in Mbps).
- `PROMISED_UP`: Set the expected upload speed (in Mbps).
- Tweet format can be customized in the `tweet_at_provider` method.

## Dependencies

The project depends on the following libraries:
- `selenium`: Used for browser automation.
- `python-dotenv`: For loading environment variables.
- `requests`: To handle HTTP requests (if needed for future enhancements).
- `smtplib`: Used to send email notifications (optional).
  
All dependencies can be installed via `requirements.txt`.

