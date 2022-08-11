# This code will be used to scrape the Box Office Mojo website for opening weekend performance


import requests
from bs4 import BeautifulSoup as BS
import re


#url request. Must insert url with quotations "url"
def html_parser(url):
    page_data = requests.get(url)
    soup = BS(page.content, 'html.parser')
    return soup
  
# This function scrapes the movie titles
def movie_titles (soup):
    movie_names=soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide')
    movie_titles = []
    for name in movie_names:
        try:
            movie_titles.append(name.string)
        except:
            movie_titles.append('NAN')
            continue
    return movie_titles
  
# This function scrapes the opening weekend gross revenue
def opening_weekend_gross (soup):
    gross_opening=soup.find_all('td', class_='a-text-right mojo-field-type-money')
    
    opening_weekend = [record.string for record in gross_opening]
  
    opening_figures = []
    for record in opening_weekend:
        try:
            parsed_amount = re.sub('\W+','', record)
            opening_figures.append(int(parsed_amount))
        except:
            opening_figures.append(record)
            
    all_opening_figures = []
    for record in opening_figures:
        if type(record) == int:
            all_opening_figures.append(record)
        else:
            all_opening_figures.append('NAN')
            continue
    return all_opening_figures
  
# This code extracts both the release date and the closing date for each movie
def release_and_closing_dates (soup):
    opening_and_closing_date=soup.find_all('td', class_='a-text-left mojo-field-type-date a-nowrap')
    opening_dates = []
    closing_dates = []
    i = 0
    for record in opening_and_closing_date:
        if i % 2 == 0:
            try:
                opening_dates.append(record.string)
            except:
                opening_dates.append('NAN')
        else:
            try:
                closing_dates.append(record.string)
            except:
                closing_dates.append('NAN')
        i += 1            
    return opening_dates, closing_dates

# This function creates a tuple to combine all the different pieces of data extracted together, so it can be inserted into a database and written out to a dataframe. 
def create_tuples(movie_titles, all_opening_figures, release_and_closing_dates, year):
    combined_dataset = []
    i=0
    for record in range(len(movie_titles)):
        new_tuple = (movie_titles[i],all_opening_figures[i], release_and_closing_dates[0][i], release_and_closing_dates[1][i], year)
        combined_dataset.append(new_tuple)
        i += 1
    return combined_dataset

# This is the main function which joins all the previous supporting functions together and runs them in sequence to create a full database with all the relevant records in it
def extract_opening_weekend_data (url, year):
    soup = html_parser(url)
    movie_title = movie_titles(soup)
    all_opening_figures = opening_weekend_gross(soup)
    opening_closing_dates = release_and_closing_dates(soup)
    final_dataset = create_tuples (movie_title, all_opening_figures, opening_closing_dates, year)
    return final_dataset

    
    
