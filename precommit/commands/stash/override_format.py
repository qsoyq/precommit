from pathlib import Path

import typer
from stash_tool.commands.override_format import (YamlStoverrideFormatter,
                                                 error, help_text, iterdir)

cmd = typer.Typer(help=help_text)


@cmd.command()
def run(
    path: Path = typer.Argument('.', help='需要格式化的路径'), inplace: bool = typer.Option(False, help='是否直接修改对应的覆写文件'), verbose: bool = typer.Option(True), indent: int = typer.Option(4)
):
    if not path.exists():
        typer.echo(error('dirpath must be valid dir'))
        raise typer.Exit(1)

    if path.is_file() and path.suffix == '.stoverride':
        YamlStoverrideFormatter(path, inplace, verbose, indent).update()
    else:
        iterdir(path, inplace, verbose, indent)
