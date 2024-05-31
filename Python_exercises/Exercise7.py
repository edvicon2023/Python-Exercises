import requests
from bs4 import BeautifulSoup

def extract_linkedin_profile(url):
    try:
        # Send an HTTP request to the LinkedIn profile URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the profile name from the title tag (as an example)
        profile_name = soup.find('title').text

        # Extract other details if available (this example assumes certain HTML structure)
        profile_headline = soup.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'}).text.strip() if soup.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'}) else 'N/A'
        profile_location = soup.find('li', {'class': 't-16 t-black t-normal inline-block'}).text.strip() if soup.find('li', {'class': 't-16 t-black t-normal inline-block'}) else 'N/A'

        print(f"Profile Name: {profile_name}")
        print(f"Headline: {profile_headline}")
        print(f"Location: {profile_location}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the profile: {e}")
    except AttributeError as e:
        print(f"Error parsing the profile: {e}")

# Example usage
profile_url = 'https://www.linkedin.com/in/example-profile/'
extract_linkedin_profile(profile_url)
