# here we will create the functions that are frequently need so we can import from here

import os
from box.exceptions import BoxError, BoxValueError
import yaml
from Text_Summerizer.logging import logger
from  ensure import ensure_annotations #if we pass str instead of int and still our function works (int ki jgh string pass hone pe alert kr dega)
from box import ConfigBox   #configbox is similar to dict but in dict d["value"] we can use d.value ,when we need to access something from yaml we will pass or use value instead of list
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_of_yaml:Path)->ConfigBox:
    """reads yaml file and returns

    Args:
        path_of_yaml(str):path like input()

    Raises:
        ValueError:if yaml file is empty
        e:empty file

    Returns:
        configBox:ConfigBox type
    """
    try:
        with open(path_of_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_of_yaml} loadded successfully")
            return ConfigBox(content)
    except  BoxValueError:
        raise ValueError("yaml file is empty")
    except  Exception as e:
        raise e
    

@ensure_annotations
def create_directiories(path_of_directories: list,verbose=True):
    """create list of directories

    Args:
        path_of_directories(list):list of path of directories
        ignore_log (bool,optional):ignore if multiple directories is to be created .Defaults to False.
        """

    for path in path_of_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    Args:
        path (Path):path of the file

    Returns:
        str:size in KB"""
    size_in_kb=round(os.path.getsize(path)/1024)
    return  f"~(size_in_kb) KB"
