# fms_project
Farm Management System (FMS)
The home page is intentionally kept simple and minimalist, focusing on functionality rather than visual complexity. There are no complex graphics or animations. Instead, the page contains:
Design Decisions
Home Page:
A header bar with links to other sections of the application (Mobs, Paddocks).
A countdown, which estimates the simulated current date of the farm management simulation or indeed any other count down. This is a session variable that is updated with each simulation carrying the date of the exercise in progress.
Copy that gives a brief description of the purpose of the application and could be placed on an ipad like app. It notifies the user that this system actually aims at the management of stock (mobs) and pastures on a farm.
The idea was to design a clear and concise web layout that will provide a consumer with minimal necessary data unrelated to product search. The conceptual decision which guides the design also aims at simplicity and easy navigation.
Mobs Page:
The Mobs page forms an integral part of the farm management system because it shows the list of mobs and the paddock currently occupied by them.
The mobs and paddock information is using the MySQL database where data is stored in tables. To display this data:
For use with the Flask application, the name of each mob is retrieved, as is the ID for each paddock it is associated with from the mobs and paddocks tables.
The data is then organized according to the mob’s name before the output is recorded to allow easy identification of certain mobs.
The table consists of listing all the mobs along with the respective paddock number through which the user gets an idea about the location of his livestock.
Bootstrap is used for applying the basic look and feel to the table without having to worrying about the end results being congested or cluttered. Sorting is done at the end, at the database level to optimize the performance, more so when organizing a large amount of data.
Paddocks Page:
The Paddocks page is intended to show the current state of each paddock depending on the DM/ha (dry matter per hectare).
DM/ha is one of the determinative parameters that indicate the portion of the usable grassland within each paddock.
Paddocks with a low DM/ha value (indicating less available pasture) are highlighted with color-coded alerts:
Lower limits of pasture levels require urgent attention and hence paddocks with low levels are colour-coded red.
Fields that are characterized by a low, but not critical density of paddocks, are painted in yellow.
Those paddocks that contain healthy levels of pasture are maintained under the default colour of blue in the map or white.
The following color-coding system benefits the user since it offers a visual response on which paddocks require the user’s attention.
New data related to the change in the DM/ha of the pasture are computed on a continual basis over the simulation period to take inter alia stock intake and pasture regeneration rates into consideration.
Data Handling:
The system uses POST requests to handle any user actions that modify data, such as:
From one paddock to the other: Transfer of mobs.
SIMPLE – creating new paddock or altering existing info like the location’s name, size and DM/ha.
POST requests are used instead of GET requests for several reasons:
Security: POST requests do not have the possibility of moving sensitive parameters at the link where the malicious user can modify the parameters needed for the execution of the request.
Idempotency: POST requests are used for operations which lead to changes in context, for example changing something in the database.
Prevention of accidental resubmissions: As POST requests result in data modification, the second disadvantage is that the risk of resubmitting a form is lower than in the case of GET requests.
Also, a technique called cast validation makes sure that all values received from the user are correct and within a given range so that no program crashes occur and data is no longer corrupted.
Bootstrap for Styling:
Bootstrap CSS is incorporated in the project at every stage to ensure contemporary look and feel, responsiveness and professionalism. Key areas where Bootstrap is applied include:
Navigation bars: A horizontal menu bar is included to the page so that the users will have easy access on the different pages such as home, mobs and paddocks.
Tables: Bootstrap inbuilt classes are used on the tables on mobs and paddocks pages to maintain a good contrast, spacing and the border around each table.
Forms and buttons: New input forms (like when creating a new paddock) are formatted using Bootstrap that will ensure that the form elements are correctly aligned irrespective of the device used – mobile, tablet, or laptop.
Bootstrap was selected because of its usability and compatibility with Flask, enabling to create a truly responsive and competitive interface without the need to learn custom CSS at every project.
Image Sources
No URLs for outside images were used in this project. Thus none graphics and other outside images where used; the tables and navigation are also powered by Bootstrap CSS.
Database Questions
Create Mobs Table:
In this case there is a table called mobs that contain information of the diverse mobs of animals within the farm. Each mob has an ID that is unique to the others, a name and is related to a specific paddock. This table is formed by the SQL statement below, also contain a foreign key that is referencing the paddocks table with each mob:
CREATE TABLE mobs (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each mob
    name VARCHAR(255),                  -- Name of the mob (e.g., Mob A)
    paddock_id INT,                     -- Foreign key linking to the paddock the mob is located in
    FOREIGN KEY (paddock_id) REFERENCES paddocks(id)  -- Ensures the paddock_id refers to a valid paddock
);
Relationship Between Mobs and Paddocks:
The mobs and paddocks tables are linked as both are accessed through a foreign key. In the mobs table, the _paddock attributes the mob with specific paddock with the help of paddock_id field. This makes certain each mob has its paddock and this avoids cases like mobs being assigned a paddock that does not exist.
The result is that through the foreign key constraint, the mob can only be placed in a paddock that has been captured in the paddocks table. If a paddock is deleted, the mobs will be deleted if ON DELETE CASCADE is used or an error will be thrown to stop having orphan records.
Create Farms Table:

The fields of this table contain information about the different farms that can be included in the system. Every farm has identification number, its name, short description (which is optional), and a name of the farm owner. This table can be extended in some of the future version of the system to manage several farms rather than being limited to one farm.
CREATE TABLE farms (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each farm
    name VARCHAR(255),                  -- Name of the farm (e.g., Greenfield Farm)
    description TEXT,                   -- Optional description (e.g., A large dairy farm)
    owner VARCHAR(255)                  -- Name of the farm owner (e.g., John Doe)
);

Insert Farm Data:
To insert data into the table farms, an INSERT INTO clause is used If we want to add data to the table farms. In this case, John Doe owns a large dairy farm named Greenfield Farm is added in this example.
INSERT INTO farms (name, description, owner) 
VALUES ('Greenfield Farm', 'A large dairy farm', 'John Doe');

Changes to Other Tables:
ALTER TABLE paddocks
ADD COLUMN farm_id INT, 
ADD FOREIGN KEY (farm_id) REFERENCES farms(id);  -- Foreign key linking paddocks to farms
For the addition of the new farms table, the first point requires creation of a new column in the paddocks table, namely FarmID. It will also come in handy as a foreign key which will enable connection of each paddock to a particular farm. This will allow the system to keep track which farm each paddock belongs to, although it will still be possible to filter the paddocks and mobs in the system by farm.




