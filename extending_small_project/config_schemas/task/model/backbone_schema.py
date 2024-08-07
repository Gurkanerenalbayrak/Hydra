from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class backboneConfig:
    _target_: str = MISSING


@dataclass
class ResNet34backboneConfig(backboneConfig):
    _target_: str = "backbones.ResNet34"
    pretrained: bool = True


@dataclass
class ResNet50backboneConfig(backboneConfig):
    _target_: str = "backbones.ResNet50"
    pretrained: bool = True



@dataclass
class ResNet18backboneConfig(backboneConfig):
    _target_: str = "backbones.ResNet18"
    pretrained: bool = True


def setup_config() -> None:

    cs = ConfigStore.instance()
    cs.store(name="backboneConfig", node=backboneConfig)
    cs.store(group="task/model/backbone",name="ResNet34_schema", node=ResNet34backboneConfig)
    cs.store(group="task/model/backbone",name="ResNet50_schema", node=ResNet50backboneConfig)
    cs.store(group="task/model/backbone",name="ResNet18_schema", node=ResNet18backboneConfig)