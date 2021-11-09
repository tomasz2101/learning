FROM gitpod/workspace-full

# add terraform repository
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
RUN sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
# add ansible repository
RUN sudo apt-add-repository --yes --update ppa:ansible/ansible

RUN sudo apt-get update

# required dependencies
RUN sudo apt-get install -y apt-utils

# install azure cli & terraform & ansible
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
RUN sudo apt-get install terraform
RUN sudo apt-get install 

