

import argparse
import configparser
import os

def create_parser(schema):
    parser = argparse.ArgumentParser()

def validate_schema(config, schema):
    pass

def load_config(filename, schema=None):
    config = configparser.ConfigParser()
    if os.path.isfile(filename):
        try:
            config.read(filename)
        except configparser.ParsingError as e:
            print("Failed to parse {} due to parsing error".format(filename))
            print(e)
        except configparser.DuplicateOptionError as e:
            print("Failed to parse {} due to duplicate sections".format(filename))
            print(e)

    if schema:
        validate_schema(config, schema)
    return config

if __name__ == "__main__":
    schema = {'help' : {'short_option' : '-h',
                        'long_option' : '--help',
                        'kwargs' : { 'type' : bool}}}

    load_config('test')
