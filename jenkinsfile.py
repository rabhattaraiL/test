pipeline {
	agent any
	stages {
	    stage('Git-checkout') {
	        steps {
	            echo "Checking out from git repo !!!";
	            git branch: 'main', url: 'https://github.com/rabhattaraiL/test.git'
	        }
	    }
	    stage('File a'){
            steps{
                echo "File a output";
                sh 'python3 a.py'
            }
        }
        stage('File b'){
            steps{
                echo "File b output";
                sh 'python3 b.py'
            }
        }
    }
}