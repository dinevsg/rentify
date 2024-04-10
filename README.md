<h2>Intro</h2>
  <p>Rentify is a car rental platform where users can book their desired car</p>
  <p><a href="https://rentify-9i9u.onrender.com/">Rentify.com</a></p>
  <p>For better experience use staff credentials
    <ul>
      <li>email - test@test.bg</li>
      <li>password - test7777</li>
    </ul>   
  </p>    
  <p>Your gift card for booking</p>
    <ul>
      <li>Card number - 4242 4242 4242 4242</li>
      <li>Expire date - Every mm/yy in the future</li>
      <li>CVC - Three random digits by your choice</li>
    </ul>
<h2>App</h2>
<p><strong>Users</strong></p>
  <ul>
    <li>Extended django user</li>
    <li>Staff users have permissions to create, read, update and delete content directly in the platform</li>
    <li>Regular(logged in) users could book cars, write reviews and edit their profile</li>
    <li>Google login functionality</li>
  </ul>
  
<p><strong>Cars, Brands and Categories</strong></p>
  <ul>
    <li>Every car on the platform could be booked</li>
    <li>Cars are divided by brands and categories</li>
    <li>Staff users can add, edit and delete cars, brands and categories</li>
    <li>All three models have relation between them by ForeignKey</li>
  </ul>

  <p><strong>Reviews and contact</strong></p>
  <ul>
    <li>Every logged in user could write reviews about the platform</li>
    <li>Users can access their reviews from the profile details page and delete them</li>
    <li>Staff users could delete all of the reviews who violates the good standarts</li>
    <li>Integrated Mailtrap for contacting the platform</li>
  </ul>

  <p><strong>Bookings and payments</strong></p>
  <ul>
    <li>Registered users could make a booking</li>
    <li>Start date has a validator if end date is behind it</li>
    <li>Bookings can be accessed via profile details page</li>
    <li>Integrated Stripe for payment provider</li>
  </ul>

<h2>Useful packages</h2>
  <p>Some of most important third party apps used in the platform</p>
    <ul>
      <li>Cloudinary</li>
      <li>Mailtrap</li>
      <li>Stripe</li>
    </ul>  
  
<h2>Tech stack</h2>
  <ul>
    <li>Django</li>
    <li>JS</li>
    <li>HTML</li>
    <li>Tailwind</li>
  </ul> 

<h2>Run locally</h2>
  <ul>
    <li>Setup your virtual enviroment - <code>virtual env - python -m venv venv</code></li>
    <li>Clone this repository - <code>git clone https://github.com/dinevsg/rentify.git</code></li>
    <li>Install dependencies - <code>pip install -r requirements.txt</code></li>
    <li>Install node modules - <code>npm install</code></li>
    <li>Migrate - <code>python manage.py migrate</code></li>
    <li>Create super user - <code>python manage.py createsuperuser</code></li>
    <li>Start app - <code>python manage.py runserver</code></li>
  </ul>

<h2>Screenshots</h2>
<img src="https://iili.io/Jk6tjea.png">
<img src="https://iili.io/Jk6tXdF.png">
<img src="https://iili.io/Jk6t0WQ.png">
<img src="https://iili.io/Jk6tabj.png">
<img src="https://iili.io/Jk6t1sV.png">
<img src="https://iili.io/Jk6tGqB.png">
<img src="https://iili.io/Jk6tVg1.png">
<img src="https://iili.io/Jk6th5g.png">
    
