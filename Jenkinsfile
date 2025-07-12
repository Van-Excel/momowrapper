pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "wrapper_pipeline"
        APP_PORT = "8000"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Build & Start Containers') {
            steps {
                script {
                    echo "Provisioning .env and building containers..."
                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        sh label: 'Build Docker', script: '''#!/bin/bash
                            echo "Using env file: $DOTENV_FILE_PATH"
                            docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                            sleep 10
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'docker-compose exec -T web pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."
                // Add your deployment logic here
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker containers and volumes..."
            sh 'docker-compose -f docker-compose.yml down -v'
        }
    }
}
