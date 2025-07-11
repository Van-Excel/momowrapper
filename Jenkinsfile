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
      stage('inject .env file'){
        steps{
          echo "injecting .env variables"
          configFileProvider([configFile(fileId:'myfirstpipelineenv', targetLocation:'.env')])
        }
      }
    }
    stage ('build'){
      steps{
        echo "This is the build phase"
        sh 'docker-compose -f docker-compose.yml up -d --build'
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
