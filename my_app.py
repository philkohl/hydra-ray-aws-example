# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import logging
import time

import hydra
from omegaconf import DictConfig

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_name="config", config_path="config")
def my_app(cfg: DictConfig) -> None:
    log.info(f"Executing task {cfg.task}")
    time.sleep(1)


if __name__ == "__main__":
    my_app()
