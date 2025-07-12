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
                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        sh '''
                          echo "Using env file: $DOTENV_FILE_PATH"
                          docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                          docker-compose ps
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                      echo "Waiting for web service..."
                      retries=5
                      while ! docker-compose exec -T web true; do
                        if [ $retries -eq 0 ]; then
                          echo "Web service did not come up in time"
                          exit 1
                        fi
                        echo "Still waiting..."
                        retries=$((retries - 1))
                        sleep 5
                      done

                      echo "Running tests..."
                      docker-compose exec -T web pytest tests/
                    '''
                }
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
