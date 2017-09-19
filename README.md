<h1>E-Seal</h1>

<h3>Description for the project</h3>
<p>This project mainly focuses on the security to transfer the file from one portal to the another one securely. Our core part lies in its encryption techniques. As we upload the file on server it is encrypted with the help of AES Encryption creating a symmetric key. If we store the symmetric key on the server, there is a chance of server being hacked and the file may get decrypted. So, for this we have encrypted the symmetric key with the help of RSA algorithm using public key which is available to all. Other part of our project is the local software we made for decryption. This software needs encrypted file as well as encrypted symmetric key to decrypt the whole file. This software includes the private key to decrypt the file which is embedded in the code itself(The code is binary compiled hence the code cannot be retrieved). But if the software is stolen the file may get decrypted, so for this we have a USB stick as a key to run the software. This USB stick is only with authorised people. To make USB a key we have a centralized management which can convert any USB to a key as well as remove any USB as a key.

This website is made by Slim and Twig Framework followed by its dependencies. This framework prevents SQL injection as well as CSRF attack.

This all technologies makes our product secure and user friendly.
</p>

<h4>For the web requirements</h4>

First of all what you want to do is go to the php_authentication folder and open cmd and fire the command:<h5> php composer.phar update</h5>
make sure that you have set the evnironment variables for php

After completing this stuff the<pre>"verdor"</pre> folder will appear which will carry all the dependencies of the project.

Then go to :<pre>verdor/slim</pre> folder and search for the file <h6>".htaccess"</h6> and copy that file and paste it into the <pre>"public"</pre> folder.

Go to :<pre>php_authentication/app/config/</pre> folder and check the appropiate development and production file and configure it according to your configuration(The mode of the file is been decided in the <pre>php_authentication/mode.php file)</p>


<h3>Then the database part:</h3>

Fire the query into the database to create the users and users_permission table into the database :

<pre>CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `password` varchar(256) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `active_hash` varchar(255) DEFAULT NULL,
  `recover_hash` varchar(255) DEFAULT NULL,
  `remember_identifier` varchar(255) DEFAULT NULL,
  `remember_token` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE `users_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
</pre>

