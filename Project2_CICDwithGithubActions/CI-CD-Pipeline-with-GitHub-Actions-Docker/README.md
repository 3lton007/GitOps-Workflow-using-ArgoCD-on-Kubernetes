# CI-CD-Pipeline-with-GitHub-Actions-Docker
Elevate Labs DevOps Internship Project 2

## Implementation

- Created a route-based python project with test cases. 
- Issued Docker-compose.yml and Dockerfile to check application workling locally.
- Created cicd.yaml for github actions to automate pytest cases for the application and build Docker image. The newly-build docker image was pushed to Dockerhub Repository with latest tag.
- Once the Github CI/CD Pipeline was achieved successfully, the new image was locally pulled using "docker pull" and tested in local enviroment. 
