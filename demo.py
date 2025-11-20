import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
from mlflow.models.signature import infer_signature
import mlflow.sklearn
import dagshub
import logging
import dagshub

#dagshub.init(repo_owner='bappymalik4161', repo_name='mlflow-test', mlflow=True)

dagshub.auth.clear_token_cache(force=False)
#mlflow.end_run()