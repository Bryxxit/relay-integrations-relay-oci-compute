#!/usr/bin/env python
import oci
from oci.config import validate_config
config = oci.config.from_file()

validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

identity = oci.identity.IdentityClient(config)

compartment_id = "ocid1.compartment.oc1..aaaaaaaa5av46cvfltbu6jqhwctvvy7hdnpd4alhguhsmvj7j63rnn5fpceq"

if not compartment_id:
    compartment_id = config["tenancy"]

instances = compute.list_instances(
    compartment_id,
    sort_by='TIMECREATED',
    sort_order='DESC').data
if not instances:
    print("No instances found")
    quit()

for instance in instances:
  print("{:<30} {:<30} {:<30} {:<30}".format(instance.id, instance.display_name, instance.availability_domain, instance.shape))