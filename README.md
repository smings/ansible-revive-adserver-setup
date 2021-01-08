# Revive adserver 5.0.5 setup via ansible playbook
This repository contains ansible roles and playbooks for an automated set up of a revive adserver on an Ubuntu 20.04 server.

## prerequisites
- Obviously a freshly installed Ubuntu 20.04 server with everything set up the way you need it.
- A MySQL/Maria Database instance with a database and user for the Revive adserver.
- Hint: Name the database with a version suffix. I.e. `revive_505`
- A domain (with subdomains) pointing to the Ubuntu instance

For the exact process of how to set up the EC2 instance, see the `preparation and provisioning process.bpmn` in this directory (you can view and edit this bpmn process with the help of the freely available Camunda Modeler https://camunda.com/download/modeler/ )

## what does this playbook do?
This playbook installs an nginx with letsencrypt SSL certificates and all prerequisites for the installation of the revive adserver.
Afterwards it downloads and installs the specified version of the revive adserver. The revive adserver gets installed into the document root directory of the nginx webserver under `/var/www/html`. The `html` directory gets replaced with a symlink to the latest installed version of revive adserver, that is located in `/var/www/revive-adserver-5.0.5` (or whatever version you install with this).

## How to use the playbook?

In order for the playbook to work properly, you have to configure the following list of things:

1. In the `~/host_vars/lmrv.yml` host file you have to replace the `ansible_ssh_host` with the domain or IP that you want to use
2. In the `~/host_vars/lmrv.yml` host file replace all occurences of domains with the domains / subdomains you want to use. Keep in mind, that the first domain in the `certbot.domain_string` dictionary variable will also be the `letsencrypt_cert_dir` value. This is part of the directory path used by letsencrypt `/etc/letsentcrypt/live/{{ letsencrypt_cert_dir }}` 
3. In the `~/host_vars/lmrv.yml` host file also change the `certbot.contact_email` so that you get reminders for expiring certificate sent to an email address you have access to
4. In the `~/host_vars/lmrv.yml` host file change the `dns_names` to the domain and optional subdomains you want to use
5. In the `~/host_vars/lmrv.yml` host file change `letsencrypt_cert_dir` to the first listed domain from `cerbot.domain_string` 

After these changes you are already good to go. Make sure your Ubuntu server instance is reachable via SSH and that you have Ansible in its lates version installed on your computer (this is not easy on a windows machine  - good luck with that)

When you are ready, simply change into the playbook root directory (`~/`) and type `ansible-playbook install.yml`

When the playbook is done and completed without errors, simply enter your domain name in a browser and continue with the installation of the revive adserver. You will need the MySQL database connection settings for this. After setting up the database, simply enter the data for the admin user and you are good to go with a clean installation of the revive adserver.

## Limitations of this ansible playbook

This playbook simply installs the revive adserver. It doesn't yet provide an automated update path (but it is structurally prepared for it).

This playbook doesn't install a cronjob or any other kind of automation for automatically renewing the ssl certificates initially obtained from letsencrypt's certbot. This can easily be done as a cronjob. It has to be done manually. Remember that letsencrypt certificates expire after 3 months!!!