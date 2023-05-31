# Google Image Scraper 📷

**Google Image Scraper** is a Python script that uses Selenium WebDriver to search Google Images and download the search results. It's an easy-to-use tool for collecting image data for use in machine learning, data analysis, or any other use cases you can think of.

## How it Works ⚙️

The script uses the Selenium WebDriver to automate a browser session, perform a Google Image search based on your search term, and then download the images. The search term, number of images to download, and other configurations can be set in a `config.json` file.

## Requirements 📋

This script requires certain Python libraries, including Selenium, Requests, and Pillow. To install these requirements, run the following command in your terminal:

```
pip install -r requirements.txt
```


You also need ChromeDriver installed, which is required by Selenium to automate the Chrome browser. You need to install this separately:

- **macOS users**: You can use `brew` to install ChromeDriver by running `brew install chromedriver` in your terminal.
- **Windows or Linux users**: Please refer to the ChromeDriver [Getting Started](https://chromedriver.chromium.org/getting-started) guide for installation instructions.

You can find ChromeDriver pth using this command in your terminal:

```
where chromedriver
```

Please ensure that the installed ChromeDriver version matches your Chrome browser version.

## Configuration 🔧

Edit the `config.json` file to specify your configurations. The keys are as follows:

- **webdriver_path**: The path to your ChromeDriver executable.
- **search_key**: The search term for Google Images.
- **number_of_images**: The number of images to download.
- **image_path**: The directory to save the downloaded images.
- **headless**: A boolean value to decide whether to run Chrome in headless mode.
- **min_resolution**: The minimum resolution for the images to download.
- **max_resolution**: The maximum resolution for the images to download.
- **max_missed**: The maximum number of missed download attempts before the scraper stops.

Here's an example `config.json`:

```
"webdriver_path": "/path/to/your/chromedriver",
"search_key": "cat",
"number_of_images": 10,
"image_path": "images",
"headless": false,
"min_resolution": "(0, 0)",
"max_resolution": "(1920, 1080)",
"max_missed": 3
```


Replace `/path/to/your/chromedriver` with the actual path to your ChromeDriver executable.

## Usage 🚀

To use the script, first ensure that all the requirements are installed and the `config.json` file is set up. Then, simply run the `main.py` script:

```
python main.py
```


**Happy scraping!**

**NOTE:** Please respect Google's [robots.txt](https://www.google.com/robots.txt) file and use this responsibly. It is not recommended to download large numbers of images from Google Images, as this may be against their terms of service.
