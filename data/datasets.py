from torch import nn
from torch.utils.data import Dataset
import librosa

import numpy as np
import pandas as pd

import os, sys, re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from utils.constants import *

class IrmasDataset(Dataset):
    def __init__(self, dataset_path, transform=None, generate_csv=True):
        """
        Args:
            dataset_name (string): Path to a dataset
            transform (callable, optional): Optional audio transform to be applied
            generate_csv (bool): flag representing need for csv creation
        """
        self.dataset_csv = pd.read_csv(dataset_path)
        self.transform = transform

    def __len__(self):
        return len(self.dataset_csv)
    
    def __getitem__(self, idx):
        # Get sample with index `idx`
        if (torch.is_tensor(idx)):
            idx = idx.tolist()

        path = self.dataset_csv.iloc[idx, 0]
        drums = self.dataset_csv.iloc[idx, 1]
        genre = self.dataset_csv.iloc[idx, 2]
        label = self.dataset_csv.iloc[idx, 3]

        audio_sample, sample_rate = librosa.load(path)

        # Get useful data
        sample = {
            'audio': audio_sample,
            'sample_rate': sample_rate,
            'input': [],
            'label': label
        }

        # Transform the sample
        if self.transform:
            sample = self.transform(sample)

        return sample

class UrbanSounds8K(Dataset):
    def __init__(self,dataset_path, transform = None):

        self.dataset_csv = pd.read_csv(dataset_path)
        self.transform = transform
    
    def __len__(self):
        return len(self.dataset_csv)

    def __getitem__(self, index):

        if (torch.is_tensor(idx)):
            idx = idx.tolist()

        # Dataset to download...


        return None
