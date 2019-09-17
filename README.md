# AsteroidDB
A TinyWebDB service but more than TinyWebDB service. AsteroidDB is cloud database that stores and retrieves values for any platform. You can access the database with simple cURL/Web requests. 

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/yyusufcihan/AsteroidDB)

#### Supported Platforms

That's the most exiciting part of TinyWebDB's core. You can use AsteroidDB in every platform (App Inventor, C#, Batch etc.) which supports Web requests.

#### Built with

Built on top of [Flask](http://flask.pocoo.org/) micro-framework, written in Python and supports hosting on [Heroku](https://www.heroku.com/).

#### Original source

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
