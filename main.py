from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_modelTraining import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04_model_evluaton import ModelEvaluation

import warnings
warnings.simplefilter('ignore')
logger.info("Welcome to App Logs")

STAGE_NAME="DATA ingestion stage"


try:
    logger.info(f'>>>>>>>>stage{STAGE_NAME} started<<<<<<<<<<<')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>stage {STAGE_NAME} compleated<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="prepare base model"


try:
    logger.info(f'>>>>>>>>stage{STAGE_NAME} started<<<<<<<<<<<')
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>stage {STAGE_NAME} compleated<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="prepare base model"


try:
    logger.info(f'>>>>>>>>stage{STAGE_NAME} started<<<<<<<<<<<')
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>stage {STAGE_NAME} compleated<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Evaluating Model Using Mlflow"


try:
    logger.info(f'>>>>>>>>stage{STAGE_NAME} started<<<<<<<<<<<')
    obj=ModelEvaluation()
    obj.main()
    logger.info(f'>>>>>>stage {STAGE_NAME} compleated<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e
