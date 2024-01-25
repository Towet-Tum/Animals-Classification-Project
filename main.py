from animalClassifier import logger
from animalClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>> The {STAGE_NAME} ,has started >>>>>>>>>>>>>>>>>")
    ingest = DataIngestionPipeline()
    ingest.main()
    logger.info(f">>>>>>>>>> The {STAGE_NAME} ,has completed succesffuly >>>>>>>>>>>>>>>>> \n\n ===============")
except Exception as e:
    logger.exception(e)
    raise e