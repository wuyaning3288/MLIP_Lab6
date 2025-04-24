import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    X_train, X_test, y_train, y_test = data_split(*feature_target_sample)
    # The returned tuple should contain 4 elements
    assert len((X_train, X_test, y_train, y_test)) == 4

    # The total number of samples after split should equal the original sample size
    n = feature_target_sample[0].shape[0]
    assert X_train.shape[0] + X_test.shape[0] == n
    assert y_train.shape[0] + y_test.shape[0] == n

    # The feature column names should remain unchanged
    original_cols = list(feature_target_sample[0].columns)
    assert list(X_train.columns) == original_cols
    assert list(X_test.columns)  == original_cols

    # Samples in X and y should have matching indices for train and test sets
    assert all(X_train.index == y_train.index)
    assert all(X_test.index  == y_test.index)
