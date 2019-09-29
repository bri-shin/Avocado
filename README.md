# Avocado
An intimate platform that connects aspiring chefs to food enthusiasts at a warm kitchen space 

<i>link: https://www.holyguacamoley.online</i>

<i> Submitted to HackNY </i>

## Inspiration
There are several individuals out there who wish to break into the culinary industry, but are unable to do so because of a lack of opportunity. This is especially noticeable in large metropolises such as New York City, Seoul, Tokyo, and other large cities where real estate is expensive and limited. But, at the same time, there are several "start-up" restaurants around these cities, and others, that have substantial amount of downtime. Downtime means less to no revenue for a restaurant at a specific time interval, and this is not good for restaurants that are trying to establish their footing. Connecting aspiring chefs, who could be home cooks or simply someone who wishes to show off an experimental cuisine, to restaurants of a similar cuisine that have unused space at certain times, would allow for a multitude of benefits on both sides. The chef would get the opportunity to showcase his cooking and gain traction within the culinary world, while the restaurant could gain further popularity if the chefs who use their space attract new customers in search of interesting cuisine. And, to the customers, they get to experience an intimate dining experience with unique, perhaps experimental food, at restaurants that they might not have otherwise paid a visit to.

## What it does
The web application has features that directly addresses the pain points of our target users. Aspiring chefs can sign up on the app and list out their cuisines of specialization. Restaurants can sign up and list any free time slots that they might have, as well as what cuisine they specialize in. Chefs can then apply to occupy a time slot at a particular restaurant, and it is up to the restaurant to decide whether or not they will allow the chef to occupy the space.To help them make this decision, each chef will have a composite rating score based on their past performances and customer ratings of them.  In the event where the restaurant agrees to give the space to the chef, they may be compensated in two different ways  : a) A flat "rent" cost at a nominal rate b) A portion of the chef's earnings for the day.  Customers, or foodies, will be presented a list of restaurants that have such chefs cooking at them, and they have an option of RSVP'ing for a meal at a flat rate. In addition to this, the foodies are provided with recommendations of which chefs' cuisines they might enjoy next.

## How we built it
The front-end of the system was built using Vue.js and the Google Maps API. The back-end was built using Python Flask and Firebase, while the server was hosted as an application on Google Cloud Platform. The recommendation system was built using KNN Classification Algorithm implemented with numpy and scikit-learn and primarily used features from both the chefs' (e.g. food price, food uniqueness, years of experience) and foodies' data (e.g. willingness to pay, importance of chef experience). 
 
## Challenges we ran into
1. Database Issue: Deciding the data flow was a bit tricky since we had multiple different tables, and since we opted to use Firebase, that meant working with a non-relational data model which got a bit tricky since the different tables did have links to each other. But, we managed to come up with a logical data flow that worked for our implementation. 

2. ML Problem: KNN Classification Algorithm was difficult to train due to the lack of user data that satisfied Avocado's specific features of entities (e.g. uniqueness of food). By populating the dataset with sample data created by ourselves, we were able to simulate a sample KNN Classification Algorithm in action, recommending Chefs to Foodies with similar tastes. This problem can be solved as users (Chefs and Foodies) are added into the platform, as data will increase to a sufficient level that enables on-line learning. 

3. Design Compatibility Issue: We faced difficulties in creating a logo and theme that best represents our service and goal of creating an intimate platform for aspiring chefs and culinary enthusiasts. After hours of experimentation and debate, our team was able to find the right "feel" for our platform, producing not only aesthetic but effective UI. 

## Accomplishments that we're proud of
1. First of all, the lack of opportunities prevalent in the culinary scene is an issue that is under-addressed and overlooked. We are proud that Avocado primarily aims to create positive opportunities for passionate chefs who do not have an outlet to present their culinary art. 

2. From an idea to implementation, we managed to build a fully functional web application that not only provides a smooth UI/UX but also operates efficiently. Moreover, we have attempted to implement early versions of a functional ML model that can be improved as data increases with time. 


## What we learned
1. Database Management: We learned the importance of carefully designing the database prior to implementation as reformatting databases causes extra problems and additional work throughout the integration process. A well designed database enables a more efficient and smoother back-end development process.

2. When attempting to implement ML algorithms into your application, collecting and cleansing data is as important as developing the right training and validation methods. Without sufficient data to initially train the ML model on, the recommender system could not provide valuable functionality to the users.

## What's next for Avocado
1. Customer acquisition efforts through unconventional marketing methods, as Avocado primarily attempts to bring in food enthusiasts / foodies onto the platform. Moreover, ensuring our platform's scalability as more users sign up is important, hence dockerization using containers will be needed.

2. In terms of the recommendation model, rather than purely depending on the KNN Classification Algorithm that only allows collaborative recommendations, a hybrid method of applying content-based recommendation into the algorithm may result in better outcomes. Gradually, as restaurant data accumulate, we may also attempt to begin recommending restaurant spaces for Chefs with specific tastes or purpose of food showcasing. 

3. Creating a smoother user interface (UI) with the addition of animated loading icons to enhance the overall user experience on Avocado. It is important to differentiate the type of designs and process that each entity within our platform (i.e. restaurants, chefs, and foodies) experience as it serves varying purposes per user type. 
