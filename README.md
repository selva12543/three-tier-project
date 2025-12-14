
# 💎 Three-Tier AWS Architecture

### Overview
This project implements a classic three-tier architecture on AWS, consisting of:

✳️ Presentation Layer (Web Tier) – A single EC2 instance running the web server. we can use ASG in production environment.

✳️ Application Layer (App Tier) – A single EC2 instance running the application backend.we can use ASG in production environment.

✳️ Data Layer (Database Tier) – An Amazon RDS instance. we can use Multi-AZ in production.



## Architecture Diagram 

<img width="2096" height="1239" alt="new1" src="https://github.com/user-attachments/assets/ea44d01d-77c4-4894-ba7b-1f391930c37c" />


## Deployment Steps
### 1. Create a VPC
### 2. Create 6 Subnets
- 2 Subnets for Web Server
- 2 Subnets for App Server
- 2 Subnets for Database
### 3. Create Route Tables
- Public Route Table: Connects with Internet Gateway and 2 public subnets.
- Private Route Table: Create Private Route table for each subnet and Map NatGateway from each Availability zone for High Availability.

### 4. Create 5 Security Groups

- interfacing LB: it get SSH (ALL), HTTP (ALL), HTTPS (ALL) from internet.

- WebServer-SG: Allows SSH (ALL), HTTP (ALL), HTTPS (ALL). it get traffic from interfacing LB

- internal LB:Allows 5000 from WebServer-SG, SSH from WebServer-SG, 80 from WebServer-SG, 443 from WebServer-SG

- AppServer-SG: only receive traffic from internal LB.

- DB-SG: Allows 3306 from AppServer-SG.

###  5. Create Route 53 (R53) Hosted Zone
- Create a Hosted Zone for a domain name.
- Map R53 NameServer with your Domain Service Provider.
- Create a CNAME record in R53 from ACM to validate your domain ownership.(optional)

### 6. Create RDS
- Create a DB Subnet group at least 2 subnets needed.
- Create a MySQL DB in a private subnet with DB-SG.
### 7. Create Web Server EC2
- Launch an EC2 instance in the public subnet with WebServer-SG.
### 8. Create App Server EC2
- Launch an EC2 instance in the private subnet with AppServer-SG.
### 9. Login to App Server via .pem file from WebServer
    vi project.pem

    chmod 400 project.pem

    ssh -i project.pem ec2-user@10.0.4.162    # remote login

### 10. Setup Database
    # install mysql

    sudo yum install mysql -y    

    mysql -h Rds-endpoint -P 3306 -u admin -p ****

- Provide queries from commands.sql file to create DB, tables, and insert data into the table.

### 11.  Setup App Server

    sudo yum install python3 python3-pip -y
    pip3 install flask flask-mysql-connector flask-cors
    vi app.py

    nohup python3 app.py > output.log 2>&1 &
    ps -ef | grep app.py

    cat output.log 
    curl http://10.0.3.47:5000/login
   
### 12.  Setup Web Server

    sudo yum install httpd -y
    sudo service httpd start
    cd /var/www/html/
    touch index.html script.js styles.css

### 13. Create Application Load Balancer (ALB)
- Create Backend Target Group for App Server EC2 with Backend Load Balancer.
- Create Frontend Target Group for Web Server EC2 with Frontend Load Balancer.
### 14. Configure Route 53 to Load Balancer
- Create an A record with alias pointing to the Frontend Load Balancer.

### ✅ Result [Visit ](http://75.101.191.233/index.html)

- All tiers are connected and functioning: Web → App → RDS.
- The web server successfully communicates with the app server, and the app server connects to the RDS MySQL database
