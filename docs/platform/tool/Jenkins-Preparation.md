Preparation
-----------

### Server requirement (hardware & software)

`   1.  Hardware`\
`       •  Disk > 500G`\
`   2.  Software`\
`       •  Jenkins LTS version 1.509.2`\
`       •  Linux distribution, recommend use openSuse 12.3 64-bit`\
`       •  Jenkins component: jenkins, jenkins-plugins, jenkins-jobs-common, jenkins-jobs, jenkins-scripts-common, jenkins-scripts`

### Service installation and Configuration

-   Setting up for Gerrit accessing

` After getting a gerrit account, you need to create an ssh key, and add your ssh key to Gerrit to enable the connection to gerrit.`

### Register your contact info on Gerrit

Log into Gerrit on UI, follow the links below to register your email
address and update your full name:

`* Settings --> Contact Information --> Register New Email...`\
`* Settings --> Contact Information --> Full Name..`

After you register the email, you will receive an email which contains a
link. Please copy the link to your browser to activate the account.

### Create SSH keys

`$ su jenkins`\
`$ ssh-keygen -t rsa`

After pressing the Enter key at several prompts, an SSH key-pair will be
created in \~/.ssh/id\_rsa.pub.

### Upload SSH pubkey to Gerrit

Click the links below to set up the Gerrit WebUI.

` Settings --> SSH Public Keys --> Add Key...`

Paste your SSH public key there, and then click \'Add\'.

### Verify your SSH connection

You can verify your Gerrit connection by executing this command:

` $ ssh -p 29418 username@gerrit_hostname`

Make sure to add the server RSA key fingerprint to the known hosts of
jenkins account if connect to gerrit server in the first time.

If your settings are correct, you\'ll see the message below. If not,
check SSH proxy and SSH public key on Gerrit.

` Welcome to Gerrit Code Review`\
` ...`

### Config Git for Gerrit Access

After the above installation, which will include git, is complete, you
can configure git.

` $ git config --global user.name "First_Name Last_Name"`\
` $ git config --global user.email "account@host"`

Note: It is recommended that you use the same email address you used for
your Gerrit account for the \"user.email\" setting. Make sure you have
developer access first.

[Category:Tool](Category:Tool "wikilink")
