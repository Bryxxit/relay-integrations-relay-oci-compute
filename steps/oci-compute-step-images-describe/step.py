#!/usr/bin/env python
import oci
from oci.config import validate_config
config = oci.config.from_file()

validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

identity = oci.identity.IdentityClient(config)

compartment_id = config["tenancy"]

images = compute.list_images(
    compartment_id,
    sort_by='TIMECREATED',
    sort_order='DESC').data
if not images:
    print("No images found")
    quit()

for image in images:
  print("{:<30} {:<30} {:<30}".format(image.id, image.operating_system, image.operating_system_version))