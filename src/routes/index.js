const {Router} = require('express')
const router = Router()
const {getUsers,createUser,
    passwordCheck, updatePassword}= require("../controllers/index.usuario")
const {refreshSongs, topRegion, getRegiones, topGenero, getCanciones} = require("../controllers/index.canciones")
const {getReproductions,deleteReproductions, updateContinents, updateRepro} = require("../controllers/index.reproducciones")


// http://localhost:5000/
//router.get('/login/:pass/:correo',getUsers)
router.post('/login/', getUsers)
router.get('/refresh/', refreshSongs)
router.post('/register/', createUser)
router.get('/reproductions/:index', getReproductions)
router.delete('/reproductions/:id', deleteReproductions)
router.put('/cambiop/', updatePassword)
router.get('/topRegion/', topRegion)
router.get('/actualizar/', updateContinents)
router.get('/regiones/', getRegiones)
router.get('/topGenero/', topGenero)
router.put('/updateRepro/', updateRepro)
router.get('/canciones/:index', getCanciones)
//router.post('/login/:pass/:correo',passwordCheck)
//router.get('/users/:correo',getUserByID)
//router.post('/users',createUser)
//router.delete('/users/:id',delUser)
//router.put('/users/:id',updateUser)
//router.put('/save/', Save)

module.exports = router
