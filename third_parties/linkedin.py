import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str,
                            mock:bool=False):
    """
    Scrape information from Linkedin profiles, 
    Manually scrape the information from the Linkedin profile
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/manojthangaraj92/5fa64e271f947363e89d0a35bc71b963/raw/01165776568ccc4cfecdbbf9fc070dde91d0f012/manoj-thangaraj.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=15
        )
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        api_key = os.environ.get('PROXYCURL_API_KEY')
        headers = {'Authorization': 'Bearer ' + api_key}
        params = {
            'url': linkedin_profile_url
        }

        response = requests.get(
                        api_endpoint,
                        params=params,
                        headers=headers,
                        timeout=10
                        )
        
    data = response.json()

    data = {
        k:v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get('groups'):
        for group_dict in data.get('groups'):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url='https://www.linkedin.com/in/manoj-kumar-thangaraj-1b7b2054/',
            mock=True
        )
    )