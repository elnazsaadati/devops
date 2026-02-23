#  GitLab CI/CD Deployment with Ansible

This project uses GitLab CI/CD and Ansible to automatically execute a script on remote servers via SSH.

---

##  Overview

This pipeline:

- Triggers on push to the `main` branch
- Uses a Docker image with Ansible installed
- Connects to remote servers using SSH
- Executes a deployment script on target hosts
- Uses GitLab CI/CD variables for secure SSH key management

---

##  Project Structure


.
├── .gitlab-ci.yml
├── inventory/
│ └── hosts
├── playbook.yml
├── scripts/
│ └── deploy.sh
└── README.md


---

## ⚙️ Requirements

- GitLab Runner with Docker executor
- SSH access to target servers
- Private SSH key stored as a GitLab CI/CD variable
- Ansible installed inside the CI image

---

##  CI/CD Variables

Add the following variable in:

Settings → CI/CD → Variables

| Variable Name         | Description                       |
|----------------------|-----------------------------------|
| DEPLOYER_PRIVATE_KEY | Private SSH key for server access |

Make sure the variable is:

- Masked
- Protected (if using protected branches)

---

##  Example `.gitlab-ci.yml`

```yaml
stages:
  - deploy

deploy:
  stage: deploy
  image: your-ansible-docker-image

  variables:
    ANSIBLE_HOST_KEY_CHECKING: "False"

  before_script:
    - mkdir -p ~/.ssh
    - echo "$DEPLOYER_PRIVATE_KEY" > ~/.ssh/id_rsa
    - chmod 600 ~/.ssh/id_rsa

  script:
    - ansible-playbook -i inventory/hosts playbook.yml

  only:
    - main
 Example playbook.yml
- name: Run deployment script
  hosts: all
  become: true

  tasks:
    - name: Execute deploy script
      script: scripts/deploy.sh
 Example inventory/hosts
[servers]
192.168.1.10
192.168.1.11
