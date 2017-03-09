

import argparse
import configparser


def create_parser(schema):
    parser = argparse.ArgumentParser()

if __name__ == "__main__":
    schema = {'help' : {'short_option' : '-h',
                        'long_option' : '--help',
                        'kwargs' : { 'type' : bool}}}
