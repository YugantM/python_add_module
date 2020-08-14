pipeline{
	agent any 

stages{
	
	stage('Build'){
		steps{
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
			echo 'packaging starts...'
			sh 'python setup.py install --root="$pkgdir/" --optimize=1 --skip-build'
		}
	}


}
}