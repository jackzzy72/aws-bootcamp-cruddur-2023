# Week 6 — Deploying Containers

### TEST RDS connection

### Create HealthCheck code in app.py and create Health check script

### Create ECS 

### Create ECR - Repsoitory

#### log into ECR - push python 3.10 to ECR repository and change Dockerfile 

### load docker contatinner and test health check

### build image backend-flask

### push backend-flask

#### add enviorment paramenter into SSM
#### Create 2-seucrity group
#### Create trust policy and permissiong policy for both secuity group

### Create task definition file

#### create service wihout service option through web interface 
#### not task
````
    aws ecs execute-command  \
    --region $AWS_DEFAULT_REGION \
    --cluster cruddur \
    --task aba2dcce4f334816a6d82f5a0c0b275f \
    --container backend-flask \
    --command "/bin/bash" \
    --interactive
```

````
    aws ecs execute-command  \
    --region $AWS_DEFAULT_REGION \
    --cluster cruddur \
    --task f9d66c18ca534872ab4ce492420496ab \
    --container frontend-react-js \
    --command "/bin/bash" \
    --interactive
```