#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:56:01 2023

@author: anandarupmukherjee
"""

import numpy as np
import json


# FUNCTION TO FORMAT THE OUTPUTS 

def listify_dictionarify(arr_val, header):
    my_list=arr_val.split()
    new_list=my_list[-5:]
    merged="_".join(str(i) for i in my_list[:-5])
    new_list.insert(0,merged)
    my_dict = dict(zip(header, new_list))
        
    return my_dict

 


with open('2023-03-23_Overall_Process_YC.out.txt', 'r') as file:
    # Read the lines and store them in a list
    lines = file.readlines()
    # Create a numpy array from the list of lines
    arr = np.array(lines)



header=arr[14].split()
tat=arr[17].split()

super_dict=[]

for i in range(18,54):
    val=listify_dictionarify(arr[i], header)
    print(val)
    print("--------------------------")
    super_dict.append({'ID':i, 'kpi':val})

new_dat=json.dumps(super_dict, sort_keys=True, indent=4)
print(new_dat)


tat=arr[17].split()
sla=arr[190].split()

header_final=arr[239].split()

CutupSU_1=arr[242].split()
CutupSU_2=arr[243].split()
CutupSU_3=arr[244].split()


RecepSU_1=arr[246].split()
RecepSU_2=arr[247].split()
RecepSU_3=arr[248].split()


util_packet={'tat_av':tat[1], 'tat_min':tat[3], 'tat_max':tat[4],
             'CU_util_transport_t_av':CutupSU_1[3], 'CU_util_transport_percent':CutupSU_1[4],
             'CU_util_busy_t_av':CutupSU_2[3], 'CU_util_busy_percent':CutupSU_2[4],
             'CU_util_idle_t_av':CutupSU_3[3], 'CU_util_idle_percent':CutupSU_3[4],
             'REC_util_transport_t_av':RecepSU_1[3], 'REC_util_transport_percent':RecepSU_1[4],
             'REC_util_busy_t_av':RecepSU_2[3], 'REC_util_busy_percent':RecepSU_2[4],
             'REC_util_idle_t_av':RecepSU_3[3], 'REC_util_idle_percent':RecepSU_3[4]}



from influxdb import InfluxDBClient
from datetime import datetime
import time


# Set up InfluxDB client
host = "shoestring-scoring.eastus.cloudapp.azure.com"  # Replace with actual host name or IP address
port = 8086         # Replace with actual port number
user = "admin"     # Replace with actual username
password = "admin"  # Replace with actual password
database = "iot"   # Replace with actual database name
client = InfluxDBClient(host=host, port=port, username=user, password=password, database=database)

# Create a JSON-formatted data point
while(True):
    data = [
        {
            "measurement": "arena_windows",
            "tags": {
                "my_tag": "my_value"
            },
            "time": datetime.utcnow().isoformat() + "Z",  # Replace with actual timestamp
            "fields": {
                "alive": 1,
                "process": np.random.randint(100),
                "alert": np.random.randint(3),
                'tat_av': tat[1], 
                'tat_min': tat[3], 
                'tat_max': tat[4],
                'CU_util_transport_t_av': CutupSU_1[3], 
                'CU_util_transport_percent': CutupSU_1[4],
                'CU_util_busy_t_av': CutupSU_2[3], 
                'CU_util_busy_percent': CutupSU_2[4],
                'CU_util_idle_t_av': CutupSU_3[3], 
                'CU_util_idle_percent': CutupSU_3[4],
                'REC_util_transport_t_av': RecepSU_1[3], 
                'REC_util_transport_percent': RecepSU_1[4],
                'REC_util_busy_t_av': RecepSU_2[3], 
                'REC_util_busy_percent': RecepSU_2[4],
                'REC_util_idle_t_av': RecepSU_3[3], 
                'REC_util_idle_percent': RecepSU_3[4]
            }
        }
    ]

    # Write the data to the database
    client.write_points(data)
    print("write done...")
    time.sleep(4)







