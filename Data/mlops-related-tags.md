## MLOps-related tags identification

- We set the initial set of tags as 𝑇0={“ `mlops`”}; 

- To extend the initial tags set, we make a query in Google with the following two search terms “top MLOps tools” and “top MLOps platforms”. We select the first 3 search
results for each query that contain various websites ranked the best MLOps tools/platforms (searched on June 30, 2023).
  - The websites of “top MLOps tools”:
    - https://www.datacamp.com/blog/top-mlops-tools
      - `MLFlow, Comet ML, Weights&Biases, Prefect, Metaflow, Kedro, achyderm, Data Version Control, TensorFlow Extended (TFX) Serving, BentoML, Cortex, Evidently, Fiddler, Censius AI, AWS SageMaker, DagsHub, Kubeflow`
    - https://www.projectpro.io/article/best-mlops-tools-/574
      - `MLflow, Comet ML, Data Version Control, Pachyderm, Optuna, Sigopt, Kubeflow, Apache Airflow, BentoML, Cortex`
    - https://www.kdnuggets.com/2022/10/top-10-mlops-tools-optimize-manage-machine-learning-lifecycle.html
      - `Amazon SageMaker, Azure Machine Learning, Databricks ml, MLflow, TensorFlow Extended (TFX), MLFlow, Google Cloud ML Engine, Data Version Control (DVC), H2O Driverless AI, Kubeflow, Metaflow`

  - The websites of “top MLOps platforms”:
    - https://www.infoworld.com/article/3572442/10-mlops-platforms-to-manage-the-machine-learning-lifecycle.html
      - `Algorithmia, Amazon SageMaker, Azure Machine Learning, Domino Data Lab, Google Cloud AI Platform, HPE Ezmeral ML Ops, Metaflow, MLflow, Paperspace, Seldon`
    - https://www.kdnuggets.com/2022/10/top-10-mlops-tools-optimize-manage-machine-learning-lifecycle.html
      - `Amazon SageMaker, Azure Machine Learning, Databricks MLflow, TensorFlow Extended (TFX), MLFlow, Google Cloud ML Engine, Data Version Control (DVC), H2O Driverless AI, Kubeflow, Metaflow`
    - https://geekflare.com/best-mlops-platforms/
      - `MLFlow, Azure Machine Learning, Google Vertex AI, Databricks, AWS SageMaker, DataRobot, Run AI, H2O.ai, Paperspace Gradient`

- To avoid incidental references, we only consider tools/platforms that are listed on at least two websites.
This yields a list of 15 top MLOps tools/platforms:
  - `MLFlow, Metaflow, Data Version Control, AWS SageMaker, Kubeflow, Azure Machine Learning, Google Cloud ML Engine, Comet ML, TensorFlow Extended (TFX) Serving, Cortex, BentoML, H2O Driverless AI, Paperspace Gradient, Databricks, Pachyderm`

- For each of these MLOps tools/platforms, we search for SO tags. We filter out tools/platforms that have no associated SO tags (e.g, ‘Paperspace’) or have rarely used tags (less than 50 posts, e.g., ‘Comet ML’). After this filtering, we find 7 SO tags
({“`mlflow`”, “`dvc`”, “`tfx`”, “`amazon-sagemaker`”, “`kubeflow`”, “`azure-machine-learning-service`”, “`google-cloud-ml-engine`”}) that related to MLOps and add them to 𝑇0;

- Then, we go through the dataset 𝑆 and extract a subset of posts 𝑃 whose tags match at least one tag in 𝑇0;

- We obtain the tags of all posts in 𝑃 (denoted as 𝑇1) to extend the initial tag set 𝑇0, including as many relevant tags as possible. Following prior studies, we use two heuristics 𝛼 and 𝛽 to refine 𝑇1 by keeping tags that
are significantly relevant to MLOps and excluding others. The 𝛼 and 𝛽 measure the significance and relevance of a tag 𝑡 in 𝑇1, respectively.

After these processing steps, we obtain the final tag set 𝑇 ={“`mlops`”, “`mlflow`”, “`dvc`”, “`tfx`”, “`amazon-sagemaker`”, “`kubeflow`”, “`azure-machine-learning-service`”, “`google-cloud-ml-engine`”, “`kubeflow-pipelines`”, “`azureml-python-
sdk`”, “`amazon-sagemaker-studio`”}.
