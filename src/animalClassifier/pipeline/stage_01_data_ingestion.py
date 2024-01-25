from animalClassifier import logger 
from animalClassifier.components.data_ingestion import DataIngestion
from animalClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion"
class DataIngestionPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file() 



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> The {STAGE_NAME} ,has started >>>>>>>>>>>>>>>>>")
        ingest = DataIngestionPipeline()
        ingest.main()
        logger.info(f">>>>>>>>>> The {STAGE_NAME} ,has completed succesffuly >>>>>>>>>>>>>>>>> \n\n ===============")
    except Exception as e:
       logger.exception(e)
       raise e
  
