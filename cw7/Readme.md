# How to run the app in Kubernets

1. Using docker start kuberenetes
2. deploy the app using the atached `example-deployment.yaml`

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: testcontainers/helloworld
        ports:
        - containerPort: 8080
        - containerPort: 8081

```

You can deploy it using the command

```bash
kubectl --context docker-desktop apply -f example-deployment.yaml
```

3. Deploy a service with loadbalancer

```yml
apiVersion: v1
kind: Service
metadata:
  name: multi-port-service-service
spec:
  selector:
    app: nginx
  type: LoadBalancer
  ports:
    - name: http
      protocol: TCP
      port: 8080
      targetPort: 8080
    - name: https
      protocol: TCP
      port: 8081
      targetPort: 8081
```

with command
```bash
kubectl --context docker-desktop apply -f example-service.yaml
```

4. Check the adresses:
   1. http://localhost:8080
   2. http://localhost:8081
5. Use curl to GET on the adress `curl http://localhost:8080/uuid`