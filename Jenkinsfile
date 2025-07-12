pipeline{
  agent any
  environment{
    COMPOSE_PROJECT_NAME = "wrapper_pipeline"
    APP_PORT = "8000"
  }
  stages{
    stage('clone repository'){
      steps{
        echo "cloning project"
        checkout scm
      }
      
    }

   stage('Build and Start Containers') {
            steps {
                script { // Use 'script' block to allow Groovy variables across shell commands
                    echo "Provisioning .env file and building Docker containers..."

                    // 1. Get the path to the temporary .env file from your credential
                    withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE_PATH')]) {
                        // The 'DOTENV_FILE_PATH' variable now holds the path to the temporary .env file
                        // e.g., /tmp/credentials/some_generated_id.env or C:\jenkins_home\workspace\@tmp\...\.env

                        // 2. Use that path directly with docker-compose
                        // Ensure double quotes around "$DOTENV_FILE_PATH" for robustness
                        sh """
                            docker-compose --env-file "$DOTENV_FILE_PATH" -f docker-compose.yml up -d --build
                            sleep 10
                        """
                        // Explanation of why `sh """..."""` is used:
                        // It allows for multi-line shell commands within Jenkins.
                        // Also, it prevents Groovy from trying to interpolate '$' variables itself,
                        // letting the shell (bash or cmd/powershell) handle '$VAR_NAME'.
                    }
                }
            }
    stage('test'){
      steps{
        echo "This is the test phase"
        sh 'docker-compose exec -T web pytest tests/'
      }
      
    }
    stage('deploy'){
      steps{
        echo "This is the deploy phase"
      }
    }
  }

  post{
    always{
      echo "cleaning up docker container and volumes"
      sh 'docker-compose -f docker-compose.yml down -v'
    }
  }
}
