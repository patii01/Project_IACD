## Assignment 4 and 5

Deploy the multi-container application using Kubernetes Imperative Approach

    - See status of the container: minikube status minikube

    - Deploy containers on kubernetes with replicas: 
        - kubectl create deployment kubs-mongo-proj-depl --image=mongo
        - kubectl create deployment kubs-backend-proj-depl --image=patii01/project_iacd_backend:backend_image --port=80 --replicas=2
        - kubectl create deployment kubs-frontend-proj-depl --image=patii01/project_iacd_frontend:frontend_image --port=3000 --replicas=3

    - See deployments: kubectl get deployments
    - See pods: kubectl get pods

Deploy the multi-container application using Kubernetes Declarative Approach

    - Change the connection in the bakend to: `mongodb://${process.env.DB_ADDRESS}:27017/course-goals`
    - Delete old image of backend
    - Build the image and push to Docker Hub: 
        - docker build -t backend_image . (in the folder backend)
        - Tag: docker tag backend_image:latest patii01/project_iacd_backend:backend_image
        - Push docker push patii01/project_iacd_backend:backend_image

    - minikube start
    
    - Persistent Volume Mongo: kubectl apply -f=mongo-pv.yaml
    - Persistent Volume Claim Mongo: kubectl apply -f=mongo-pvc.yaml

    - Persistent Volume Backend: kubectl apply -f=backend-pv.yaml
    - Persistent Volume Claim Backend: kubectl apply -f=backend-pvc.yaml

    - Deployment mongo: kubectl apply -f=mongo-deployment.yaml 
    - Service mongo: kubectl apply -f=mongo-service.yaml 

    - Deployment backend: kubectl apply -f=backend-deployment.yaml 
    - Service backend: kubectl apply -f=backend-service.yaml 

    - Deployment frontend: kubectl apply -f=frontend-deployment.yaml
    - Service frontend: kubectl apply -f=frontend-service.yaml

    - See deployments: kubectl get deployments
    - See services: kubectl get services

    - minikube service backend

    - To test this, use Postman with the address shown after the minikube service backend command.

    - Example:
        - Get: http://127.0.0.1:46107/goals
        - Post: http://127.0.0.1:35925/goals
            - Body, JSON:
                {
                    "text": "teste"
                }
        - Delete: http://127.0.0.1:46107/goals/6541509513f468852e2f059f

    - minikube stop




    
