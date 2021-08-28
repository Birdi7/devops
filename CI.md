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
