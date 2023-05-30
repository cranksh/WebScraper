import requests

import colorama

from colorama import Fore, Style

from bs4 import BeautifulSoup

from pyfiglet import Figlet

import whois

colorama.init()

# Function to print ASCII logo

def print_logo():

    custom_fig = Figlet(font='cyberlarge')

    print(Fore.LIGHTGREEN_EX + custom_fig.renderText("Web Scraper") + Style.RESET_ALL)

    print(Fore.GREEN + '=' * 58)

    print(Fore.WHITE + f'Simple web scraper made by cranksh')

    print(Fore.GREEN + '=' * 58)

# Function to scrape website

def scrape_website(url):

    try:

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Get website title

        title = soup.title.string.strip()

        print(Fore.CYAN + f"\nTitle: {title}\n")

        # Get meta tags

        meta_tags = soup.find_all('meta')

        print(Fore.YELLOW + "Meta Tags:")

        for tag in meta_tags:

            print(tag.get('name'), "-", tag.get('content'))

        print()

        # Get headings

        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        print(Fore.YELLOW + "Headings:")

        for heading in headings:

            print(Style.BRIGHT + heading.text.strip())

        print()

        # Get paragraphs

        paragraphs = soup.find_all('p')

        print(Fore.MAGENTA + "Paragraphs:")

        for paragraph in paragraphs:

            print(paragraph.text.strip())

        print()

        # Get links

        links = soup.find_all('a')

        print(Fore.BLUE + "Links:")

        for link in links:

            href = link.get('href')

            if href and not href.startswith('#'):

                print(href)

        print()

        # Get images

        images = soup.find_all('img')

        print(Fore.GREEN + "Images:")

        for image in images:

            src = image.get('src')

            print(src)

        print()

        # Search for banners

        banner_url = f"http://www.example.com/banner.php?url={url}"

        banner_response = requests.get(banner_url)

        banner_data = banner_response.text

        if banner_data:

            print(Fore.LIGHTGREEN_EX + "Banner Found:")

            print(banner_data)

        else:

            print(Fore.RED + "No banner found.")

        print()

        # Admin page finder

        admin_pages = ["admin", "login", "dashboard", "wp-admin", "admin.php"]

        print(Fore.MAGENTA + "Admin Pages:")

        for page in admin_pages:

            admin_url = f"{url}/{page}"

            admin_response = requests.get(admin_url)

            if admin_response.status_code == 200:

                print(admin_url)

        print()

    except requests.exceptions.RequestException:

        print(Fore.RED + "Error: Failed to connect to the website.")

# Main function

def main():

    print_logo()

    # Get user input

    url = input(Style.BRIGHT + Fore.MAGENTA + "> Enter the website URL: ")

    # Scrape the website

    scrape_website(url)

if __name__ == '__main__':

    main()

