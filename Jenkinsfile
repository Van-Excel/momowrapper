pipeline {
    agent any

    parameters {
        booleanParam(name: 'CLEAN_WORKSPACE', defaultValue: false, description: 'Clean workspace before starting?')
    }

    environment {
        COMPOSE_PROJECT_NAME = "wrapper_pipeline"
        APP_PORT = "8000"
    }

    stages {
        stage('Clean Workspace') {
            when {
                expression { return params.CLEAN_WORKSPACE == true }
            }
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
                // Write the file to .env
                sh '''
                  echo "Copying env file..."
                  cp "$DOTENV_FILE_PATH" .env
                  docker-compose --env-file .env -f docker-compose.yml up -d --build
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

