pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "wrapper_pipeline"
        APP_PORT = "8000"
    }

    stages {
        // Corrected indentation for this stage
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('clone repository') {
            steps {
                echo "cloning project"
                checkout scm
            }
        }

        stage('Build and Start Containers') {
            steps {
                script {
                    echo "Provisioning .env file and building Docker containers..."

                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        sh(script: """
                            chmod 666 /var/run/docker.sock
                            docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                            sleep 10
                        """,
                        env: [DOTENV_FILE_PATH: DOTENV_FILE_PATH])
                    }
                }
            }
        }

        stage('test') {
            steps {
                echo "This is the test phase"
                sh 'docker-compose exec -T web pytest tests/'
            }
        }

        stage('deploy') {
            steps {
                echo "This is the deploy phase"
            }
        }
    }

    post {
        always {
            echo "cleaning up docker containers and volumes"
            sh 'docker-compose -f docker-compose.yml down -v'
        }
    }
}
  }
}
