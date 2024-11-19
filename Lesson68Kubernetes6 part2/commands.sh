# check the status of the minikube
minikube status

# see all pods in the default namespace
kubectl get pods

# see all pods in all namespaces
kubectl get pods -A

# see all nodes in the cluster
kubectl get nodes

# get namespaces
kubectl get namespaces

# create namespace prod
kubectl create namespace prod

# change the default namespace to prod
kubectl config set-context --current --namespace=<Your NAMESPACE_NAME>

# check the api resources
kubectl api-resources


# delete all workloads in the default namespace
kubectl delete all --all

# get all workloads in the default namespace
kubectl get all

# rollout restart the deployment
kubectl rollout restart deployment <deployment-name>

# change namespace to ilia-flask (by default)
kubectl config set-context --current --namespace=ilia-flask

# look on contexts
kubectl config get-contexts


# list all installed charts
helm list

# list all added repositories
helm repo list

# create bolierplace for the helm chart
helm create <chart-name>

# install local helm chart
helm install <chart-name> <path-to-chart>
helm install my-helm-chart ./my-helm-chart

# look into the template of the helm chart
helm template <chart-name> <path-to-chart>

# upgrade the helm chart
helm upgrade <chart-name> <path-to-chart>
helm upgrade my-helm-chart ./my-helm-chart

# show helm chart history 
helm history <chart-name>
helm history my-helm-chart

# rollback the helm chart 1 revision back
helm rollback <chart-name> 
helm rollback my-helm-chart 

# rollback the helm chart to the specific revision
helm rollback <chart-name> <revision-number>