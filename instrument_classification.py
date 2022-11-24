import os
import argparse
import shutil
import time

import numpy as np
import torch

from train import TrainNeuralNetwork

import utils.utils as utils
from utils.constants import *

# TODO complete
def train(config):
    trainNeuralNet = TrainNeuralNetwork(config=config)
    trainNeuralNet.startTrain()

def test(config):
    pass

def custom_test(config):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Common params
    parser.add_argument("--type", choices=[m.name for m in ModelType], type=str, help="Input TRAIN, TEST or CUSTOM_TEST for type of classification", default=ModelType.TRAIN.name)
    parser.add_argument("--model_name", choices=[m.name for m in SupportedModels], type=str, help="Neural network (model) to use", default=SupportedModels.LINEAR.name)
    parser.add_argument("--make_csv", help="Generate csv files for training, validation and test", default=True, action=argparse.BooleanOptionalAction)

    # Wrapping configuration into a dictionary
    args = parser.parse_args()
    config = dict()
    for arg in vars(args):
        config[arg] = getattr(args, arg)

    # Generate csv if --make_csv is included
    if (config['make_csv']):
        print("?")
        utils.parseIrmasDataset(irmas_csv_path=IRMAS_DATASET_DIRECTORY, dataset_path=IRMAS_SINGLE_INST_DATASET_PATH)
    
    if config['type'] == "TRAIN" or config['type'] == "TRAIN_AND_TEST":
        train(config)
    elif config['type'] == "TEST" or config['type'] == "TRAIN_AND_TEST":
        test(config)
    elif config['type'] == "CUSTOM_TEST":
        custom_test(config)
    