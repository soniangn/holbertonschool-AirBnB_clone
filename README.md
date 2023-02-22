<img width="450" src="https://user-images.githubusercontent.com/113889290/220651819-3bb7044c-f49b-4cd6-b7e3-fb2b6ecde871.png">

<h2><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=44&pause=1000&color=CF0000&center=true&vCenter=true&width=735&height=45&lines=Introduction+to+AirBnb+clone" alt="Typing SVG" /></a></h2>
▪ The objective of this project is to implement a simple copy of the AirBnB website.   ▪ This project will be divided, each focused on different aspects and technologies. 
▪ This is the first part of the project which consists of building the console.  

<h2>The console</h2>
<p align="justify"><b>create your data model
manage (create, update, destroy, etc)</b> objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system.  This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself).
The console will be a tool to validate this storage engine</p>

<h2> Install the console :</h2>

<h3>Git clone the repository</h3>  

```bash  
$ git clone https://github.com/TessierV/holbertonschool-AirBnB_clone.git  
```  

<h3>Run the project with "console.py"</h3>  

```bash
$ ./console.py
```

<details><summary>click for read more | Interactive Mode & Non-Interactive Mode </summary>

<h3>Interactive Mode</h3>

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all create  destroy help  quit show update

(hbnb) quit
$
```

<h3>Non Interactive Mode</h3>

```bash
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
$
```
</details>

<h2> Examples :</h2>

<h3>Create a Model</h3>

```
(hbnb) create BaseModel
d0ef8146-4664-4de5-8e89-096d667b728e
(hbnb)

```

<h3>Show a Model</h3>

```
(hbnb) show BaseModel d0ef8146-4664-4de5-8e89-096d667b728e
[User](d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}

```

<h2> Flowcharts :</h2>

<img width="600" src="https://user-images.githubusercontent.com/113889290/220693285-b293179e-b126-4204-a55d-5ebc67c896f3.png">


<h2> Files & Directories descriptions :</h2>

|  AirBnB_clone Repository            | Name                         | Description           |
|  --------------|---------------|------------------------------------------ |
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) | console.py | Contains the entry point of the command interpreter | 
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) | AUTHORS | Contains the list of the creators and their e-mail | 
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) | README.md | Contains all the informations of the project | 
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) |  [models/](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models) | Directory contains all the models files of the project |
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) | [models/engine/](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models/engine) | Serialization - Deserialization directory
|  [holbertonschool-AirBnB_clone](https://github.com/TessierV/holbertonschool-AirBnB_clone) | [tests/](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/tests) | Directory contains all the tests files of the project | 

<details><summary>click for read more</summary>

|  Models Repository            | Name                         | Description           |
|  --------------|---------------|------------------------------------------ |
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| init.py | Create a unique FileStorage instance
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| base_model.py | Defines all common attributes/methods for other classes
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| user.py | User that inherits from BaseModel - email/password/first_name/last_name
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| city.py | City that inherits from BaseModel - state_id/name
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| place.py | Place that inherits from BaseModel - <br>city_id/user_id/name/description/number_rooms/number_bathrooms/<br>max_guest/price_by_night/<br>latitude/longitude/amenity_ids
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| review.py | Review that inherits from BaseModel - place_id/user_id/text
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| state.py | State that inherits from BaseModel - name
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| amenity.py | Amenity that inherits from BaseModel - name
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models)| [engine/](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models/engine) | Serialization - Deserialization directory

|  Engine Repository            | Name                         | Description           |
|  --------------|---------------|------------------------------------------ |
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models/engine)| init.py | Create a unique FileStorage instance
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/models/engine)| file_storage.py |  Serialization - Deserialization

|  Tests Repository            | Name                         | Description           |
|  --------------|---------------|------------------------------------------ |
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/tests)|  | 
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/tests)|  | 
|[models](https://github.com/TessierV/holbertonschool-AirBnB_clone/tree/main/tests)|  | 
</details>
<br><br>
<h3>Autors :
    <a href="https://www.linkedin.com/in/nguyensonia/">
       <img alt="Anurag Hazra | CodeSandbox" height="20px" src="https://img.shields.io/badge/NguyenSonia-4A6552?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://www.linkedin.com/in/vanessa-tessier-601794252/">
        <img alt="Anurag Hazra | CodeSandbox" height="20px" src="https://img.shields.io/badge/TessierVanessa-4A6552?style=for-the-badge&logo=linkedin&logoColor=white"/>
    </a>
    </h3>
<hr>
<p align="right">Holberton School - TOULOUSE C19 Cohort FEB. 2023
</p>
