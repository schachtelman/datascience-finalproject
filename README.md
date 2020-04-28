# Data Science - Final Project
The final project for the Data Science course.

The general topic is to find out something interesting about the alcohol consumption of humans. We will fix a more specific topic and hypothesis once we have an overview of available datasets.

## Ideas

### Gin Score Predictor (Genie)

It would be nice to predict how well a certain mixture of gin-tonic (or drink in general) is received by a thirsty customer. This score could for example be used to build a basic recommender system as well. We could build a basic system were the user can select ingredients for his/her drink and his/her age, etc. and then predict how likely it is that the user likes the drink. 

#### Dataset

[Statista](https://de.statista.com/statistik/daten/studie/171629/umfrage/mindestens-einmal-im-monat-konsumierte-spirituosen/) seems to have quite a large selection of surveys on how people like to consume their alcohol (favorite brands, favorite drink, amount of cosumption, etc.). From this we could infer some simple score based on the brands and drinks used in the mixture.

Maybe we also find some demographic data on alcohol consumption and attitudes towards certain drinks. Then we could include a score based on the age, gender, education status of the user as well. 

[Beer, Liquor and Wine reviews](https://www.kaggle.com/datafiniti/wine-beer-and-liquor-reviews) 

#### Questions

* Which age groups prefer which alcoholic drinks?

### Student Alcohol Consumption

Answer questions about alcohol consumption of students. Nice and tidy dataset.

#### Dataset

[Kaggel Dataset](https://www.kaggle.com/uciml/student-alcohol-consumption)

### Beer Taste Profile

Get and idea of the taste profile of beer.

#### Dataset

1.5 Million beer reviews. A lot of info on taste profile. Breweries and name/style of beer are also given. Maybe we can expand it by location etc. Unfortunately only username given as info. We could also add gender, age, location of users (data is available on beeradvocate website).
[Beer Advocate Reviews](https://data.world/socialmediadata/beeradvocate)

##### Columns

`review_time` is given as a UNIX timestamp
`beer_abv` is alcohol by volume

Added country of breweries with the help of a scraper. 15 ids did not corresponds to an active brewery on the website ([1930, 5318, 1548, 3257, 1549, 10097, 1193, 5379, 9343, 18968, 10099, 1953, 3817, 27, 23980]). This is no problem, as we have a total of 5840 breweries.

#### Questions
* Which user did the most reviews?
* Which user did the most positive reviews on average?
* Which style of beer is the most liked one?
* Which beer is the most liked one?
* Which region produces the best beer (if we mange to get the region in our dataset)?
* Which style of beer is most liked in Austria?
* Which beer is the most disliked one?
* How did the reviews change over the 10 year period of the dataset?
* How do the ratings change with the alcohol content?
* Which brewery produces the strongest beers?
* Which brewery produces the best / worst beers?

