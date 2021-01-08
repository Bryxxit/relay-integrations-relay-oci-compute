FROM python:3-alpine
RUN apk --no-cache add bash ca-certificates curl git jq openssh gcc musl-dev libffi-dev openssl-dev && update-ca-certificates
RUN pip --no-cache-dir install "https://packages.nebula.puppet.net/sdk/support/python/v1/nebula_sdk-1-py3-none-any.whl"
RUN pip --no-cache-dir install oci
COPY "./step.py" "/nebula/step-compute-reboot-instances.py"
COPY "./.oci/*" "/root/.oci/"
ENTRYPOINT []
CMD ["python3", "/nebula/step-compute-reboot-instances.py"]

LABEL "org.opencontainers.image.title"="Reboot OCI compute instances"
LABEL "org.opencontainers.image.description"="This task reboots the compute instances in a given region."
LABEL "com.puppet.nebula.sdk.version"="v1"
