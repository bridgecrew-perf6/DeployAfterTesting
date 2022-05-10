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
  }
}
