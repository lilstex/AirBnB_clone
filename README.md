# AirBnB_clone
Welcome to the **AirBnB_clone** project for the ALX software engineering training.

## Description :
This project is built with a command interpreter to manage the AirBnB_clone objects.
The **command interpreter** does the following:
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file or a database
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object


<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />



* File Storage Engine:



  * `/models/engine/file_storage.py`
  


* Database Storage Engine:



  * `/models/engine/db_storage.py`
  


  * To Setup the DataBase for testing and development, there are 2 setup
  
  scripts that setup a database with certain privileges: `setup_mysql_test.sql`
  
  & `setup_mysql_test.sql` (for more on setup, see below).
  


  * The Database uses Environmental Variables for tests.  To execute tests with
  
  the environmental variables prepend these declarations to the execution
  
  command:
  


```

$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \

HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \

[COMMAND HERE]

```



## Environment



* __OS:__ Ubuntu 14.04 LTS

* __language:__ Python 3.4.3

* __frontend:__ Javascript, jQuery, Ajax

* __web server:__ nginx/1.4.6

* __application server:__ Flask 0.12.2, Jinja2 2.9.6

* __web server gateway:__ gunicorn (version 19.7.1)

* __database:__ mysql Ver 14.14 Distrib 5.7.18, SQLAlchemy

* __documentation:__ Swagger (flasgger==0.6.6)

* __style:__

  * __python:__ PEP 8 (v. 1.7.0)
  
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  
  * __bash:__ ShellCheck 0.3.3
  


<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/hbnb_step5.png" />

## Testing



### `unittest`



This project uses python library, `unittest` to run tests on all python files.

All unittests are in the `./tests` directory with the command:



* File Storage Engine Model:



  * `$ python3 -m unittest discover -v ./tests/`
  


* DataBase Storage Engine Model



```

$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \

HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \

python3 -m unittest discover -v ./tests/

```



---



### All Tests



The bash script `init_test.sh` executes all these tests for both File Storage &

DataBase Engine Models:



  * checks `pep8` style
  


  * runs all unittests
  


  * runs all w3c_validator tests
  


  * cleans up all `__pycache__` directories and the storage file, `file.json`
  


  * **Usage `init_test.sh`:**
  


```

$ ./dev/init_test.sh

```



---



### CLI Interactive Tests



* This project uses python library, `cmd` to run tests in an interactive command

  line interface.  To begin tests with the CLI, run this script:
  


#### File Storage Engine Model



```

$ ./console.py

```



#### To execute the CLI using the Database Storage Engine Model:



```

$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \

HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \

./console.py

```



#### For a detailed description of all tests, run these commands in the CLI:



```

(hbnb) help help

List available commands with "help" or detailed help with "help cmd".

(hbnb) help



Documented commands (type help <topic>):

========================================

Amenity    City  Place   State  airbnb  create   help  show

BaseModel  EOF   Review  User   all     destroy  quit  update



(hbnb) help User

class method with .function() syntax

        Usage: User.<command>(<id>)
	
(hbnb) help create

create: create [ARG] [PARAM 1] [PARAM 2] ...

        ARG = Class Name
	
        PARAM = <key name>=<value>
	
                value syntax: "<value>"
		
        SYNOPSIS: Creates a new instance of the Class from given input ARG
	
                  and PARAMS. Key in PARAM = an instance attribute.
		  
        EXAMPLE: create City name="Chicago"
	
                 City.create(name="Chicago")
		 
```



* Tests in the CLI may also be executed with this syntax:



  * **destroy:** `<class name>.destroy(<id>)`
  


  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`
  


  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`
    


---

## AUTHORS

* Emmanuel Chisom, [lilstex](https://github.com/lilstex)
* Sonkay Conteh, [SonkayAugustine](https://github.com/SonkayAugustine)