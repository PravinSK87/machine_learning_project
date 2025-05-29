from collections import namedtuple

DataInjectionConfig = namedtuple("DataInjectionConfig",
                                 ["data_set_url","tgz_download_dir","raw_data_dir","train_dir","test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",["Schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                  "transformed_train_dir",
                                                                  "transformed_test_dir",
                                                                  "preprocessed_object_file_path"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])