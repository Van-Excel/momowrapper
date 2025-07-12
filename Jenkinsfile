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
                echo "Cloning project"
                checkout scm
            }
        }

        stage('Build and Start Containers') {
            steps {
                script {
                    echo "Provisioning .env file and building Docker containers..."

                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        // Avoid Groovy interpolation warning by using triple single-quotes
                        sh(script: '''
                            chmod 666 /var/run/docker.sock
                            docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                            sleep 10
                        ''')
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo "Running test phase"
                sh 'docker-compose exec -T web pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo "This is the deploy phase"
            }
        }
    }

    post {
        always {
            echo "Cleaning up docker containers and volumes"
            sh 'docker-compose -f docker-compose.yml down -v'
        }
    }
}
