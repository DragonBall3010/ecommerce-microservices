
# E-commerce Microservices

This project consists of multiple microservices for an e-commerce platform. It includes services for managing users, products, and orders. The project uses **Docker**, **Kubernetes**, and **Minikube** to deploy and manage the services in a containerized environment.

## Architecture

The project is structured into three main microservices:

- **User Service**: Handles user management (e.g., creating users, fetching user details).
- **Product Service**: Manages products (e.g., adding products, listing products).
- **Order Service**: Manages orders (e.g., creating orders, fetching order details).

All services are deployed as Docker containers and orchestrated using Kubernetes.

## Prerequisites

Before getting started, make sure you have the following tools installed:

- **Docker**: To build and run Docker containers.
- **Kubernetes**: To deploy and manage containers in a cluster.
- **Minikube**: A tool to run Kubernetes clusters locally.
- **kubectl**: The Kubernetes command-line tool.

## Setting Up the Environment

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ecommerce-microservices.git
cd ecommerce-microservices
```

### Start Minikube

Start a Minikube cluster to run your Kubernetes services locally:

```bash
minikube start
```

### Build Docker Images

Build Docker images for each microservice:

```bash
docker build -t your-dockerhub-username/user-service ./user-service
docker build -t your-dockerhub-username/product-service ./product-service
docker build -t your-dockerhub-username/order-service ./order-service
```

### Push Docker Images to Docker Hub

Push your images to Docker Hub:

```bash
docker push your-dockerhub-username/user-service
docker push your-dockerhub-username/product-service
docker push your-dockerhub-username/order-service
```

### Deploy Services to Kubernetes

Apply the Kubernetes configurations to deploy the services:

```bash
kubectl apply -f ./k8s/user-service.yaml
kubectl apply -f ./k8s/product-service.yaml
kubectl apply -f ./k8s/order-service.yaml
```

### Access Services Locally

Use `kubectl port-forward` to access the services on your local machine:

```bash
kubectl port-forward service/user-service 8080:80
kubectl port-forward service/product-service 8081:80
kubectl port-forward service/order-service 8082:80
```

Now you can access the following endpoints:

- **User Service**: `http://localhost:8080/users`
- **Product Service**: `http://localhost:8081/products`
- **Order Service**: `http://localhost:8082/orders`

## Docker and Kubernetes Configuration

- **Docker**: Each service has its own `Dockerfile` to build the container image. These images are pushed to Docker Hub for deployment.

- **Kubernetes**: Each service has a corresponding Kubernetes deployment configuration (`user-service.yaml`, `product-service.yaml`, `order-service.yaml`) for deploying to a Kubernetes cluster.

## Testing the Microservices

Use tools like **Postman** or **Curl** to test the services. Here are some basic API endpoints you can use:

### User Service:

- `GET /users`: Get a list of users.
- `POST /users`: Create a new user.

### Product Service:

- `GET /products`: Get a list of products.
- `POST /products`: Add a new product.

### Order Service:

- `GET /orders`: Get a list of orders.
- `POST /orders`: Create a new order.

## Project Structure

```plaintext
ecommerce-microservices/
│
├── user-service/
│   ├── Dockerfile
│   └── ... (other files for user service)
│
├── product-service/
│   ├── Dockerfile
│   └── ... (other files for product service)
│
├── order-service/
│   ├── Dockerfile
│   └── ... (other files for order service)
│
├── k8s/
│   ├── user-service.yaml
│   ├── product-service.yaml
│   ├── order-service.yaml
│
└── README.md
```

## Conclusion

This project demonstrates how to build, deploy, and manage microservices in a Kubernetes environment. It provides a foundation for creating scalable and maintainable microservices architectures for real-world applications.

## Additional Notes

- Make sure to replace `your-dockerhub-username` with your actual Docker Hub username.
- If you encounter any issues, ensure that you have proper Docker and Kubernetes configurations, and that the services are correctly defined in their respective `yaml` files.
