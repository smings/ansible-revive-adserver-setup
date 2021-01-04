#!/usr/bin/env python3

# puts a key value pair to consul. see: https://www.consul.io/api/kv.html#create-update-key
# Takes 3 Arguments:
# * targetEnv -> the environment -> see als env.py
# * key
# * value

# Example:
# ./consulKvPut.py dev config/application/app.whitelabel.darksite.enabled false

import env

import sys
import subprocess
import urllib.request

print("Running consulKvPut script")

_, targetEnv, key, value, *_ = sys.argv

print("targetEnv: ", targetEnv)
print("key: ", key)
print("value: ", value)

target = env.environments[targetEnv]
consul_server = target["consul-server"]

print("running: ", "PUT: " + consul_server + "/v1/kv/" + key + "  >>  " + value)

headers = {'Content-Type': 'application/json; charset=utf-8'}
data = value.encode("utf-8")# the value will be transfered as the payload/data

# example: http://lmwr-search01.test-server.ag:8500/v1/kv/config/application/app.whitelabel.darksite.enabled 
req = urllib.request.Request(consul_server + "/v1/kv/" + key, data, headers, method='PUT')
with urllib.request.urlopen(req) as response:
    pass
if response.status != 200:
    raise Exception(response)