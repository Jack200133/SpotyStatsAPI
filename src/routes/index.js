const {Router} = require('express')
const router = Router()
const {getUsers,createUser,
    passwordCheck}= require("../controllers/index.usuario")
const {refreshSongs} = require("../controllers/index.canciones")

// http://localhost:5000/
//router.get('/login/:pass/:correo',getUsers)
router.post('/login/', getUsers)
router.get('/refresh/', refreshSongs)
router.post('/register/', createUser)
//router.post('/login/:pass/:correo',passwordCheck)
//router.get('/users/:correo',getUserByID)
//router.post('/users',createUser)
//router.delete('/users/:id',delUser)
//router.put('/users/:id',updateUser)
//router.put('/save/', Save)

module.exports = router
