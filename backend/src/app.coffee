express = require 'express'
path = require 'path'
favicon = require 'serve-favicon'
logger = require 'morgan'
cookieParser = require 'cookie-parser'
bodyParser = require 'body-parser'

index = require './routes/index'
users = require './routes/users'

app = express()

app.set 'views',path.join __dirname,'views'
app.set 'view engine','jade'

app.use logger 'dev'
app.use bodyParser.json()
app.use bodyParser.urlencoded extended:false
app.use cookieParser()
app.use express.static path.join __dirname,'public'

app.use '/', index
app.use '/users',users

app.use (req,res,next) ->
    err = new Error 'not Found'
    err.status = 404
    next err

app.use (err,req,res,next) ->
    res.locals.message = err.message
    res.locals.error = if (req.app.get 'env') == 'development'  then err else {}
    res.status err.status || 500
    res.render 'error'

app.listen 3000,->
    console.log 'listening  3000'

module.exports = app
