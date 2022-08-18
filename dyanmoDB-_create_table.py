# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:36:03 2020

@author: hp
"""

import boto3

# Get the service resource.

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id='xxx',
                          # aws_secret_access_key='xxx',
                          aws_secret_access_key='xxxxx',
                          )

# dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='userdata',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='userdata')
print(table.item_count)




