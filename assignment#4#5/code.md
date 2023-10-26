## Assignment 4

3. Deploy the multi-container application using Kubernetes Declarative Approach
    - Deployment frontend: kubectl apply -f=frontend-deployment.yaml
    - Deployment backend: kubectl apply -f=backend-deployment.yaml 
    - Deployment mongo: kubectl apply -f=mongo-deployment.yaml 
    - See deployments: kubectl get deployments

    - Service frontend: kubectl apply -f=frontend-service.yaml
    - Service backend: kubectl apply -f=backend-service.yaml 
    - Service mongo: kubectl apply -f=mongo-service.yaml 

    -Run: minikube service frontend-service
    
