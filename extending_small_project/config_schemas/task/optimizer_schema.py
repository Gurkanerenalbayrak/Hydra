from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class OptimizerConfig:
    _target_: str = MISSING
    _partial_: bool = True


@dataclass
class AdamOptimizerConfig(OptimizerConfig):
    _target_: str = "torch.optim.Adam"
    lr: float = 0.001
    betas: tuple[float,float] = (0.9, 0.999)
    eps: float = 1e-08
    weight_decay: float = 0.0
    amsgrad: bool = False


def setup_config() -> None:
    cs = ConfigStore.instance() : ConfigStore
    cs.store(group="task/optimizer" ,name="adam_optimizer_schema", node=AdamOptimizerConfig)


