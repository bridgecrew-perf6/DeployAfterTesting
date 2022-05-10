pipeline {
  agent any
  triggers {
    GenericTrigger(causeString: 'Generic Webhook Trigger', 
                   genericVariables: [[key:'TAG', value: '$.release.tag_name'],
                                      [key:'REMOVING', value: '$.head_commit.removed']])
  }
  stages {
    stage("") {
      steps
    }
  }
}
