pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 test.py'
            }
        }
        post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
