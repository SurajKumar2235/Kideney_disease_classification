from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.modelTraining import Training
from cnnClassifier import logger


STAGE_NAME="TRAINING THE MODEL"


class ModelTrainingPipeline:
    def __init__(self) :
        pass


    def main(self):
        config =ConfigurationManager()
        Training_config =config.get_training_config()
        training=Training(config=Training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__=="__main__":
    try:
        logger.info(f'>>>>>>>>stage{STAGE_NAME} started<<<<<<<<<<<')
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>stage {STAGE_NAME} compleated<<<<<\n\nx==========x')
    except Exception as e:
        logger.exception(e)
        raise e
        