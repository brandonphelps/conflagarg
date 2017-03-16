

import argparse
import configparser
import os


def create_parser(schema):
    parser = argparse.ArgumentParser()

def validate_schema(config, schema):
    pass

def config_section_map(section):
    """
    pulled from config parser example code located at
    https://wiki.python.org/moin/ConfigParserExamples
    slightly modified
    """
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("Exception on {}".format(option))
            dict1[option] = None
    return dict1

def create_config(schema):
    """
    Given the schema, a config is returned which will contain sections and options based on the schema.
    """
    #TODO: perform validation on the schema to ensure it meets formatting requirements
    # if the schema is a class this is easy, currently its a dictionary.

    config = configparser.ConfigParser()
    
    for section in schema:
        config.add_section(section)
        for option in schema[section]:
            config.set(section, option['name'], option['default'])
    return config

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
        passed_validation = validate_schema(config, schema)
    else:
        passed_validation = False

    return config, passed_validation

def save_config(filename, config):
    try:
        with open(filename, 'w') as writer:
            config.write(writer)
    except Exception as e:
        print("Failed to write to file {} due to exception {}".format(filename, e))

def create_or_load_config(filename, schema):
    """
    attempts to load a config from filename and will validate that it meets
    the schema requirements. 
    if the config fails to load due to file not existing a defaulted config is created
    and false is returned.
    """

    if os.path.isfile(filename):
        config, validated = load_config(filename, schema)
        created = False
    else:
        config = create_config(schema)
        save_config(filename, config)
        created = True

    return config, created

if __name__ == "__main__":

    test_schema = {"section1" : [{'name' : 'value1', 'default' : '0'},
                                 {'name' : 'value2', 'default' : '1'},],
                   "section2" : [{'name' : 'value3', 'default' : '2'}]}



    config, created = create_or_load_config('config.ini', test_schema)
