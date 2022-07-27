print("Content-type:text/html\r\n\r\n");
import cgi
import mysql.connector
# open data base connection
db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="fiem")
# prepare a cursor object using cursor() method
cursor=db.cursor()
data=cgi.FieldStorage()
u=data.getvalue('email')
r=data.getvalue('password')
sql=cursor.execute("select * from register_waste where email='{0}'".format(u))
result=cursor.fetchone()
#print(result[0])
for i in range(len(result)):
    d=result[12]
if r==d:
    print("<script>window.alert('login successfull');</script>")
    
    print("""<html>
    <head>
        <title> waste management</title>
        <link rel="stylesheet" href="style11.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" ></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
<body>
    <section id="nav-bar">
        <nav class="navbar navbar-expand-lg navbar-light">
  <a class="navbar-brand" href="#"><img src="images/3590d692e7f5ebdb0d727757eaf5c043.png"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <i class="fa fa-bars"></i>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item ">
        <a class="nav-link" href="#top">HOME </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#services">SERVICES</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#about-us">ABOUT US</a>
      </li>
        <li class="nav-item">
        <a class="nav-link " href="#testimonials" >TESTIMONIAL</a>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="#footer" >CONTACT</a>
      </li>
        <li class="nav-item">
        <a class="nav-link " href="index1.html" >
            <i class="fa fa-user"></i>
            LOGOUT</a>    
      </li>
    </ul>
  </div>
</nav>
    </section>
   <!--------------------------------banner section--------------------> 
    
    <section id="banner">
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <p class="promo-title">CLEAN CITY</p>
                <p> Our aim is to make our city clean and make it more beautiful for the people,animal ,birds so that everyone can breathe in fresh air.</p>
                <a href='http://localhost/phpmyadmin/index.php?route=/database/structure&db=fiem/profileserverfetch.py?email="""+u+
                """'><button class="btn-primary">PROFILE</button>
                </a>
                <a href="wastecontain3.html">	   
                    <button class="btn-primary">waste contain</button>
	            </a>
            </div>
            <div class="col-md-6" text-center>
            <img src="images/2137734236_d085c92666.jpg" class="img-fluid">
            </div>
        </div>
    </div>
        
        <img src="images/maxresdefault.jpg"class="bottom-img">
    </section>
    
<!-----------services section-------------------->
    <section id="services">
    <div class="container text-center">
        <h1 class="title">What we do?</h1>
        <div class="row text-center">
            <div class="col-md-4 services">
                <img src="images/litter-organization-waste-logo-cleaning-png-favpng-Gu7tQ08vkiG2AahCds5XVBhtV.jpg" class="service-img">
                <h4>CLEAN</h4>
                <p> Our aim is to make our city clean and make it more beautiful for the people,animal ,birds so that everyone can breathe in fresh air.Everyone support us for this mission of city clean.the staffs of K.M.C is making their full effort</p>
    
    
            </div>
            <div class="col-md-4 services">
                <img src="images/brown-sand-2645245.jpg" class="service-img">
                <h4>CLEAN BEACHES</h4>
                <p> Our aim is to make our city clean and make it more beautiful for the people,animal ,birds so that everyone can breathe in fresh air. the result of our effor is beaces are clean .</p>
    
    
            </div>
            <div class="col-md-4 services">
                <img src="images/serviceimage3.jpg" class="service-img">
                <h4>TRANSPORT</h4>
                <p> Powerfull Transport which took all the waste for the recycle purposes and this make the city clean and beautiful</p>
    
    
            </div>
            
        </div>
        <a href="sevice3.html"><button type="button" class="btn btn-primary">All services</button></a>
    </div> 
    </section> 
    
<!----------About us---------------> 

    <section id="about-us">
        <div class="container text-center">
        <h1 class="title text-center">Why Choose Us?</h1>
            <div class="row text-center">
                <div class="col-md-6 about-us">
                    <p class="about-title">Why we are different</p>
                        <ul>
                            <li>Give your contribution to clean city</li>
                            <li>Make our city clean and Beautiful</li>
                            <li>Everyone will be able to beathe fresh air.</li>
                            <li>Smell the aweet smell of ground .</li>
                            <li>Everoyone can swim in clear water.</li>
                            <li>Let us your hand in the mission.</li>
                        </ul>
                </div>
                <div class="col-md-6">
                <img src="images/brown-sand-2645245.jpg" height="40px" class="img-fluid">
                </div>
            </div>
            <a href="about_us3.html"><button type="button" class="btn btn-primary">More About Us</button></a>
        </div>
    </section>
<!------------testimonial---------------->
    <section id="testimonials">
        <div class="container">
        <h1 class="title text-center">What People Say</h1>
            <div class="row offset-1">
                <div class="col-md-5 testimonials">
                    <p>everyone should take part in this</p>
                    <img src="images/photo-1544005313-94ddf0286df2.jpg">
                    <p class="user-details"><b> Scarlet</b><br> co-founder at phptography</p>
                </div>
                <div class="col-md-5 testimonials">
                    <p>generous mission to be completed</p>
                    <img src="images/5-create-fake-people-in-2-seconds-on-this-insane-site.webp">
                    <p class="user-details"><b> bethenie</b><br> co-founder a IT</p>
                </div>
                <div class="col-md-5 testimonials">
                    <p>This make our city clean</p>
                    <img src="images/pexels-photo-415829.jpeg">
                    <p class="user-details"><b> Angelina</b><br> Model in kolkata</p>
                </div>
                <div class="col-md-5 testimonials">
                    <p>I smell sweet smell of grounds now</p>
                    <img src="images/100k-ai-faces-6.jpg">
                    <p class="user-details"><b> Alex</b><br>Model in kolkata </p>
                </div>                
            </div>
        </div>
    </section>
    
<!------------social media section------------------>
    <section id="social-media">
    <div class="container text-center">
    <p> Find Us On Social Media</p>
        <div class="social-icons">
            <a href="#"><img src="images/1200px-Facebook_icon.svg.png"></a>
            <a href="#"><img src="images/00-story-insta.jpg"></a>
            <a href="#"><img src="images/1200px-WhatsApp.svg.webp"></a>
            <a href="#"><img src="images/unnamed%20(1).png"></a>
            <a href="#"><img src="images/unnamed.png"></a>
            
        </div>
    </div>
    </section>
    
<!-----------footer Section------------------>
<section id="footer">
    <img src="images/maxresdefault1.jpg" class="footer-img">
    <div class="container">
     <div class="row ">
         <div class="col-md-4 footer-box">
             <img src="images/gt1.png">
             <p>Lets make our city clean</p>
         </div>
         <div class="col-md-4 footer-box">
             <p><b>CONTACT US</b></p>
             <p><i class="fa fa-map-marker" aria-hidden="true"></i>KOLKATA MUNICIPAL CORPORATION,WEST BENGAL</p>
             <p><i class="fa fa-phone" aria-hidden="true"></i>033-123456</p>
             <p><i class="fa fa-envelope-o" aria-hidden="true"></i>ayushsrivastava895@gmail.com</p>
         </div>
         <div class="col-md-4 footer-box">
             <p><b>SUBSCRIBE NEWSLETTER</b></p>
             <input type="email" class="form-control" placeholder="Your Email">
             <button type="button" class="btn btn-primary">Subscribe</button>
         </div>
     </div>
        <hr>
        <p class="copyright">website crafted by as tech</p>
    </div>
</section> 
    <!---------------smooth scroll------------------>
    <script src="smooth-scroll.js"></script>
    <script>
	var scroll = new SmoothScroll('a[href*="#"]');
    </script>
    
</body>
</html>""")
else:
    print("<script>window.alert('wrong emailid');</script>")
    
cursor.close()
db.close()
