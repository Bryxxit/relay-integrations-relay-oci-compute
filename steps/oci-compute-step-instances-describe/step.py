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

compartment_id = relay.get(D.oci.compartmentID)

if not compartment_id:
  compartment_id = config["tenancy"]

instances = compute.list_instances(compartment_id).data
if not instances:
  print("No instances found")
  exit(0)

for instance in instances:
  print("{:<30} {:<30} {:<30}".format(instance.id, instance.lifecycle_state, instance.shape))

print('\nAdding {0} instance(s) to the output `instances`'.format(len(instances)))