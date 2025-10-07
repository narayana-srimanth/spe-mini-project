pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        IMAGE_NAME_BASE = "scientific-calculator" 
    }

    stages {
        stage('Test') {
            steps {
                sh 'pip install pytest'
                // *** FIX IS HERE: Run pytest as a Python module ***
                sh 'python3 -m pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME_BASE}:${BUILD_NUMBER}"
                sh "docker build -t ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', passwordVariable: 'DOCKOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    script {
                        echo "Logging in to Docker Hub as ${DOCKER_USERNAME}..."
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        
                        def fullImageName = "${DOCKER_USERNAME}/${IMAGE_NAME_BASE}"
                        
                        echo "Tagging image as ${fullImageName}:${BUILD_NUMBER} and ${fullImageName}:latest"
                        sh "docker tag ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ${fullImageName}:${BUILD_NUMBER}"
                        sh "docker tag ${IMAGE_NAME_BASE}:${BUILD_NUMBER} ${fullImageName}:latest"
                        
                        echo "Pushing Docker image to Docker Hub..."
                        sh "docker push ${fullImageName} --all-tags"
                    }
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
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
            cleanWs()
            sh 'docker logout'
        }
    }
}