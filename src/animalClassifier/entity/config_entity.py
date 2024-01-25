from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path 
    unzip_dir: Path




@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path 
    model_path: Path
    IMG_SIZE: int
    EPOCHS: int
    BATCH_SIZE: int
    INCLUDE_TOP: bool
    WEIGHTS: str