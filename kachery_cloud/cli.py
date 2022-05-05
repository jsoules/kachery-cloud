import os
import click
import kachery_cloud as kc


@click.group(help="Kachery cloud command-line client")
def cli():
    pass

@click.command(help="One-time initialization of the kachery cloud client")
def init():
    kc.init()

@click.command(help="Store file in IPFS")
@click.argument('filename')
@click.option('--cache-locally', is_flag=True)
def store_file(filename: str, cache_locally: bool):
    uri = kc.store_file(filename, label=os.path.basename(filename), cache_locally=cache_locally)
    print(uri)

@click.command(help="Load file from IPFS")
@click.argument('uri')
def load_file(uri: str):
    fname = kc.load_file(uri)
    print(fname)

@click.command(help="Load file from IPFS and write to stdout")
@click.argument('uri')
def cat_file(uri: str):
    kc.cat_file(uri)

@click.command(help="Store file in the local cache")
@click.argument('filename')
@click.option('--reference', is_flag=True)
def store_file_local(filename: str, reference: bool):
    uri = kc.store_file_local(filename, label=os.path.basename(filename), reference=reference)
    print(uri)

cli.add_command(init)
cli.add_command(store_file)
cli.add_command(load_file)
cli.add_command(cat_file)
cli.add_command(store_file_local)