const { MongoClient } = require('mongodb');


const uri = "mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);



const getUsers = async (req,res) => {
    try {
        const database = client.db('SpotyStats')
        const users = database.collection('users')
        const id = req.params.id;

        const query = { correo : id }
        const user = await users.findOne(query)
        console.log(user)
        res.json(user)
      } 
      catch (e){
        console.log("ERROR")

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

const passwordCheck = async (req,res) => {
    try {
        const database = client.db('SpotyStats')
        const users = database.collection('users')
        const {id} = req.params

        const query = { correo : id }
        const user = await users.findOne(query)
        console.log(user)
        res.json(user)
      } 
      catch (e){
        console.log("ERROR")

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
            message:'Error en getUsers',
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
            message:'Error en getUsers',
            error: e
        })
    }
    finally {
        // Ensures that the client will close when you finish/error
        await client.close();
      }

}

const getReproductions = async (req,res) => {
    try {
        const database = client.db('SpotyStats')
        const users = database.collection('users')
        const id = req.params.id;

        const query = { correo : id }
        const user = await users.findOne(query)
        console.log(user)
        res.json(user)
      } 
      catch (e){
        console.log("ERROR")

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




module.exports = {
    getUsers,passwordCheck,getArtist
}