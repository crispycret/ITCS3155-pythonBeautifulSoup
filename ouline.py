import os, sys, json
from collections import namedtuple
from textwrap import indent
from attr import attrs 
from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS


def displayJobDetails(jobDetails):
    print("Display job details")
    for job in jobDetails:
        print ()
        pprint(list(job), indent=4)





#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    # Modified url by prefixing the string with `f` which tells python that this string should be formatted with the decalred variables.
    url = f'https://www.indeed.com/jobs?q={role}&l={location}'

    # Complete the missing part of this function here

    # Make the request to the url with the user paramers formatted in
    response = requests.get(url)

    # If the response status code is not `OK` raise an exception
    if (response.status_code != 200):
        raise Exception("getJobList: Unexpected request status %d. Exiting" % response.status_code)

    # Soupify the response content
    soup = BS(response.text,'html.parser')

    # Create a named tuple to cleanly store extracted job dat
    Job = namedtuple ("Job", ['job_title', 'company_name', 'description', 'salary'])

    # List to store the extracted jobs
    jobs = []

    # Narrow the score of search by selecting all job containers
    job_containers = soup.find_all('div', class_='job_seen_beacon')

    # Raise an exception if no jobs were found
    if (len(job_containers) == 0):
            raise Exception("getJobList: No jobs were found. Exiting")


    # For each container extract all the wanted information and store as a `Job` 
    for container in job_containers:

        # Some entries lack the salary information and are replaced with `N/A` 
        try:
            salary = container.find('div', attrs={'class': 'salary-snippet-container'}).text
        except:
            salary = "N/A"

        jobs.append( 
            Job(
                container.find('h2', attrs={'class': 'jobTitle'}).find_all('span')[-1].text,
                container.find('span', attrs={'class': 'companyName'}).text,
                container.find('div', attrs={'class': 'job-snippet'}).text,
                salary
            )
        )

    return jobs




#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    
    with open('jobDetails.json', 'w') as f:
        f.write(json.dumps(jobDetails))

    return



#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    # role = input()
    role = "software engineer"

    # Complete the missing part of this function here
    print("\nEnter the location you want to search")
    # location = input()
    location = "charlotte"

    print("\nRole: %s\nLocation: %s\n" % (role, location))

    jobDetails = getJobList(role, location)

    displayJobDetails(jobDetails)

    # saveDataInJSON(jobDetails)





if __name__ == '__main__':
    main()
