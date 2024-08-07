from omegaconf import DictConfig, OmegaConf
import hydra


@hydra.main(version_base="1.2",config_path="configs", config_name="config.yaml")
def main(config:DictConfig) -> None:
    print(OmegaConf.to_yaml(config))




if __name__ == "__main__":
    main()

