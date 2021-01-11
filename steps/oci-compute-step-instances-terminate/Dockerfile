FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-ec2-terminate-instances.py"
ENTRYPOINT []
CMD ["python3", "/nebula/step-ec2-terminate-instances.py"]

LABEL "org.opencontainers.image.title"="Terminates AWS EC2 instances"
LABEL "org.opencontainers.image.description"="This task terminates a given list of EC2 instances."
LABEL "com.puppet.nebula.sdk.version"="v1"
