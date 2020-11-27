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
        print("Retrieving article...")
        # use parser to parse through HTML code
        soup = BeautifulSoup(r.text, 'lxml')
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
        # write content of wikipedia page to a file
        with open('test_wiki.txt', 'w') as f:
            for i in paragraphs:
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
        selection = input("Which section will you like to learn more about?") 
    else:
        print('Error has occurred :/')

wiki_helper('harry potter')


# check = input('Is this what you were looking for?\n1. Yes, continue.\n2.No, try again.')






    
        
   
    
    
    # summary = body.find('div', {'class': 'mw-content-text'})
    # 
    
    # q = soup.find('div', {'id': 'bodyContent'})
    # print(q.find('p').text)
    # for i in l.findAll("a"):
    #     print(i.text)
    #     cont = i.get('href')
    #     link = (target + cont)





# links = []
# for i in soup.find_all(name = 'li'):
# # pull the actual link for each one
#     for link in i.find_all('a', href=True):
#         links.append(link['href'])

# links = links[1:11]
# print(links)





# return contents in navigation
# find all elements of a 

    



# TODO: ask user what specific contant they want from nav, return 
# first paragraph of the selected conetent, if wants full, 
# return full body of SC, if not, ask again what user wants   
def return_contents():
    pass

def wiki_pdf():
    pass 

def email_wiki():
    pass

# l=soup.find("ul",{"class":"searchNews"}) 

# #now we want to print only the text part of the anchor. 
# #find all the elements of a, i.e anchor 
# for i in l.findAll("a"): 
#     print(i.text)


