1. **Set Up the Environment:**
   - Make sure Docker is installed:
     ```bash
     # Check Docker version
     docker --version
     ```
   - Clone or download the web application project:
     ```bash
     # Clone the project from a Git repository
     git clone https://github.com/M-Enes/todo-app.git
     ```

2. **Create a Dockerfile:**
   - Create a Dockerfile in the project directory:
     ```bash
     # Navigate to the project directory
     cd <project_directory>
     # Create a new Dockerfile
     touch Dockerfile
     ```
   - Open the Dockerfile with a text editor and define the image:
     ```Dockerfile
     # Use an existing base image
     FROM nginx:latest
     # Copy the web application files to the container
     COPY . /usr/share/nginx/html
     ```

3. **Build the Docker Image:**
   - Build the Docker image using the Dockerfile:
     ```bash
     docker build -t my-web-app .
     ```

4. **Run the Docker Container:**
   - Run the Docker container from the image:
     ```bash
     docker run -d -p 8080:80 my-web-app
     ```
   - Check if the container is running:
     ```bash
     docker ps
     ```

5. **Test the Dockerized Web Application:**
   - Open a web browser and navigate to `http://localhost:8080` to access the web application.
   - Interact with the application to ensure it functions correctly within the Docker container.

6. **Publish the Docker Image (Optional):**
   - Log in to Docker Hub (if you haven't already):
     ```bash
     docker login
     ```
   - Tag the Docker image with your Docker Hub username and repository name:
     ```bash
     docker tag my-web-app <username>/<repository_name>:<tag>
     ```
   - Push the Docker image to Docker Hub:
     ```bash
     docker push <username>/<repository_name>:<tag>
     ```

7. **Cleanup:**
   - Stop and remove the running container:
     ```bash
     docker stop <container_id>
     docker rm <container_id>
     ```
   - Delete the Docker image (if necessary):
     ```bash
     docker rmi my-web-app
     ```