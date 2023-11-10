


# # BLOG

In a Django web application, implement functionality allowing users to perform two primary actions: the creation and viewing of blog posts. Each individual blog post should comprise structured data fields encompassing a title and content. The application architecture necessitates the definition of a Django model, BlogPost, to encapsulate these fields. Furthermore, the application requires the creation of views, such as create_blog_post and blog_post_list, which respectively handle the submission of new blog posts and the rendering of a list showcasing existing blog posts. To ensure a secure and authenticated user experience, consider incorporating Django's built-in authentication features, requiring users to be logged in for creating new blog posts. URL routing and template rendering will be orchestrated to seamlessly integrate these features into the application's user interface. Finally, database migrations will be executed to align the model with the underlying database schema, fostering data integrity and persistence.

## Prerequisites

Make sure you have the following installed:

- Python (>=3.9)
- pip
- virtualenv (optional but recommended)
- Django (>=4.2)
## Setup

1. Clone the repository:

 
    git clone[https://github.com/Nikunj6265/BLOG]
    cd Blog


2. Activate a virtual environment:


    virtualenv myproject
    source, myproject\Scripts\activate 
  


3. Apply migrations:

    python manage.py makemigrate
    python manage.py migrate
    ```

## Run the Application

1. Start the development server:

    cd Blog
    python manage.py runserver
    

2. Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
