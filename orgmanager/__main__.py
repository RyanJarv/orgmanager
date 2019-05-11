#!/usr/bin/env python3

import collections
import argparse
import organization as org
from operator import attrgetter
from tabulate import tabulate


parser = argparse.ArgumentParser(description='Manage AWS Organizations')

what = parser.add_subparsers(title='what', dest='what', required=True, metavar='TYPE')
account = what.add_parser('account', help='account help')

action = account.add_subparsers(title='action', dest='action', required=True, metavar='ACTION')

action.add_parser('list', help='list help')

create = action.add_parser('create', help='create help')
create.add_argument('--name', '-n', help='name action')
create.add_argument('--email', '-e', help='email action')
create.add_argument('--role', '-r', help='role action')

args = parser.parse_args()

run_obj = attrgetter(str(args.what).capitalize())(org)()
output = attrgetter(args.action)(run_obj)()

if isinstance(output, str):
    print(output)
elif isinstance(output, collections.abc.Sequence) and isinstance(output[1], dict):
    print('asdf')
    headers = list(map(str, output[0].keys()))
    data = [list(map(str, x.values())) for x in output]
    print(tabulate(data, headers=headers))

exit(0)





