# AutoEnumerator
AutoEnumerator is a project intended for those with no penetration testing experience. AutoEnumerator allows various penetration testing tools such as Nmap, nikto, and gobuster to run one after the other with a simple click of a button.

# Installation
AutoEnumerator is currently only supported on Linux. To get this repository, simply type ```git clone https://github.com/ChinmayBhide154/AutoEnumerator```
Furthermore, if the user is not using Kali Linux, (a specific penetration testing distribution of Linux) they will have to install the following tools on their machine before proceding:
 - Nmap (along with the vulners script)
 - Nikto
 - Gobuster
 
# Usage 
In the first 4 images below, I am using a metasploitable 2 VM as my target machine (hence the obscene number of CVE's). In the last image (With the FTP Tab, my target machine is an available starting point machine from Hackthebox. Please see the results below:

![image](https://user-images.githubusercontent.com/85247848/181116565-be76698b-59a7-4859-9d8e-54827047f10e.png)
![image](https://user-images.githubusercontent.com/85247848/181116649-a43875fc-a1ed-40aa-b6a7-10ca391823bf.png)
![image](https://user-images.githubusercontent.com/85247848/181116702-473dda38-2c65-438c-a537-0f08e90ac0b1.png)
![image](https://user-images.githubusercontent.com/85247848/181116764-42f18568-14ed-49ed-931f-9200573bb59b.png)
![image](https://user-images.githubusercontent.com/85247848/181116833-552592ed-ac83-4ba8-8332-b9a5e2c488af.png)
![image](https://user-images.githubusercontent.com/85247848/181116987-9597ea1e-cdd7-4111-a646-6592208635fb.png)

This app is very simple to use and can be summarized in the following steps: (1) Type in the IP Address of the target machine, in this case, it is 192.168.1.74; (2) Check off the boxes to indicate which kind of scanning you will allow the scanner to perform (In this case, I have enabled all the boxes) and (3) Click "Scan". Thats it! its that simple. 

# Explanation
The results for these scans may seem complicated. I will explain them here by Tab:
 - Open Ports: An open port is simply a port that accepts packets. Port numbers typically have a particular service associated with them. For instance, port 21 is usually for FTP, and port 80 is for http. When a port is open, we can interact with this service. This means that if I type the IP Address into a web browser, I will be able to interact with a webpage since port 80 is open. Additionally, since Port 21 is open, I can download files on the FTP server if I like. This is significant because open ports are the main attack vector for hackers.
 - Vulnerability Analysis: This simply shows the vulnerabilities present in a web application
 - CVE: Stands for "Common Vulnerabilities and Exposures". These show any exploits that are currently lurking out there that people have already found that your app is vulnerable to.
 - Directory Scan: If ports 80 or 443 (http or https) are open, with this option we can see what directories are available for viewing. We can use this tab to see if there is anything exposed on a webpage which should not be exposed.
 - FTP Files: Automatically Lists FTP Files if port 21 is open. Note that this is only possible if anonymous login is allowed.


# Future Update Ideas
 - Will containerize with docker so that the app can be used on any machine (Not just Linux)

# Code of Conduct
I am not responsible for any unethical uses of AutoEnumerator. Only use on apps you have permission to test.

