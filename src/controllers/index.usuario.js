const { MongoClient } = require('mongodb');
const yup = require('yup');
const uri = "mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

const userSchema = yup.object().shape({
    email: yup.string().required(),
    password: yup.string().required(),
    nombre: yup.string().required(),
    apellido: yup.string().notRequired(),
    seguidores: yup.number().notRequired(),
    nombre_artisitco: yup.string().notRequired(),
    cantidad_canciones: yup.number().notRequired(),
    generos: yup.array().of(yup.string()).required()
});



const getUsers = async (req,res) => {
    try {
        

        MongoClient.connect(uri, { useNewUrlParser: true }, (err, client) => {
            if (err) throw err
            const db = client.db('SpotyStats')
            const collection = db.collection('users')
            const {email,password} = req.body
    
            collection.findOne({ email: email }, (err, user) => {
                if (err) throw err
                res.send(user)
                client.close()
            })
        })
      } 
      catch (e){
        console.log("ERROR ",e)

        res.json({
            message:'Error en getUsers',
            error: e
        })
    }
    finally {
        // Ensures that the client will close when you finish/error
        await client.close();
      }
}

const createUser = async (req,res) => {
    {
        try {
            await userSchema.validate(req.body, { abortEarly: false })
        } catch (error) {
            return res.status(400).send(error.errors)
        }
    
        const user = {
            email: req.body.email,
            password: req.body.password,
            nombre: req.body.nombre,
            apellido: req.body.apellido,
            seguidores: req.body.seguidores,
            nombre_artisitco: req.body.nombre_artisitco,
            cantidad_canciones: req.body.cantidad_canciones,
            generos: req.body.generos
        }
        console.log(user)
        const db = client.db("SpotyStats")
        const collection = db.collection("users")
    
        collection.insertOne(user, (err, result) => {
            if (err) throw err
            res.send(user)
            client.close()
        })
        
    }
}


const getArtist = async (req,res) => {
    try {
        const database = client.db('SpotyStats')
        const users = database.collection('users')

        const user = await users.findMany()
        console.log(user)
        res.json(user)
        
      } 
      catch (e){
        console.log("ERROR")

        res.json({
            message:'Error en getArtist',
            error: e
        })
    }
    finally {
        // Ensures that the client will close when you finish/error
        await client.close();
      }

}



module.exports = {
    getUsers,getArtist,createUser
}