from animalClassifier.constants import *
from animalClassifier.utils.common import read_yaml, create_directories
from animalClassifier.entity.config_entity import DataIngestionConfig, TrainingConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion 
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training 
        params = self.params
        create_directories([config.root_dir])

        training_config = TrainingConfig(
            root_dir=Path(config.root_dir),
            model_path=config.model_path,
            EPOCHS=params.EPOCHS,
            WEIGHTS=params.WEIGHTS,
            IMG_SIZE=params.IMG_SIZE,
            BATCH_SIZE=params.BATCH_SIZE,
            INCLUDE_TOP=params.INCLUDE_TOP
        )
        return training_config
