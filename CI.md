# CI best practices

1. Run checks on every push to master branch
2. Run unit-tests during the CI stage
3. Run linting tools on the CI stage
4. Divide testing part and building part into different
stages of the CI
5. Try to follow single responsibility principal
while writing your jobs — one job should perform
only one goal
6. Cache your dependencies — don't reinstall them on
every workflow trigger

Related to Jenkins best practices:
Inspired by [this](https://www.lambdatest.com/blog/jenkins-best-practices/) website

1. Keep it secure. Use security features such as `Access Control`
2. **Regurally** ackup `JENKINS_HOME` directory, as it contains a lot of configuration
files for your CI
3. Use different job for each branch which is in either
development or in maintainance
4. Use “File Fingerprinting” To Manage Dependencies
5. Keep your configuration simple, don't use any
complicated groovy functions (such as `JsonSlurper`)
