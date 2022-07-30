# This code will be used to scrape the Box Office Mojo website for opening weekend performance


import requests
from bs4 import BeautifulSoup as BS
import requests
import sqlite3
from datetime import datetime
from dateutil.parser import parse
import re

conn = sqlite3.connect('movie_opening_weekend.db')
cursor = conn.cursor()

#url request. Must insert url with quotations "url"
def request_func (url):
    page = requests.get(url)
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
    i = 0
    opening_weekend = []
    for record in gross_opening:
        if i % 2 != 0:
            opening_weekend.append(record.string)
        else 
          continue
        i += 1
        
    opening_figures = []
    for record in opening_weekend:
        try:
            parsed_amount = re.sub('\W+','', record)
            opening_figures.append(int(parsed_amount))
        except:
            opening_figures.append(record)
            
    all_opening_figures = []
    for record in opening_figures:
        if type(item) == int:
            all_opening_figures.append(item)
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
             continue
        else:
          try:
             closing_dates.append(record.string)
          except:
              closing_dates.append('NAN')
             continue
        i += 1
            
    opening_dates_clean = []
    closing_dates_clean = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_dic = {month:f"{datetime.datetime.strptime(month, '%b').month:02}" for month in months}
    
    
# WIP to get the cleaned versions of dates
            
    return opening_dates_clean, closing_dates_clean

# This function creates a tuple to combine all the different pieces of data extracted together, so it can be inserted into a database and written out to a dataframe. 
def create_tuples(movie_titles, all_opening_figures):
    combined_dataset = []
    for record in range(len(movie_titles)):
        new_tuple = (movie_titles[i],all_opening_figures[i], opening_dates_clean, closing_dates_clean)
        combined_dataset.append(new_tuple)
    return combined_dataset
  
# This function adds the tuples to the created database
def add_to_database (conn, cursor, combined_dataset):
    statement = """INSERT INTO mojo_data (title, opening_earnings, opening_date, closing_date) 
    VALUES (%s, %s, %s, %s)"""
    cursor.executemany(statement, combined_dataset)
    conn.commit()

# This is the main function which joins all the previous supporting functions together and runs them in sequence to create a full database with all the relevant records in it
def extract_opening_weekend_data (url):
    soup = request_func(url)
    movie_titles = movie_titles(soup)
    opening_numbers_with_none = opening_weekend_gross(soup)
    opening_closing_dates = release_and_closing_dates(soup)
    final_dataset = create_tuples (movie_titles, all_opening_figures)
    add_to_database(conn, cursor, final_dataset)
    return final_dataset

    
    
