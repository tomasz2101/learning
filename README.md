0. Update your git repo to last version

1. Create group resource with name Learning, location Germany West Central

2. Start your docker engine (only mac and windows)

3. Execute in repo directory:
    docker run -it --rm -v $(pwd):/app tomasz2101/learning bash

4. Login to azure portal with CLI: 
    az login 

5. Execute script 
    azure/create_tfstate.sh

6. Login to azure portal and inside resource group Learning find your tstateXXXX reource 

7. Change to same name azure/provider.tf line 9: storage_account_name  = "tstate21404" this should be your tstate that you just created

8. Create file azure/secret.tfvars and put inside:
    vm_password="123456aA!"

6. In directory "azure" execute: 
    teraform init

6.1 If needed execute:
    terraform init  -reconfigure

7. In directory "azure" execute: 
    terraform apply -var-file=secret.tfvars -auto-approve

8. Get your public ip from Azure portal or by executing previous command again and save it in line 12 in file ansible/envs/prod

9. Execute in "ansible" directory:
    ansible-playbook -i envs/prod playbook.yml

10. Check if everything is running in browser on your_public_ip:8080

10. After everything is done in directory "azure" execute:
    terraform destroy -var-file=secret.tfvars -auto-approve