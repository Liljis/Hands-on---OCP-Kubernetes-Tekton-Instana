# Chapter 1: Create OpenShift Project
oc new-project chapter1

oc project

oc get all

# Chapter 2: Create Flask Application
mkdir employee-api

cd employee-api

### create:

app.py

requirements.txt

# Chapter 3: Test Application Locally

### Create virtual environment:

python3 -m venv venv

source venv/bin/activate

### Install dependencies:

pip install -r requirements.txt

### Run application:

python app.py

### Verify application:

curl localhost:8080/

curl localhost:8080/health

curl localhost:8080/version

### Check running process:

ps -ef | grep python


# Chapter 4: Containerize Application

### Create:

Dockerfile

### Build image:

docker build -t employee-api:v1 .

### Verify image:

docker images

### Run container:

docker run -p 8080:8080 employee-api:v1

### Verify endpoints:

curl localhost:8080/

curl localhost:8080/health

curl localhost:8080/version

### Inspect container:

docker ps

docker exec -it <container-id> sh

### Inside container:

ps -ef

### If unavailable:

ls

env

cat /proc/1/cmdline

cat /proc/1/status


# Chapter 5: Pod Creation

### Create:

pod.yaml

### Deploy pod:

oc apply -f pod.yaml

### Inspect pod:

oc get pods

oc describe pod <pod-name>

oc logs <pod-name>

oc exec -it <pod-name> -- sh

### Delete pod:

oc delete pod <pod-name>


# Chapter 6: Deployments and ReplicaSets

### Create:

deployment.yaml

### Deploy:

oc apply -f deployment.yaml

### Inspect:

oc get deployment

oc get rs

oc get pods

oc get all

### View Deployment YAML:

oc get deployment employee-api -o yaml

# Chapter 7: OpenShift Build from GitHub

### Deploy directly from Git repository:

oc new-app https://github.com/Liljis/Hands-on---OCP-Kubernetes-Tekton-Instana.git \
--context-dir=employee-api \
--name=employee-api

### Inspect created resources:

oc get all

oc get bc

oc get is

oc get svc

### Inspect build logs:

oc logs build/employee-api-1

# Chapter 8: Services

### Inspect Service:

oc describe svc employee-api

### View labels:

oc get pods --show-labels

### Observation:

Service
      ↓ Selector
deployment=employee-api
      ↓
Pod
deployment=employee-api

# Chapter 9: Routes

### Expose Service:

oc expose service employee-api

### Verify Route:

oc get route

### Application URL:

http://employee-api-chapter1.apps.dragon.cp.fyre.ibm.com

### Verify Application:

curl http://employee-api-chapter1.apps.dragon.cp.fyre.ibm.com/

curl http://employee-api-chapter1.apps.dragon.cp.fyre.ibm.com/version

curl http://employee-api-chapter1.apps.dragon.cp.fyre.ibm.com/health


# Chapter 10: ConfigMaps

### Create:

configmap.yaml

### Apply ConfigMap:

oc apply -f configmap.yaml

### Verify:

oc get configmap

oc describe configmap employee-api-config

### Update Deployment:

oc edit deployment employee-api

( or edit through ui deployment --> edit deployment is right corner )

### Verify environment variables:

oc exec -it <pod-name> -- printenv | grep APP



OpenShift Resources Created

BuildConfig

Build

ImageStream

Deployment

ReplicaSet

Pod

Service





Troubleshooting Practice

oc logs <pod-name>

oc describe pod <pod-name>

oc get events --sort-by=.metadata.creationTimestamp

Update deployment image:

oc set image deployment/employee-api employee-api=registry.access.redhat.com/ubi9/nginx-124



