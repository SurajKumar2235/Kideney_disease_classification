from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

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