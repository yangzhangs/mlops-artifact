# Artifact
Artifact package for our paper. This repository includes our data and scripts.

## Data
1. Data source (2023.06.30): SO questions and answers.
2. Tag identification method: see `mlops-related-tags.md`
3. Data for manual classification:
- Our final dataset consists of 8,443 posts (6,345 questions and 2,098 accepted answers)
- `mlops_questions.csv` and `mlops_accepted_answers.csv`
4. Random sample size for each topic can be found in `sample-size-per-topic.md`
5. Solution strategies and examples can be found in `solutions.md`

## Scripts
We use LDA topic modeling to aggregate and discover what is being asked in the SO questions: `topic_modeling.py`

## Figures
`popularity_trend_posts`:  The popularity trend of new posts

`popularity_trend_users`:  The popularity trend of new users
