import importlib
import logging

from pathlib import Path
from typing import Optional

import toml
import typer

import precommit

_typer = typer.Typer()
logger = logging.getLogger(__name__)


def version_callback(value: bool):
    if value:
        print(f"{__package__} CLI Version: {precommit.__version__}")
        raise typer.Exit()


def check_version(config_path: Optional[Path] = None) -> bool:
    """检查配置文件中的版本号与源码目录下的版本号是否一致.

    Args:
        config_path (Optional[Path], optional): 配置文件路径. 默认读取工作目录下的 `pyproject.toml` . Defaults to None.

    Returns:
        bool: 配置版本与包版本是否一致
    """
    if config_path is None:
        config_path = Path('pyproject.toml')

    if not config_path.exists():
        logger.warning(f"{config_path.absolute()} is not exists.")
        return False

    logger.debug(config_path.absolute())
    document = toml.load(config_path)
    logger.debug(f"document: {document}")
    try:
        name = document["tool"]["poetry"]["name"]
        version = document["tool"]["poetry"]["version"]
    except KeyError:
        logger.warning("name or version is not found in pyproject.toml")
        return False
    try:
        module = importlib.import_module(f"{name}")
    except ImportError:
        logger.warning("can't import module", exc_info=True)
        return False
    package_version = getattr(module, '__version__', None)

    if package_version is None:
        logger.warning(f'not found __version__ in {name} package')
        return False

    if package_version != version:
        logger.warning(f"version is not match, config version: {version}, package version: {package_version}")
        return False
    logger.debug(f"config version: {version}, package version: {package_version}")
    return True


@_typer.command()
def check_poetry_package_version(
    log_level: int = typer
    .Option(logging.INFO,
            '--log_level',
            envvar='log_level',
            help='日志级别, DEBUG:10, INFO: 20, WARNING: 30, ERROR:40'),
    log_format: str = typer.Option(r'%(message)s'),
    version: Optional[bool] = typer.Option(None,
                                           "--version",
                                           "-V",
                                           callback=version_callback),
    config_path: Optional[Path] = typer.Option(None,
                                               '--config_path'),
):
    """"""
    logging.basicConfig(level=log_level, format=log_format)
    if not check_version(config_path):
        raise typer.Exit(-1)


def main():
    _typer()


if __name__ == '__main__':
    main()
