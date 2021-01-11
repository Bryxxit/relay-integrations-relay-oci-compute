FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-ec2-stop-instances.py"
ENTRYPOINT []
CMD ["python3", "/nebula/step-ec2-stop-instances.py"]

LABEL "org.opencontainers.image.title"="Stop AWS EC2 instances"
LABEL "org.opencontainers.image.description"="This task stops a given list of EC2 instances."
LABEL "com.puppet.nebula.sdk.version"="v1"
