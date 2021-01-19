"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Blending ToolKit."""


if __name__ == "__main__":
    main(prog_name="BlendingToolKit")  # pragma: no cover
