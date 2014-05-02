opsgadget
=========

Fullscreen Take Home Test

Approach Taken for Fullscreen Project:

My approach deviated a bit from the documentation since I created the environment in my own AWS account – but for the most but it follows it closely.  I created one VPC  (10.0.0.0/16) and placed all instances within one subnet (10.0.1.0/24).  All instances have a security group and public IP assigned to them and are only accessible from specific IP address.  Ideally in a production environment I would have set up a site-to-site VPN to route all traffic for provisioning.  Here are the specific steps I took to approach the problem.     

1)	Built out the environment on my local workstation and noted the packages, configs, and steps that I took so I could automate the process using Salt. 

2)	Created two Ubuntu images (Ubuntu Server 12.04 64-bit) in my AWS environment.  One that I turned into the Salt Master (10.0.1.92) and the other image I used to create the base AMI image.  The only thing that I added to the base Ubuntu image was the salt-minion package that had the minion_id removed so that new copies will be able to connect to the Salt Master. 

3)	Created salt states to automate the deployment process. (see GitHub for details)

4)	Created a bash script that automates the entire process for a developer.  It creates a new instance, runs the salt states and then provides the user with a link to the newly launched app.

*Notes about security: I used key pairs and the root account for the entire process and in my scripts.  Obviously this is not an ideal situation from a security perspective, but since this was a prof of concept, I didn’t properly lock down the process.  In a production environment I would have used non-root users and created a process where only one script is viewable and executable by developers and all keys and passwords would be properly secured and hidden. 

*The instructions also mentioned that the script should be able to accept the following format (ec2.sh app environment num_servers server_size).  The bash script that I wrote only creates 1 server for the master branch of the opsgadget app.  In a production environment I would have expanded the script to include the options to pull a different branch, specify the environment to launch to, and allow the developer to spin up more servers. 
