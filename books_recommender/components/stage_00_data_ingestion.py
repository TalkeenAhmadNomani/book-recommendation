import os
import sys
from six.moves import urllib
import zipfile
import glob
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration

class DataIngestion:
    def __init__(self, app_config=AppConfiguration()):
        """
        DataIngestion Initialization
        """
        try:
            logging.info(f"{'=' * 20} Data Ingestion log started. {'=' * 20}")
            self.data_ingestion_config = app_config.get_data_ingestion_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def download_data(self):
        """
        Download ZIP file from given URL
        """
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(zip_download_dir, exist_ok=True)

            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)

            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info(f"Downloaded data successfully.")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys) from e

    def extract_zip_file(self, zip_file_path: str):
        """
        Extracts the ZIP file into the ingested_dir
        """
        try:
            ingested_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(ingested_dir, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
                logging.info(f"Extracted zip file: {zip_file_path} into dir: {ingested_dir}")

            # Log all extracted files
            for root, dirs, files in os.walk(ingested_dir):
                for file in files:
                    logging.info(f"Extracted file: {os.path.join(root, file)}")

            # Confirm required file exists
            required_files = ["BX-Books.csv", "BX-Book-Ratings.csv"]
            for file_name in required_files:
                matched_files = glob.glob(os.path.join(ingested_dir, "**", file_name), recursive=True)
                if not matched_files:
                    raise FileNotFoundError(f"{file_name} not found in extracted ZIP.")
                else:
                    logging.info(f"{file_name} found at {matched_files[0]}")

        except Exception as e:
            raise AppException(e, sys) from e

    def initiate_data_ingestion(self):
        """
        Complete ingestion pipeline: download + extract + verify
        """
        try:
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            logging.info(f"{'=' * 20} Data Ingestion completed. {'=' * 20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e
