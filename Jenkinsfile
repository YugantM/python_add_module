pipeline{
	agent any 

stages{
	
	stage('Build'){
		steps{
			echo 'building process starts...'
			sh 'cd add'
			sh 'python setup.py build'
		}
	}

	stage('Testing') {
		steps{	
			echo 'testings starts...'	
		 	sh 'cd ./add/python_add_module/add'
		 	sh 'python test_add.py'
		}
	}

	stage('Package'){
		steps{
			echo 'packaging starts...'
			sh 'cd ./add'
			sh 'python setup.py install --root="$pkgdir/" --optimize=1 --skip-build'
		}
	}


}
}