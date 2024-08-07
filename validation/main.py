from dataclasses import dataclass, field
from typing import Any, List

from omegaconf import DictConfig, OmegaConf, MISSING
import hydra
from hydra.core.config_store import ConfigStore



@dataclass
class ExperimentSchema:
    model: str = MISSING
    nrof_epochs: int = 30
    learning_rate: float = 5e-3


@dataclass
class Resnet18ExperimentSchema(ExperimentSchema):
    model: str = "resnet18"
    

@dataclass
class Resnet50ExperimentSchema(ExperimentSchema):
    model: str = "resnet50"
    

@dataclass
class ConfigSchema:
    experiment: ExperimentSchema


cs = ConfigStore.instance()
cs.store(name="config_schema",node=ConfigSchema)
cs.store(group="experiment", name="resnet18_schema", node=Resnet18ExperimentSchema)
cs.store(group="experiment", name="resnet50_schema", node=Resnet50ExperimentSchema)



@hydra.main(config_name="config", config_path="configs",version_base=None)
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))




if __name__ == "__main__":
    main()



    
