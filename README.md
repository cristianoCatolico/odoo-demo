# odoo-demo
### Setup project
- Install Docker and Docker compose
- Create a docker compose file that allows to run odoo
- Add a line where the folder contains the module of school
- Run docker compose file with docker-compose up -d
- Open browser and go to http://localhost:8069

### Comments
- During the creation of the module for school, I realized the structure that a module should have. The models were created however I could not test if it were correct. One obstacle was that the addon did not appear in the dashboard. That was because the file odoo.conf did not have the path of addons. Then the other obstace that I could not overcome was that I was not able to see the the views of the models. I add the security view and the csv, but I do not know why it does not show. I have seen different blogs but not achieved yet. 