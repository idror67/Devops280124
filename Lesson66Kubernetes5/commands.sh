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