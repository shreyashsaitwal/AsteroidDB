# AsteroidDB
Why people just can't set up a simple and free database for apps/softwares? They are actually just saving values and getting the values by using the tags. So there is no reason to providing an almost impossible solution for creating online database. We are in 2019. 

So welcome to a new generation in database service. If you want a too simple database which only holds string values, then AsteroidDB is for you. It based on TinyWebDB which is an App Inventor component, but with more data managing functions.

It can be installed on [Heroku](https://www.heroku.com/) with one click, if you don't want to deal with setting up thing (as I did). AsteroidDB is using [Flask](http://flask.pocoo.org/) micro-framework and written in Python, so you can understand that how it is easy to improve the code.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/yyusufcihan/AsteroidDB)

#### Supported Platforms

If your platforms supports Web requests (POST/GET etc.) then AsteroidDB can run safely on your platform.

#### Thanks

This is a cloned and improved project from [pavi2410/TinyDB](https://github.com/pavi2410/TinyWebDB). 

## Usage

Refer to [Wiki](https://github.com/yyusufcihan/AsteroidDB/wiki) for installing and usage.

### Progress
This the list of features I implemented after forking.

* **Security**
  * Password Protection
    * If you set a password for database, then all actions will require a password.
    * You can delete your password with `/auth/unlock` method.
    * There is no recovering password method, so don't forget your password!
        
* **Methods**
  * Basics
     - [x] Store record: `/store`
     - [x] Get value: `/get`
     - [ ] Get all tags
     - [x] Delete record: `/delete`
  * Auth
     - [x] Change password: `/auth/password`
     - [x] Delete password: `/auth/unlock`
     - [ ] Users
