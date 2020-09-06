from debian:stretch

COPY ./ImapAsFs.service /lib/systemd/system/
COPY ./ /app

RUN apt update && apt install -y python3 software-properties-common python3-pip python-pip && \
#pip3 install -r ./requirements/requirements.txt && \
mkdir -p /emails/templates && mkdir /emails/senders



RUN systemctl enable ImapAsFs.service
#ENTRYPOINT ["wsgidav", "--host=0.0.0.0", "--port=80", "--root", "/emails", "--auth=anonymous"]
