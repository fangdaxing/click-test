import click
from print_result import (
  three,
  four,
  five,
  run,

  
  
  )

@click.group()
def cli():
    pass

@cli.command(name="three")
def result_three():
  three()

@cli.command(name="four")
def result_four():
  four()

@cli.command(name="five")
def result_five():
  five()

@cli.command(name="run")
@click.option("--function_name", type=click.Choice(["all", "three", "four", "five"],case_sensitive=False))
def run_cmd(function_name):
  run(function_name)


if __name__ == "__main__":
  cli()