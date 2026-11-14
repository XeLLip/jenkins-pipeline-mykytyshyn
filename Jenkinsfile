// Lab 11. Declarative pipeline: Build -> Test -> Deploy (local)
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'mykytyshynapp'
        APP_PORT   = '5055'              // http://localhost:5055 on the host
    }

    triggers {
        // Jenkins checks the GitHub repository every 2 minutes and starts a build if there are new commits
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER -t $IMAGE_NAME:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests inside the image...'
                sh 'docker run --rm $IMAGE_NAME:$BUILD_NUMBER python -m unittest -v'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy stage (local test environment)'
                sh 'docker images $IMAGE_NAME'
                sh '''
                    docker rm -f $IMAGE_NAME 2>/dev/null || true
                    docker run -d --name $IMAGE_NAME -p $APP_PORT:5000 $IMAGE_NAME:$BUILD_NUMBER
                    sleep 3
                    docker exec $IMAGE_NAME wget -qO- http://localhost:5000
                '''
            }
        }
    }

    post {
        success { echo "SUCCESS: ${env.IMAGE_NAME}:${env.BUILD_NUMBER} is running on port ${env.APP_PORT}" }
        failure { echo 'FAILED: see Console Output' }
    }
}
