# Shopfiy Summer 2022 Backend Challenge
## By: Benjamin Chang

This is my inventory tracking web application I have created for the challenge. I used a combination of Python + Flask to create the application, as well as bootstrap 
for some of the styling. 

<img width="1156" alt="crud1" src="https://user-images.githubusercontent.com/57234733/149593329-01b76ba0-971d-4468-92db-27303ae7f532.png">

The user can add a new item specifying:
- the name
- the quantity (stock)
- what category it falls under
- and add a short description

<img width="509" alt="crud2" src="https://user-images.githubusercontent.com/57234733/149593338-47331072-1790-404a-945b-70ca9774a641.png">


An additional functionality I have added is that we can export all the data as a csv file which will be downloaded in your browser. The idea for this was to make it 
easier to obtain all the data, having it all nicely formatted in order to feed into data science pipelines and workflows.

**NOTE: the following Python packages will need to be installed in order for the application to run:**
- pandas
- flask
- flask_sqlalchemy
