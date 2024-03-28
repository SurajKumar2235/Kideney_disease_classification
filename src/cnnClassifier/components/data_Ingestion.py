import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import get_size

from kaggle.api.kaggle_api_extended import KaggleApi

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.dataset_name
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            print(">>>>>>>>>>>>>>>>>------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<")
            # file_id = dataset_url.split("/")[-2]
            # prefix = 'https://drive.google.com/uc?/export=download&id='
            # gdown.download(prefix+file_id,zip_download_dir)
            api = KaggleApi()
            api.authenticate()

            # Replace 'dataset_owner/dataset_name' with the actual owner and name of the dataset
            dataset_name = 'nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone'

            # Download the dataset
            api.dataset_download_files(dataset_name)



            api.dataset_download_files(dataset_name, path=self.config.root_dir)  # Specify the download path

            # Rename the downloaded file to data.zip
            # downloaded_files = os.listdir(zip_download_dir)
            # for file in downloaded_files:
            #     if file.endswith('.zip'):
            #         os.rename(os.path.join(zip_download_dir, file), os.path.join(zip_download_dir, 'data.zip'))
            #         break  # Exit the loop after renaming the first zip file


            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)