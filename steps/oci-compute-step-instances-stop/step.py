#!/usr/bin/env python
import oci
from relay_sdk import Interface, Dynamic as D

relay = Interface()

config = {
    "user": relay.get(D.oci.connection.userOCID),
    "key_content": relay.get(D.oci.connection.keyContent),
    "fingerprint": relay.get(D.oci.connection.fingerprint),
    "tenancy": relay.get(D.oci.connection.tenancy),
    "region": relay.get(D.oci.region)
}

from oci.config import validate_config
validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

instanceIDs = relay.get(D.oci.instanceIDs)

if not instanceIDs:
  print("No instance IDs found")
  exit(0)

graceful = relay.get(D.oci.GracefulReboot)

if graceful:
  print('Gracefully stoping instances: {}'.format(instanceIDs))
  action = "SOFTSTOP"
else:
  print('Stoping instances: {}'.format(instanceIDs))
  action = "STOP"

for instanceID in instanceIDs:
  compute.instance_action(instanceID,action)
