from debian:stretch

COPY ./ImapAsFs.service /lib/systemd/system/
COPY ./ /app

WORKDIR /app

RUN apt update && apt install -y python3 software-properties-common python3-pip python-pip && \
pip3 install -r ./requirements/requirements.txt && \
mkdir -p /emails/templates && mkdir /emails/senders && mkdir /emails/topics
# {senders,templates,topics} didn't work in docker


RUN systemctl enable ImapAsFs.service
ENTRYPOINT ["wsgidav", "--host=0.0.0.0", "--port=80", "--root", "/emails", "--auth=anonymous"]

EXPOSE 80
