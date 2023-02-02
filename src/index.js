const express = require('express')
const app = express()
const cors = require('cors')
const client_id = '3e5c97ca35184e2e907593dce6277b70'
const redirect_uri = 'http://localhost:5000/callback'
const client_secret = '508c63883dfc48f2a4988c39154a3d9e'

// defino middlewares 
app.use(cors())
app.use(express.json())
app.use(express.urlencoded({extended: false}))

// app.get('/login', function(req, res) {

//     var state = generateRandomString(16);
//     var scope = 'user-read-private user-read-email';
  
//     res.redirect('https://accounts.spotify.com/authorize?' +
//       querystring.stringify({
//         response_type: 'code',
//         client_id: client_id,
//         scope: scope,
//         redirect_uri: redirect_uri,
//         state: state
//       }));
//   });

app.get('/callback', function(req, res) {

    var code = req.query.code || null;
    var state = req.query.state || null;
  
    if (state === null) {
      res.redirect('/#' +
        querystring.stringify({
          error: 'state_mismatch'
        }));
    } else {
      var authOptions = {
        url: 'https://accounts.spotify.com/api/token',
        form: {
          code: code,
          redirect_uri: redirect_uri,
          grant_type: 'authorization_code'
        },
        headers: {
          'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
        },
        json: true
      };

      request.post(authOptions, function(error, response, body) {
        if (!error && response.statusCode === 200) {
          var access_token = body.access_token;
          res.send({
            'access_token': access_token
          });
        }
      });
    }
  });
// defino mis rutas
app.use(require('./routes/index'))

app.listen(5000)
console.log("Server de pruebas")
