#!/usr/bin/env python
import oci
from oci.config import validate_config
from relay_sdk import Interface, Dynamic as D

relay = Interface()

config = oci.config.from_file()

validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

compartment_id = "ocid1.compartment.oc1..aaaaaaaa5av46cvfltbu6jqhwctvvy7hdnpd4alhguhsmvj7j63rnn5fpceq"

if not compartment_id:
    compartment_id = config["tenancy"]

raw_images = compute.list_images(compartment_id).data
if not raw_images:
    print("No images found")
    quit()
for image in raw_images:
    print('Found the following images: {}'.format(image.id))

print('Adding {} image(s) to the output `images`'.format(len(raw_images)))
relay.outputs.set('images', raw_images)