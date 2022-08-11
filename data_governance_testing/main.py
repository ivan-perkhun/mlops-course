import click

@click.command()
@click.option(
    '--name', 
    prompt='Your name',
    help='The person to greet.'
)

def hello(name):
    """Simple program that greets NAME."""
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()