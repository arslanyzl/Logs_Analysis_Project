# Logs_Analysis_Project

### Project Overview
>This project is part of Full Stack Web Developer Nanodegree, we'll work with data that could have come from a real-world 
web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. 
The web server and the reporting tool both connect to the same database, allowing information to flow from the web server 
into the report.

### How to Run?

#### Required programs:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup:
  1. Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  2. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here.
  3. Unzip data file after downloading it.
  4. Move downloaded newsdata.sql file to 1. downloaded - ```fullstack-nanodegree-vm/vagrant```
  
#### Runing:
  1. In the downloaded fullstack-nanodegree-vm repository run this in terminal:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant.
  
  4. To load the data, use the command in terminal
  ```
    psql -d news -f newsdata.sql
  ```
  5. Download ```news-reporting``` file and move to ```fullstack-nanodegree-vm/vagrant```. Run this in termal by:
  ```
    python3 news-reporting.py
  ```
  
 
