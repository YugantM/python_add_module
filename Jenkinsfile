pipeline{
	agent any 

stages{
	
	stage('Build'){
		steps{
			sh 'pwd'
			echo 'desplaying the repo'
			sh 'ls'
			echo 'building process starts...'
			sh 'cd add'
			sh 'ls'
			sh 'python setup.py build'
		}
	}

	stage('Testing') {
		steps{	
			echo 'testings starts...'	
		 	sh 'python ./add/test_add.py'
		}
	}

	stage('Package'){
		steps{
			sh 'ls'
			echo 'packaging starts...'
			sh 'sudo python setup.py install --root="$pkgdir/" --optimize=1 --skip-build'
			sh 'ls'
		}
	}


}
}