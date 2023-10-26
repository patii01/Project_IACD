## Assignment 1 and 2

__Network__
- Create Network
- docker network create projectdb

__Mongo__
1. Run database with the network
    - docker run --name mongo --network projectdb mongo

__Backend__
1. In the code of the backend in the "app.js" change in the connection: mongodb://mongo:27017/course-goals
2. Create the image for the backend
    - docker build -t backend_image . 
3. Run the backend part
    - docker run --name backend --network projectdb -p 80:80 backend_image

__Frontend__

1. Create the image for the frontend
    - docker build -t frontend_image .
2. Run the frontend part
    - docker run -it --name frontend --network projectdb -p 3000:3000 frontend_image

__Persist data from database__

1. Create volume for the database
    - docker volume create mongodb_data

2. Run the database part with the volume
    - docker run --name mongo --network projectdb -v mongodb_data:/data/db mongo

__Persist data from Node js__

1. Create volume for the backend
    - docker volume create app_logs
    
2. Run the database part with the volume
    - docker run --name backend --network projectdb -p 80:80 -v app_logs:/logs backend_image
