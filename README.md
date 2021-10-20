# python-ci-exercise
A simple travis-ci exercise repository

## Goals:
- Know Travis CI
- Be able to write simple configuration file for Travis CI and run it

## Steps:
- Access [Travis CI](https://www.travis-ci.com) and Sign In with your GitHub account
- Fork this repository to your GitHub account
- Add file **.travis.yml** to your python-ci-exercise repository, including command **python catstr.py hello world** anb **python catstr.py hello world !!** in your testing
- Run a build in [Travis CI](https://www.travis-ci.com). You can see your repositories in ‘dashboard' page in Travis CI.
- The build may be failed. You can modify **catstr.py** and **.travis.yml** to make the build succeed, then commit to your repository. The commit will trigger a build on Travis CI automatically. 
- Repeat the previous step until a build succeeds. **Warning:** You should always include those two commands in your building process.
- Finally, send a screenshot, which captures the building history of your python-ci-exercise repository, to the TA

## References:
- https://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html
- https://docs.travis-ci.com
