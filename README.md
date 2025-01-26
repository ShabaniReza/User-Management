# User Management System

This is a **User Management System** API that created with Django REST Framework .   

This API has two models that named **User** and **Profile** .   

**User**    

    This model created with **AbstractUser* object to saved users informations .   
    Because this object (AbstractUser) itself has username and is_active fields, I gave up writing them again .    

**Profile**    

    This model created for showing users profile in website .    

-------------    

**APIs main features**    

    *Sign-up and log-in with **JWT**    
    *Sending email for recover password    
    *Profile information management CRUD    
    *Manage user access with **Permissions**    
    *Search and filter users in admin site    

-------------    

**Security features**    

    *Rate limiting
    *Protection against Brute-Force attacks with **DRF throttling**    
    *Using django-secure    
    *Hashing & Salting    


-------------    


**Optimization and performance**    

    *Using **Redis cashing**    
    *Using **ElasticSearch**     
    *Using Pagination    


-------------    


**Dockerization**    

    *Using **Docker & Docker-compose**    
    *Microservices-ready structure    



-------------    


**Test & CI/CD**    

    *Using **pytest** for testing API (89% cover)    
    *CI/CD with GitHub Actions


## How to use    

**For using project run bellow terminal command**    

    1.  `source UserManagement/bin/activate`    
    2.  `cd UserManagement`    
    3.  `python manage.py runserver`    
