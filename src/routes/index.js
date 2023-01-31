const {Router} = require('express')
const router = Router()
const {getUsers,
    createUser,
    getUserByID,
    delUser,
    updateUser,
    Save,
    passwordCheck}= require("../controllers/index.usuario")
// http://localhost:5000/
router.get('/users',getUsers)
router.get('/login/:pass/:correo',passwordCheck)
router.get('/users/:correo',getUserByID)
router.post('/users',createUser)
router.delete('/users/:id',delUser)
router.put('/users/:id',updateUser)
router.put('/save/', Save)

module.exports = router
