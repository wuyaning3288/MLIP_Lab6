pipeline {
  agent any

  environment {
    // Change this if your Miniconda lives elsewhere
    CONDA_HOME = "/opt/anaconda3"
    ENV_NAME   = "mlip"
  }

  stages {
    stage('Checkout') {
      steps {
        // Pull down your GitHub fork
        checkout scm
      }
    }

    stage('Build') {
      steps {
        // Stub: e.g. compile C/Java or package Python wheel
        sh '''#!/bin/bash
        echo 'In C/Java you would compile here; in Python you might build your package'
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''#!/bin/bash
        set -e

        echo "=== Initialize Conda ==="
        # Load conda functions
        source "${CONDA_HOME}/etc/profile.d/conda.sh"

        echo "=== Activate Env: ${ENV_NAME} ==="
        conda activate "${ENV_NAME}"

        echo "=== Installing dependencies (if needed) ==="
        pip install --upgrade pip pytest numpy pandas scikit-learn

        echo "=== Running pytest ==="
        pytest -q
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo 'In a real pipeline you’d publish artifacts or deploy here'
      }
    }
  }

  post {
    always {
      // Archive console log, test reports, etc.
      archiveArtifacts artifacts: '**/reports/*.xml', allowEmptyArchive: true
    }
  }
}
