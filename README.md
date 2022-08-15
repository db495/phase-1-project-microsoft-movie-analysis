# Microsoft Corp. Movie Studio Analysis

**Author**: [David Boyd](mailto:dboyd580@gmail.com)


## Overview

Microsoft is looking to open up their own movie studio, but don't know anything about movies to know where they should invest their efforts in. This project looks at data from various sources, ranging from IMDB, Rotten Tomatoes, Movie Budgets and gathering additional data from Box Office Mojo to understand the answers to the following questions:

- Which genre has the best ROI
- What movie rating gets the best reviews on rotten tomatoes?
- Should they focus on family friendly or non-family friendly movies?
- How long should the movie last?
- Which month of the year is the best to release a movie, both for overall ROI and best opening weekend sales?

We can see that in the US the best genres to produce for ROI are Horror/Thriller movies due to their low production costs. Afterwards, it is mainly Comedy, Romance & Drama films. When looking at gross revenue, we can see that Action/Adventure/Sci-Fi based movies rank highest. The movie ratings with the best Rotten Tomatoes score is NR, followed by R & PG. Movies should last no longer than 135 minutes and the best months to release movies is January & February for opening weekend % of return. For gross revenue, the best month to release is May/June.


## Business Problem

I have been tasked with providing recommendations to Microsoft around what type of movies perform best so they know where to invest their budgets when launching a movie studio to get good returns. In order to do this, I focused on the main questions to be able to answer:

- Which genre has the best ROI
- What movie rating gets the best reviews on rotten tomatoes?
- Should they focus on family friendly or non-family friendly movies?
- How long should the movie last?
- Which month of the year is the best to release a movie, both for overall ROI and best opening weekend sales?

The reason I chose these questions is because, since Microsoft is new to the industry, it is important to focus on understanding the different metrics and measures that revolve around them being able to make money from their films. This is why focusing on ratings, length of movies, genres and month of release are important, as they all factor into overall return on investment. This is important, as movies are very expensive ventures, so unless they have an ulterior motive (to attract a new demographic, target audience for other products) the business should be profit making.


## Data

There are a range of sources being used with the data, these range from rating data both from IMDB and Rotten Tomatoes, production & revenue values from The Numbers movie budgets and opening weekend revenue from Box Office Mojo. Across these different sources we're able to calculate metrics around movie ratings, ROI, time in cinema, genres, runtime which can be used to answer the questions set above


## Data Preparation

To prepare the data, each dataset had it's own set of requirements, whether it was drop some columns, as they either didn't have enough data in them, or they weren't relevant to the questions I was trying to answer. Reformat columns and change datatypes from objects to either integers, or datetime. To make the code cleaner, all of the necessary commands were added into a seprate python script to be imported and ran below.

There were some outliers in the IMDB data when it came to the runtime field, these were handled by excluding all values which went above a reasonable figure of 4 hours, as everything else is unrealistic and likely a data entry error.

## Data Modelling

After the data was cleaned and ready to model, I split the data into two different final datasets, the first being related to the ROI of each movie, this was done through joining the Movie budgets dataset with my opening weekend scraped data. This was then combined with the imdb data to collect features such as genre and director name.

The other dataset focused on our Rotten Tomatoes data and all the reviews related to each movie.

Once the datasets were joined, the next step was doing some feature engineering to create new columns and then create aggregations by Genre, Movie Rating, Director, Writer, Year of release & Month of release. This allowed for the charts below to be created.


## Results

When looking at which genre has the highest domestic_gross and ROI. **Action/Adventure/Sci-fi** scored the best in the US for revenue generated. When looking at ROI purely, across all markets **Thriller and Horror** movies had the **highest ROI**, due to the low production costs associated. When looking at IMDB ratings, for the top ten highest grossing genre combinations, **Action/Adventure/Sci-fi** remained in the top three, showing not only does it drive large revenues, but is also rated highly in customer reviews. These should be the main genre groups to focus on when creating new projects and content.

