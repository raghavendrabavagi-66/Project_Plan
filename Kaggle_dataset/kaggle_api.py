import os
os.environ['KAGGLE_CONFIG_DIR'] = '/Users/raghavendra2/Desktop/Kaggle_dataset'

import kaggle
kaggle.api.authenticate()


import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('mmohaiminulislam/ecommerce-data-analysis', path='./Datasets_Folder', unzip=True)