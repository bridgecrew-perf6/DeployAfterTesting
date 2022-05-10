pipeline {
  agent any
  triggers {
    GenericTrigger(causeString: 'Generic Webhook Trigger', 
                   genericVariables: [[key:'COMMIT_HASH', value: '$.head_commit.id']])
  }
  stages {
    stage("Echo") {
      steps {
        sh "git log"
        echo "${COMMIT_HASH}"
      }
    }
    stage("Run REDIS server") {
      steps {
        sh "docker run -d --name redis-server redis || true"
      }
    }
    stage("Set hash as commit") {
      steps {
        sh """docker exec redis-server bash -c "set commit ${COMMIT_HASH}" """
      }
    }
  }
}
