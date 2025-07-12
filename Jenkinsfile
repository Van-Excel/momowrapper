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

    stage('Inject .env') {
      steps {
        withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE')]) {
          sh 'cp $DOTENV_FILE .env'
        }
      }
    }

    stage('Build') {
      steps {
        sh 'docker-compose up -d --build'
        sh 'sleep 10'
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
