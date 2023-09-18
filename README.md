# LittleLemon
A website for the LittleLemon Restaurant 

## Running the Project

Make sure you have pipenv installed

If not you can use: 

```
pip install pipenv
```

After making sure pipenv is on your system run the following commands in order
_Do make sure you have the correct directory opened in your terminal_

```
pipenv shell
pipenv install
py manage.py runserver
```

The server should be up and running, now you can use the API endpoints to test the output.

# API END POINTS: 

## Booking API : 
**GET and POST requests for authorized users**

`http://127.0.0.1:8000/restaurant/booking/table`

## MenuItems API : 
**GET and POST requests for authorized users**
    
`http://127.0.0.1:8000/restaurant/menu/items`

**GET, PUT, DELETE requests for authorized users**
    
`http://127.0.0.1:8000/restaurant/menu/items/<int:pk>` 


## STATIC HTML PAGES (STATIC PAGES CONTENT ONLY) :
**GET request ONLY**

`
http://127.0.0.1:8000/restaurant/menu/home
http://127.0.0.1:8000/restaurant/menu/about
http://127.0.0.1:8000/restaurant/menu/book
http://127.0.0.1:8000/restaurant/menu/menuitems
http://127.0.0.1:8000/restaurant/menu/menuitems/<int:pk>
`
