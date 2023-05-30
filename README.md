# Web Scraper

This is a simple web scraping script written in Python. It allows you to scrape information from a website, including the website title, meta tags, headings, paragraphs, links, images, and more. Additionally, it can search for banners and discover common admin pages.
--
## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x

- Requests library: `pip install requests`

- Colorama library: `pip install colorama`

- BeautifulSoup library: `pip install beautifulsoup4`

- PyFiglet library: `pip install pyfiglet`

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:
```
python web_scraper.py
```
4. You will be prompted to enter the URL of the website you want to scrape. Provide the URL and press Enter.

5. The script will then scrape the website and display the extracted information, including the website title, meta tags, headings, paragraphs, links, images, banners (if found), and common admin pages (if found).

## Script Overview

### 1. Imports

The script uses the following Python libraries:

- `requests` for making HTTP requests to the website.

- `colorama` for colored output in the terminal.

- `BeautifulSoup` for parsing the HTML content of the website.

- `pyfiglet` for printing an ASCII logo.

### 2. Function: `print_logo()`

This function prints an ASCII logo using the `Figlet` class from the `pyfiglet` library. It is called at the beginning of the script to display the logo.

### 3. Function: `scrape_website(url)`

This function takes a URL as input and performs the web scraping. It makes an HTTP request to the specified URL, extracts information using BeautifulSoup, and prints the scraped data in different categories such as title, meta tags, headings, paragraphs, links, images, banners, and admin pages.

### 4. Function: `main()`

This is the main function of the script. It calls the `print_logo()` function to display the logo and then prompts the user to enter the URL of the website they want to scrape. It then calls the `scrape_website(url)` function to perform the web scraping.

### 5. Script Execution

The script is executed by calling the `main()` function at the end. When you run the script, it will display the logo, prompt for a URL, scrape the website, and print the extracted information in the terminal.

Feel free to customize the script according to your needs and explore additional functionality for web scraping!



