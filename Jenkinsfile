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
                checkout scm
            }
        }

        stage('Build & Start Containers') {
            steps {
                script {
                    echo "Provisioning .env and building containers..."
                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        sh """
                            docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                            sleep 10
                        """
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose exec -T web pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."
            }
        }
    }

    post {
        always {
            sh 'docker-compose -f docker-compose.yml down -v'
        }
    }
}
