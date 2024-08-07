from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class LostFunctionConfig:
    _target_: str = MISSING



@dataclass
class CrossEntropyLostFunctionConfig(LostFunctionConfig):
    _target_: str = 'torch.nn.CrossEntropyLoss'


def setup_config() -> None:
    cs = ConfigStore.instance() : ConfigStore
    cs.store(group=task/loss_function,name="cross_entropy_loss_function_schema", node=CrossEntropyLostFunctionConfig)




