# -*- coding: utf-8 -*-
import boto3
from helpers import *
from time import sleep


class Account:
    def __init__(self, args):
        self.client = boto3.client('organizations')
        self.root_account = None
        self.accounts: list = []

        if args.subcommand == 'create':
            self.name: str = getattr(args, 'name', None)
            self.email: str = getattr(args, 'email', None).format(self.name)
            self.role: str = getattr(args, 'role', 'OrganizationAccountAccessRole')
            self.billing_access: str = getattr(args, 'billing_access', 'DENY')

    def list(self):
        page_iterator = self.client.get_paginator('list_accounts').paginate()
        accounts_output = sum([page['Accounts'] for page in page_iterator], [])
        format_print(accounts_output)

    def create(self):
        resp: dict = self.client.create_account(
            Email=self.email,
            AccountName=self.name,
            RoleName=self.role,
            IamUserAccessToBilling=self.billing_access,
        )

        del(resp['ResponseMetadata'])
        format_print(resp)

        while resp['CreateAccountStatus']['State'] == 'IN_PROGRESS':
            sleep(3)
            resp = self.client.describe_create_account_status(
                CreateAccountRequestId=resp['CreateAccountStatus']['Id']
            )
            del(resp['ResponseMetadata'])
            format_print(resp)




        print('Account created successfully!')

