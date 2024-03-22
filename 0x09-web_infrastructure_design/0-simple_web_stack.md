Simple Web Stack
To design a simple web infrastructure that hosts the website reachable via www.foobar.com, let's start with the basics.
1.	User Accessing Website:
•	A user types www.foobar.com into their web browser.
2.	Server:
•	A server (physical or virtual machine) with IP address 8.8.8.8 is set up to host the website.
3.	Domain Name:
•	The domain name, foobar.com, is registered and configured with a DNS (Domain Name System) provider to point to the server's IP address (8.8.8.8). This allows users to reach the website by typing www.foobar.com into their browsers.
4.	DNS Record:
•	The "www" in www.foobar.com is a subdomain. The DNS record associated with www is a CNAME (Canonical Name) record, which points to the main domain foobar.com. This record directs traffic to the correct server.
5.	Web Server (Nginx):
•	Nginx is installed and configured on the server to handle incoming HTTP requests. It acts as a reverse proxy, forwarding requests to the application server and serving static files directly if needed.
6.	Application Server:
•	An application server, such as Gunicorn or uWSGI for Python applications, is installed and configured. It is responsible for executing the application code (e.g., Python, PHP) and generating dynamic content based on user requests.
7.	Application Files (Code Base):
•	The application files, containing the website's codebase (e.g., HTML, CSS, JavaScript, server-side scripts), are deployed on the server. These files are served by the application server in response to user requests.
8.	Database (MySQL):
•	MySQL, a relational database management system, is installed and configured on the server. It stores and manages the website's data, such as user information, content, and configurations.
9.	Communication with User's Computer:
•	When a user requests the website, their computer sends an HTTP request to the server's IP address (8.8.8.8). The request is routed through the internet to the server. The server processes the request, retrieves necessary resources (static files or dynamic content), and sends back an HTTP response to the user's computer.
Issues with this Infrastructure:
1.	Single Point of Failure (SPOF):
•	Since all components are hosted on a single server, any failure in hardware or software could result in downtime for the entire website.
2.	Downtime During Maintenance:
•	When maintenance tasks, such as deploying new code or updating server configurations, are performed, the web server needs to be restarted, resulting in downtime for the website.
3.	Limited Scalability:
•	If the website experiences a sudden increase in traffic, the single server may not be able to handle the load efficiently, leading to degraded performance or downtime. Scaling options are limited with this setup.