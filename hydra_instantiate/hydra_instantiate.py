import hydra 
from omegaconf import DictConfig
from hydra.utils import instantiate

import torch 






class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hello(self):
        print(f"hello, {self.name}!")






@hydra.main(version_base="1.3",config_path=".", config_name="config")
def main(config: DictConfig) -> None:
    my_class: MyClass = MyClass(name="John")
    my_class.say_hello()

    my_class_hydra: MyClass = instantiate(config.my_class)
    my_class_hydra.say_hello()


    #torch
    parameters = torch.nn.Parameter(torch.randn(10, 10))

    

    parameters: Parameter = torch.nn.Parameter(torch.randn(10,10))


    partial_optimizer: any = instantiate(config.optimizer)

    optimizer = partial_optimizer([parameters])
    print(optimizer)





if __name__ == "__main__":
    main()




