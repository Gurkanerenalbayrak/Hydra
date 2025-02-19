from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING



from config_schemas.task.model import backbone_schema, adapter_schema, head_schema #are not created yet



@dataclass
class ModelConfig:
    _target_: str = MISSING



@dataclass
class SimpleModelConfig(ModelConfig):
    _target_: str = "models.SimpleModel"    
    backbone: backbone_schema.BackboneConfig = MISSING
    adapter: adapter_schema.AdapterConfig = MISSING
    head: head_schema.HeadConfig = MISSING


def setup_config() -> None:
    backbone_schema.setup_config()
    adapter_schema.setup_config()
    head_schema.setup_config()


    cs = ConfigStore.instance()
    cs.store(group="task_model", name="simple_model_schema", node=SimpleModelConfig)

    






