# github-api-interview
It's React/Django based interview project that communicates with Github API.<br>
Before going to live I highly suggest to use your test github account [link to live](http://ec2-52-28-6-236.eu-central-1.compute.amazonaws.com/)
<br> 
Some of the features: stateless backend, synced session between tabs, project works without a database (yet).

![Image of the project](https://i.imgur.com/4hnYaIw.png)

# TODO:
- [ ] Unit tests
- [ ] Move deployment of the front end to serve bit.ly/CRA-deploy
- [ ] Solve "Resource not accessible by integration" on some github endpoints
- [ ] Use cookies instead of local storage

# Tech Stack
* python/Django
* Django-rest-framework
* React
* Docker/Docker-compose
* nginx

# Requirements:
 * node==14

# Deployment
Deployment uses docker and docker-compose. <br>
* create production version of django_server.env.example and node_server.env.example (without .example extension)
## Frontend:
### ec2, docker-compose flow:

```
# install nodejs and npm

$curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
$sudo yum install -y nodejs

$npm config set registry http://registry.npmjs.org/  

$npm i react-scripts
$npm run build
```