U need:
1. docker
2. docker-compose v>=3.4
3. helm and k8s cluster if you want to deploy it from chart :)
4. bash
5. port 8080 free

Usage:

1.play script ./start.sh with parameters:
- --email-login - login to your email account
- --email-password - password to your email app
- --imap-url (default - imap.fastmail.com)
Example: ./start.sh rsiliwoniukgolem@fastmail.com secretpassword1
or ./start.sh --email-login rsiliwoniukgolem@fastmail.com --email-password secretpassword1 --imap-url imap.someemailserver.com
4. Enjoy :)
