Secured and Monitored Web Infrastructure

To design a secured and monitored web infrastructure hosting www.foobar.com, we'll incorporate firewalls, SSL encryption, and monitoring tools. Here's the breakdown:
1.	User Accessing Website:
•	A user accesses www.foobar.com through their web browser.
2.	Server Setup:
•	Three servers are employed, each with the following components:
•	Web Server (Nginx)
•	Application Server
•	Database Server (MySQL)
3.	Firewalls:
•	Three firewalls are added to enhance security.
•	One firewall is placed in front of each server to control incoming and outgoing traffic, filtering and blocking potentially malicious connections.
4.	SSL Certificate (HTTPS):
•	An SSL certificate is installed on the load balancer to enable HTTPS encryption for traffic between users and the website. This ensures data confidentiality, integrity, and authenticity, protecting sensitive information from eavesdropping and tampering.
5.	Monitoring Clients (Sumo Logic):
•	Three monitoring clients, such as Sumo Logic, are deployed on each server to collect and analyze system metrics, logs, and performance data in real-time.
•	These monitoring tools provide insights into server health, resource usage, application performance, and security incidents, enabling proactive maintenance and troubleshooting.
Specifics about the Infrastructure:
•	Firewalls: Firewalls are added to restrict unauthorized access to the servers and prevent potential security threats.
•	HTTPS Encryption: Traffic is served over HTTPS to encrypt data transmitted between users and the website, safeguarding sensitive information.
•	Monitoring: Monitoring tools are used to track server performance, detect anomalies, and troubleshoot issues promptly.
•	Data Collection: Monitoring tools collect data by accessing system logs, metrics, and performance counters from each server, aggregating and analyzing the information to provide insights into the system's health and behavior.
•	Monitoring Web Server QPS: To monitor the web server's QPS (Queries Per Second), you can configure the monitoring tool to track HTTP requests handled by Nginx. This involves setting up custom metrics or utilizing built-in features of the monitoring tool to capture and analyze request rates over time.
Issues with this Infrastructure:
1.	Terminating SSL at the Load Balancer Level:
•	Terminating SSL at the load balancer level can pose a security risk as decrypted traffic is then transmitted over the internal network. It exposes sensitive data to potential interception or tampering.
2.	Single MySQL Server Accepting Writes:
•	Having only one MySQL server capable of accepting writes creates a single point of failure. If the server fails, it can result in data loss or downtime for the website.
3.	Identical Components Across Servers:
•	Having servers with identical components (database, web server, and application server) might lead to uniform vulnerabilities. A single vulnerability affecting one component could potentially impact all servers, increasing the risk of widespread outages or security breaches.