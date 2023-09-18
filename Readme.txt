API END POINTS: ( http://127.0.0.1:8000/ )

    Booking API : 
        ********** GET and POST requests for authorized users **********
        -- http://127.0.0.1:8000/restaurant/booking/table 

    MenuItems API : 
        ********** GET and POST requests for authorized users **********
        -- http://127.0.0.1:8000/restaurant/menu/items 
        
        ********** GET, PUT, DELETE requests for authorized users **********
        -- http://127.0.0.1:8000/restaurant/menu/items/<int:pk> 


    STATIC HTML PAGES (STATIC PAGES CONTENT ONLY) :
        ********** GET request ONLY **********
        http://127.0.0.1:8000/restaurant/menu/home
        http://127.0.0.1:8000/restaurant/menu/about
        http://127.0.0.1:8000/restaurant/menu/book
        http://127.0.0.1:8000/restaurant/menu/menuitems
        http://127.0.0.1:8000/restaurant/menu/menuitems/<int:pk>
