# AutoEnumerator
AutoEnumerator is a project intended for those with no penetration testing experience. AutoEnumerator allows various penetration testing tools such as nmap, nikto, and gobuster to run one after the other with a simple click of a button.

# Usage and Installation
AutoEnumerator is currently only supported on Linux. To get this repository, simply type ```git clone https://github.com/ChinmayBhide154/AutoEnumerator```
Furthermore, if the user is not using Kali Linux, (a specific penetration testing distribution of Linux) they will have to install the following tools on their machine before proceding:
 - Nmap (along with the vulners script)
 - Nikto
 - Gobuster
 
 In the video below, I am using a metasploitable 2 VM as my target machine (hence the obscene number of CVE's). Here is how it works:
 1. Type in the IP Address of the Target
 2. Click on "Scan"
 3. Wait about 5 minutes for the scan to complete. The results of the scan will show in each of the tabs.
 
![image](https://user-images.githubusercontent.com/85247848/177885065-f88bd524-bc72-4478-890b-2586d0aff667.png)
![image](https://user-images.githubusercontent.com/85247848/177885171-5b365b27-f638-4c18-b5b6-35161586d26c.png)
![image](https://user-images.githubusercontent.com/85247848/177885230-fc32c4e9-c44f-4f26-8847-7ed6e0781fc6.png)
![image](https://user-images.githubusercontent.com/85247848/177885306-1c7584cb-2809-4848-b54c-801d31899ac0.png)
![image](https://user-images.githubusercontent.com/85247848/177885458-440ced85-cf73-4ce4-963f-7ef171f16eab.png)

# Future Updates
 - Will containerize with docker so that the app can be used on any machine (Not just Linux)

# Code of Conduct
I am not responsible for any unethical uses of AutoEnumerator. Only use on apps you have permission to test.

