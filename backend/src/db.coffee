mysql = require 'mysql'
connection = mysql.createPool
    host: 'localhost'
    user: 'root'
    password: '123456'
    database: 'test'

module.exports = connection
