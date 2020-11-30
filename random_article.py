import requests 
from bs4 import BeautifulSoup
import ezgmail, os 

# a simple program to look up select wikipedia articles and save them to a pdf and email them.  
# include a command line interface so that this can be done at anytime via command line 

def wiki_helper(target):    
# fetch wiki article for user 
    req = target 
    req = req.replace(' ', '_')
    target = f'https://wikipedia.com/wiki/{req.lower()}'
    r = requests.get(target)
    r = requests.get('https://wikipedia.com/wiki/spiderman')
    if r.status_code == 200:
        wiki_article(r)
    else:
        print('An error has occurred. Press space to try again')

def wiki_article(req):
    print("Retrieving article...")
    # parse through HTML code
    soup = BeautifulSoup(req.text, 'lxml')
    # print the title of the article retrieved and a brief summary
    print('Here is the article pulled for you with a quick summary:')
    title = soup.find('h1', {'id': 'firstHeading'})
    print("Title: ",title.text)
    # retrieve main body text of wikipedia article
    paragraphs = []
    for i in soup.find_all('div', {'id': 'bodyContent'}):
        for p in i.find_all('p'):       
            paragraphs.append(p.text)
    # print out first paragraph to user         
    print("Snipit:\n", paragraphs[2])
    # retrieve main headings in the page 
    headings = []
    for i in soup.find_all('div', {'id': 'bodyContent'}):
        for i in soup.find_all('h2'):
            headings.append(i.text)
    # print out the main headings in the page
    print('Topics Covered: ')
    for i in range(len(headings)):
        print(i, headings[i])
    check = int(input("Is this what you were looking for?\n1. Yes\n2. No"))
    if check == 1:
        wiki_file(paragraphs)

    else: 
        wiki_helper()


def wiki_file(content):           
    # write content of wikipedia page to a file
    with open('test_wiki.txt', 'w') as f:
        for i in content:
            f.writelines(i)
            print('\n')
    # send an email with attached file
    # initiate ezgmail         
    ezgmail.init()
    # ask for credentials from user
    email = input('Input the email you will like to have a copy of the document sent to.')
    subject = input('Input a subject line')
    message = input('Input a message...press enter to continue when done.')
    text_doc = 'test_wiki.txt'
    ezgmail.send(email, subject, 'Here is a copy of your wikipedia article!', [text_doc])

# example
wiki_helper('harry potter')
