express = require 'express'
router = express.Router()
connection = require '../db'


router.get '/',(req,res,next)->
    connection.query 'select count(1) from user', (error,results,field) ->
        console.log 'result:',results
    res.render 'index', title: 'Express ...'

module.exports = router
