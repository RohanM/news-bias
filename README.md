# News Bias Rater

## Data
### All the News (AtN)
https://www.kaggle.com/datasets/snapcrack/all-the-news

Dataset of 143k American news articles. Reasonable spread of political bias, but lacking in centrist sources.

### All the News 2 (AtN2)
https://components.one/datasets/all-the-news-2-news-articles-dataset

Much larger dataset of 2.7M American news articles. Heavily left-leaning.

## Notebooks
1. fetch-media-bias.ipynb: Scrape allsides.com media bias ratings and save to CSV
2. build-dataset.ipynb: Load data from AtN and correlate with media bias ratings
3. augment-dataset.ipynb: Extract centrist publications from AtN2 to augment AtN
4. finetune.ipynb: Load data and fine tune
