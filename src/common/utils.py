from typing import Callable, Optional, Union, List, Tuple

import os
import datetime
import yaml
from django.utils.decorators import method_decorator


class Config:
    def __init__(self, config_file: str):
        if not os.path.exists(config_file):
            msg = (
                'Could not find "config.yml" file. '
                "Make sure to read the instructions from README.md"
            )
            raise FileNotFoundError(msg)

        with open(config_file) as file:
            self.__config = yaml.safe_load(file)
            if not self.__config:
                raise Exception("Config file is empty!")

    def get(
        self,
        var_name: str,
        default: Optional[Union[str, int, Tuple]] = None,
        cast: Callable = str,
        raise_error: bool = False,
    ) -> Union[str, int, bool, List[str], None]:
        if value := self.__config.get(var_name, default):
            value = cast(value)
            if isinstance(value, str):
                value = value.strip()
            return value
        if raise_error:
            raise LookupError(f"Cannot find value for setting {var_name}!")
        return None


def get_upload_path(instance, file_name: str) -> str:
    """
    Takes filename and creates new one with random string at the end
    :param instance: DO NOT delete this parameter, it's required for upload_to
    :param file_name: raw file name from admin
    :return: new file name
    """
    if instance is None:
        file_name, extension = file_name.rsplit(".", 1)
        return f"{file_name}_{str(datetime.datetime.now())[:19]}.{extension}"

    # noinspection PyProtectedMember
    model = instance.__class__._meta
    model_name = model.verbose_name_plural.replace(" ", "_")
    file_name, extension = file_name.rsplit(".", 1)
    return f"{model_name}/{file_name}_{str(datetime.datetime.now())[:19]}.{extension}"


def create_swagger_info(schema):
    return method_decorator(name="create", decorator=schema)
