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

    stage('Setup Environment Variables') {
  steps {
    script {
      echo "Parsing and injecting .env variables..."

      // Use your Jenkins file credential
      withCredentials([file(credentialsId: 'myfirstpipelineenv', variable: 'DOTENV_FILE')]) {

        def dotenvContent = readFile(file: DOTENV_FILE)
        def envVars = [:]

        dotenvContent.split('\n').each { line ->
          line = line.trim()
          if (line && !line.startsWith('#')) {
            def parts = line.split('=', 2)
            if (parts.size() == 2) {
              envVars[parts[0].trim()] = parts[1].trim()
            } else {
              echo "Warning: Skipping malformed .env line: '${line}'"
            }
          }
        }

        envVars.each { key, value ->
          env."${key}" = value
          echo "Injected: ${key}=*** (value hidden for security)"
        }
      }
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
