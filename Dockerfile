FROM ubuntu:focal

RUN apt-get update

# required dependencies
RUN apt-get install -y apt-utils curl gnupg software-properties-common

# add terraform repository
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
RUN apt-get update
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com focal main"

# add ansible repository
RUN apt-add-repository --yes --update ppa:ansible/ansible-2.9



# install azure cli & terraform & ansible
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
RUN apt-get install -y terraform
RUN apt-get install -y ansible

RUN apt install sshpass