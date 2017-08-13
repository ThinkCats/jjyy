express = require 'express'

app = express()

app.get '/',(req,res) ->
    res.send 'test'

app.listen 3000, ->
    console.log 'listen 3000'

