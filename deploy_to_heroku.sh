#!/bin/sh

#################################################################
# SHELL SCRIPT DEPLOY SG-TAXI APP TO HERORU
#################################################################

heroku create sgtaxi-heroku-app --buildpack heroku/python
heroku git:remote -a sgtaxi-heroku-app
git push heroku master
echo 'deploy OK, please visit the app via http://sgtaxi-heroku-app.herokuapp.com'