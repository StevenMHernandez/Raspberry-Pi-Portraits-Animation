var express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

app.use('/assets', express.static(__dirname + '/public/assets'));
app.use('/uploads', express.static(__dirname + '/public/uploads'));

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('storage/db/animation.db');
db.serialize(function () {
  db.run("CREATE TABLE IF NOT EXISTS images (" +
  "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
  "uri TEXT, " +
  "timestamp DATE DEFAULT CURRENT_TIMESTAMP)");
});

app.get('/', function (req, res) {
  res.redirect('/animation');
});

app.get('/animation', function (req, res) {
  res.sendFile(__dirname + '/public/animation.html');
});

app.post('/animation/images', function (req, res) {
  var uri = req.body.uri;
  if (uri != undefined) {
    db.serialize(function() {
      db.run("INSERT INTO images ('uri') VALUES ('" + uri + "')");
      res.send(uri + ' stored');
    });
  }
  else {
    res.send('Nothing stored.');
  }
});

app.get('/animation/images/random', function (req, res) {
  db.serialize(function() {
    db.get("SELECT * FROM images ORDER BY RANDOM() LIMIT 1;", function(err, row) {
      res.send(row);
    });
  });
});

var animation = io.of('/animation');

server.listen(3005);
