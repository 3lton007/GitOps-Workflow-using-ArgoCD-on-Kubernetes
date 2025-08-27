# GitOps-Workflow-using-ArgoCD-on-Kubernetes

GitOps Workflow using ArgoCD on Kubernetes

## Implementation

- Created Demo app for Argo CD with Deployment.yaml, service.yaml and configmap.yaml. 
- Installed Minikube and ArgoCD. 
- Exposed Port 8080 to localhost to Use ArgoCD UI
- Deployed Application using demo-app.yaml
- Pushed The code changes to Git to Auto Sync with argoCD. Synced with the latest commit.
- Added Demo-app-dev.yaml and Demo-app-prod.yaml to restructure and create multi-enviroment 