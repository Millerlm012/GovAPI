# retrieves all gov. data from https://www.nga.org/governors/

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests


# retrieving all info for gov.
def retrieve_info():

    # initializing chromedriver
    url = "https://www.nga.org/governors/"
    #options = Options()
    #options.headless = True
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.switch_to.window(driver.window_handles[0])

    # navigating to gov url
    driver.get(url)

    # retrieving all urls with more details about each gov. and storing in list
    detail_urls = []
    div = driver.find_elements_by_class_name('current-governors__wrapper a')
    for element in div:
        detail_urls.append(element.get_attribute('href'))

    '''
            CSV File Layout:
            State | Gov. Name | Address | Phone Number | Fax | Media Contact | State-Federal Contact
    '''

    # creating df to hold gov. data
    gov_info_df = pd.DataFrame(columns=(
                                    'State',
                                    'Gov. Name',
                                    'Address',
                                    'Phone Number',
                                    'Fax',
                                    'Media Contact',
                                    'State-Federal Contact',
                                    'Gov. Website',
                                    'Gov. Bio',
                                    'State Website',
                                    'Coronavirus Resources'))


    # setting headers to allow us to request page html
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    for url in detail_urls:
        # navigating selenium driver to additional details page
        driver.get(url)

        # requesting page html info with requests
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        # parsing html to find state name and gov. name
        name_and_state = soup.find('div', attrs={'class': 'hero-post__container__right hero-post__container__right--lg'})
        # retrieves state
        state_name = name_and_state.get_text().splitlines()[1]
        # retrieves gov. name
        gov_name = name_and_state.get_text().splitlines()[2]

        # parsing html to find address, phone number, fax, media contact, and state-federal contact
        contact_info = soup.find('div', attrs={'class': 'page-publication__sidebar__group'})
        # retrieves gov. address
        gov_address = contact_info.get_text().splitlines()[7]
        # retrieves gov. phone number
        gov_phone_number = contact_info.get_text().splitlines()[12]
        # retrieves gov. fax number
        try:
            gov_fax_number = contact_info.get_text().splitlines()[17]
        except IndexError:
            'Gov. did not have fax'
            gov_fax_number = 'N/A'
        # retrieves gov. media contact
        try:
            gov_media_contact = contact_info.get_text().splitlines()[22]
        except IndexError:
            'Gov. did not have media contact'
            gov_media_contact = 'N/A'
        # retrieves gov. state-federal contact
        try:
            gov_state_federal_contact = contact_info.get_text().splitlines()[27]
        except IndexError:
            'Gov. did not have federal contact'
            gov_state_federal_contact = 'N/A'


        # retrieving additional website links and storing them in additional urls list
        additional_urls = []
        additional_links = driver.find_elements_by_class_name('page-publication__sidebar__group a')
        for element in additional_links:
            additional_urls.append(element.get_attribute('href'))

        try:
            gov_website = additional_urls[0]
        except:
            'Gov. does not have a website'
            gov_website = 'N/A'
            additional_urls.append(gov_website)
        try:
            gov_bio = additional_urls[1]
        except IndexError:
            'Gov. does not have a bio website'
            gov_bio = 'N/A'
            additional_urls.append(gov_bio)
        try:
            state_website = additional_urls[2]
        except IndexError:
            'Gov. does not have a state website'
            state_website = 'N/A'
            additional_urls.append(state_website)
        try:
            covid_resources = additional_urls[3]
        except IndexError:
            'Gov. does not have a covid resources page'
            covid_resources = 'N/A'
            additional_urls.append(covid_resources)

        data = pd.DataFrame({
                            'State': [state_name],
                            'Gov. Name': [gov_name],
                            'Address': [gov_address],
                            'Phone Number': [gov_phone_number],
                            'Fax': [gov_fax_number],
                            'Media Contact': [gov_media_contact],
                            'State-Federal Contact': [gov_state_federal_contact],
                            'Gov. Website': [additional_urls[0]],
                            'Gov. Bio': [additional_urls[1]],
                            'State Website': [additional_urls[2]],
                            'Coronavirus Resources': [additional_urls[3]]})


        gov_info_df = gov_info_df.append(data, ignore_index = True)

    gov_info_df.to_csv('/Users/lmiller/PythonProjects/GovAPI/gov_info_df.csv')


if __name__ == "__main__":
    retrieve_info()
