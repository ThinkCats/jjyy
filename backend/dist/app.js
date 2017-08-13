// Generated by CoffeeScript 2.0.0-beta4
(function() {
  var app, bodyParser, cookieParser, express, favicon, index, logger, path, users;

  express = require('express');

  path = require('path');

  favicon = require('serve-favicon');

  logger = require('morgan');

  cookieParser = require('cookie-parser');

  bodyParser = require('body-parser');

  index = require('./routes/index');

  users = require('./routes/users');

  app = express();

  app.set('views', path.join(__dirname, 'views'));

  app.set('view engine', 'jade');

  app.use(logger('dev'));

  app.use(bodyParser.json());

  app.use(bodyParser.urlencoded({
    extended: false
  }));

  app.use(cookieParser());

  app.use(express.static(path.join(__dirname, 'public')));

  app.use('/', index);

  app.use('/users', users);

  app.use(function(req, res, next) {
    var err;
    err = new Error('not Found');
    err.status = 404;
    return next(err);
  });

  app.use(function(err, req, res, next) {
    res.locals.message = err.message;
    res.locals.error = (req.app.get('env')) === 'development' ? err : {};
    res.status(err.status || 500);
    return res.render('error');
  });

  app.listen(3000, function() {
    return console.log('listening  3000');
  });

  module.exports = app;

}).call(this);
