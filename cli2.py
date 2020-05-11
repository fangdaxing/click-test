import click
from print_result import (
  three,
  four,
  five,
  run
  
  
  )

@click.group()
def cli():
    pass

@cli.command(name="three")
# @click.option("--number", default=None, help="three")
def result_three():
  three()

@cli.command(name="four")
# @click.option("--number", default=None, help="four")
def result_four():
  four()

@cli.command(name="five")
# @click.option("--number", default=None, help="five")
def result_five():
  five()

@cli.command(name="run")
def run_cmd():
  run()

if __name__ == "__main__":
  cli()