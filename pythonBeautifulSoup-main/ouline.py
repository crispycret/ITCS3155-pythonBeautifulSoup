#import beautifulsoup and request here
from bs4 import BeautifulSoup
import json
import requests
def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here 
    status = requests.get(url)
    job = BeautifulSoup(status.content, 'html.parser')
    jobTitle = job.find('h2', class_= 'jobTitle').text
    print(jobTitle)

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()
    getJobList(role, location)
    print("Role: " + role + ", Location: " + location)
    # Complete the missing part of this function here
    
if __name__ == '__main__':
    main()
