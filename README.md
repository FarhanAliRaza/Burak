# Burak
Burak is PWA B2B ecommerce marketplace that helps mom-and-pop stores source inventory and manage their debit and credits
 
---------
## About the Project
I started to build this mvp for my startup in 2019 but then I did not even launched it. Because it required a large capital. But I learnt a lot of stuff from this web app. It taught me few things about startups, plan first build later and why business plans matter in a startup pitch :). It really helped me to learn Django.I built this in urdu so that it will be easier for local people to understand. It is not complete, it was Just an MVP.


---------

## Setup
	Phone = 03123456789
	Pass  = 1234
	With Docker 
		docker build -t burak -f Dockerfile .
		docker run -ti -p 8000:8000 burak
	Without Docker 
		pipenv shell
		pip3 install -r requirements.txt
		activate enviroment
		python manage.py runserver
	open 127.0.0.1:8000 or localhost:8000

---------

## ScreenShots

## Home page for Shops
  <img src='./screenshots/home.png' alt=''  height="600"/>
## Home Page Dark Mode :) 
<img src='./screenshots/home_dark.png' alt='' height="600" />
## Add to Cart
<img src='./screenshots/add_to_cart.png' alt='' height="600" />
## Cart 
<img src='./screenshots/cart.png' alt='' height="600" />
## Cart Delete
<img src='./screenshots/cart_delete.png' alt='' height="600" />
## Dukan view of summary of purchasing and credits given
<img src='./screenshots/dukan_acc_detail.png' alt='' height="600" />
## Detail view of customer credits and debits
<img src='./screenshots/khata_view_customer.png' alt='' height="600" />
## Summary of customers credits and debits
<img src='./screenshots/khata.png' alt='' height="600" />
## Search Page
<img src='./screenshots/search_p.png' alt='' height="600" />
## Search Result 
<img src='./screenshots/search_result.png' alt='' height="600" />
## Order Detail 
<img src='./screenshots/order_detail.png' alt='' height="600" />

---------
