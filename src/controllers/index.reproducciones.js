const { MongoClient } = require('mongodb');
const yup = require('yup');
const uri = "mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);


const getReproductions = async (req,res) => {
    try {

        MongoClient.connect(uri, { useNewUrlParser: true }, async (err, client) => {
            if (err) throw err
            const db = client.db('SpotyStats')
            const collection = db.collection('reproducciones')
    
            const query = {}
            const sort = { length: -1 }
            const limit = 5
            const skip = parseInt(req.params.index)
            console.log(skip)
            const cursor = collection.find(query).sort(sort).skip(skip).limit(limit)
            cursor.toArray((err, data) => {
                if (err) {
                  console.error(err)
                  res.status(500).send(err)
                } else {
                  res.send(data)
                }
                client.close()
              })
        })

      } 
      catch (e){
        console.log("ERROR")

        res.json({
            message:'Error en getReproductions',
            error: e
        })
    }
    finally {
        // Ensures that the client will close when you finish/error
        await client.close();
      }
}





module.exports = {
    getReproductions
}