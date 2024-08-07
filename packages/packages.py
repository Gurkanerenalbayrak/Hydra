




import hydra
from omegaconf import OmegaConf

@hydra.main(config_name="config", config_path="configs",version_base=None)
def main(config) -> None:
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()