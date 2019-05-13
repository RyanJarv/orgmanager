#!/usr/bin/env python3

import configparser
import os
from os import path
import argparse
import organization as org
from operator import attrgetter
from helpers import *

CONFIG_PATH = path.expanduser('~/orgmanager.ini')

config = configparser.ConfigParser()
if not path.exists(CONFIG_PATH):
    with safe_open(CONFIG_PATH) as f:
        config.read(f)

parser = argparse.ArgumentParser(description='Manage AWS Organizations')
subcommand = parser.add_subparsers(title='subcommand', dest='subcommand', required=True, metavar='TYPE')

account = subcommand.add_parser('account', help='account help')
action = account.add_subparsers(title='action', dest='action', required=True, metavar='ACTION')
action.add_parser('list', help='list help')

create = action.add_parser('create', help='create help')
create.add_argument('name', metavar='NAME', help='name action')
create.add_argument('--email', '-e', default=config.get('DEFAULT', 'email', raw=True, fallback=None),
                    required=True, help='email action')
create.add_argument('--role', '-r', default=config.get('DEFAULT', 'role', fallback='OrganizationAccountAccessRole'),
                    required=False, help='role action')
create.add_argument('--billing-access', action='store_const', const='ALLOW', default='DENY',
                    required=False, help='billing access')

args = parser.parse_args()

run_obj = attrgetter(str(args.subcommand).capitalize())(org)(args)
attrgetter(args.action)(run_obj)()

exit(0)





