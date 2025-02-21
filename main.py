from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    ingest_data = DataIngestionTrainingPipeline()
    ingest_data.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    validate_data = DataValidationTrainingPipeline()
    validate_data.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    transform_data = DataTransformationPipeline()
    transform_data.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    train_model = ModelTrainerTrainingPipeline()
    train_model.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    evaluate_model = ModelEvaluationPipeline()
    evaluate_model.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

