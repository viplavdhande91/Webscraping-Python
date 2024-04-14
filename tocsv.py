import requests
from bs4 import BeautifulSoup ,NavigableString
import csv
import time
import re
outputList = []
indexList = [1,2,3,4,5,6,13,15,17,19,21,23,25,27,29,65]

def findAllchildren(property_cards):
    # if isinstance(property_cards, NavigableString) and type(property_cards) != None :
    #     outputList.append(property_cards);
    #     return
    
    # for child in property_cards.children:
    #     findAllchildren(child)
    if(property_cards is not None):

        for child in property_cards.recursiveChildGenerator():
            name = getattr(child, "name", None)
            if name is not None:
              pass
            elif not child.isspace(): # leaf node, don't print spaces
              outputList.append(child)




def IsNewLaunch(property_cards):
    regexCheck = re.search("New Launch", str(property_cards.find("span")))
    if regexCheck:
        return True
    return False


# Function to scrape properties
def scrape_properties(url,startNum):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all property cards
        posData = "srp-{0}".format(startNum)
        property_cards = soup.find('div', attrs={"data-pos": posData})

        # IsNewLaunch_ = IsNewLaunch(property_cards)
        # Starting_Price = property_cards
        findAllchildren(property_cards)
        
        finalList = []
        # print(len(outputList));

        for x in outputList:
            finalList.append(x)
            # print(x)
            # print("/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n");
            pass
            # finalList.append(x)
        # for indexValue in indexList:
        #     if(len(outputList) > 0 and indexValue < len(outputList)):
        #         finalList.append(outputList[indexValue])
        # for x in outputList:
        #     print(x)
        #     print("\n")
        outputList.clear()

        

        return finalList;
    else:
        # If the request was not successful, print an error message
        print("Failed to retrieve page")
        return None

# Function to write properties to CSV
def write_to_csv(finalProperties, filename):
    # Define fieldnames    
    # Write properties to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(finalProperties)

# URL of the webpage to scrape
url = "https://housing.com/in/buy/searches/Pskwz0ocdh7q42r5?gad_source=1&gclid=CjwKCAjw_LOwBhBFEiwAmSEQAZConyodM2LSkqj1N_iBUlBa33sNK0utT0P4iJm0X_oBJz3RIknGTxoCgBIQAvD_BwE"

# Number of times to scrape
num_scrapes = 4000

startNum = 2;
finalProperties = []
# Loop to scrape properties
for i in range(num_scrapes):
    print(f"Scraping {i+1}/{num_scrapes}")
     
    properties = scrape_properties(url ,startNum)
    finalProperties.append(properties)
    startNum += 1;
    # time.sleep(1)  # Add a delay to be polite to the server

write_to_csv(finalProperties, 'properties.csv')
print("Scraping completed and saved to properties.csv")
