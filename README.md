## Simple project using Page Object model and selenium to automate https://wikipedia.org
### Structure:
+ Pages
```
+ Base page 
+ Login page
+ Main page
+ Search Results page
```
+ Tests:
```
+ Regression.feature
+ Validation.feature
```
### Installation
```
brew install python
brew install chromedriver
pip install git+https://github.com/behave/behave
pip install -r requirements.txt
```
### Run 
```
behave
```
+ Use tag
```
behave --tags=regression,search
```
+ Generate allure report
```
behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=regression,search  
allure generate --clean "allure-results" -o "allure-report"
allure serve allure-results
```
+ Run parallel (by features)
```
python behave-parallel.py --tags=regression,search
```
