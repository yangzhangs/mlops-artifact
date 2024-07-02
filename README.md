# Artifact
Artifact package for our paper. This repository includes our data and scripts. We intend to enhance the explanation of this artifact if the paper is accepted.

## Tools
- MALLET v2.0.8
- Gensim v4.1.2
- pandas v1.5.2
- BeautifulSoup v4.11.1
- NLTK v3.8.1
- Senti4SD
- R

## Data
1. Data source (2023.06.30): SO questions and answers, GitHub Issues.
2. Tag identification method, the details of the 6 selected websites and the full list of MLOpstools/platforms are available in: `mlops-related-tags.md`
3. Data for manual classification:
- Our final dataset consists of 8,443 posts (6,345 questions and 2,098 accepted answers) and 2,103 issues. 
- `mlops_questions.csv` and `mlops_accepted_answers.csv`
- `mlops_issues.csv`
4. LDA results can be found in `lda_results.md`
5. Solution strategies and examples can be found in `solutions.md`

## Scripts
1. We use LDA topic modeling to aggregate and discover what is being discussed: 
`topic_modeling.py`
2. We use the Cox Stuart trend test to determine if each topic's yearly rate metric is increasing or decreasing over time, to a statistically significant degree:
`stats.R`
3. We use Senti4SD tool to identify the sentiment expressed in the post or issue’s text description text:
`sentiment_analysis.py`

## Figures
`popularity_trend_posts`:  The popularity trend of new posts

`popularity_trend_users`:  The popularity trend of new users
