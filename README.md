# TinyWebDB
A TinyWebDB service that stores and retrieves values for any platform. You can access the database with simple cURL requests. This is a forked project from [pavi2410/TinyDB](https://github.com/pavi2410/TinyWebDB). 

You can use Heroku's one-click deploy feature:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/yyusufcihan/TinyWebDB/tree/release)

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


Built on top of [Flask](http://flask.pocoo.org/) micro-framework, and supports hosting on [Heroku](https://www.heroku.com/) and other hosts.
