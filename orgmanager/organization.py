# -*- coding: utf-8 -*-
import boto3


class Account:
    def __init__(self):
        self.client = boto3.client('organizations')
        self.root_account = None
        self.accounts = []

    def list(self):
        page_iterator = self.client.get_paginator('list_accounts').paginate()
        accounts_output = sum([page['Accounts'] for page in page_iterator], [])
        return accounts_output

    def create(self):
        print("not implemeted")
