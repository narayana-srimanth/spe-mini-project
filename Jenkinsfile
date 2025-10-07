pipeline {
    agent any

    // This block triggers the pipeline automatically on a push to the GitHub repo.
    triggers {
        githubPush()
    }

    environment {
        // Define a base name for the image. The username will be added later.
        IMAGE_NAME_BASE = "scientific-calculator" 
    }

    stages {
        stage('Checkout') {
            steps {
                // Clones your repository from GitHub
                git 'https://github.com/narayana-srimanth/spe-mini-project'
            }
        }
        stage('Test') {
            steps {
                // Runs the Pytest unit tests
                sh 'pip install pytest'
                sh 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Builds the Docker image using the base name
                echo "Building Docker image: ${IMAGE_NAME_BASE}:${BUILD_NUMBER}"
                sh "docker build -t ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // Uses your global credential with the ID 'docker-creds'
                withCredentials([usernamePassword(credentialsId: 'docker-creds', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    
                    echo "Logging in to Docker Hub as ${DOCKER_USERNAME}..."
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    
                    // Construct the full image name using the username from the credential
                    def fullImageName = "${DOCKER_USERNAME}/${IMAGE_NAME_BASE}"
                    
                    echo "Tagging image as ${fullImageName}:${BUILD_NUMBER} and ${fullImageName}:latest"
                    sh "docker tag ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ${fullImageName}:${BUILD_NUMBER}"
                    sh "docker tag ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ${fullImageName}:latest"
                    
                    echo "Pushing Docker image to Docker Hub..."
                    sh "docker push ${fullImageName} --all-tags"
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                // Triggers the Ansible playbook for deployment
                echo "Deploying application using Ansible..."
                ansiblePlaybook(
                    playbook: 'playbook.yml',
                    inventory: 'inventory',
                    credentialsId: 'ansible-credentials' // Assumes SSH key for localhost
                )
            }
        }
    }
    post {
        always {
            // Cleans up workspace and logs out of Docker Hub
            cleanWs()
            sh 'docker logout'
        }
    }
}