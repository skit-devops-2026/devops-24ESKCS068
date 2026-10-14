pipeline {
    agent any

    options {
        timeout(time: 15, unit: 'MINUTES')
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Repository Hygiene') {
            steps {
                echo 'Running repository hygiene checks...'
                sh 'bash scripts/hygiene.sh'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                sh 'make install'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Running automated test suite...'
                sh 'make test'
            }
        }

        stage('Build Artifacts') {
            steps {
                echo 'Building project artifacts...'
                sh 'make build'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        success {
            echo 'Student Management System build and test pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Please check build logs.'
        }
    }
}
