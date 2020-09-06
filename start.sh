#!/bin/sh
#DOCUMENTATION, WHICH I DON'T HAVE TIME FOR :(

set -e

########   FUNCTIONS   #########

check_docker(){
  echo "CHECKING DOCKER..."
  docker --version;
  if [[ $? -ne 0 ]]; then
    echo "Docker is missing";
    exit 1;
  fi
  docker-compose --version;
  if [[ $? -ne 0 ]]; then
    echo "docker-compose is missing";
    exit 1;
  fi
  echo "DOCKER AND DOCKER-COMPOSE INSTALLED"
}

help(){
  echo "USAGE: ./start.sh --email-login (your login) --email-password (your password) --imap-url (your email url. default: imap.fastmail.com)"
}

start_container(){
  docker-compose up -d --force-recreate
  docker-compose exec app sh -c 'echo $EMAIL_LOGIN; echo $EMAIL_PASSWORD; echo $EMAIL_IMAP_URL'
}

#####   MAIN   #######

while test $# -gt 0; do
  case "$1" in
    --email-login)
      shift
      email_login=$1
      shift
      ;;
    --email-password)
      shift
      email_password=$1
      shift
      ;;
    --imap-url)
      shift
      email_imap=$1
      shift
      ;;
    help)
      help;
      exit;
      ;;
    *)
      echo "$1 is not a recognized flag!"
      exit 1;
      ;;
  esac
done


check_docker
start_container $email_login $email_password $email_imap
