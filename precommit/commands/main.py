import typer

from precommit.commands import default_invoke_without_command

helptext = """
toolkit for pre-commit hooks.
"""

cmd = typer.Typer(help=helptext)
# cmd.add_typer(precommit.commands.override_format.cmd, name="stash-override-format")


def add_default_invoke():
    for _cmd in (cmd,):
        _cmd.callback(invoke_without_command=True)(default_invoke_without_command)


add_default_invoke()

if __name__ == '__main__':
    cmd()
