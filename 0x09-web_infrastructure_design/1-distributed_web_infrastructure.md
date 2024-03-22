Distributed Web Infrastructure

To design a distributed web infrastructure hosting www.foobar.com, we'll incorporate multiple servers, a load balancer, and a database cluster. Here's the breakdown:
1.	User Accessing Website:
•	A user types www.foobar.com into their web browser.
2.	Server Setup:
•	Three servers are employed:
•	Two application servers
•	One database server
3.	Web Server (Nginx):
•	Nginx is installed on each application server. It serves as a web server handling incoming HTTP requests, serving static files, and acting as a reverse proxy to the application server.
4.	Application Server:
•	Each application server runs the application codebase. It executes dynamic code, generates content, and interacts with the database to serve user requests.
5.	Load Balancer (HAProxy):
•	HAProxy is deployed as the load balancer to distribute incoming traffic across the two application servers. It improves scalability, reliability, and performance by evenly distributing requests and managing server health.
6.	Application Files (Code Base):
•	The codebase of the website is deployed on both application servers. This ensures redundancy and fault tolerance, allowing the website to remain accessible even if one server fails.
7.	Database (MySQL Primary-Replica Cluster):
•	MySQL is set up as a Primary-Replica cluster, also known as a Master-Slave setup.
•	The Primary node (Master) handles write operations, while the Replica nodes (Slaves) replicate data from the Primary node and handle read operations.
•	This setup improves database performance, fault tolerance, and scalability.
Distribution Algorithm for Load Balancer (HAProxy):
•	HAProxy can be configured with various distribution algorithms. In this setup, we'll use a Round Robin algorithm. It works by sequentially distributing requests across the available servers in a circular order, ensuring each server receives an equal share of traffic.
Active-Active vs. Active-Passive Setup:
•	The load balancer configuration enables an Active-Active setup, where both application servers are actively handling incoming requests simultaneously. In contrast, an Active-Passive setup would designate one server as active while the other remains passive, serving as a backup in case the active server fails. Active-Active setups generally offer better resource utilization and scalability.
Primary-Replica (Master-Slave) Database Cluster:
•	In a Primary-Replica database cluster, the Primary node handles write operations, ensuring consistency and integrity of the data. Replica nodes replicate data from the Primary node asynchronously and handle read operations, distributing the read workload and improving scalability and fault tolerance.
Issues with this Infrastructure:
1.	Single Points of Failure (SPOFs):
•	Potential SPOFs include the load balancer and the database Primary node. If any of these components fail, it could disrupt the entire system.
2.	Security Issues:
•	Lack of firewall configuration exposes servers to potential security threats.
•	Absence of HTTPS encryption leaves data transmitted between users and servers vulnerable to interception.
3.	No Monitoring:
•	Without proper monitoring tools and procedures in place, it's challenging to identify and address performance issues, security breaches, or system failures proactively.