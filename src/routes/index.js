const {Router} = require('express')
const router = Router()
const {getUsers,createUser,
    passwordCheck}= require("../controllers/index.usuario")
const {refreshSongs, topRegion} = require("../controllers/index.canciones")
const {getReproductions} = require("../controllers/index.reproducciones")


// http://localhost:5000/
//router.get('/login/:pass/:correo',getUsers)
router.post('/login/', getUsers)
router.get('/refresh/', refreshSongs)
router.post('/register/', createUser)
router.get('/reproductions/:index', getReproductions)
router.get('/topRegion/', topRegion)
//router.post('/login/:pass/:correo',passwordCheck)
//router.get('/users/:correo',getUserByID)
//router.post('/users',createUser)
//router.delete('/users/:id',delUser)
//router.put('/users/:id',updateUser)
//router.put('/save/', Save)

module.exports = router
