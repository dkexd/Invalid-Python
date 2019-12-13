Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.7.4' } }
    stages {
        stage('build') {
            steps {
                ps 'python petuch.py'
            }
        }
    }
}