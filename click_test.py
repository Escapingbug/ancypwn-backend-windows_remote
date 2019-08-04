import click

@click.group()
def one():
    pass

@click.command()
@click.option('-c', default='')
def hello(c):
    print(c)

one.add_command(hello)

one()
