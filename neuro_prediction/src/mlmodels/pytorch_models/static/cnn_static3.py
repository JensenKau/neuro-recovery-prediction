from __future__ import annotations
from typing import Dict, Any
import math

from optuna import Trial
import torch
from torch import nn, Tensor

from src.mlmodels.pytorch_models.static.static_model import StaticModel


class CnnStatic3(StaticModel):
    class InternalModel(nn.Module):
        def __init__(
            self, 
            out_chn1: int = 5,
            kernel1: int = 3,
            stride1: int = 1,
            relu1: bool = False,
            out_chn2: int = 5,
            kernel2: int = 3,
            stride2: int = 1,
            relu2: bool = False,
            out_chn3: int = 5,
            kernel3: int = 3,
            stride3: int = 1,
            relu3: bool = False,
            pooling: int = 1,
            linear_layers: int = 2
        ) -> None:
            super().__init__()
            dimension0 = 22
            padding1 = math.ceil((21 * stride1 + kernel1 - dimension0) / 2)
            dimension1 = math.floor(((dimension0 + 2 * padding1 - (kernel1 - 1) - 1) / stride1) + 1)
            padding2 = math.ceil((21 * stride2 + kernel2 - dimension1) / 2)
            dimension2 = math.floor(((dimension1 + 2 * padding2 - (kernel2 - 1) - 1) / stride2) + 1)
            padding3 = math.ceil((21 * stride3 + kernel3 - dimension2) / 2)
            dimension3 = math.floor(((dimension2 + 2 * padding3 - (kernel3 - 1) - 1) / stride3) + 1)
            dimension4 = math.floor(((dimension3 - (pooling - 1) - 1) / pooling) + 1)
            linear_size = dimension4 * dimension4 * out_chn3
            
            layers = [
                nn.Conv2d(1, out_chn1, kernel1, stride1, padding1),
                nn.ReLU() if relu1 else None,
                nn.Conv2d(out_chn1, out_chn2, kernel2, stride2, padding2),
                nn.ReLU() if relu2 else None,
                nn.Conv2d(out_chn2, out_chn3, kernel3, stride3, padding3),
                nn.ReLU() if relu3 else None,
                nn.MaxPool2d(pooling) if pooling > 1 else None,
                nn.Flatten()
            ] + {
                1: [nn.Linear(linear_size, 2)],
                2: [nn.Linear(linear_size, 1000), nn.Linear(1000, 2)],
                3: [nn.Linear(linear_size, 1000), nn.Linear(1000, 250), nn.Linear(250, 2)],
            }[linear_layers] + [
                nn.Softmax(1)
            ]
                        
            self.stack = nn.Sequential(*list(filter(lambda x: x is not None, layers)))
            
        
        def forward(self, static_fc: Tensor) -> Tensor:
            return self.stack(torch.unsqueeze(static_fc, 1))
    
    
    
    
    def __init__(self) -> None:
        super().__init__("cnn_static3", self.InternalModel)
    
    
    def objective(self, trial: Trial) -> Dict[str, Any]:
        epoch = trial.suggest_categorical("epoch", [100, 150, 200, 250, 300])
        out_chn1 = trial.suggest_int("out_chn1", 2, 10)
        kernel1 = trial.suggest_int("kernel1", 2, 5)
        stride1 = trial.suggest_int("stride1", 1, kernel1)
        relu1 = trial.suggest_categorical("relu1", [True, False])
        out_chn2 = trial.suggest_int("out_chn2", out_chn1 + 1, 20)
        kernel2 = trial.suggest_int("kernel2", 2, 5)
        stride2 = trial.suggest_int("stride2", 1, kernel2)
        relu2 = trial.suggest_categorical("relu2", [True, False])
        out_chn3 = trial.suggest_int("out_chn3", out_chn2 + 1, 30)
        kernel3 = trial.suggest_int("kernel3", 2, 5)
        stride3 = trial.suggest_int("stride3", 1, kernel3)
        relu3 = trial.suggest_categorical("relu3", [True, False])
        pooling = trial.suggest_int("pooling", 1, 5)
        linear_layers = trial.suggest_int("linear_layers", 1, 3)
        
        return trial.params
    
    

if __name__ == "__main__":
    pass