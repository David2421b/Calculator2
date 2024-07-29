import click

from app.model import Calculadora

@click.group()
@lick.pass_context
def calc(ctx: click.Context):
    """A simple calculator"""
    ctx.obj = {"calculator_object": Calculadora()}