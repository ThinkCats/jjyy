schedule = require 'node-schedule'
http = require 'http'

fetch_data = ->
    schedule.scheduleJob('*/1 * * * * *', ->
        console.log 'hello'
    )


options =
    hostname: 'www.baidu.com'
    method: 'get'

doRequest = (options) ->
    new Promise((resolve,reject) ->
        req = http.request(options, (res) ->
            console.log "STATUS: #{res.statusCode}"
            res.setEncoding 'utf-8'
            res.on 'data', (chunk) ->
                resolve(chunk)
        )

        req.on 'error', (e) ->
            console.error "PROBLEM :${e.message}"
            reject(e)

        req.end()
    )


main = ->
    data = await doRequest(options)
    console.log 'result:',data

main()

# fetch_data()
