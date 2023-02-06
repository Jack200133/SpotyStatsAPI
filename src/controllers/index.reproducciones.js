const paises = require('../archivos/regiones.json')
const continentes = require('../archivos/continentes.json')

const { MongoClient } = require('mongodb');
const yup = require('yup');
const uri = "mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri);


const s = async (req,res) => {


    try {
        MongoClient.connect(uri, { useNewUrlParser: true }, async (err, client) => {
            if (err) throw err
            const db = client.db('SpotyStats')
            const collection = db.collection('reproducciones')

            const database = client.db('SpotyStats')

            const reproducciones = database.collection('reproducciones')
            
            reproducciones.find({}).toArray((err, result) => {
                if (err) throw err;
            
                

                result.forEach((item) => {

                    conteo = 0;

                    paises.forEach(element => {
                        
                        if (element.country === item.usuario.pais && element.continent === "Central America"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Central America" } })
                        }
                        else if (element.country === item.usuario.pais && element.continent === "North America"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "North America" } })
                        }
                    
                        else if (element.country === item.usuario.pais && element.continent === "South America"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "South America" } })
                        }
    
                        else if (element.country === item.usuario.pais && element.continent === "Europe"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Europe" } })
                        }
                        else if (element.country === item.usuario.pais && element.continent === "Asia"){
                            
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Asia" } })
                        }
    
                        else if (element.country === item.usuario.pais && element.continent === "Oceania"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Oceania" } })
                        }
    
                        else if (element.country === item.usuario.pais && element.continent === "Antarctica"){
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Antarctica" } })
                        }
    
                        else if (element.country === item.usuario.pais && element.continent === "Africa"){
                            
                            conteo ++;
                            reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": "Africa" } })
                        }
                    })
                    console.log(conteo)
                    
                })


                
            })
            
            res.json({
                message:'Continente actualizado',
                
            })
        })
    }
    catch (e){
      console.log("ERROR")

      res.json({
          message:'Error en updateContinents',
          err: e
      })
  }
  finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

function getContinent(country, countries) {
    for (let i = 0; i < countries.length; i++) {
        if (countries[i].country === country) {
            return countries[i].continent;
        }
    }
    return null;
}

const updateContinents = async (req,res) => {


    try {
        MongoClient.connect(uri, { useNewUrlParser: true }, async (err, client) => {
            if (err) throw err
            const database = client.db('SpotyStats')
            const reproducciones = database.collection('reproducciones')
            
            reproducciones.find({}).toArray((err, result) => {
                if (err) throw err;
            
                
    
                result.forEach((item) => {
    
                    conteo = 0;
                    const pai = item.usuario.pais
                    const continent = getContinent(pai, paises)
                    if(continent === null){
    
                        console.log("Pais: " + pai + " Continente: " + continent + "")
                    }
                    reproducciones.updateOne({ "usuario.pais": item.usuario.pais}, { $set: { "usuario.continente": continent } }, (err, result) => {
                        if (err) throw err;
                    });
                })
    
                
                res.json({
                    message:'Continente actualizado',
                    
                })
            })
        })
    }
    catch (e){
      console.log("ERROR")
    
      res.json({
          message:'Error en updateContinents',
          err: e
      })
    
} finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }}


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


const deleteReproductions = async (req,res) => {
    try {
        const client = await MongoClient.connect(uri, { useNewUrlParser: true })
        const db = client.db('SpotyStats');
        const collection = db.collection('reproducciones')
        ObjectId = require('mongodb').ObjectId;

        const id = ObjectId(req.params.id)
        const query = { _id: id }
        await collection.deleteOne(query)
        res.json({
            message:'Reproduccion eliminada'
        })
    }
    catch (e){
        console.log("ERROR", e)
        res.json({
            message:'Error en deleteReproduccion',
            error: e
        });
    } 
    finally {
        // Ensures that the client will close when you finish/error
        client.close();
    }
}    

const updateRepro = async (req,res) => {
    try{
        MongoClient.connect(uri, { useNewUrlParser: true }, async (err, client) => {
            if (err) throw err
            const db = client.db('SpotyStats')
            const repro = db.collection('reproducciones')


            console.log*(req.body.nombre , " ", req.body.nuevap)
            const reprod = await repro.updateOne( { "nombre": req.body.nombre }, { $set: { "password": req.body.nuevap } })
            res.json(reprod)
        
        })
    }
    catch (e){
      console.log("ERROR")

      res.json({
          message:'Error en update reproduccion',
          error: e
      })
  }
  finally {
      // Ensures that the client will close when you finish/error
      await client.close();
    }
}

module.exports = {
    getReproductions,
    deleteReproductions,
    updateContinents,
    updateRepro
}