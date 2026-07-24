# Cheatsheet

## Ansible
#Enter Ansible through Distrobox using 
distrobox enter ansible-box

#Running a playbook:
ansible-playbook -i inventory.ini playbooks/update.yml -K

#Git stuff
#get my github stuff
git clone <my github>

#update my github stuff
git pull

#check what changes made locally
git status

#add to staging area
git add .
#or
git add playbook/update.yml

#Commit
git commit -m "message is needed"

#Push
git push