![total_production_spend_per_genre](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/images/total_production_spend_per_genre.png)

![imdb_rating_by_genre](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/images/imdb_rating_by_genre.png)

When you start to look at how long a movie should run and which month in the year is the best in gross revenue and also highest % returns on opening weekend box office sales. We can see that movies have on average continued to get longer and longer throughout the decade, with the longest movies now sitting at **180 minutes in 2013**. We recommend movies should be created **no longer than 135 minutes** to remain profitable.

![runtime_avg_by_year](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/images/runtime_avg_by_year.png)

In terms of the best month to release your movie, we can see that both the summer and winter festive season have the highest production costs attached, however when you look at the % of returns from opening weekend box office sales, we can see that on average only **10% of production costs are reclaimed** for movies released in **December**, this pales in comparison to the **23-24%** which can be reclaimed for movies launching between **May & June**.

![total_spend_opening_weekend_perc_by_month](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/images/total_spend_opening_weekend_perc_by_month.png)

Finally, after looking which genre to produce, how long to make the movie and when to release the movie, we turn our attention to understand what movie rating performs the best in terms of critic ratings on Rotten Tomatoes, a popular movie review site, which might have a direct correlation between their score and overall box office revenues. We can see below that NR, R & PG rated movies have the best ratings and amount of movies being released, so they should focus writing content within these rating guidelines.

![rotten_tomatoes_rating_by_rating_group](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/images/rotten_tomatoes_rating_by_rating_group.png)


## Conclusions
#### Key Findings:
- Movies that aren't family friendly have the higher Rotten Tomatoes score. When broken down deeper we can see this is largely driven from "NR" based movies. The three best rated movie ratings to produce are **G, NR & PG**
- Movies lengths are getting longer over time, make sure to keep your movie **less than 135 minutes** but **over 105-110 minutes**
- The best months to release a movie, varies depending on how quickly you want to get returns. If you care about overall domestic ROI, is June, followed closely by Dec, Jan and Feb. When coupled with what % of sales can be made on the opening weekend, the best two months to release movies on are Jan & Feb, followed by June, due to the massive difference in production budgets.
- In the US, the best ROI genre focuses around **thriller based movies**, due to **low production costs**, in terms of having a large amount of movies with a good domestic ROI, you should focus on Comedy,Drama,Romance based movies.If you also want to consider overall gross, then you should focus on **Action,Adventure,Sci-Fi**.

    - Internationally they should also consider the following genres: 
         - **Adventure,Animation,Comedy**
         - **Action,Adventure,Sci-Fi**
         - **Comedy,Romance**
         - **Drama,Thriller**

#### Limitations:
With the datasets given the limitations occur when trying to connect different data sources together, as there was a loss rate of ***at least 40%*** with each join, meaning the dataset we're able to analyse at the end is only a subset of the data. There were also a lot of other metrics/pieces of relevant information missing that would help enrich the analysis.

#### Future analysis 
- Explore what is the distribution between cinema sales & DVD sales
- Explore what type of movie (animation, etc) drives the best ROI
- See if there is a correlation between rotten tomatoes score & ROI
- What are the most common traits of movies in the top grossing films
- Which countries outside of the US gross the highest % for movies & does it differ by genre? To understand where they should release their movies next & make sure translations are sourced early to increase ROI
- Once defining that G rated movies have the best rating, scrape movie names, directors & writers from that list to get the best performing directors & writers to hire

## For More Information

The full analysis is located in the Jupyter Notebook or review this summary [presentation](https://github.com/db495/phase-1-project-microsoft-movie-analysis/blob/master/presentation.pdf)).

For additional info, contact David Boyd at [dboyd580@gmail.com](mailto:dboyd580@gmail.com)


## Repository Structure

```
├── ZippedData
├── images
├── src
├── README.md
├── presentation.pdf
├── Microsoft-Movie-Analysis-Summary.ipynb
└── EDA-Notebook.ipynb
```
