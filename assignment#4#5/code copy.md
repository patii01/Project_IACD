## Assignment 4 and 5

Deploy the multi-container application using Kubernetes Declarative Approach

    - Change the connection in the bakend to: `mongodb://${process.env.AUTH_ADDRESS}:27017/course-goals`
    - Build the image and push to Docker Hub: 
        - Tag: docker tag backend_image:latest patii01/project_iacd_backend:backend_image
        - Push docker push patii01/project_iacd_backend:backend_image
    
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


    
