const { MongoClient } = require('mongodb');
//const yup = require('yup');
const uri = "mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);

const client_id = "3e5c97ca35184e2e907593dce6277b70"
const client_secret = "508c63883dfc48f2a4988c39154a3d9e "
const redirect_uri = "http://localhost:5000/callback"

/*
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
*/

const topRegion = async (req, res) => {
    try{
        MongoClient.connect(uri, { useNewUrlParser: true }, async (err, client) => {
            const database = client.db('SpotyStats')

            const reproducciones = database.collection('reproducciones')


            const aggregateResult = await reproducciones.aggregate(
                [
                    {
                    $project:
                        {
                        _id: "$cancion",
                        region: "$usuario.pais",
                        continente: "$usuario.continente",
                        tiempo_reproducido: "$tiempo_reproducido",
                        },
                    },
                    {
                    $sort:
                        {
                        tiempo_reproducido: -1,
                        },
                    },
                    {
                    $group:
                        {
                        _id: {region : "$region", continente: "$continente"},
                        canciones: {
                            $push: {
                            cancion: "$_id",
                            tiempo: {
                                $sum: "$tiempo_reproducido",
                            },
                            },
                        },
                        },
                    },
                    {
                    $project:
                        {
                        _id: "$_id",
                        canciones: {
                            $slice: ["$canciones", 10],
                        },
                        },
                    },
                ]
            )
            aggregateResult.toArray((err, data) => {
                if (err) {
                    console.error(err)
                    res.status(500).send(err)
                } else {
                    console.log(data)
                    res.send(data)
                }
                client.close()
            })



        })
    }
    catch (e) {
        console.log("ERROR")

        res.json({
            message:'Error en topRegion',
            error: e
        })
    }
}

const refreshSongs = async (req, res) => {
    try{
        const database = client.db('SpotyStats')

        const songs = database.collection('songs')


        // jalar generos

        // jalar 10 canciones por genero

        // si no existe, crear

        // si si existe, cambiar cantidad de reproducciones
    }
    catch (e){

    }
}


const createSong = async (req,res) => {
    {
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

const getCanciones = async (req,res) => {
    try {
        const database = client.db('SpotyStats')
        const songs = database.collection('songs')

        const song = await songs.findMany()
        console.log(song)
        res.json(song)
        
      } 
      catch (e){
        console.log("ERROR")

        res.json({
            message:'Error en getCanciones',
            error: e
        })
    }
    finally {
        // Ensures that the client will close when you finish/error
        await client.close();
      }

}




module.exports = {
    refreshSongs,
    topRegion
}