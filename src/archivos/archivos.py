import random
import json

usuarios = [
	{
		"nombre": "Shaeleigh Langley",
		"edad": 37,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Chandler Mooney",
		"edad": 6,
		"region": "Europa",
		"pais": "España",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Alexander Sellers",
		"edad": 23,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Yuli Skinner",
		"edad": 77,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Jerry Cochran",
		"edad": 13,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Maryam Reid",
		"edad": 19,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Halee Paul",
		"edad": 22,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Denton Mccarty",
		"edad": 50,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Wyatt Mayer",
		"edad": 35,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Jada Coleman",
		"edad": 42,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Macy Cantu",
		"edad": 39,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Sebastian Cooke",
		"edad": 54,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kim Perry",
		"edad": 21,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Kenneth Vinson",
		"edad": 29,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Jonah Byrd",
		"edad": 35,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Boris Dickson",
		"edad": 27,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ria Waters",
		"edad": 7,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Riley Bean",
		"edad": 24,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kenyon Gallegos",
		"edad": 26,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Steven Orr",
		"edad": 46,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Keith Dixon",
		"edad": 33,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Nash Terrell",
		"edad": 7,
		"region": "Europa",
		"pais": "Italia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Berk Todd",
		"edad": 53,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Cassidy Bryant",
		"edad": 55,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Vanna Powell",
		"edad": 72,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Cain Wells",
		"edad": 57,
		"region": "Europa",
		"pais": "España",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Boris Christian",
		"edad": 51,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Kibo Diaz",
		"edad": 47,
		"region": "Europa",
		"pais": "Inglaterra",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Nigel Brewer",
		"edad": 1,
		"region": "Europa",
		"pais": "España",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ryder Sargent",
		"edad": 31,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Walker Contreras",
		"edad": 50,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Andrew Hogan",
		"edad": 76,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Vincent Mendoza",
		"edad": 59,
		"region": "Europa",
		"pais": "Francia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Quamar Powell",
		"edad": 3,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kristen Orr",
		"edad": 79,
		"region": "Europa",
		"pais": "Portugal",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Gabriel Cook",
		"edad": 72,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Stewart Faulkner",
		"edad": 62,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Camille Taylor",
		"edad": 17,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Tad O'Neill",
		"edad": 30,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Zoe Calderon",
		"edad": 10,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Orlando Serrano",
		"edad": 48,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Xanthus Woods",
		"edad": 56,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Beatrice Pitts",
		"edad": 25,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Stewart Dunn",
		"edad": 17,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Harding Huff",
		"edad": 7,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Chiquita Duke",
		"edad": 57,
		"region": "Centro América",
		"pais": "Guatemala",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Uta Goff",
		"edad": 36,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "August Waller",
		"edad": 70,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Fulton Elliott",
		"edad": 76,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Aquila Snider",
		"edad": 67,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Constance Rocha",
		"edad": 56,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Charlotte Larson",
		"edad": 26,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kiara Parks",
		"edad": 34,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Leroy Nash",
		"edad": 67,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Hu Dudley",
		"edad": 75,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Leilani Hahn",
		"edad": 38,
		"region": "Centro América",
		"pais": "Guatemala",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Christian Pratt",
		"edad": 10,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Genevieve Russo",
		"edad": 28,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Dane Gamble",
		"edad": 12,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Jared Coffey",
		"edad": 45,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Pamela Noel",
		"edad": 31,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Gray Stanton",
		"edad": 65,
		"region": "Centro América",
		"pais": "Guatemala",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Eaton Burton",
		"edad": 65,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Gwendolyn Reid",
		"edad": 8,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "MacKensie Webb",
		"edad": 21,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Bree Martin",
		"edad": 30,
		"region": "Centro América",
		"pais": "Guatemala",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Chastity Glass",
		"edad": 59,
		"region": "Centro América",
		"pais": "Nicaragua",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Lillith Combs",
		"edad": 76,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hillary Waters",
		"edad": 15,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Octavius Wynn",
		"edad": 59,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ahmed Pacheco",
		"edad": 80,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Paul Langley",
		"edad": 18,
		"region": "Centro América",
		"pais": "El-Salvador",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Chancellor Dunlap",
		"edad": 77,
		"region": "Centro América",
		"pais": "Honduras",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kenyon Atkinson",
		"edad": 71,
		"region": "Centro América",
		"pais": "Guatemala",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Madison Cook",
		"edad": 25,
		"region": "Centro América",
		"pais": "Panamá",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Vera Gonzalez",
		"edad": 50,
		"region": "Norte América",
		"pais": "Mexico",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Moses Franklin",
		"edad": 39,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Miranda Duke",
		"edad": 75,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Eugenia Tyler",
		"edad": 22,
		"region": "Norte América",
		"pais": "Mexico",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Madonna Mayo",
		"edad": 51,
		"region": "Norte América",
		"pais": "Mexico",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Darrel Suarez",
		"edad": 30,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Tashya Burns",
		"edad": 27,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Eugenia Holden",
		"edad": 64,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Xavier Harper",
		"edad": 26,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Wendy Herring",
		"edad": 30,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Shelly Mcdowell",
		"edad": 24,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Allen Terrell",
		"edad": 41,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Jeremy Brewer",
		"edad": 35,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Dara Dudley",
		"edad": 60,
		"region": "Norte América",
		"pais": "USA",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Luke Barnes",
		"edad": 49,
		"region": "Norte América",
		"pais": "Mexico",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Kameko Parker",
		"edad": 45,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Maisie Sullivan",
		"edad": 70,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Drew Moran",
		"edad": 69,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Serena Warner",
		"edad": 3,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Carson Juarez",
		"edad": 71,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Alvin Vega",
		"edad": 14,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Alfonso Carlson",
		"edad": 72,
		"region": "Asia",
		"pais": "China",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Nora Fitzpatrick",
		"edad": 73,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Bernard Williams",
		"edad": 47,
		"region": "Asia",
		"pais": "Taiwan",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "MacKenzie Delacruz",
		"edad": 31,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hamilton Santos",
		"edad": 31,
		"region": "Asia",
		"pais": "China",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Amethyst Valenzuela",
		"edad": 47,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Xaviera Harrington",
		"edad": 68,
		"region": "Asia",
		"pais": "Taiwan",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Lee Mercado",
		"edad": 63,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Daryl Burns",
		"edad": 42,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Adara Eaton",
		"edad": 57,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Lane Wynn",
		"edad": 59,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Connor Hebert",
		"edad": 9,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Castor West",
		"edad": 3,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Rigel Rose",
		"edad": 4,
		"region": "Asia",
		"pais": "Taiwan",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Justin Cash",
		"edad": 30,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Alfreda Collins",
		"edad": 41,
		"region": "Asia",
		"pais": "China",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Brent Brooks",
		"edad": 76,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Dai Burch",
		"edad": 39,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Karyn Sims",
		"edad": 53,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Basia Tyson",
		"edad": 65,
		"region": "Asia",
		"pais": "Taiwan",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Fuller Savage",
		"edad": 51,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Riley Gomez",
		"edad": 8,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Melanie Ward",
		"edad": 64,
		"region": "Asia",
		"pais": "Japón",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ursa Becker",
		"edad": 17,
		"region": "Asia",
		"pais": "Korea",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Neville Jones",
		"edad": 29,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Preston Foreman",
		"edad": 65,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Jeanette Larson",
		"edad": 80,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Declan Kirby",
		"edad": 3,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Wing Garza",
		"edad": 51,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ivor Greene",
		"edad": 67,
		"region": "Sur América",
		"pais": "Brazil",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Hayley Holland",
		"edad": 64,
		"region": "Sur América",
		"pais": "Brazil",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Mason Carlson",
		"edad": 2,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ivana Morris",
		"edad": 62,
		"region": "Sur América",
		"pais": "Brazil",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Tatum Burks",
		"edad": 77,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Guy Crane",
		"edad": 38,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Sonya Woodward",
		"edad": 33,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Elmo Bell",
		"edad": 46,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kylynn Harrell",
		"edad": 1,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Maris Reed",
		"edad": 20,
		"region": "Sur América",
		"pais": "Brazil",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Glenna Reeves",
		"edad": 31,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Chantale Kinney",
		"edad": 15,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Peter Rodgers",
		"edad": 19,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Teegan Webster",
		"edad": 78,
		"region": "Sur América",
		"pais": "Argentina",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Phillip David",
		"edad": 76,
		"region": "Sur América",
		"pais": "Perú",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kevyn Munoz",
		"edad": 21,
		"region": "África",
		"pais": "Nigeria",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kiona Ayers",
		"edad": 48,
		"region": "África",
		"pais": "Camerún",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Charde Castro",
		"edad": 15,
		"region": "África",
		"pais": "Nigeria",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Martin Castro",
		"edad": 21,
		"region": "África",
		"pais": "Nigeria",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Justin Blankenship",
		"edad": 15,
		"region": "África",
		"pais": "Nigeria",
		"suscripcion": 0,
		"genero": "Femenino"
	}
]

reproducciones = [
    
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 140
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 125
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 66
	},
	{
		"tiempo_reproducido": 156
	},
	{
		"tiempo_reproducido": 51
	},
	{
		"tiempo_reproducido": 48
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 54
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 102
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 147
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 63
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 154
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 73
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 130
	},
	{
		"tiempo_reproducido": 174
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 48
	},
	{
		"tiempo_reproducido": 151
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 125
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 50
	},
	{
		"tiempo_reproducido": 115
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 131
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 151
	},
	{
		"tiempo_reproducido": 138
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 48
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 154
	},
	{
		"tiempo_reproducido": 0
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 52
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 7
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 0
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 121
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 146
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 31
	},
	{
		"tiempo_reproducido": 105
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 93
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 40
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 154
	},
	{
		"tiempo_reproducido": 13
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 86
	},
	{
		"tiempo_reproducido": 80
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 113
	},
	{
		"tiempo_reproducido": 93
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 122
	},
	{
		"tiempo_reproducido": 152
	},
	{
		"tiempo_reproducido": 70
	},
	{
		"tiempo_reproducido": 150
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 93
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 72
	},
	{
		"tiempo_reproducido": 12
	},
	{
		"tiempo_reproducido": 79
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 84
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 66
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 51
	},
	{
		"tiempo_reproducido": 135
	},
	{
		"tiempo_reproducido": 56
	},
	{
		"tiempo_reproducido": 160
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 122
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 121
	},
	{
		"tiempo_reproducido": 94
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 61
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 150
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 176
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 20
	},
	{
		"tiempo_reproducido": 47
	},
	{
		"tiempo_reproducido": 140
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 113
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 69
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 43
	},
	{
		"tiempo_reproducido": 84
	},
	{
		"tiempo_reproducido": 128
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 73
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 37
	},
	{
		"tiempo_reproducido": 22
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 136
	},
	{
		"tiempo_reproducido": 177
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 33
	},
	{
		"tiempo_reproducido": 25
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 98
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 40
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 50
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 82
	},
	{
		"tiempo_reproducido": 2
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 138
	},
	{
		"tiempo_reproducido": 43
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 13
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 138
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 24
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 70
	},
	{
		"tiempo_reproducido": 69
	},
	{
		"tiempo_reproducido": 156
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 8
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 119
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 138
	},
	{
		"tiempo_reproducido": 146
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 71
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 135
	},
	{
		"tiempo_reproducido": 117
	},
	{
		"tiempo_reproducido": 102
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 121
	},
	{
		"tiempo_reproducido": 95
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 28
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 167
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 82
	},
	{
		"tiempo_reproducido": 56
	},
	{
		"tiempo_reproducido": 114
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 174
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 88
	},
	{
		"tiempo_reproducido": 145
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 128
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 42
	},
	{
		"tiempo_reproducido": 135
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 167
	},
	{
		"tiempo_reproducido": 43
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 33
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 177
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 177
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 40
	},
	{
		"tiempo_reproducido": 42
	},
	{
		"tiempo_reproducido": 87
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 114
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 25
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 135
	},
	{
		"tiempo_reproducido": 90
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 121
	},
	{
		"tiempo_reproducido": 151
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 86
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 131
	},
	{
		"tiempo_reproducido": 88
	},
	{
		"tiempo_reproducido": 124
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 146
	},
	{
		"tiempo_reproducido": 117
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 156
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 152
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 79
	},
	{
		"tiempo_reproducido": 71
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 122
	},
	{
		"tiempo_reproducido": 114
	},
	{
		"tiempo_reproducido": 58
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 118
	},
	{
		"tiempo_reproducido": 177
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 152
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 88
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 146
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 117
	},
	{
		"tiempo_reproducido": 0
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 105
	},
	{
		"tiempo_reproducido": 51
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 113
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 115
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 42
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 147
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 47
	},
	{
		"tiempo_reproducido": 145
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 178
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 167
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 152
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 32
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 140
	},
	{
		"tiempo_reproducido": 150
	},
	{
		"tiempo_reproducido": 115
	},
	{
		"tiempo_reproducido": 95
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 54
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 124
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 11
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 91
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 24
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 113
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 72
	},
	{
		"tiempo_reproducido": 86
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 43
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 94
	},
	{
		"tiempo_reproducido": 103
	},
	{
		"tiempo_reproducido": 65
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 110
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 179
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 161
	},
	{
		"tiempo_reproducido": 87
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 7
	},
	{
		"tiempo_reproducido": 13
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 45
	},
	{
		"tiempo_reproducido": 102
	},
	{
		"tiempo_reproducido": 78
	},
	{
		"tiempo_reproducido": 40
	},
	{
		"tiempo_reproducido": 138
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 95
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 135
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 90
	},
	{
		"tiempo_reproducido": 40
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 8
	},
	{
		"tiempo_reproducido": 24
	},
	{
		"tiempo_reproducido": 177
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 65
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 145
	},
	{
		"tiempo_reproducido": 121
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 49
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 98
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 147
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 43
	},
	{
		"tiempo_reproducido": 93
	},
	{
		"tiempo_reproducido": 105
	},
	{
		"tiempo_reproducido": 180
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 22
	},
	{
		"tiempo_reproducido": 119
	},
	{
		"tiempo_reproducido": 131
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 130
	},
	{
		"tiempo_reproducido": 119
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 12
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 90
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 10
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 174
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 73
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 167
	},
	{
		"tiempo_reproducido": 33
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 90
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 178
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 31
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 65
	},
	{
		"tiempo_reproducido": 86
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 134
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 45
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 151
	},
	{
		"tiempo_reproducido": 143
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 80
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 50
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 0
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 125
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 179
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 98
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 12
	},
	{
		"tiempo_reproducido": 115
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 24
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 125
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 17
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 28
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 128
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 18
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 154
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 88
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 49
	},
	{
		"tiempo_reproducido": 85
	},
	{
		"tiempo_reproducido": 79
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 41
	},
	{
		"tiempo_reproducido": 52
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 170
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 69
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 75
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 145
	},
	{
		"tiempo_reproducido": 63
	},
	{
		"tiempo_reproducido": 13
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 28
	},
	{
		"tiempo_reproducido": 94
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 33
	},
	{
		"tiempo_reproducido": 118
	},
	{
		"tiempo_reproducido": 17
	},
	{
		"tiempo_reproducido": 118
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 118
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 157
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 21
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 33
	},
	{
		"tiempo_reproducido": 131
	},
	{
		"tiempo_reproducido": 2
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 110
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 136
	},
	{
		"tiempo_reproducido": 20
	},
	{
		"tiempo_reproducido": 178
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 131
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 15
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 61
	},
	{
		"tiempo_reproducido": 116
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 178
	},
	{
		"tiempo_reproducido": 134
	},
	{
		"tiempo_reproducido": 56
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 110
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 136
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 2
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 27
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 136
	},
	{
		"tiempo_reproducido": 55
	},
	{
		"tiempo_reproducido": 179
	},
	{
		"tiempo_reproducido": 91
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 22
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 87
	},
	{
		"tiempo_reproducido": 25
	},
	{
		"tiempo_reproducido": 134
	},
	{
		"tiempo_reproducido": 110
	},
	{
		"tiempo_reproducido": 50
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 45
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 95
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 122
	},
	{
		"tiempo_reproducido": 130
	},
	{
		"tiempo_reproducido": 80
	},
	{
		"tiempo_reproducido": 51
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 110
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 160
	},
	{
		"tiempo_reproducido": 162
	},
	{
		"tiempo_reproducido": 104
	},
	{
		"tiempo_reproducido": 165
	},
	{
		"tiempo_reproducido": 22
	},
	{
		"tiempo_reproducido": 94
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 28
	},
	{
		"tiempo_reproducido": 163
	},
	{
		"tiempo_reproducido": 142
	},
	{
		"tiempo_reproducido": 119
	},
	{
		"tiempo_reproducido": 50
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 126
	},
	{
		"tiempo_reproducido": 146
	},
	{
		"tiempo_reproducido": 107
	},
	{
		"tiempo_reproducido": 124
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 129
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 49
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 97
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 118
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 45
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 114
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 80
	},
	{
		"tiempo_reproducido": 160
	},
	{
		"tiempo_reproducido": 179
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 36
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 57
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 79
	},
	{
		"tiempo_reproducido": 51
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 117
	},
	{
		"tiempo_reproducido": 153
	},
	{
		"tiempo_reproducido": 0
	},
	{
		"tiempo_reproducido": 127
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 63
	},
	{
		"tiempo_reproducido": 160
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 98
	},
	{
		"tiempo_reproducido": 29
	},
	{
		"tiempo_reproducido": 31
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 8
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 52
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 30
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 83
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 147
	},
	{
		"tiempo_reproducido": 59
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 6
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 132
	},
	{
		"tiempo_reproducido": 92
	},
	{
		"tiempo_reproducido": 87
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 2
	},
	{
		"tiempo_reproducido": 65
	},
	{
		"tiempo_reproducido": 44
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 171
	},
	{
		"tiempo_reproducido": 58
	},
	{
		"tiempo_reproducido": 96
	},
	{
		"tiempo_reproducido": 159
	},
	{
		"tiempo_reproducido": 46
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 120
	},
	{
		"tiempo_reproducido": 180
	},
	{
		"tiempo_reproducido": 77
	},
	{
		"tiempo_reproducido": 24
	},
	{
		"tiempo_reproducido": 66
	},
	{
		"tiempo_reproducido": 91
	},
	{
		"tiempo_reproducido": 8
	},
	{
		"tiempo_reproducido": 26
	},
	{
		"tiempo_reproducido": 72
	},
	{
		"tiempo_reproducido": 8
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 95
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 161
	},
	{
		"tiempo_reproducido": 111
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 100
	},
	{
		"tiempo_reproducido": 14
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 67
	},
	{
		"tiempo_reproducido": 1
	},
	{
		"tiempo_reproducido": 168
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 166
	},
	{
		"tiempo_reproducido": 125
	},
	{
		"tiempo_reproducido": 66
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 176
	},
	{
		"tiempo_reproducido": 5
	},
	{
		"tiempo_reproducido": 27
	},
	{
		"tiempo_reproducido": 155
	},
	{
		"tiempo_reproducido": 65
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 169
	},
	{
		"tiempo_reproducido": 74
	},
	{
		"tiempo_reproducido": 123
	},
	{
		"tiempo_reproducido": 102
	},
	{
		"tiempo_reproducido": 68
	},
	{
		"tiempo_reproducido": 105
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 172
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 81
	},
	{
		"tiempo_reproducido": 52
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 62
	},
	{
		"tiempo_reproducido": 137
	},
	{
		"tiempo_reproducido": 35
	},
	{
		"tiempo_reproducido": 144
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 54
	},
	{
		"tiempo_reproducido": 70
	},
	{
		"tiempo_reproducido": 164
	},
	{
		"tiempo_reproducido": 101
	},
	{
		"tiempo_reproducido": 136
	},
	{
		"tiempo_reproducido": 23
	},
	{
		"tiempo_reproducido": 53
	},
	{
		"tiempo_reproducido": 117
	},
	{
		"tiempo_reproducido": 54
	},
	{
		"tiempo_reproducido": 109
	},
	{
		"tiempo_reproducido": 76
	},
	{
		"tiempo_reproducido": 130
	},
	{
		"tiempo_reproducido": 34
	},
	{
		"tiempo_reproducido": 37
	},
	{
		"tiempo_reproducido": 19
	},
	{
		"tiempo_reproducido": 60
	},
	{
		"tiempo_reproducido": 22
	},
	{
		"tiempo_reproducido": 3
	},
	{
		"tiempo_reproducido": 108
	},
	{
		"tiempo_reproducido": 89
	},
	{
		"tiempo_reproducido": 175
	},
	{
		"tiempo_reproducido": 133
	},
	{
		"tiempo_reproducido": 156
	},
	{
		"tiempo_reproducido": 90
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 38
	},
	{
		"tiempo_reproducido": 4
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 17
	},
	{
		"tiempo_reproducido": 112
	},
	{
		"tiempo_reproducido": 141
	},
	{
		"tiempo_reproducido": 42
	},
	{
		"tiempo_reproducido": 64
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 79
	},
	{
		"tiempo_reproducido": 173
	},
	{
		"tiempo_reproducido": 158
	},
	{
		"tiempo_reproducido": 39
	},
	{
		"tiempo_reproducido": 139
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 106
	},
	{
		"tiempo_reproducido": 71
	},
	{
		"tiempo_reproducido": 156
	},
	{
		"tiempo_reproducido": 149
	},
	{
		"tiempo_reproducido": 99
	},
	{
		"tiempo_reproducido": 13
	},
	{
		"tiempo_reproducido": 93
	},
	{
		"tiempo_reproducido": 31
	},
	{
		"tiempo_reproducido": 94
	},
	{
		"tiempo_reproducido": 16
	},
	{
		"tiempo_reproducido": 52
	},
	{
		"tiempo_reproducido": 9
	},
	{
		"tiempo_reproducido": 47
	}
]

canciones = [
	{
		"nombre": "lacinia at,",
		"duracion": 24,
		"autor": "Patricia Bowers",
		"generos": "Clásica Jazz",
		"popularidad": 4,
		"rating": "5, 7, 1, 17, 3, 19, 11, 15"
	},
	{
		"nombre": "eget, venenatis a,",
		"duracion": 125,
		"autor": "Kiayada Cortez",
		"generos": "Techno",
		"popularidad": 9,
		"rating": "5, 15, 11, 13, 3, 9, 1, 19, 17"
	},
	{
		"nombre": "Aliquam",
		"duracion": 146,
		"autor": "Jillian Rice",
		"generos": "Góspel Soul",
		"popularidad": 3,
		"rating": "11, 5, 7, 15, 19, 3, 17, 13, 9, 1"
	},
	{
		"nombre": "Phasellus ornare.",
		"duracion": 120,
		"autor": "Tad Gilmore",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "17, 3, 11, 9, 1, 5, 15, 7"
	},
	{
		"nombre": "egestas. Sed",
		"duracion": 115,
		"autor": "Adria Newton",
		"generos": "Techno",
		"popularidad": 5,
		"rating": "1, 5, 9, 3, 17"
	},
	{
		"nombre": "convallis ligula. Donec",
		"duracion": 25,
		"autor": "Imogene Foreman",
		"generos": "Soul Pop",
		"popularidad": 8,
		"rating": "17, 13, 7, 5, 1, 19, 9, 15, 3"
	},
	{
		"nombre": "magnis",
		"duracion": 131,
		"autor": "Travis Cardenas",
		"generos": "Blues",
		"popularidad": 5,
		"rating": "9, 3, 15, 17, 19, 7"
	},
	{
		"nombre": "tincidunt,",
		"duracion": 52,
		"autor": "Moana Barnett",
		"generos": "Blues Góspel Soul",
		"popularidad": 10,
		"rating": "3, 1, 7"
	},
	{
		"nombre": "mauris eu",
		"duracion": 5,
		"autor": "Gemma Blankenship",
		"generos": "Techno Hip-Hop",
		"popularidad": 0,
		"rating": "11, 19, 3, 13, 5, 7, 9, 15"
	},
	{
		"nombre": "penatibus",
		"duracion": 164,
		"autor": "Yuri Sparks",
		"generos": "Blues Góspel",
		"popularidad": 5,
		"rating": "3, 1, 19, 7, 15, 13, 9, 17, 11"
	},
	{
		"nombre": "molestie. Sed",
		"duracion": 53,
		"autor": "Hanae Alford",
		"generos": "Jazz Blues",
		"popularidad": 2,
		"rating": "13, 3, 7, 11, 17, 1, 19, 9, 15"
	},
	{
		"nombre": "libero",
		"duracion": 89,
		"autor": "Herrod Terry",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "3, 9"
	},
	{
		"nombre": "a sollicitudin",
		"duracion": 31,
		"autor": "Axel Berry",
		"generos": "Disco Techno",
		"popularidad": 1,
		"rating": 5
	},
	{
		"nombre": "dui. Suspendisse",
		"duracion": 111,
		"autor": "Jemima Lamb",
		"generos": "Disco Techno",
		"popularidad": 9,
		"rating": "17, 9, 11, 13, 19, 3"
	},
	{
		"nombre": "tristique",
		"duracion": 178,
		"autor": "Arden Bentley",
		"generos": "Blues Góspel",
		"popularidad": 3,
		"rating": "1, 15, 7, 19, 13, 9"
	},
	{
		"nombre": "tincidunt",
		"duracion": 104,
		"autor": "Fritz Mitchell",
		"generos": "Techno",
		"popularidad": 2,
		"rating": "5, 13, 9, 1"
	},
	{
		"nombre": "eget, volutpat",
		"duracion": 98,
		"autor": "Jin Fischer",
		"generos": "Clásica",
		"popularidad": 9,
		"rating": "3, 13, 5, 7, 9, 17, 1, 15, 19"
	},
	{
		"nombre": "semper egestas,",
		"duracion": 20,
		"autor": "Bevis Wade",
		"generos": "Jazz Blues",
		"popularidad": 8,
		"rating": "3, 11, 5, 9, 19, 7, 13"
	},
	{
		"nombre": "Ut",
		"duracion": 51,
		"autor": "Lillian Armstrong",
		"generos": "Disco",
		"popularidad": 8,
		"rating": "5, 11, 7, 13, 15, 17"
	},
	{
		"nombre": "Phasellus nulla.",
		"duracion": 59,
		"autor": "Zenia Richards",
		"generos": "Country",
		"popularidad": 7,
		"rating": "9, 15, 13, 1, 19, 17"
	},
	{
		"nombre": "dis parturient",
		"duracion": 44,
		"autor": "Mariam Cantu",
		"generos": "Soul Pop",
		"popularidad": 1,
		"rating": "1, 11, 7, 9, 5, 15, 19"
	},
	{
		"nombre": "vel pede blandit",
		"duracion": 120,
		"autor": "Orlando Zamora",
		"generos": "Soul Pop",
		"popularidad": 6,
		"rating": "9, 19, 15, 17, 5, 7, 11, 3"
	},
	{
		"nombre": "mi, ac",
		"duracion": 77,
		"autor": "Tate Bowen",
		"generos": "Rock Country Disco",
		"popularidad": 2,
		"rating": "7, 3, 1, 13, 19, 9, 15, 17"
	},
	{
		"nombre": "Nulla dignissim. Maecenas",
		"duracion": 40,
		"autor": "Kameko Mcmahon",
		"generos": "Hip-Hop Metal",
		"popularidad": 3,
		"rating": "19, 11, 9, 3, 17"
	},
	{
		"nombre": "lobortis",
		"duracion": 167,
		"autor": "Sawyer England",
		"generos": "Rock Country",
		"popularidad": 9,
		"rating": "15, 13"
	},
	{
		"nombre": "ultricies",
		"duracion": 118,
		"autor": "Ignacia Velez",
		"generos": "Jazz Blues",
		"popularidad": 4,
		"rating": "5, 17, 1, 7, 3, 19, 13, 11, 9, 15"
	},
	{
		"nombre": "orci lacus",
		"duracion": 8,
		"autor": "Morgan Whitley",
		"generos": "Pop",
		"popularidad": 0,
		"rating": "15, 1, 7, 13, 19, 17, 11"
	},
	{
		"nombre": "habitant",
		"duracion": 50,
		"autor": "Yuli Kinney",
		"generos": "Soul",
		"popularidad": 4,
		"rating": "9, 3, 1"
	},
	{
		"nombre": "consectetuer",
		"duracion": 28,
		"autor": "Kennedy Watkins",
		"generos": "Jazz",
		"popularidad": 2,
		"rating": "7, 13, 17, 3"
	},
	{
		"nombre": "vulputate",
		"duracion": 112,
		"autor": "Brody Ewing",
		"generos": "Country Disco",
		"popularidad": 8,
		"rating": "7, 17, 19, 15, 5, 1, 3"
	},
	{
		"nombre": "dui. Cum",
		"duracion": 88,
		"autor": "Rhona Herman",
		"generos": "Clásica Jazz",
		"popularidad": 5,
		"rating": "13, 5, 19, 11, 1"
	},
	{
		"nombre": "tellus",
		"duracion": 165,
		"autor": "Garth Serrano",
		"generos": "Rock Country Disco",
		"popularidad": 7,
		"rating": "15, 1, 9, 5, 17"
	},
	{
		"nombre": "malesuada augue",
		"duracion": 176,
		"autor": "Christopher Guy",
		"generos": "Jazz Blues",
		"popularidad": 10,
		"rating": "9, 1, 13, 3, 7, 17, 11"
	},
	{
		"nombre": "Nullam feugiat placerat",
		"duracion": 69,
		"autor": "Samson Reese",
		"generos": "Disco Techno",
		"popularidad": 6,
		"rating": "17, 11, 7, 15, 13, 3, 1, 19"
	},
	{
		"nombre": "libero. Proin",
		"duracion": 70,
		"autor": "Arsenio May",
		"generos": "Pop Rock",
		"popularidad": 10,
		"rating": "3, 15, 1, 19, 7, 17, 5"
	},
	{
		"nombre": "tempor, est",
		"duracion": 10,
		"autor": "Judah Giles",
		"generos": "Blues Góspel Soul",
		"popularidad": 5,
		"rating": "15, 19, 17, 9"
	},
	{
		"nombre": "sem.",
		"duracion": 169,
		"autor": "Declan Schwartz",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"rating": "3, 13, 1, 5, 17, 15, 9, 7, 11"
	},
	{
		"nombre": "rhoncus. Nullam velit",
		"duracion": 81,
		"autor": "Brenda Avila",
		"generos": "Soul Pop",
		"popularidad": 4,
		"rating": 15
	},
	{
		"nombre": "blandit at,",
		"duracion": 48,
		"autor": "Craig Rose",
		"generos": "Techno Hip-Hop Metal",
		"popularidad": 5,
		"rating": "17, 3, 15, 19, 5, 9, 13, 7"
	},
	{
		"nombre": "sit",
		"duracion": 69,
		"autor": "Dennis Adams",
		"generos": "Pop",
		"popularidad": 1,
		"rating": "1, 7, 5, 17"
	},
	{
		"nombre": "tortor,",
		"duracion": 66,
		"autor": "Ivana Skinner",
		"generos": "Soul Pop",
		"popularidad": 6,
		"rating": "11, 13, 15, 9, 19"
	},
	{
		"nombre": "Donec",
		"duracion": 49,
		"autor": "Logan Hampton",
		"generos": "Rock Country",
		"popularidad": 8,
		"rating": "5, 17, 1, 7, 3, 19, 9"
	},
	{
		"nombre": "Pellentesque habitant morbi",
		"duracion": 166,
		"autor": "Chadwick Dunlap",
		"generos": "Soul",
		"popularidad": 4,
		"rating": 1
	},
	{
		"nombre": "tincidunt",
		"duracion": 100,
		"autor": "Kaitlin Humphrey",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 8,
		"rating": "9, 5, 7, 15, 19, 13"
	},
	{
		"nombre": "pede. Nunc sed",
		"duracion": 86,
		"autor": "Nathan Roberson",
		"generos": "Pop Rock Country",
		"popularidad": 1,
		"rating": "15, 5, 9, 17, 7"
	},
	{
		"nombre": "primis in faucibus",
		"duracion": 123,
		"autor": "Dorothy Mclean",
		"generos": "Góspel Soul Pop",
		"popularidad": 6,
		"rating": "15, 7"
	},
	{
		"nombre": "eget massa.",
		"duracion": 102,
		"autor": "Hayley Black",
		"generos": "Soul Pop",
		"popularidad": 3,
		"rating": "19, 17, 9, 15"
	},
	{
		"nombre": "auctor, velit",
		"duracion": 143,
		"autor": "Piper Sloan",
		"generos": "Techno Hip-Hop Metal",
		"popularidad": 1,
		"rating": "3, 13, 15, 17, 1, 9, 7, 11"
	},
	{
		"nombre": "ipsum",
		"duracion": 28,
		"autor": "Callum Humphrey",
		"generos": "Soul Pop",
		"popularidad": 4,
		"rating": "19, 9, 15, 17"
	},
	{
		"nombre": "egestas. Duis",
		"duracion": 130,
		"autor": "Rahim Bush",
		"generos": "Hip-Hop Metal",
		"popularidad": 3,
		"rating": "13, 19, 5, 1, 11"
	},
	{
		"nombre": "neque",
		"duracion": 156,
		"autor": "Tobias Bennett",
		"generos": "Metal",
		"popularidad": 1,
		"rating": "7, 3"
	},
	{
		"nombre": "Etiam",
		"duracion": 11,
		"autor": "Leonard Schwartz",
		"generos": "Country Disco Techno",
		"popularidad": 1,
		"rating": "7, 1, 3"
	},
	{
		"nombre": "natoque penatibus",
		"duracion": 137,
		"autor": "Beverly Fulton",
		"generos": "Soul",
		"popularidad": 6,
		"rating": "17, 15, 5, 13, 1"
	},
	{
		"nombre": "lobortis ultrices. Vivamus",
		"duracion": 147,
		"autor": "Dawn Cervantes",
		"generos": "Jazz Blues",
		"popularidad": 4,
		"rating": "1, 19, 15, 17, 13, 11, 9"
	},
	{
		"nombre": "tristique ac,",
		"duracion": 90,
		"autor": "Kristen Prince",
		"generos": "Blues Góspel",
		"popularidad": 8,
		"rating": "13, 3, 17, 7, 15, 5, 11, 1, 9, 19"
	},
	{
		"nombre": "at auctor",
		"duracion": 53,
		"autor": "Keane Bryant",
		"generos": "Disco",
		"popularidad": 5,
		"rating": "1, 3, 17, 11, 15, 5, 13, 19"
	},
	{
		"nombre": "tempus eu, ligula.",
		"duracion": 13,
		"autor": "Daryl Welch",
		"generos": "Blues",
		"popularidad": 2,
		"rating": "1, 11, 3, 13, 15"
	},
	{
		"nombre": "nulla. Integer urna.",
		"duracion": 29,
		"autor": "Christine Rollins",
		"generos": "Jazz",
		"popularidad": 9,
		"rating": 1
	},
	{
		"nombre": "tempor, est",
		"duracion": 68,
		"autor": "Cairo Talley",
		"generos": "Country Disco Techno",
		"popularidad": 0,
		"rating": "17, 11, 1, 13"
	},
	{
		"nombre": "iaculis aliquet",
		"duracion": 13,
		"autor": "Elton Tran",
		"generos": "Techno Hip-Hop",
		"popularidad": 9,
		"rating": "7, 13, 19, 1, 3, 5, 17, 11"
	},
	{
		"nombre": "id, mollis",
		"duracion": 96,
		"autor": "Lamar Cotton",
		"generos": "Soul",
		"popularidad": 8,
		"rating": "15, 1, 3"
	},
	{
		"nombre": "arcu. Curabitur",
		"duracion": 108,
		"autor": "Emi Fulton",
		"generos": "Góspel Soul",
		"popularidad": 1,
		"rating": "3, 7, 5, 19, 9, 1, 13, 11"
	},
	{
		"nombre": "facilisis",
		"duracion": 125,
		"autor": "Clarke Holden",
		"generos": "Blues",
		"popularidad": 0,
		"rating": "9, 15, 17, 11, 5, 7"
	},
	{
		"nombre": "varius et,",
		"duracion": 29,
		"autor": "Damon Barrera",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "15, 7, 13, 17, 5, 9, 1, 11"
	},
	{
		"nombre": "morbi tristique",
		"duracion": 122,
		"autor": "Gisela Peters",
		"generos": "Country Disco",
		"popularidad": 4,
		"rating": 17
	},
	{
		"nombre": "Morbi vehicula. Pellentesque",
		"duracion": 95,
		"autor": "Garrett Calderon",
		"generos": "Blues Góspel Soul",
		"popularidad": 10,
		"rating": "3, 5, 17, 7, 13, 15, 1, 19"
	},
	{
		"nombre": "vehicula.",
		"duracion": 173,
		"autor": "Devin Hutchinson",
		"generos": "Clásica Jazz",
		"popularidad": 9,
		"rating": "3, 7, 15, 17, 9, 19, 5, 1"
	},
	{
		"nombre": "pharetra nibh.",
		"duracion": 47,
		"autor": "Herrod Alvarez",
		"generos": "Rock Country Disco",
		"popularidad": 6,
		"rating": "17, 15, 1, 5, 19"
	},
	{
		"nombre": "Pellentesque habitant morbi",
		"duracion": 125,
		"autor": "Charles Burke",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 9,
		"rating": "15, 7, 9, 13, 17"
	},
	{
		"nombre": "adipiscing non,",
		"duracion": 54,
		"autor": "Damian Moody",
		"generos": "Pop Rock",
		"popularidad": 7,
		"rating": "1, 5, 7, 11, 15, 9, 19, 3, 13"
	},
	{
		"nombre": "ridiculus",
		"duracion": 137,
		"autor": "Vaughan Vinson",
		"generos": "Blues",
		"popularidad": 5,
		"rating": "15, 9, 1, 17, 19, 11"
	},
	{
		"nombre": "vel",
		"duracion": 8,
		"autor": "Dominique Caldwell",
		"generos": "Disco Techno",
		"popularidad": 6,
		"rating": "1, 9"
	},
	{
		"nombre": "Cras vulputate velit",
		"duracion": 33,
		"autor": "Uriah Hunter",
		"generos": "Techno Hip-Hop",
		"popularidad": 8,
		"rating": "19, 9, 11, 17, 7, 15, 13"
	},
	{
		"nombre": "nibh.",
		"duracion": 94,
		"autor": "Amelia Hickman",
		"generos": "Clásica",
		"popularidad": 8,
		"rating": "15, 13"
	},
	{
		"nombre": "at pretium aliquet,",
		"duracion": 24,
		"autor": "Quamar Sweeney",
		"generos": "Techno",
		"popularidad": 0,
		"rating": 11
	},
	{
		"nombre": "luctus et",
		"duracion": 57,
		"autor": "Micah Cobb",
		"generos": "Jazz",
		"popularidad": 3,
		"rating": "7, 17, 1"
	},
	{
		"nombre": "amet luctus",
		"duracion": 130,
		"autor": "Zelenia Todd",
		"generos": "Disco",
		"popularidad": 8,
		"rating": "7, 15, 11"
	},
	{
		"nombre": "imperdiet nec, leo.",
		"duracion": 98,
		"autor": "Kylee Raymond",
		"generos": "Pop Rock",
		"popularidad": 3,
		"rating": "1, 3, 7, 13"
	},
	{
		"nombre": "eu,",
		"duracion": 151,
		"autor": "Brent Rojas",
		"generos": "Góspel Soul",
		"popularidad": 6,
		"rating": "1, 5, 13, 7, 17"
	},
	{
		"nombre": "lectus",
		"duracion": 147,
		"autor": "Ann Sweeney",
		"generos": "Rock Country Disco",
		"popularidad": 6,
		"rating": "9, 11, 5, 1, 7, 13, 17, 15, 19, 3"
	},
	{
		"nombre": "nunc est,",
		"duracion": 165,
		"autor": "Timon Franklin",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "3, 11, 9, 5, 1, 17, 13, 7"
	},
	{
		"nombre": "Cras vulputate",
		"duracion": 20,
		"autor": "Drake Key",
		"generos": "Soul Pop Rock",
		"popularidad": 3,
		"rating": "17, 7, 11, 3, 13"
	},
	{
		"nombre": "nec, leo.",
		"duracion": 67,
		"autor": "Barbara Daniel",
		"generos": "Góspel",
		"popularidad": 8,
		"rating": 9
	},
	{
		"nombre": "egestas. Fusce aliquet",
		"duracion": 140,
		"autor": "Breanna Ward",
		"generos": "Pop Rock",
		"popularidad": 5,
		"rating": "11, 3, 5, 15, 19, 17, 7, 1"
	},
	{
		"nombre": "et magnis",
		"duracion": 179,
		"autor": "Maia Padilla",
		"generos": "Soul",
		"popularidad": 3,
		"rating": "1, 7, 9, 19, 15, 17, 13"
	},
	{
		"nombre": "vitae nibh.",
		"duracion": 88,
		"autor": "Suki Tate",
		"generos": "Country Disco",
		"popularidad": 7,
		"rating": "17, 7, 11, 13, 9, 19"
	},
	{
		"nombre": "tincidunt congue turpis.",
		"duracion": 52,
		"autor": "Diana Ramos",
		"generos": "Jazz",
		"popularidad": 10,
		"rating": "5, 1, 9"
	},
	{
		"nombre": "tincidunt, neque vitae",
		"duracion": 23,
		"autor": "Petra Harding",
		"generos": "Góspel Soul",
		"popularidad": 6,
		"rating": "5, 15, 3, 13, 1, 7, 9, 19, 11"
	},
	{
		"nombre": "ipsum primis",
		"duracion": 142,
		"autor": "Hope Valdez",
		"generos": "Hip-Hop",
		"popularidad": 4,
		"rating": "5, 11, 19, 13, 9, 15, 7"
	},
	{
		"nombre": "malesuada",
		"duracion": 13,
		"autor": "Stewart Blackburn",
		"generos": "Pop Rock",
		"popularidad": 10,
		"rating": "7, 9, 5, 3, 19"
	},
	{
		"nombre": "neque. Nullam",
		"duracion": 123,
		"autor": "Chloe Oneil",
		"generos": "Blues Góspel",
		"popularidad": 1,
		"rating": "5, 19, 11"
	},
	{
		"nombre": "tincidunt",
		"duracion": 30,
		"autor": "Mary Berg",
		"generos": "Metal",
		"popularidad": 10,
		"rating": "5, 19, 3, 7, 9, 11, 13, 1"
	},
	{
		"nombre": "Nunc ullamcorper,",
		"duracion": 24,
		"autor": "Alvin Hurst",
		"generos": "Clásica Jazz Blues",
		"popularidad": 5,
		"rating": "7, 17, 19, 11, 5"
	},
	{
		"nombre": "metus. Aenean sed",
		"duracion": 90,
		"autor": "Damian Bernard",
		"generos": "Pop",
		"popularidad": 8,
		"rating": "13, 9, 1, 7, 11, 15, 5"
	},
	{
		"nombre": "neque",
		"duracion": 86,
		"autor": "Odessa Beasley",
		"generos": "Blues Góspel",
		"popularidad": 6,
		"rating": "1, 11, 3"
	},
	{
		"nombre": "Fusce feugiat.",
		"duracion": 76,
		"autor": "Hammett Albert",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 1,
		"rating": "7, 11, 3, 17, 13, 9, 15, 5, 19"
	},
	{
		"nombre": "ut, nulla. Cras",
		"duracion": 126,
		"autor": "Cynthia Beard",
		"generos": "Hip-Hop",
		"popularidad": 2,
		"rating": "11, 7, 9, 19"
	},
	{
		"nombre": "eu",
		"duracion": 19,
		"autor": "Vera Ellison",
		"generos": "Hip-Hop Metal",
		"popularidad": 10,
		"rating": 1
	},
	{
		"nombre": "non, egestas",
		"duracion": 35,
		"autor": "Beau Sutton",
		"generos": "Disco",
		"popularidad": 3,
		"rating": 17
	},
	{
		"nombre": "dignissim",
		"duracion": 4,
		"autor": "Carissa Ayala",
		"generos": "Rock Country",
		"popularidad": 2,
		"rating": "17, 7, 11, 9, 3, 5, 1, 19, 13"
	},
	{
		"nombre": "velit.",
		"duracion": 2,
		"autor": "Jana Ortega",
		"generos": "Techno Hip-Hop",
		"popularidad": 7,
		"rating": "19, 7, 1, 5, 9, 13, 17, 11"
	},
	{
		"nombre": "pede. Praesent",
		"duracion": 173,
		"autor": "Stephanie Phelps",
		"generos": "Pop Rock",
		"popularidad": 5,
		"rating": "15, 19, 5, 1, 11, 9, 3, 13, 17"
	},
	{
		"nombre": "lacus.",
		"duracion": 150,
		"autor": "Deborah Dawson",
		"generos": "Techno Hip-Hop",
		"popularidad": 7,
		"rating": "3, 7, 19, 17, 5"
	},
	{
		"nombre": "Nulla",
		"duracion": 70,
		"autor": "Patricia Gilmore",
		"generos": "Blues Góspel Soul",
		"popularidad": 5,
		"rating": 15
	},
	{
		"nombre": "Etiam ligula tortor,",
		"duracion": 161,
		"autor": "Aidan Weiss",
		"generos": "Soul Pop",
		"popularidad": 4,
		"rating": "3, 17, 5, 7, 15, 9, 13, 19"
	},
	{
		"nombre": "adipiscing elit.",
		"duracion": 122,
		"autor": "Deacon Lawrence",
		"generos": "Disco Techno",
		"popularidad": 0,
		"rating": "5, 9"
	},
	{
		"nombre": "quis, pede.",
		"duracion": 8,
		"autor": "Darryl Livingston",
		"generos": "Hip-Hop Metal",
		"popularidad": 6,
		"rating": "3, 7, 19, 9, 11, 5"
	},
	{
		"nombre": "velit. Quisque varius.",
		"duracion": 104,
		"autor": "Rebekah Vazquez",
		"generos": "Góspel Soul",
		"popularidad": 8,
		"rating": "19, 17, 1, 5"
	},
	{
		"nombre": "eget",
		"duracion": 58,
		"autor": "Audrey Cleveland",
		"generos": "Blues Góspel",
		"popularidad": 10,
		"rating": "5, 13, 7"
	},
	{
		"nombre": "ut,",
		"duracion": 13,
		"autor": "Plato Holt",
		"generos": "Clásica",
		"popularidad": 10,
		"rating": "5, 7, 19, 9, 3, 1, 17, 15, 11"
	},
	{
		"nombre": "viverra. Donec",
		"duracion": 30,
		"autor": "Blythe Contreras",
		"generos": "Techno Hip-Hop Metal",
		"popularidad": 9,
		"rating": "19, 11, 7, 17, 9, 5"
	},
	{
		"nombre": "ac, eleifend",
		"duracion": 173,
		"autor": "Buckminster Farley",
		"generos": "Jazz",
		"popularidad": 9,
		"rating": "11, 17, 9, 13"
	},
	{
		"nombre": "Maecenas",
		"duracion": 156,
		"autor": "Amos Lancaster",
		"generos": "Góspel Soul",
		"popularidad": 2,
		"rating": "1, 11"
	},
	{
		"nombre": "eu, accumsan",
		"duracion": 90,
		"autor": "Serina James",
		"generos": "Pop Rock Country",
		"popularidad": 1,
		"rating": "13, 15, 3, 7, 11, 19, 9, 5, 1"
	},
	{
		"nombre": "Cum sociis natoque",
		"duracion": 33,
		"autor": "Naida Dixon",
		"generos": "Rock Country",
		"popularidad": 2,
		"rating": "9, 1, 3, 17, 19, 15"
	},
	{
		"nombre": "iaculis,",
		"duracion": 12,
		"autor": "Cleo Giles",
		"generos": "Disco Techno",
		"popularidad": 3,
		"rating": "15, 19, 11, 7, 9, 17"
	},
	{
		"nombre": "id",
		"duracion": 27,
		"autor": "Joseph Bridges",
		"generos": "Pop Rock",
		"popularidad": 2,
		"rating": "13, 17"
	},
	{
		"nombre": "nec metus",
		"duracion": 128,
		"autor": "Kay Lambert",
		"generos": "Soul Pop Rock",
		"popularidad": 5,
		"rating": "5, 7"
	},
	{
		"nombre": "pharetra nibh.",
		"duracion": 129,
		"autor": "Dale Sutton",
		"generos": "Hip-Hop",
		"popularidad": 6,
		"rating": "3, 1, 11, 9, 7, 5, 17, 15, 19, 13"
	},
	{
		"nombre": "molestie orci",
		"duracion": 99,
		"autor": "Kimberley Valdez",
		"generos": "Blues Góspel",
		"popularidad": 9,
		"rating": "9, 19"
	},
	{
		"nombre": "dolor.",
		"duracion": 85,
		"autor": "Idona Goodwin",
		"generos": "Pop",
		"popularidad": 7,
		"rating": "5, 9, 7, 15, 11, 19"
	},
	{
		"nombre": "ac, fermentum",
		"duracion": 102,
		"autor": "Diana Wilcox",
		"generos": "Blues Góspel",
		"popularidad": 1,
		"rating": "5, 17, 15, 1, 11, 13, 3"
	},
	{
		"nombre": "eu tempor",
		"duracion": 138,
		"autor": "Regan O'brien",
		"generos": "Pop Rock",
		"popularidad": 7,
		"rating": "5, 7, 1, 3, 17"
	},
	{
		"nombre": "sociis natoque penatibus",
		"duracion": 169,
		"autor": "Portia Holcomb",
		"generos": "Hip-Hop",
		"popularidad": 4,
		"rating": "15, 11"
	},
	{
		"nombre": "sed dictum",
		"duracion": 8,
		"autor": "Charity Huffman",
		"generos": "Rock",
		"popularidad": 3,
		"rating": "17, 7"
	},
	{
		"nombre": "nec urna",
		"duracion": 39,
		"autor": "Alice Cook",
		"generos": "Pop Rock",
		"popularidad": 9,
		"rating": "15, 7, 9, 19, 13, 5, 3, 17, 11, 1"
	},
	{
		"nombre": "sit amet",
		"duracion": 101,
		"autor": "Maile Ferguson",
		"generos": "Rock",
		"popularidad": 9,
		"rating": "1, 3, 15, 5, 13, 19, 17, 9, 7, 11"
	},
	{
		"nombre": "nonummy ut,",
		"duracion": 127,
		"autor": "Driscoll Vinson",
		"generos": "Country",
		"popularidad": 5,
		"rating": 15
	},
	{
		"nombre": "sapien. Nunc",
		"duracion": 69,
		"autor": "Michael Spence",
		"generos": "Blues Góspel",
		"popularidad": 3,
		"rating": "11, 9, 7"
	},
	{
		"nombre": "hendrerit consectetuer,",
		"duracion": 175,
		"autor": "Tara Grimes",
		"generos": "Country Disco",
		"popularidad": 1,
		"rating": "1, 17, 7, 3, 15"
	},
	{
		"nombre": "at risus.",
		"duracion": 2,
		"autor": "Lucy Townsend",
		"generos": "Blues Góspel Soul",
		"popularidad": 3,
		"rating": "7, 9, 17, 11, 3, 13, 15, 1, 5, 19"
	},
	{
		"nombre": "et libero.",
		"duracion": 11,
		"autor": "Catherine Hayden",
		"generos": "Techno",
		"popularidad": 8,
		"rating": "7, 13, 15, 3, 1, 11, 9, 19"
	},
	{
		"nombre": "eget, dictum placerat,",
		"duracion": 39,
		"autor": "Brielle Hahn",
		"generos": "Techno",
		"popularidad": 3,
		"rating": "9, 3"
	},
	{
		"nombre": "dignissim",
		"duracion": 54,
		"autor": "Roth Yates",
		"generos": "Techno Hip-Hop",
		"popularidad": 4,
		"rating": "1, 11, 17, 3, 7"
	},
	{
		"nombre": "ipsum",
		"duracion": 157,
		"autor": "Jameson Anthony",
		"generos": "Country Disco",
		"popularidad": 3,
		"rating": "3, 15, 11, 9, 1, 17, 13, 5, 7"
	},
	{
		"nombre": "ligula.",
		"duracion": 78,
		"autor": "Drew Goff",
		"generos": "Country",
		"popularidad": 3,
		"rating": "15, 17, 19, 9"
	},
	{
		"nombre": "tincidunt congue",
		"duracion": 60,
		"autor": "Ila Britt",
		"generos": "Techno Hip-Hop",
		"popularidad": 7,
		"rating": "7, 3, 13, 5, 15, 17"
	},
	{
		"nombre": "euismod",
		"duracion": 106,
		"autor": "Caldwell Holloway",
		"generos": "Techno Hip-Hop",
		"popularidad": 6,
		"rating": "19, 15, 13, 7, 11, 3, 5"
	},
	{
		"nombre": "eget, venenatis a,",
		"duracion": 66,
		"autor": "Nicole Gomez",
		"generos": "Soul",
		"popularidad": 8,
		"rating": "7, 5"
	},
	{
		"nombre": "velit",
		"duracion": 146,
		"autor": "Winter Ford",
		"generos": "Blues",
		"popularidad": 5,
		"rating": "15, 13, 19, 11, 3"
	},
	{
		"nombre": "eget laoreet",
		"duracion": 19,
		"autor": "Vivien Orr",
		"generos": "Rock Country",
		"popularidad": 7,
		"rating": "1, 13, 19, 17, 9, 3, 11, 7, 5"
	},
	{
		"nombre": "fringilla. Donec feugiat",
		"duracion": 11,
		"autor": "Thor Harmon",
		"generos": "Disco",
		"popularidad": 9,
		"rating": "15, 5, 11, 19"
	},
	{
		"nombre": "mi lorem,",
		"duracion": 137,
		"autor": "Lani Shaw",
		"generos": "Blues Góspel",
		"popularidad": 9,
		"rating": "1, 13, 19, 9, 3, 15, 7, 17, 5, 11"
	},
	{
		"nombre": "pede ac",
		"duracion": 175,
		"autor": "Delilah Hopkins",
		"generos": "Pop Rock",
		"popularidad": 7,
		"rating": "15, 3, 1, 9, 7, 11, 19"
	},
	{
		"nombre": "adipiscing non, luctus",
		"duracion": 19,
		"autor": "Hedda Hernandez",
		"generos": "Clásica",
		"popularidad": 1,
		"rating": "3, 1, 7"
	},
	{
		"nombre": "luctus",
		"duracion": 171,
		"autor": "Jason Wilkerson",
		"generos": "Pop Rock Country",
		"popularidad": 5,
		"rating": "15, 17, 7, 9, 3, 19, 13"
	},
	{
		"nombre": "adipiscing non, luctus",
		"duracion": 165,
		"autor": "Fiona Kerr",
		"generos": "Pop Rock Country",
		"popularidad": 3,
		"rating": "11, 7, 17"
	},
	{
		"nombre": "convallis erat,",
		"duracion": 5,
		"autor": "Nathaniel Hendrix",
		"generos": "Soul",
		"popularidad": 6,
		"rating": "15, 11"
	},
	{
		"nombre": "egestas ligula. Nullam",
		"duracion": 152,
		"autor": "Louis Collier",
		"generos": "Jazz Blues Góspel",
		"popularidad": 6,
		"rating": "17, 13, 9, 19, 3, 7"
	},
	{
		"nombre": "Mauris vestibulum,",
		"duracion": 175,
		"autor": "Lionel Rhodes",
		"generos": "Jazz Blues",
		"popularidad": 8,
		"rating": "7, 19"
	},
	{
		"nombre": "massa.",
		"duracion": 89,
		"autor": "Callum Price",
		"generos": "Pop Rock Country",
		"popularidad": 2,
		"rating": "11, 15, 13, 1"
	},
	{
		"nombre": "sit",
		"duracion": 34,
		"autor": "Daquan Medina",
		"generos": "Blues Góspel Soul",
		"popularidad": 0,
		"rating": "3, 11"
	},
	{
		"nombre": "Nunc",
		"duracion": 170,
		"autor": "Yoshio Solis",
		"generos": "Blues",
		"popularidad": 0,
		"rating": "9, 17"
	},
	{
		"nombre": "risus. Duis",
		"duracion": 154,
		"autor": "Aladdin Bullock",
		"generos": "Techno Hip-Hop",
		"popularidad": 3,
		"rating": "9, 3, 5"
	},
	{
		"nombre": "feugiat",
		"duracion": 50,
		"autor": "Maris King",
		"generos": "Metal",
		"popularidad": 2,
		"rating": "13, 17, 1, 7, 15, 3, 9, 19"
	},
	{
		"nombre": "consectetuer, cursus et,",
		"duracion": 83,
		"autor": "Tanner Eaton",
		"generos": "Country Disco Techno",
		"popularidad": 3,
		"rating": "15, 13, 7, 3, 17, 5, 11, 1, 9"
	},
	{
		"nombre": "mollis. Duis",
		"duracion": 119,
		"autor": "Armand Payne",
		"generos": "Soul Pop",
		"popularidad": 0,
		"rating": "9, 7, 19, 11, 17, 1, 15, 3"
	},
	{
		"nombre": "risus,",
		"duracion": 136,
		"autor": "Macon Tate",
		"generos": "Disco Techno",
		"popularidad": 10,
		"rating": "15, 13, 7"
	},
	{
		"nombre": "tortor, dictum",
		"duracion": 59,
		"autor": "Anika Mccarty",
		"generos": "Jazz Blues",
		"popularidad": 9,
		"rating": "15, 7, 11, 9, 13, 3, 17, 5, 19, 1"
	},
	{
		"nombre": "non sapien molestie",
		"duracion": 110,
		"autor": "Portia Lott",
		"generos": "Rock",
		"popularidad": 3,
		"rating": "19, 13, 11, 1, 17, 5, 9, 3, 15, 7"
	},
	{
		"nombre": "sem. Pellentesque",
		"duracion": 138,
		"autor": "Ray Dillard",
		"generos": "Blues Góspel",
		"popularidad": 0,
		"rating": "11, 5, 17, 7, 1"
	},
	{
		"nombre": "primis in",
		"duracion": 25,
		"autor": "Isabelle Clark",
		"generos": "Hip-Hop",
		"popularidad": 8,
		"rating": "7, 13"
	},
	{
		"nombre": "tellus non",
		"duracion": 89,
		"autor": "Lilah Reyes",
		"generos": "Disco Techno",
		"popularidad": 8,
		"rating": "19, 7, 1"
	},
	{
		"nombre": "Suspendisse",
		"duracion": 130,
		"autor": "Selma Zamora",
		"generos": "Country Disco",
		"popularidad": 10,
		"rating": "13, 5, 3, 7, 1, 15, 11, 17, 9"
	},
	{
		"nombre": "elit sed",
		"duracion": 136,
		"autor": "Martena Huber",
		"generos": "Rock Country Disco",
		"popularidad": 3,
		"rating": "11, 7, 13, 5, 15, 3, 19, 9, 17"
	},
	{
		"nombre": "Cras",
		"duracion": 95,
		"autor": "Marny White",
		"generos": "Blues Góspel Soul",
		"popularidad": 3,
		"rating": "7, 11"
	},
	{
		"nombre": "tellus sem",
		"duracion": 39,
		"autor": "Odysseus Vega",
		"generos": "Pop Rock",
		"popularidad": 6,
		"rating": "19, 1, 15, 17, 7, 11, 3, 9, 13"
	},
	{
		"nombre": "Suspendisse",
		"duracion": 42,
		"autor": "Audrey Velasquez",
		"generos": "Blues Góspel",
		"popularidad": 9,
		"rating": "11, 15, 9, 19, 13, 5, 1, 7, 17"
	},
	{
		"nombre": "magna nec",
		"duracion": 111,
		"autor": "Lance Kaufman",
		"generos": "Techno Hip-Hop",
		"popularidad": 4,
		"rating": "13, 7, 11, 19"
	},
	{
		"nombre": "adipiscing elit.",
		"duracion": 1,
		"autor": "Aimee Slater",
		"generos": "Country Disco",
		"popularidad": 6,
		"rating": "17, 15, 3, 13, 9, 7, 1, 11"
	},
	{
		"nombre": "Aliquam rutrum",
		"duracion": 8,
		"autor": "Britanni Christian",
		"generos": "Blues Góspel Soul",
		"popularidad": 10,
		"rating": "5, 3, 11, 17, 19, 15, 13, 9, 1, 7"
	},
	{
		"nombre": "ac",
		"duracion": 167,
		"autor": "Kevyn Hooper",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "13, 7"
	},
	{
		"nombre": "Aliquam auctor,",
		"duracion": 153,
		"autor": "Madison Cooper",
		"generos": "Góspel Soul Pop",
		"popularidad": 2,
		"rating": "11, 1"
	},
	{
		"nombre": "mauris ut",
		"duracion": 28,
		"autor": "Yasir Weaver",
		"generos": "Soul",
		"popularidad": 1,
		"rating": "15, 9, 5, 3, 19, 1"
	},
	{
		"nombre": "orci, in",
		"duracion": 144,
		"autor": "Lev Hughes",
		"generos": "Country Disco",
		"popularidad": 10,
		"rating": "17, 15, 19, 1, 9, 7, 5, 13, 3, 11"
	},
	{
		"nombre": "Praesent",
		"duracion": 80,
		"autor": "Gil Owens",
		"generos": "Góspel Soul",
		"popularidad": 2,
		"rating": "9, 19, 1, 11, 15"
	},
	{
		"nombre": "Nunc lectus",
		"duracion": 110,
		"autor": "Salvador Moses",
		"generos": "Hip-Hop Metal",
		"popularidad": 4,
		"rating": "19, 5, 7, 15"
	},
	{
		"nombre": "libero est,",
		"duracion": 175,
		"autor": "Ayanna Lindsey",
		"generos": "Disco",
		"popularidad": 9,
		"rating": "11, 17, 3, 13, 19, 1"
	},
	{
		"nombre": "dolor",
		"duracion": 57,
		"autor": "Stacy Franco",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 5,
		"rating": "15, 17"
	},
	{
		"nombre": "velit.",
		"duracion": 169,
		"autor": "Jana Mathis",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "15, 13, 3, 17, 5, 1"
	},
	{
		"nombre": "sollicitudin",
		"duracion": 74,
		"autor": "Barrett Mckay",
		"generos": "Disco",
		"popularidad": 5,
		"rating": "17, 11"
	},
	{
		"nombre": "eget, venenatis a,",
		"duracion": 66,
		"autor": "Winter Hamilton",
		"generos": "Clásica",
		"popularidad": 9,
		"rating": "5, 15, 19, 7, 1, 9, 13"
	},
	{
		"nombre": "Fusce",
		"duracion": 127,
		"autor": "Acton Bowen",
		"generos": "Country Disco Techno",
		"popularidad": 1,
		"rating": "17, 3, 1, 15, 9"
	},
	{
		"nombre": "mattis. Cras",
		"duracion": 76,
		"autor": "Jordan Lloyd",
		"generos": "Jazz Blues Góspel",
		"popularidad": 6,
		"rating": "7, 11, 5, 17, 15, 3, 9, 13, 1"
	},
	{
		"nombre": "Quisque imperdiet, erat",
		"duracion": 161,
		"autor": "Elizabeth Sexton",
		"generos": "Soul",
		"popularidad": 8,
		"rating": "9, 15, 7, 11, 13, 19, 5, 3, 1, 17"
	},
	{
		"nombre": "elementum, dui quis",
		"duracion": 36,
		"autor": "Madeson Hancock",
		"generos": "Techno Hip-Hop",
		"popularidad": 9,
		"rating": "13, 11, 3, 15, 9, 1, 7, 5"
	},
	{
		"nombre": "bibendum. Donec felis",
		"duracion": 118,
		"autor": "Ciaran Lambert",
		"generos": "Soul Pop Rock",
		"popularidad": 1,
		"rating": "9, 17, 5, 19"
	},
	{
		"nombre": "convallis convallis",
		"duracion": 80,
		"autor": "Nina Horne",
		"generos": "Soul Pop",
		"popularidad": 5,
		"rating": "15, 9, 17"
	},
	{
		"nombre": "dolor, tempus non,",
		"duracion": 12,
		"autor": "Kasimir Mason",
		"generos": "Jazz Blues",
		"popularidad": 8,
		"rating": "19, 7, 5"
	},
	{
		"nombre": "amet,",
		"duracion": 163,
		"autor": "Hall Burton",
		"generos": "Góspel Soul",
		"popularidad": 2,
		"rating": "7, 11, 1, 17"
	},
	{
		"nombre": "est",
		"duracion": 38,
		"autor": "Lillian Everett",
		"generos": "Góspel",
		"popularidad": 4,
		"rating": "7, 19, 1, 3, 13, 11"
	},
	{
		"nombre": "lacus vestibulum",
		"duracion": 126,
		"autor": "Damian Morales",
		"generos": "Hip-Hop",
		"popularidad": 8,
		"rating": "7, 3, 15, 13, 5, 9, 19, 11"
	},
	{
		"nombre": "dictum augue",
		"duracion": 85,
		"autor": "Conan Durham",
		"generos": "Disco Techno",
		"popularidad": 2,
		"rating": "19, 3, 11"
	},
	{
		"nombre": "blandit",
		"duracion": 77,
		"autor": "Price Albert",
		"generos": "Soul Pop",
		"popularidad": 2,
		"rating": "11, 9, 13, 1, 5, 3, 15"
	},
	{
		"nombre": "non, feugiat nec,",
		"duracion": 104,
		"autor": "Kessie Leon",
		"generos": "Disco Techno",
		"popularidad": 2,
		"rating": "17, 5, 19, 15, 3, 13"
	},
	{
		"nombre": "semper pretium",
		"duracion": 85,
		"autor": "Geoffrey Barry",
		"generos": "Soul",
		"popularidad": 3,
		"rating": "5, 7"
	},
	{
		"nombre": "Fusce fermentum fermentum",
		"duracion": 125,
		"autor": "Jael Herring",
		"generos": "Jazz Blues Góspel",
		"popularidad": 4,
		"rating": "11, 5, 19, 1, 9, 17, 13, 7, 15"
	},
	{
		"nombre": "Mauris molestie",
		"duracion": 170,
		"autor": "Galvin Roberson",
		"generos": "Disco Techno",
		"popularidad": 4,
		"rating": "5, 11"
	},
	{
		"nombre": "magna nec quam.",
		"duracion": 39,
		"autor": "Zeus Sanford",
		"generos": "Disco Techno",
		"popularidad": 9,
		"rating": "13, 17, 9, 5, 11"
	},
	{
		"nombre": "euismod urna. Nullam",
		"duracion": 17,
		"autor": "Ciara Anthony",
		"generos": "Pop Rock",
		"popularidad": 4,
		"rating": "3, 17, 19, 7, 9, 5, 15, 13, 1"
	},
	{
		"nombre": "porttitor",
		"duracion": 171,
		"autor": "Hedley Flynn",
		"generos": "Pop Rock",
		"popularidad": 3,
		"rating": "1, 15, 19"
	},
	{
		"nombre": "ridiculus mus.",
		"duracion": 151,
		"autor": "Colt Green",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"rating": "9, 5, 11, 19, 13"
	},
	{
		"nombre": "commodo ipsum. Suspendisse",
		"duracion": 137,
		"autor": "Oprah Herrera",
		"generos": "Disco Techno",
		"popularidad": 6,
		"rating": "13, 3, 1, 15, 7"
	},
	{
		"nombre": "magna nec",
		"duracion": 155,
		"autor": "Lyle Woodard",
		"generos": "Blues Góspel Soul",
		"popularidad": 5,
		"rating": "19, 17, 1, 11, 13, 9, 7, 15, 3"
	},
	{
		"nombre": "sit",
		"duracion": 112,
		"autor": "Scarlett Ferrell",
		"generos": "Pop Rock",
		"popularidad": 1,
		"rating": "13, 17, 11, 7, 3, 5, 1, 9, 19"
	},
	{
		"nombre": "neque sed",
		"duracion": 55,
		"autor": "Kay Nieves",
		"generos": "Techno Hip-Hop",
		"popularidad": 9,
		"rating": "17, 5, 19, 13, 3, 1, 9, 15, 7"
	},
	{
		"nombre": "hymenaeos. Mauris ut",
		"duracion": 168,
		"autor": "Mufutau Blankenship",
		"generos": "Clásica Jazz",
		"popularidad": 2,
		"rating": "9, 19, 17, 15"
	},
	{
		"nombre": "tempor",
		"duracion": 113,
		"autor": "Adrienne Lewis",
		"generos": "Rock Country",
		"popularidad": 9,
		"rating": "9, 3, 5"
	},
	{
		"nombre": "ut",
		"duracion": 149,
		"autor": "Tobias Barber",
		"generos": "Techno Hip-Hop",
		"popularidad": 1,
		"rating": "1, 15"
	},
	{
		"nombre": "placerat velit.",
		"duracion": 174,
		"autor": "Uta Savage",
		"generos": "Soul Pop Rock",
		"popularidad": 9,
		"rating": "19, 9, 11, 17"
	},
	{
		"nombre": "enim nisl",
		"duracion": 12,
		"autor": "Alden Wolfe",
		"generos": "Pop Rock",
		"popularidad": 1,
		"rating": 17
	},
	{
		"nombre": "metus urna",
		"duracion": 77,
		"autor": "Denton Jacobson",
		"generos": "Pop Rock",
		"popularidad": 5,
		"rating": "19, 7, 13, 15, 9"
	},
	{
		"nombre": "ipsum.",
		"duracion": 99,
		"autor": "Shad Hunt",
		"generos": "Blues Góspel Soul",
		"popularidad": 7,
		"rating": "9, 13, 19"
	},
	{
		"nombre": "leo. Vivamus nibh",
		"duracion": 139,
		"autor": "Britanni Boone",
		"generos": "Jazz Blues Góspel",
		"popularidad": 10,
		"rating": "13, 3, 19, 15, 11, 5, 7, 9, 1"
	},
	{
		"nombre": "massa. Quisque",
		"duracion": 63,
		"autor": "Dillon Hughes",
		"generos": "Pop Rock",
		"popularidad": 0,
		"rating": "17, 15, 11, 1"
	},
	{
		"nombre": "turpis nec",
		"duracion": 151,
		"autor": "Maxwell Wilson",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "9, 3, 5, 17, 19, 11, 1, 15, 7, 13"
	},
	{
		"nombre": "Cras",
		"duracion": 99,
		"autor": "Lareina Solomon",
		"generos": "Soul Pop Rock",
		"popularidad": 10,
		"rating": "1, 5, 7, 9"
	},
	{
		"nombre": "non, bibendum",
		"duracion": 117,
		"autor": "Cameron Allison",
		"generos": "Country Disco Techno",
		"popularidad": 8,
		"rating": "15, 1, 9, 11"
	},
	{
		"nombre": "malesuada. Integer",
		"duracion": 174,
		"autor": "Brody Compton",
		"generos": "Clásica",
		"popularidad": 7,
		"rating": "11, 3, 17"
	},
	{
		"nombre": "malesuada fames",
		"duracion": 110,
		"autor": "Hedda Miranda",
		"generos": "Country Disco",
		"popularidad": 4,
		"rating": "5, 17"
	},
	{
		"nombre": "at, velit.",
		"duracion": 172,
		"autor": "Piper Mejia",
		"generos": "Soul Pop Rock",
		"popularidad": 6,
		"rating": "1, 15, 7, 13, 17, 5, 9, 3, 19"
	},
	{
		"nombre": "metus urna",
		"duracion": 115,
		"autor": "Aquila Slater",
		"generos": "Blues Góspel",
		"popularidad": 1,
		"rating": "7, 17, 13"
	},
	{
		"nombre": "ipsum. Donec",
		"duracion": 161,
		"autor": "Teagan Serrano",
		"generos": "Blues Góspel",
		"popularidad": 0,
		"rating": "13, 19, 5, 11, 1, 3, 9"
	},
	{
		"nombre": "a odio semper",
		"duracion": 137,
		"autor": "Zia Acevedo",
		"generos": "Clásica Jazz",
		"popularidad": 1,
		"rating": "3, 17, 7, 19, 9, 5, 11, 15"
	},
	{
		"nombre": "Nunc sollicitudin",
		"duracion": 102,
		"autor": "Uma Goodwin",
		"generos": "Hip-Hop",
		"popularidad": 2,
		"rating": "15, 17, 5, 11, 3"
	},
	{
		"nombre": "sed libero.",
		"duracion": 149,
		"autor": "Gil Watson",
		"generos": "Góspel Soul Pop",
		"popularidad": 2,
		"rating": 1
	},
	{
		"nombre": "lorem ac",
		"duracion": 156,
		"autor": "Dillon Christensen",
		"generos": "Country Disco Techno",
		"popularidad": 5,
		"rating": "3, 11, 7, 17, 1, 19, 13, 5, 15"
	},
	{
		"nombre": "et magnis dis",
		"duracion": 85,
		"autor": "Benjamin Maddox",
		"generos": "Góspel Soul Pop",
		"popularidad": 7,
		"rating": "5, 3, 19"
	},
	{
		"nombre": "in,",
		"duracion": 118,
		"autor": "Keaton Schmidt",
		"generos": "Blues Góspel",
		"popularidad": 2,
		"rating": "5, 1, 13, 19, 9, 3, 11, 15, 7, 17"
	},
	{
		"nombre": "Aliquam fringilla cursus",
		"duracion": 7,
		"autor": "Aquila Moran",
		"generos": "Pop Rock Country",
		"popularidad": 8,
		"rating": "19, 5, 1, 13, 17, 3, 7, 15"
	},
	{
		"nombre": "varius et,",
		"duracion": 31,
		"autor": "Quintessa Herrera",
		"generos": "Rock Country",
		"popularidad": 4,
		"rating": "1, 13, 5, 15"
	},
	{
		"nombre": "Aliquam gravida",
		"duracion": 109,
		"autor": "Willow Pickett",
		"generos": "Country Disco",
		"popularidad": 8,
		"rating": "13, 9"
	},
	{
		"nombre": "Ut nec",
		"duracion": 95,
		"autor": "Sydnee Hewitt",
		"generos": "Pop Rock",
		"popularidad": 3,
		"rating": "3, 19, 1, 15, 7"
	},
	{
		"nombre": "sed",
		"duracion": 133,
		"autor": "Savannah Cannon",
		"generos": "Soul",
		"popularidad": 6,
		"rating": "3, 11, 1"
	},
	{
		"nombre": "at sem",
		"duracion": 107,
		"autor": "Linus Higgins",
		"generos": "Country",
		"popularidad": 8,
		"rating": "17, 9, 7, 1, 3"
	},
	{
		"nombre": "tempor, est",
		"duracion": 15,
		"autor": "Vance Terry",
		"generos": "Rock",
		"popularidad": 0,
		"rating": "9, 13, 11, 1, 15"
	},
	{
		"nombre": "ornare placerat,",
		"duracion": 137,
		"autor": "Burke Copeland",
		"generos": "Góspel Soul Pop",
		"popularidad": 0,
		"rating": "3, 19, 5"
	},
	{
		"nombre": "Nunc sed",
		"duracion": 55,
		"autor": "Emma Middleton",
		"generos": "Rock Country",
		"popularidad": 8,
		"rating": "15, 7, 1, 13, 3, 11, 5, 9"
	},
	{
		"nombre": "lacinia. Sed",
		"duracion": 65,
		"autor": "Kelly Hurley",
		"generos": "Soul Pop",
		"popularidad": 7,
		"rating": "9, 3, 1, 15, 5, 13, 17"
	},
	{
		"nombre": "vitae, sodales at,",
		"duracion": 37,
		"autor": "Demetrius Kelly",
		"generos": "Hip-Hop",
		"popularidad": 9,
		"rating": "17, 15"
	},
	{
		"nombre": "Etiam ligula tortor,",
		"duracion": 156,
		"autor": "Sheila Bradford",
		"generos": "Rock",
		"popularidad": 8,
		"rating": "19, 15, 17, 3, 7"
	},
	{
		"nombre": "tristique pellentesque,",
		"duracion": 124,
		"autor": "Daria Sykes",
		"generos": "Country Disco Techno",
		"popularidad": 6,
		"rating": "11, 13, 1, 17, 19, 7, 9"
	},
	{
		"nombre": "pede ac urna.",
		"duracion": 94,
		"autor": "Noelani Kirk",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "13, 1, 17, 3, 19"
	},
	{
		"nombre": "erat",
		"duracion": 165,
		"autor": "Ashton Sanders",
		"generos": "Góspel Soul Pop",
		"popularidad": 6,
		"rating": "17, 5"
	},
	{
		"nombre": "ipsum primis in",
		"duracion": 75,
		"autor": "Armand Guerra",
		"generos": "Jazz",
		"popularidad": 7,
		"rating": "17, 5, 3, 7"
	},
	{
		"nombre": "convallis convallis",
		"duracion": 155,
		"autor": "Savannah Mclaughlin",
		"generos": "Soul",
		"popularidad": 6,
		"rating": "11, 5, 17, 3, 15"
	},
	{
		"nombre": "ac mattis",
		"duracion": 21,
		"autor": "Tucker Graham",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "11, 19, 13, 1, 9, 7"
	},
	{
		"nombre": "aliquet vel,",
		"duracion": 145,
		"autor": "Noah Bullock",
		"generos": "Techno Hip-Hop",
		"popularidad": 5,
		"rating": "1, 5"
	},
	{
		"nombre": "Donec at",
		"duracion": 80,
		"autor": "Signe Booker",
		"generos": "Rock Country",
		"popularidad": 5,
		"rating": 3
	},
	{
		"nombre": "consectetuer",
		"duracion": 21,
		"autor": "Phelan Richmond",
		"generos": "Soul Pop Rock",
		"popularidad": 1,
		"rating": "19, 9, 7"
	},
	{
		"nombre": "parturient",
		"duracion": 100,
		"autor": "Darius Carney",
		"generos": "Techno Hip-Hop",
		"popularidad": 6,
		"rating": "1, 5, 19, 13, 11, 3, 15, 17, 9, 7"
	},
	{
		"nombre": "eget metus. In",
		"duracion": 153,
		"autor": "Tamara Hurst",
		"generos": "Góspel Soul",
		"popularidad": 7,
		"rating": "5, 11, 9, 1, 7, 13, 19, 15, 3"
	},
	{
		"nombre": "Phasellus",
		"duracion": 54,
		"autor": "Caesar Roth",
		"generos": "Disco Techno",
		"popularidad": 7,
		"rating": "11, 13, 7, 9"
	},
	{
		"nombre": "sit amet orci.",
		"duracion": 142,
		"autor": "Claire Robbins",
		"generos": "Techno Hip-Hop Metal",
		"popularidad": 5,
		"rating": "3, 9, 17, 7, 11, 1"
	},
	{
		"nombre": "erat",
		"duracion": 60,
		"autor": "Drew Mendez",
		"generos": "Blues",
		"popularidad": 1,
		"rating": "7, 15, 19, 1, 9, 5, 13, 3, 17"
	},
	{
		"nombre": "diam at pretium",
		"duracion": 63,
		"autor": "Kevyn Gray",
		"generos": "Soul",
		"popularidad": 0,
		"rating": "7, 15, 11, 1, 9, 17, 13, 19, 3, 5"
	},
	{
		"nombre": "sapien,",
		"duracion": 8,
		"autor": "Nicole Mack",
		"generos": "Jazz Blues Góspel",
		"popularidad": 7,
		"rating": "3, 15, 11, 17, 13, 7, 19, 5, 9"
	},
	{
		"nombre": "nec urna",
		"duracion": 101,
		"autor": "Joshua Fletcher",
		"generos": "Jazz Blues",
		"popularidad": 4,
		"rating": "11, 9, 17"
	},
	{
		"nombre": "lectus, a sollicitudin",
		"duracion": 165,
		"autor": "Palmer Lawson",
		"generos": "Soul Pop Rock",
		"popularidad": 1,
		"rating": "15, 13, 17, 9, 7"
	},
	{
		"nombre": "et",
		"duracion": 80,
		"autor": "Louis Keith",
		"generos": "Rock Country Disco",
		"popularidad": 3,
		"rating": "3, 7, 1, 17, 11"
	},
	{
		"nombre": "nec",
		"duracion": 129,
		"autor": "Camden Mercer",
		"generos": "Pop Rock Country",
		"popularidad": 8,
		"rating": "9, 15, 19, 13"
	},
	{
		"nombre": "Nulla aliquet.",
		"duracion": 117,
		"autor": "Miranda Delacruz",
		"generos": "Blues Góspel",
		"popularidad": 3,
		"rating": "19, 15, 13, 5, 17"
	},
	{
		"nombre": "Pellentesque habitant",
		"duracion": 73,
		"autor": "Sharon Wynn",
		"generos": "Rock",
		"popularidad": 6,
		"rating": "19, 7, 11, 5, 1, 9, 15, 3"
	},
	{
		"nombre": "aliquet diam. Sed",
		"duracion": 107,
		"autor": "Edan Glenn",
		"generos": "Hip-Hop",
		"popularidad": 0,
		"rating": "15, 9"
	},
	{
		"nombre": "elementum sem,",
		"duracion": 64,
		"autor": "Zelenia Palmer",
		"generos": "Góspel",
		"popularidad": 10,
		"rating": "15, 5, 9, 11, 19, 13, 17, 3, 1"
	},
	{
		"nombre": "arcu. Sed",
		"duracion": 156,
		"autor": "Olga Walters",
		"generos": "Soul Pop",
		"popularidad": 2,
		"rating": "15, 19, 17, 5, 1, 11, 9, 7"
	},
	{
		"nombre": "neque. In",
		"duracion": 17,
		"autor": "Joy Olson",
		"generos": "Soul Pop",
		"popularidad": 4,
		"rating": "9, 19"
	},
	{
		"nombre": "egestas. Fusce aliquet",
		"duracion": 11,
		"autor": "Nomlanga Caldwell",
		"generos": "Blues",
		"popularidad": 3,
		"rating": "13, 17, 11, 15, 7, 1, 19"
	},
	{
		"nombre": "accumsan",
		"duracion": 53,
		"autor": "Wade Allen",
		"generos": "Country Disco Techno",
		"popularidad": 1,
		"rating": "1, 7, 13, 15, 17"
	},
	{
		"nombre": "habitant morbi tristique",
		"duracion": 4,
		"autor": "Sade Benson",
		"generos": "Jazz Blues Góspel",
		"popularidad": 8,
		"rating": "13, 19, 17, 11"
	},
	{
		"nombre": "faucibus lectus,",
		"duracion": 41,
		"autor": "Lesley Bowen",
		"generos": "Góspel Soul",
		"popularidad": 9,
		"rating": "3, 19, 5"
	},
	{
		"nombre": "erat.",
		"duracion": 91,
		"autor": "Hollee Kirk",
		"generos": "Hip-Hop",
		"popularidad": 7,
		"rating": "17, 19"
	},
	{
		"nombre": "neque. Morbi",
		"duracion": 160,
		"autor": "Lacy Ballard",
		"generos": "Góspel Soul Pop",
		"popularidad": 2,
		"rating": "13, 17, 15, 5, 11, 9, 7, 3, 19, 1"
	},
	{
		"nombre": "ipsum primis",
		"duracion": 17,
		"autor": "Katell Wolf",
		"generos": "Pop Rock",
		"popularidad": 10,
		"rating": "9, 15, 19, 11"
	},
	{
		"nombre": "sem molestie",
		"duracion": 67,
		"autor": "Dorian Gallegos",
		"generos": "Techno Hip-Hop Metal",
		"popularidad": 0,
		"rating": "5, 13, 3, 9, 15, 19, 11, 1, 17, 7"
	},
	{
		"nombre": "Cras eget",
		"duracion": 78,
		"autor": "Ulla Leach",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 3,
		"rating": "15, 1, 19, 9, 3"
	},
	{
		"nombre": "risus. Donec egestas.",
		"duracion": 105,
		"autor": "Todd Gilliam",
		"generos": "Metal",
		"popularidad": 4,
		"rating": "5, 7"
	},
	{
		"nombre": "Maecenas iaculis",
		"duracion": 28,
		"autor": "Rajah Kirby",
		"generos": "Jazz",
		"popularidad": 2,
		"rating": "1, 19, 3, 13, 9, 11"
	},
	{
		"nombre": "eget nisi",
		"duracion": 167,
		"autor": "Jack Stanley",
		"generos": "Rock",
		"popularidad": 7,
		"rating": "5, 11, 7"
	},
	{
		"nombre": "erat vitae risus.",
		"duracion": 68,
		"autor": "Urielle Baird",
		"generos": "Techno Hip-Hop",
		"popularidad": 2,
		"rating": "11, 15"
	},
	{
		"nombre": "ornare.",
		"duracion": 154,
		"autor": "Fitzgerald Evans",
		"generos": "Techno Hip-Hop",
		"popularidad": 9,
		"rating": "9, 11, 5, 13, 1, 17, 15, 3, 19"
	},
	{
		"nombre": "posuere vulputate,",
		"duracion": 93,
		"autor": "Ingrid Duffy",
		"generos": "Techno",
		"popularidad": 8,
		"rating": "3, 17, 1, 5, 19, 11, 9, 13"
	},
	{
		"nombre": "tellus. Aenean",
		"duracion": 126,
		"autor": "Shelly Roberts",
		"generos": "Pop",
		"popularidad": 8,
		"rating": "19, 3, 5, 13, 15, 1, 9, 11"
	},
	{
		"nombre": "nulla. In tincidunt",
		"duracion": 92,
		"autor": "Maggie Montgomery",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 3,
		"rating": "5, 15, 1, 7"
	},
	{
		"nombre": "dui.",
		"duracion": 135,
		"autor": "Robert Cote",
		"generos": "Rock Country Disco",
		"popularidad": 8,
		"rating": 15
	},
	{
		"nombre": "cubilia Curae",
		"duracion": 142,
		"autor": "Xavier Johns",
		"generos": "Blues Góspel",
		"popularidad": 4,
		"rating": "3, 5, 17"
	},
	{
		"nombre": "parturient montes,",
		"duracion": 152,
		"autor": "Warren Roach",
		"generos": "Soul Pop",
		"popularidad": 9,
		"rating": "19, 11, 3"
	},
	{
		"nombre": "enim. Mauris",
		"duracion": 54,
		"autor": "Micah Cline",
		"generos": "Country Disco",
		"popularidad": 8,
		"rating": "17, 19, 1"
	},
	{
		"nombre": "convallis in,",
		"duracion": 151,
		"autor": "Jeremy Langley",
		"generos": "Disco Techno",
		"popularidad": 5,
		"rating": "9, 15, 17, 11, 7, 5, 3"
	},
	{
		"nombre": "Phasellus ornare. Fusce",
		"duracion": 19,
		"autor": "Melvin Marquez",
		"generos": "Disco",
		"popularidad": 0,
		"rating": "17, 19, 5, 15, 13, 7, 9"
	},
	{
		"nombre": "Nulla",
		"duracion": 120,
		"autor": "Randall Rhodes",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "1, 11, 13, 9, 17, 7"
	},
	{
		"nombre": "placerat velit.",
		"duracion": 71,
		"autor": "Basia Everett",
		"generos": "Rock",
		"popularidad": 3,
		"rating": "7, 17"
	},
	{
		"nombre": "lectus",
		"duracion": 83,
		"autor": "Kato Morgan",
		"generos": "Jazz Blues",
		"popularidad": 3,
		"rating": "19, 9, 1"
	},
	{
		"nombre": "fringilla, porttitor",
		"duracion": 66,
		"autor": "MacKensie Pittman",
		"generos": "Hip-Hop",
		"popularidad": 6,
		"rating": "11, 9, 7"
	},
	{
		"nombre": "sed",
		"duracion": 50,
		"autor": "Hamilton Rutledge",
		"generos": "Clásica",
		"popularidad": 7,
		"rating": "3, 13, 15, 7"
	},
	{
		"nombre": "molestie",
		"duracion": 122,
		"autor": "Hiroko Long",
		"generos": "Hip-Hop Metal",
		"popularidad": 9,
		"rating": "19, 13, 5"
	},
	{
		"nombre": "et malesuada fames",
		"duracion": 135,
		"autor": "Colton Barnett",
		"generos": "Jazz Blues",
		"popularidad": 4,
		"rating": "17, 5, 19, 15, 3, 13, 1"
	},
	{
		"nombre": "auctor,",
		"duracion": 137,
		"autor": "Jessica Lambert",
		"generos": "Góspel Soul Pop",
		"popularidad": 3,
		"rating": "7, 9, 13, 5, 1, 15, 11, 3"
	},
	{
		"nombre": "nunc interdum",
		"duracion": 15,
		"autor": "Fredericka Griffin",
		"generos": "Pop Rock Country",
		"popularidad": 9,
		"rating": "11, 5, 9, 7, 13, 17"
	},
	{
		"nombre": "lacus. Cras interdum.",
		"duracion": 32,
		"autor": "Cecilia Byrd",
		"generos": "Soul",
		"popularidad": 5,
		"rating": "9, 15, 11, 7, 19, 13"
	},
	{
		"nombre": "Cras",
		"duracion": 90,
		"autor": "Price Carroll",
		"generos": "Blues Góspel",
		"popularidad": 8,
		"rating": "1, 5, 3, 11, 17, 19, 15, 13"
	},
	{
		"nombre": "ut, pellentesque eget,",
		"duracion": 161,
		"autor": "Nina Bryant",
		"generos": "Techno Hip-Hop",
		"popularidad": 2,
		"rating": "15, 11, 17, 9, 1, 5"
	},
	{
		"nombre": "Sed",
		"duracion": 37,
		"autor": "Leah Carney",
		"generos": "Soul Pop Rock",
		"popularidad": 9,
		"rating": "5, 3, 17, 15, 9, 19"
	},
	{
		"nombre": "risus, at fringilla",
		"duracion": 165,
		"autor": "Harding French",
		"generos": "Pop",
		"popularidad": 5,
		"rating": "13, 11"
	},
	{
		"nombre": "non arcu. Vivamus",
		"duracion": 30,
		"autor": "Luke Tanner",
		"generos": "Blues Góspel Soul",
		"popularidad": 9,
		"rating": 19
	},
	{
		"nombre": "purus.",
		"duracion": 67,
		"autor": "Mariko Stanton",
		"generos": "Techno Hip-Hop",
		"popularidad": 10,
		"rating": "7, 19, 15"
	},
	{
		"nombre": "parturient",
		"duracion": 82,
		"autor": "Tamara Reid",
		"generos": "Góspel Soul Pop",
		"popularidad": 8,
		"rating": 7
	},
	{
		"nombre": "diam at pretium",
		"duracion": 60,
		"autor": "Xantha Osborn",
		"generos": "Techno",
		"popularidad": 0,
		"rating": 19
	},
	{
		"nombre": "orci quis",
		"duracion": 32,
		"autor": "Channing Fuentes",
		"generos": "Hip-Hop Metal",
		"popularidad": 7,
		"rating": "13, 17, 3, 15"
	},
	{
		"nombre": "pede nec",
		"duracion": 92,
		"autor": "Pandora Bridges",
		"generos": "Techno Hip-Hop",
		"popularidad": 8,
		"rating": "9, 3, 11, 5, 19, 13, 15"
	},
	{
		"nombre": "mauris. Integer",
		"duracion": 43,
		"autor": "Sybil Spence",
		"generos": "Country",
		"popularidad": 8,
		"rating": "19, 17, 3, 15, 13"
	},
	{
		"nombre": "ultricies dignissim lacus.",
		"duracion": 13,
		"autor": "Darius Rowland",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "15, 19, 13, 3"
	},
	{
		"nombre": "Proin mi. Aliquam",
		"duracion": 163,
		"autor": "Arthur Bird",
		"generos": "Country Disco Techno",
		"popularidad": 5,
		"rating": "1, 17, 15, 5, 19, 7"
	},
	{
		"nombre": "mattis. Integer eu",
		"duracion": 143,
		"autor": "Leonard Turner",
		"generos": "Góspel Soul Pop",
		"popularidad": 3,
		"rating": "17, 11, 7, 5, 9, 19, 1, 13"
	},
	{
		"nombre": "Donec",
		"duracion": 75,
		"autor": "Madeline Ingram",
		"generos": "Pop Rock",
		"popularidad": 4,
		"rating": "17, 7, 19, 1, 5, 11, 15, 3"
	},
	{
		"nombre": "non",
		"duracion": 123,
		"autor": "Brenden Nixon",
		"generos": "Pop Rock Country",
		"popularidad": 3,
		"rating": 15
	},
	{
		"nombre": "tincidunt orci",
		"duracion": 35,
		"autor": "Allen York",
		"generos": "Blues Góspel",
		"popularidad": 2,
		"rating": "19, 13, 15"
	},
	{
		"nombre": "sodales",
		"duracion": 179,
		"autor": "Deanna Rosa",
		"generos": "Clásica",
		"popularidad": 3,
		"rating": "17, 13, 15, 7, 11, 3"
	},
	{
		"nombre": "at, egestas a,",
		"duracion": 144,
		"autor": "Lionel Frost",
		"generos": "Hip-Hop",
		"popularidad": 5,
		"rating": "17, 9, 1, 19, 5, 11, 15, 7, 13, 3"
	},
	{
		"nombre": "tellus",
		"duracion": 118,
		"autor": "Kenneth Parrish",
		"generos": "Techno",
		"popularidad": 7,
		"rating": "9, 11, 3, 1, 5, 7"
	},
	{
		"nombre": "Nullam nisl.",
		"duracion": 173,
		"autor": "Venus Rose",
		"generos": "Jazz Blues",
		"popularidad": 2,
		"rating": "7, 13, 17, 19, 15, 11, 3, 5, 1"
	},
	{
		"nombre": "fringilla purus",
		"duracion": 52,
		"autor": "Beau Mcneil",
		"generos": "Rock",
		"popularidad": 8,
		"rating": "15, 3, 11, 7, 19, 9, 1, 5"
	},
	{
		"nombre": "neque sed",
		"duracion": 40,
		"autor": "Sade Kinney",
		"generos": "Disco",
		"popularidad": 4,
		"rating": "13, 1, 5, 15"
	},
	{
		"nombre": "elit. Aliquam auctor,",
		"duracion": 38,
		"autor": "Harper Hurley",
		"generos": "Pop Rock",
		"popularidad": 8,
		"rating": "15, 19, 1, 17, 7, 3, 13"
	},
	{
		"nombre": "ut odio",
		"duracion": 25,
		"autor": "Alvin Wright",
		"generos": "Clásica Jazz",
		"popularidad": 5,
		"rating": "3, 7, 13, 19, 17, 15, 1, 11, 9"
	},
	{
		"nombre": "Nunc commodo",
		"duracion": 158,
		"autor": "Lucius Delacruz",
		"generos": "Pop",
		"popularidad": 10,
		"rating": "11, 13, 3, 9, 15, 5, 17, 7, 19, 1"
	},
	{
		"nombre": "in felis. Nulla",
		"duracion": 119,
		"autor": "Amy Charles",
		"generos": "Clásica Jazz Blues",
		"popularidad": 9,
		"rating": "1, 15, 13, 9, 5, 11"
	},
	{
		"nombre": "lacus. Etiam",
		"duracion": 31,
		"autor": "Melissa Burks",
		"generos": "Clásica Jazz",
		"popularidad": 1,
		"rating": "1, 19, 13, 17, 7, 9, 15"
	},
	{
		"nombre": "varius. Nam",
		"duracion": 130,
		"autor": "Demetrius Sandoval",
		"generos": "Disco",
		"popularidad": 8,
		"rating": "9, 7, 13, 11"
	},
	{
		"nombre": "fermentum fermentum arcu.",
		"duracion": 6,
		"autor": "Maris Price",
		"generos": "Country Disco",
		"popularidad": 6,
		"rating": "17, 7, 19, 3, 1"
	},
	{
		"nombre": "Donec luctus",
		"duracion": 5,
		"autor": "Mason Mejia",
		"generos": "Clásica Jazz",
		"popularidad": 0,
		"rating": "3, 19, 1, 13, 9, 17"
	},
	{
		"nombre": "ridiculus mus.",
		"duracion": 151,
		"autor": "Ethan Cannon",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "9, 13, 17, 15, 5"
	},
	{
		"nombre": "vehicula et,",
		"duracion": 169,
		"autor": "Fuller Christensen",
		"generos": "Pop Rock",
		"popularidad": 4,
		"rating": "11, 15, 9, 7, 3, 1, 17"
	},
	{
		"nombre": "tempus risus.",
		"duracion": 37,
		"autor": "Sylvia Palmer",
		"generos": "Rock",
		"popularidad": 0,
		"rating": "11, 17, 13, 9, 1, 15, 5, 3, 19"
	},
	{
		"nombre": "ut, pharetra sed,",
		"duracion": 178,
		"autor": "Jescie Carlson",
		"generos": "Rock",
		"popularidad": 5,
		"rating": "3, 13, 19, 9, 7, 5, 11"
	},
	{
		"nombre": "consequat dolor",
		"duracion": 100,
		"autor": "Hayley Burks",
		"generos": "Country",
		"popularidad": 2,
		"rating": "1, 7, 11"
	},
	{
		"nombre": "in magna.",
		"duracion": 46,
		"autor": "Travis Smith",
		"generos": "Disco Techno",
		"popularidad": 8,
		"rating": "1, 3, 17, 5, 19, 15, 7, 9, 13"
	},
	{
		"nombre": "porttitor eros",
		"duracion": 126,
		"autor": "May Boone",
		"generos": "Góspel",
		"popularidad": 7,
		"rating": "9, 19, 7, 15, 3, 17, 5, 13, 11"
	},
	{
		"nombre": "Nunc sollicitudin commodo",
		"duracion": 89,
		"autor": "Tucker Stein",
		"generos": "Country Disco",
		"popularidad": 4,
		"rating": 3
	},
	{
		"nombre": "enim nisl elementum",
		"duracion": 170,
		"autor": "Yolanda Whitfield",
		"generos": "Jazz",
		"popularidad": 7,
		"rating": "17, 9, 3, 19, 7, 15, 11, 13, 1"
	},
	{
		"nombre": "purus. Maecenas libero",
		"duracion": 59,
		"autor": "Lucian Moon",
		"generos": "Techno Hip-Hop",
		"popularidad": 2,
		"rating": "5, 19, 13, 3"
	},
	{
		"nombre": "enim diam",
		"duracion": 148,
		"autor": "Breanna Beasley",
		"generos": "Country Disco",
		"popularidad": 10,
		"rating": "11, 17, 5, 9, 7"
	},
	{
		"nombre": "cursus a, enim.",
		"duracion": 88,
		"autor": "Zelda Le",
		"generos": "Soul Pop",
		"popularidad": 5,
		"rating": "13, 15, 7, 1, 9"
	},
	{
		"nombre": "dui",
		"duracion": 16,
		"autor": "Brent Townsend",
		"generos": "Country Disco Techno",
		"popularidad": 0,
		"rating": "11, 5, 1, 19, 15"
	},
	{
		"nombre": "arcu",
		"duracion": 130,
		"autor": "Angelica Maxwell",
		"generos": "Pop Rock Country",
		"popularidad": 2,
		"rating": "17, 5"
	},
	{
		"nombre": "ultricies",
		"duracion": 71,
		"autor": "Zephania Merrill",
		"generos": "Hip-Hop Metal",
		"popularidad": 7,
		"rating": "13, 3, 15, 5, 11, 1, 9, 17, 19"
	},
	{
		"nombre": "Aliquam",
		"duracion": 14,
		"autor": "Alexa Watts",
		"generos": "Clásica",
		"popularidad": 2,
		"rating": "1, 7, 5"
	},
	{
		"nombre": "arcu. Sed et",
		"duracion": 160,
		"autor": "Jeremy Brock",
		"generos": "Soul Pop",
		"popularidad": 5,
		"rating": "13, 11, 7, 5, 1, 17, 3, 9"
	},
	{
		"nombre": "tristique pellentesque,",
		"duracion": 92,
		"autor": "Germane Bowman",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "5, 9, 7, 17, 13, 1, 15"
	},
	{
		"nombre": "ut, molestie in,",
		"duracion": 44,
		"autor": "Zahir Bailey",
		"generos": "Country",
		"popularidad": 5,
		"rating": "19, 11, 9, 17, 13, 5"
	},
	{
		"nombre": "id, blandit at,",
		"duracion": 9,
		"autor": "Jonah Kline",
		"generos": "Hip-Hop Metal",
		"popularidad": 8,
		"rating": "9, 19, 13, 17, 7, 15, 3, 5"
	},
	{
		"nombre": "vulputate velit",
		"duracion": 126,
		"autor": "Lucius Hebert",
		"generos": "Rock Country",
		"popularidad": 9,
		"rating": "1, 3, 9, 13, 11"
	},
	{
		"nombre": "scelerisque",
		"duracion": 80,
		"autor": "Wang Johnson",
		"generos": "Techno Hip-Hop",
		"popularidad": 1,
		"rating": "15, 5, 1, 7"
	},
	{
		"nombre": "mauris id",
		"duracion": 168,
		"autor": "Shannon Rutledge",
		"generos": "Disco",
		"popularidad": 1,
		"rating": "3, 7, 5, 9, 13, 11, 19, 1, 17"
	},
	{
		"nombre": "ac mattis ornare,",
		"duracion": 161,
		"autor": "Macaulay Baxter",
		"generos": "Disco Techno",
		"popularidad": 8,
		"rating": "1, 11, 5"
	},
	{
		"nombre": "felis. Nulla tempor",
		"duracion": 159,
		"autor": "Ashely Riley",
		"generos": "Rock Country",
		"popularidad": 8,
		"rating": "11, 19"
	},
	{
		"nombre": "Phasellus dolor",
		"duracion": 157,
		"autor": "Elliott Leach",
		"generos": "Rock",
		"popularidad": 1,
		"rating": "7, 1, 9, 15, 19, 13, 5"
	},
	{
		"nombre": "In",
		"duracion": 92,
		"autor": "Xavier Young",
		"generos": "Disco Techno",
		"popularidad": 6,
		"rating": "5, 1, 9, 17, 19"
	},
	{
		"nombre": "elit,",
		"duracion": 102,
		"autor": "Lois Delaney",
		"generos": "Disco",
		"popularidad": 6,
		"rating": "1, 7, 19, 15, 5, 9, 13, 17, 11"
	},
	{
		"nombre": "quis, tristique ac,",
		"duracion": 96,
		"autor": "Tobias Langley",
		"generos": "Blues Góspel",
		"popularidad": 8,
		"rating": "11, 13, 5, 17, 3, 1"
	},
	{
		"nombre": "pellentesque eget,",
		"duracion": 132,
		"autor": "George Howard",
		"generos": "Techno",
		"popularidad": 3,
		"rating": "19, 9, 15, 7, 5, 17, 13, 11, 1"
	},
	{
		"nombre": "Duis",
		"duracion": 160,
		"autor": "Kimberly Hawkins",
		"generos": "Jazz",
		"popularidad": 10,
		"rating": "19, 3, 1, 9, 15, 5, 13, 17, 11"
	},
	{
		"nombre": "tellus. Aenean",
		"duracion": 114,
		"autor": "Maia Everett",
		"generos": "Góspel Soul",
		"popularidad": 8,
		"rating": "1, 13, 9, 17, 11, 15, 5"
	},
	{
		"nombre": "magna. Ut tincidunt",
		"duracion": 37,
		"autor": "Cynthia Rivera",
		"generos": "Metal",
		"popularidad": 2,
		"rating": "19, 13, 3, 11"
	},
	{
		"nombre": "varius",
		"duracion": 121,
		"autor": "Wylie Mclean",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 6,
		"rating": "9, 11, 5, 1, 19, 7, 13"
	},
	{
		"nombre": "ut",
		"duracion": 51,
		"autor": "Aspen Snider",
		"generos": "Pop",
		"popularidad": 5,
		"rating": "15, 5, 9, 3, 17, 19, 13, 1, 11"
	},
	{
		"nombre": "et",
		"duracion": 8,
		"autor": "Neve Crawford",
		"generos": "Pop Rock Country",
		"popularidad": 6,
		"rating": 1
	},
	{
		"nombre": "Cras eget nisi",
		"duracion": 41,
		"autor": "Leslie Wyatt",
		"generos": "Country",
		"popularidad": 4,
		"rating": "1, 5, 19, 3, 7"
	},
	{
		"nombre": "ipsum",
		"duracion": 25,
		"autor": "Quail Mcdowell",
		"generos": "Pop Rock Country",
		"popularidad": 6,
		"rating": "7, 13, 17, 5"
	},
	{
		"nombre": "enim, sit amet",
		"duracion": 79,
		"autor": "Mannix Finch",
		"generos": "Blues Góspel",
		"popularidad": 8,
		"rating": "7, 3, 5, 15, 17, 19, 13, 9, 1"
	},
	{
		"nombre": "arcu et pede.",
		"duracion": 150,
		"autor": "Tobias Nielsen",
		"generos": "Soul Pop",
		"popularidad": 0,
		"rating": "19, 3, 7, 17"
	},
	{
		"nombre": "tortor. Integer",
		"duracion": 114,
		"autor": "Jasper Winters",
		"generos": "Blues Góspel Soul",
		"popularidad": 9,
		"rating": "7, 15, 13, 1"
	},
	{
		"nombre": "Integer in magna.",
		"duracion": 87,
		"autor": "Omar Gilliam",
		"generos": "Jazz Blues",
		"popularidad": 8,
		"rating": "9, 15, 19, 5, 1"
	},
	{
		"nombre": "libero et",
		"duracion": 45,
		"autor": "Charity Walton",
		"generos": "Country Disco",
		"popularidad": 1,
		"rating": "1, 19, 11, 5, 17, 3, 9, 7, 15, 13"
	},
	{
		"nombre": "mi fringilla",
		"duracion": 56,
		"autor": "Connor Fitzgerald",
		"generos": "Jazz Blues Góspel",
		"popularidad": 10,
		"rating": "5, 17, 3, 13, 7, 9, 1"
	},
	{
		"nombre": "Ut",
		"duracion": 176,
		"autor": "Odette Rivera",
		"generos": "Rock",
		"popularidad": 5,
		"rating": 15
	},
	{
		"nombre": "Phasellus elit",
		"duracion": 157,
		"autor": "Dalton Foreman",
		"generos": "Góspel Soul Pop",
		"popularidad": 2,
		"rating": "1, 9, 7, 11, 3, 19"
	},
	{
		"nombre": "Etiam",
		"duracion": 104,
		"autor": "Chase Byrd",
		"generos": "Clásica Jazz",
		"popularidad": 2,
		"rating": "3, 13, 9, 7, 11"
	},
	{
		"nombre": "erat volutpat. Nulla",
		"duracion": 77,
		"autor": "Gregory Vega",
		"generos": "Pop Rock",
		"popularidad": 8,
		"rating": "15, 9, 11, 1, 17, 3, 19"
	},
	{
		"nombre": "vitae",
		"duracion": 84,
		"autor": "Hadley Kane",
		"generos": "Country Disco",
		"popularidad": 0,
		"rating": "3, 19, 17, 9, 15, 13, 7"
	},
	{
		"nombre": "a felis",
		"duracion": 35,
		"autor": "Hammett Pate",
		"generos": "Hip-Hop",
		"popularidad": 1,
		"rating": "5, 1"
	},
	{
		"nombre": "metus. Aliquam",
		"duracion": 39,
		"autor": "Charissa Cantrell",
		"generos": "Góspel Soul",
		"popularidad": 5,
		"rating": "11, 19, 3, 13"
	},
	{
		"nombre": "netus et malesuada",
		"duracion": 29,
		"autor": "Nigel Nicholson",
		"generos": "Country",
		"popularidad": 7,
		"rating": "15, 9"
	},
	{
		"nombre": "primis",
		"duracion": 68,
		"autor": "Kellie Jensen",
		"generos": "Pop Rock",
		"popularidad": 8,
		"rating": "17, 13, 15, 11, 1, 3"
	},
	{
		"nombre": "elit.",
		"duracion": 157,
		"autor": "Kaitlin Barker",
		"generos": "Jazz Blues",
		"popularidad": 5,
		"rating": "9, 11, 7, 17, 15, 3, 1"
	},
	{
		"nombre": "enim consequat purus.",
		"duracion": 45,
		"autor": "Fuller Guzman",
		"generos": "Góspel",
		"popularidad": 7,
		"rating": "9, 11, 19, 5, 1, 3, 7, 17, 15"
	},
	{
		"nombre": "nunc nulla",
		"duracion": 164,
		"autor": "Hillary Gillespie",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 6,
		"rating": 1
	},
	{
		"nombre": "nulla. Cras",
		"duracion": 37,
		"autor": "Flynn Hurst",
		"generos": "Country",
		"popularidad": 2,
		"rating": "9, 13, 19, 15, 5, 3"
	},
	{
		"nombre": "ligula elit, pretium",
		"duracion": 141,
		"autor": "Kuame Thornton",
		"generos": "Jazz",
		"popularidad": 5,
		"rating": "17, 9"
	},
	{
		"nombre": "rhoncus. Nullam velit",
		"duracion": 162,
		"autor": "Gareth Hall",
		"generos": "Jazz Blues",
		"popularidad": 7,
		"rating": "13, 3, 19, 1, 17, 15, 7, 11, 9"
	},
	{
		"nombre": "nostra,",
		"duracion": 31,
		"autor": "Ulla Graham",
		"generos": "Rock Country",
		"popularidad": 7,
		"rating": "13, 3, 7, 19, 17, 1, 15, 9, 5"
	},
	{
		"nombre": "interdum ligula eu",
		"duracion": 100,
		"autor": "Lawrence Valenzuela",
		"generos": "Disco Techno",
		"popularidad": 4,
		"rating": "3, 7"
	},
	{
		"nombre": "eros. Proin ultrices.",
		"duracion": 177,
		"autor": "Avram Gates",
		"generos": "Jazz Blues",
		"popularidad": 2,
		"rating": "17, 13, 7, 15, 9, 11, 5, 3, 19, 1"
	},
	{
		"nombre": "ligula. Nullam",
		"duracion": 138,
		"autor": "Flavia Ochoa",
		"generos": "Country Disco Techno",
		"popularidad": 2,
		"rating": "13, 17, 9"
	},
	{
		"nombre": "Nulla facilisi.",
		"duracion": 29,
		"autor": "Halee Neal",
		"generos": "Blues Góspel Soul",
		"popularidad": 5,
		"rating": "17, 1, 5, 3, 11"
	},
	{
		"nombre": "nisl. Quisque",
		"duracion": 82,
		"autor": "Dora Nelson",
		"generos": "Jazz",
		"popularidad": 7,
		"rating": "19, 11, 13, 1, 5, 15"
	},
	{
		"nombre": "ornare",
		"duracion": 139,
		"autor": "Dorian Jensen",
		"generos": "Blues",
		"popularidad": 2,
		"rating": "9, 7, 1"
	},
	{
		"nombre": "dui",
		"duracion": 104,
		"autor": "Ifeoma Rowland",
		"generos": "Country",
		"popularidad": 0,
		"rating": "5, 7"
	},
	{
		"nombre": "lectus quis",
		"duracion": 114,
		"autor": "Nolan Gay",
		"generos": "Pop Rock Country",
		"popularidad": 3,
		"rating": "15, 11, 19, 7"
	},
	{
		"nombre": "Vivamus euismod urna.",
		"duracion": 21,
		"autor": "Raymond Jackson",
		"generos": "Blues Góspel Soul",
		"popularidad": 9,
		"rating": "1, 3, 9"
	},
	{
		"nombre": "aliquet, metus",
		"duracion": 60,
		"autor": "Bevis Smith",
		"generos": "Soul Pop Rock",
		"popularidad": 2,
		"rating": "5, 11"
	},
	{
		"nombre": "Donec sollicitudin",
		"duracion": 87,
		"autor": "Indira Mccullough",
		"generos": "Góspel",
		"popularidad": 6,
		"rating": "5, 19, 11, 1, 3, 15, 7, 9"
	},
	{
		"nombre": "Vestibulum ante ipsum",
		"duracion": 112,
		"autor": "Chancellor Hopper",
		"generos": "Góspel Soul Pop",
		"popularidad": 3,
		"rating": "17, 9, 7, 19"
	},
	{
		"nombre": "euismod mauris eu",
		"duracion": 18,
		"autor": "Zoe Cooke",
		"generos": "Jazz Blues Góspel",
		"popularidad": 2,
		"rating": "1, 13, 11, 17, 15, 7, 19, 3"
	},
	{
		"nombre": "faucibus orci luctus",
		"duracion": 89,
		"autor": "Igor Hodge",
		"generos": "Soul Pop",
		"popularidad": 1,
		"rating": "7, 13, 3"
	},
	{
		"nombre": "Proin ultrices. Duis",
		"duracion": 19,
		"autor": "Reece Franco",
		"generos": "Soul",
		"popularidad": 2,
		"rating": "15, 9, 11, 7, 1, 5, 17, 3, 19"
	},
	{
		"nombre": "Praesent luctus.",
		"duracion": 95,
		"autor": "Zachary Foster",
		"generos": "Pop Rock",
		"popularidad": 8,
		"rating": "9, 15, 1, 11"
	},
	{
		"nombre": "sociosqu ad litora",
		"duracion": 19,
		"autor": "Dolan Shaffer",
		"generos": "Pop Rock",
		"popularidad": 1,
		"rating": "3, 17, 13"
	},
	{
		"nombre": "Proin",
		"duracion": 141,
		"autor": "Alvin Finley",
		"generos": "Jazz Blues",
		"popularidad": 0,
		"rating": "1, 7"
	},
	{
		"nombre": "quam quis",
		"duracion": 36,
		"autor": "Preston Bryan",
		"generos": "Jazz Blues Góspel",
		"popularidad": 6,
		"rating": "19, 17, 3, 11, 7, 15, 5"
	},
	{
		"nombre": "vitae odio",
		"duracion": 141,
		"autor": "Vaughan West",
		"generos": "Rock Country",
		"popularidad": 4,
		"rating": "9, 19, 17"
	},
	{
		"nombre": "elit, a feugiat",
		"duracion": 44,
		"autor": "Shelly Mcdonald",
		"generos": "Techno Hip-Hop",
		"popularidad": 6,
		"rating": "13, 5, 7, 19"
	},
	{
		"nombre": "elit fermentum",
		"duracion": 82,
		"autor": "Fredericka Roberts",
		"generos": "Techno Hip-Hop",
		"popularidad": 3,
		"rating": "1, 17, 5, 9, 13"
	},
	{
		"nombre": "ornare. Fusce mollis.",
		"duracion": 116,
		"autor": "Patricia Ellison",
		"generos": "Góspel Soul Pop",
		"popularidad": 4,
		"rating": "13, 5, 1, 3, 15, 19"
	},
	{
		"nombre": "tellus lorem",
		"duracion": 169,
		"autor": "Lisandra Fowler",
		"generos": "Blues Góspel",
		"popularidad": 5,
		"rating": "17, 19, 1, 5, 9, 7"
	},
	{
		"nombre": "iaculis odio. Nam",
		"duracion": 157,
		"autor": "Hope Bright",
		"generos": "Rock Country Disco",
		"popularidad": 3,
		"rating": "15, 7, 5, 13, 9, 1"
	},
	{
		"nombre": "eget",
		"duracion": 100,
		"autor": "Alexis Caldwell",
		"generos": "Jazz Blues",
		"popularidad": 8,
		"rating": "17, 13, 9, 1, 11, 5, 3, 15, 19, 7"
	},
	{
		"nombre": "adipiscing. Mauris",
		"duracion": 134,
		"autor": "Phyllis Pittman",
		"generos": "Góspel",
		"popularidad": 7,
		"rating": "19, 3, 7"
	},
	{
		"nombre": "risus, at fringilla",
		"duracion": 33,
		"autor": "Bertha Pacheco",
		"generos": "Techno",
		"popularidad": 2,
		"rating": "7, 9"
	},
	{
		"nombre": "cursus,",
		"duracion": 112,
		"autor": "Lillith Jones",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"rating": "1, 17, 7"
	},
	{
		"nombre": "dolor egestas",
		"duracion": 29,
		"autor": "Bruce Moss",
		"generos": "Clásica Jazz Blues",
		"popularidad": 1,
		"rating": "9, 19, 13, 7, 17"
	},
	{
		"nombre": "metus",
		"duracion": 1,
		"autor": "Thane Morrison",
		"generos": "Disco Techno",
		"popularidad": 10,
		"rating": 7
	},
	{
		"nombre": "imperdiet ornare.",
		"duracion": 11,
		"autor": "Ifeoma Moreno",
		"generos": "Country",
		"popularidad": 4,
		"rating": "9, 15, 19, 1, 5"
	},
	{
		"nombre": "ad litora torquent",
		"duracion": 142,
		"autor": "Miranda Nielsen",
		"generos": "Hip-Hop",
		"popularidad": 7,
		"rating": "5, 13, 11, 7, 1, 3, 15, 19, 9"
	},
	{
		"nombre": "Nulla facilisis.",
		"duracion": 160,
		"autor": "Bert Tyler",
		"generos": "Techno",
		"popularidad": 3,
		"rating": "17, 9, 7, 5, 13"
	},
	{
		"nombre": "massa.",
		"duracion": 126,
		"autor": "Yoshi Anthony",
		"generos": "Hip-Hop Metal",
		"popularidad": 6,
		"rating": "17, 15, 3, 11, 9, 19"
	},
	{
		"nombre": "urna.",
		"duracion": 44,
		"autor": "Marshall Wiley",
		"generos": "Techno Hip-Hop",
		"popularidad": 2,
		"rating": "13, 5, 3, 9, 15, 7, 19"
	},
	{
		"nombre": "nonummy",
		"duracion": 74,
		"autor": "Halee Contreras",
		"generos": "Pop Rock Country",
		"popularidad": 3,
		"rating": "1, 19, 3, 17, 11, 15, 7, 9"
	},
	{
		"nombre": "fringilla",
		"duracion": 0,
		"autor": "Marshall Quinn",
		"generos": "Country Disco",
		"popularidad": 6,
		"rating": "1, 13, 15, 9, 5, 17, 19, 7, 3"
	},
	{
		"nombre": "elit pede,",
		"duracion": 111,
		"autor": "Lana Benton",
		"generos": "Jazz Blues Góspel",
		"popularidad": 5,
		"rating": "13, 3, 17, 15, 7, 19, 5, 1, 11, 9"
	},
	{
		"nombre": "fermentum metus.",
		"duracion": 89,
		"autor": "Hayley Drake",
		"generos": "Soul Pop",
		"popularidad": 10,
		"rating": "15, 17, 7, 5, 13, 3, 1, 9, 19, 11"
	},
	{
		"nombre": "Cras dolor dolor,",
		"duracion": 134,
		"autor": "Palmer Mcmillan",
		"generos": "Techno",
		"popularidad": 7,
		"rating": "17, 3, 7, 19, 1, 11, 9"
	},
	{
		"nombre": "tortor, dictum eu,",
		"duracion": 177,
		"autor": "Wang Hayes",
		"generos": "Góspel",
		"popularidad": 7,
		"rating": "9, 7, 3, 19, 17"
	},
	{
		"nombre": "sem",
		"duracion": 98,
		"autor": "Chiquita Williams",
		"generos": "Techno Hip-Hop",
		"popularidad": 1,
		"rating": "7, 3, 9, 17, 13, 1, 15"
	},
	{
		"nombre": "ac metus",
		"duracion": 34,
		"autor": "Dennis Ray",
		"generos": "Clásica Jazz Blues",
		"popularidad": 2,
		"rating": "15, 1, 3, 5, 7, 9"
	},
	{
		"nombre": "vestibulum nec,",
		"duracion": 145,
		"autor": "Paula Potts",
		"generos": "Country Disco",
		"popularidad": 1,
		"rating": "5, 1, 15, 19, 9"
	},
	{
		"nombre": "neque sed",
		"duracion": 23,
		"autor": "Haviva Sherman",
		"generos": "Techno Hip-Hop",
		"popularidad": 2,
		"rating": "7, 3"
	},
	{
		"nombre": "Mauris vel",
		"duracion": 170,
		"autor": "Noah Knox",
		"generos": "Disco Techno",
		"popularidad": 7,
		"rating": "3, 17, 15"
	},
	{
		"nombre": "aliquet molestie",
		"duracion": 170,
		"autor": "Calvin Kennedy",
		"generos": "Góspel Soul Pop",
		"popularidad": 2,
		"rating": "7, 19, 1, 11, 13"
	},
	{
		"nombre": "a",
		"duracion": 122,
		"autor": "Drew Randall",
		"generos": "Clásica Jazz Blues",
		"popularidad": 10,
		"rating": "7, 17, 13, 19, 1"
	},
	{
		"nombre": "Donec fringilla.",
		"duracion": 13,
		"autor": "Malcolm Riddle",
		"generos": "Rock Country",
		"popularidad": 6,
		"rating": "19, 1"
	},
	{
		"nombre": "ac, eleifend vitae,",
		"duracion": 89,
		"autor": "Julie Gould",
		"generos": "Country",
		"popularidad": 6,
		"rating": "19, 9, 13, 15, 7, 5"
	},
	{
		"nombre": "ipsum. Suspendisse sagittis.",
		"duracion": 96,
		"autor": "Kane Alston",
		"generos": "Soul",
		"popularidad": 9,
		"rating": "15, 13, 1, 7, 19, 3, 11, 17, 5, 9"
	},
	{
		"nombre": "ligula. Donec",
		"duracion": 76,
		"autor": "Dolan Johnston",
		"generos": "Hip-Hop",
		"popularidad": 8,
		"rating": "9, 19, 7, 13"
	},
	{
		"nombre": "vulputate mauris",
		"duracion": 105,
		"autor": "Harriet Morton",
		"generos": "Soul Pop Rock",
		"popularidad": 6,
		"rating": 19
	},
	{
		"nombre": "at",
		"duracion": 43,
		"autor": "Jaquelyn Valencia",
		"generos": "Jazz Blues",
		"popularidad": 0,
		"rating": "19, 1"
	},
	{
		"nombre": "tellus. Phasellus",
		"duracion": 28,
		"autor": "Lillith Weber",
		"generos": "Techno Hip-Hop",
		"popularidad": 3,
		"rating": "15, 1, 19, 7, 11, 17, 5"
	},
	{
		"nombre": "imperdiet",
		"duracion": 145,
		"autor": "Kathleen Jacobs",
		"generos": "Pop Rock",
		"popularidad": 9,
		"rating": "11, 7, 19, 15, 3, 9, 13"
	},
	{
		"nombre": "enim, sit",
		"duracion": 36,
		"autor": "Giacomo Mclean",
		"generos": "Rock Country",
		"popularidad": 1,
		"rating": "3, 15, 19, 13, 17"
	},
	{
		"nombre": "auctor",
		"duracion": 72,
		"autor": "Ciara Pennington",
		"generos": "Blues Góspel",
		"popularidad": 2,
		"rating": "15, 9, 5, 19, 11, 1, 13, 3, 17, 7"
	},
	{
		"nombre": "adipiscing lacus.",
		"duracion": 124,
		"autor": "Jarrod Conrad",
		"generos": "Góspel Soul",
		"popularidad": 8,
		"rating": "17, 7, 3"
	},
	{
		"nombre": "Nulla facilisis. Suspendisse",
		"duracion": 28,
		"autor": "Alvin Glass",
		"generos": "Country",
		"popularidad": 7,
		"rating": "15, 7"
	},
	{
		"nombre": "dolor.",
		"duracion": 65,
		"autor": "Destiny Patel",
		"generos": "Soul Pop Rock",
		"popularidad": 6,
		"rating": "7, 11, 1, 9, 17, 3, 15, 19, 5"
	},
	{
		"nombre": "orci, consectetuer",
		"duracion": 42,
		"autor": "Gannon Lang",
		"generos": "Góspel Soul",
		"popularidad": 5,
		"rating": "5, 17, 19, 15, 3, 11, 13, 9"
	},
	{
		"nombre": "cursus a,",
		"duracion": 28,
		"autor": "Burke Potter",
		"generos": "Disco Techno Hip-Hop",
		"popularidad": 3,
		"rating": "19, 1, 15, 11, 13, 5, 3"
	},
	{
		"nombre": "faucibus orci",
		"duracion": 173,
		"autor": "Elijah Romero",
		"generos": "Pop Rock",
		"popularidad": 2,
		"rating": "17, 19, 9, 7, 15, 3, 5, 13, 11, 1"
	},
	{
		"nombre": "faucibus lectus,",
		"duracion": 68,
		"autor": "Reese Sims",
		"generos": "Jazz Blues Góspel",
		"popularidad": 6,
		"rating": "15, 11, 17, 19, 5, 9, 1"
	},
	{
		"nombre": "Donec at",
		"duracion": 34,
		"autor": "Regan Schwartz",
		"generos": "Pop",
		"popularidad": 10,
		"rating": "17, 5, 1, 7, 3, 19, 9"
	},
	{
		"nombre": "enim. Nunc",
		"duracion": 4,
		"autor": "Stephen Sharpe",
		"generos": "Rock",
		"popularidad": 7,
		"rating": "1, 9, 13, 17, 15, 5, 3"
	},
	{
		"nombre": "ligula. Donec luctus",
		"duracion": 17,
		"autor": "Zeus Ball",
		"generos": "Jazz Blues Góspel",
		"popularidad": 2,
		"rating": "19, 3, 1, 7, 5, 15, 9"
	},
	{
		"nombre": "scelerisque dui. Suspendisse",
		"duracion": 172,
		"autor": "Chaim Mathis",
		"generos": "Clásica",
		"popularidad": 1,
		"rating": "15, 11, 17, 19, 7"
	},
	{
		"nombre": "malesuada",
		"duracion": 150,
		"autor": "Arthur Sharpe",
		"generos": "Country Disco",
		"popularidad": 8,
		"rating": "9, 15"
	},
	{
		"nombre": "mauris sagittis",
		"duracion": 90,
		"autor": "Vernon Duke",
		"generos": "Jazz Blues Góspel",
		"popularidad": 8,
		"rating": "1, 9, 13, 17, 15"
	},
	{
		"nombre": "ultrices. Vivamus rhoncus.",
		"duracion": 97,
		"autor": "Sara Crane",
		"generos": "Country Disco",
		"popularidad": 7,
		"rating": "9, 5, 11, 7, 17, 3, 13, 1"
	},
	{
		"nombre": "malesuada vel, convallis",
		"duracion": 87,
		"autor": "Nehru Brady",
		"generos": "Rock Country",
		"popularidad": 9,
		"rating": "11, 3, 15, 7, 9"
	},
	{
		"nombre": "venenatis a,",
		"duracion": 114,
		"autor": "Kelsie Oneil",
		"generos": "Blues",
		"popularidad": 1,
		"rating": "1, 3, 15, 19, 13, 11, 9, 17, 7"
	},
	{
		"nombre": "Pellentesque tincidunt",
		"duracion": 128,
		"autor": "Nolan Mcdowell",
		"generos": "Góspel Soul",
		"popularidad": 4,
		"rating": "3, 9, 15, 17, 7"
	},
	{
		"nombre": "Sed eget lacus.",
		"duracion": 138,
		"autor": "Lana Dickson",
		"generos": "Soul Pop",
		"popularidad": 6,
		"rating": 15
	},
	{
		"nombre": "Duis ac arcu.",
		"duracion": 34,
		"autor": "Caldwell Foley",
		"generos": "Hip-Hop Metal",
		"popularidad": 8,
		"rating": "19, 15, 1, 17, 7, 11, 5, 13, 9"
	},
	{
		"nombre": "Nunc mauris",
		"duracion": 44,
		"autor": "Hayden Everett",
		"generos": "Techno Hip-Hop",
		"popularidad": 10,
		"rating": "9, 5, 15, 17"
	},
	{
		"nombre": "tempus",
		"duracion": 144,
		"autor": "Christopher Payne",
		"generos": "Soul Pop Rock",
		"popularidad": 5,
		"rating": "9, 5, 3, 7, 11, 15, 17"
	},
	{
		"nombre": "imperdiet dictum",
		"duracion": 69,
		"autor": "Macon Reyes",
		"generos": "Soul Pop",
		"popularidad": 1,
		"rating": "3, 19, 17, 15, 1"
	},
	{
		"nombre": "tincidunt orci quis",
		"duracion": 55,
		"autor": "Sylvester Livingston",
		"generos": "Clásica Jazz",
		"popularidad": 6,
		"rating": "3, 7, 11"
	},
	{
		"nombre": "porta elit, a",
		"duracion": 15,
		"autor": "Aimee Gilbert",
		"generos": "Rock Country Disco",
		"popularidad": 3,
		"rating": "5, 1"
	},
	{
		"nombre": "dictum eu,",
		"duracion": 114,
		"autor": "Maia Casey",
		"generos": "Rock Country",
		"popularidad": 5,
		"rating": "17, 13, 15, 11, 5"
	},
	{
		"nombre": "diam eu",
		"duracion": 108,
		"autor": "Imogene Oliver",
		"generos": "Techno",
		"popularidad": 0,
		"rating": "3, 11, 1"
	},
	{
		"nombre": "vulputate, risus",
		"duracion": 156,
		"autor": "Dolan Foley",
		"generos": "Country Disco",
		"popularidad": 4,
		"rating": "13, 17"
	},
	{
		"nombre": "mauris. Integer",
		"duracion": 105,
		"autor": "Kibo Morrison",
		"generos": "Blues Góspel",
		"popularidad": 4,
		"rating": "17, 19, 7, 3, 5"
	},
	{
		"nombre": "diam vel arcu.",
		"duracion": 3,
		"autor": "Shay Roach",
		"generos": "Country Disco",
		"popularidad": 0,
		"rating": "3, 15, 5, 19, 1"
	},
	{
		"nombre": "sed",
		"duracion": 143,
		"autor": "Tanya Harmon",
		"generos": "Hip-Hop",
		"popularidad": 5,
		"rating": "19, 11, 1, 7, 15, 17, 5, 13"
	},
	{
		"nombre": "quis",
		"duracion": 34,
		"autor": "Allen Nicholson",
		"generos": "Soul Pop",
		"popularidad": 8,
		"rating": "9, 3, 19, 13, 1, 7"
	},
	{
		"nombre": "non lorem vitae",
		"duracion": 73,
		"autor": "Heidi Haley",
		"generos": "Techno",
		"popularidad": 3,
		"rating": "11, 15"
	},
	{
		"nombre": "at risus. Nunc",
		"duracion": 26,
		"autor": "Mason Kennedy",
		"generos": "Disco Techno",
		"popularidad": 9,
		"rating": "19, 1"
	},
	{
		"nombre": "elementum, dui",
		"duracion": 141,
		"autor": "Zena Rodriquez",
		"generos": "Rock Country Disco",
		"popularidad": 3,
		"rating": "5, 15, 9, 11, 7, 17, 1, 13, 19, 3"
	},
	{
		"nombre": "consequat purus.",
		"duracion": 43,
		"autor": "Noel Ayers",
		"generos": "Góspel Soul",
		"popularidad": 3,
		"rating": "5, 11, 7, 15, 17, 1, 19, 3, 9"
	},
	{
		"nombre": "interdum libero dui",
		"duracion": 151,
		"autor": "Marsden Clark",
		"generos": "Pop",
		"popularidad": 6,
		"rating": "9, 5, 15, 17, 11, 7, 19, 3, 13, 1"
	},
	{
		"nombre": "cubilia Curae",
		"duracion": 9,
		"autor": "Emerson Bird",
		"generos": "Country Disco",
		"popularidad": 4,
		"rating": "3, 11, 13, 1, 5, 19, 9, 15"
	},
	{
		"nombre": "justo eu arcu.",
		"duracion": 83,
		"autor": "Nelle Harrell",
		"generos": "Jazz Blues Góspel",
		"popularidad": 6,
		"rating": "5, 17, 19, 7, 3, 11, 9, 1"
	},
	{
		"nombre": "Maecenas malesuada",
		"duracion": 153,
		"autor": "Harrison Kinney",
		"generos": "Country Disco Techno",
		"popularidad": 10,
		"rating": "15, 19"
	},
	{
		"nombre": "quis, pede.",
		"duracion": 157,
		"autor": "Noel Macdonald",
		"generos": "Rock",
		"popularidad": 7,
		"rating": "11, 7, 15"
	},
	{
		"nombre": "vehicula. Pellentesque tincidunt",
		"duracion": 81,
		"autor": "Wyoming Strong",
		"generos": "Disco Techno",
		"popularidad": 5,
		"rating": "3, 13, 17, 15, 7, 11"
	},
	{
		"nombre": "fringilla est.",
		"duracion": 89,
		"autor": "Victor Weiss",
		"generos": "Soul Pop",
		"popularidad": 5,
		"rating": "1, 7, 17"
	},
	{
		"nombre": "in",
		"duracion": 49,
		"autor": "Alexa Fuentes",
		"generos": "Country Disco",
		"popularidad": 1,
		"rating": "17, 15, 3, 11, 7, 1, 13, 9"
	},
	{
		"nombre": "erat vitae",
		"duracion": 124,
		"autor": "Nicole Dillon",
		"generos": "Blues Góspel",
		"popularidad": 8,
		"rating": "17, 5, 9, 7, 3, 15, 11"
	},
	{
		"nombre": "Vivamus",
		"duracion": 61,
		"autor": "Germaine Walters",
		"generos": "Góspel",
		"popularidad": 4,
		"rating": "7, 17, 15"
	},
	{
		"nombre": "vitae risus. Duis",
		"duracion": 142,
		"autor": "Bert Estes",
		"generos": "Soul Pop Rock",
		"popularidad": 6,
		"rating": "3, 11, 5, 7, 15"
	},
	{
		"nombre": "ornare,",
		"duracion": 123,
		"autor": "Karyn Bullock",
		"generos": "Góspel Soul",
		"popularidad": 3,
		"rating": "15, 19, 5, 3, 17, 7"
	},
	{
		"nombre": "natoque",
		"duracion": 106,
		"autor": "Fiona Fuller",
		"generos": "Hip-Hop Metal",
		"popularidad": 1,
		"rating": "11, 13"
	},
	{
		"nombre": "odio tristique",
		"duracion": 15,
		"autor": "Jeremy Henson",
		"generos": "Soul Pop",
		"popularidad": 4,
		"rating": "13, 3, 5, 9"
	},
	{
		"nombre": "neque sed dictum",
		"duracion": 107,
		"autor": "Jamalia Riley",
		"generos": "Soul Pop Rock",
		"popularidad": 6,
		"rating": "17, 9, 1"
	}
]

for reproduccion in reproducciones:
    cancion = canciones[random.randint(0, len(canciones) - 1)]
    usuario = usuarios[random.randint(0, len(usuarios) - 1)]
    reproduccion["usuario"] = usuario
    reproduccion["cancion"] = cancion["nombre"]

for cancion in canciones:
	if isinstance(cancion["rating"], int):
		cancion["rating"] = [cancion["rating"]]
	else:
		rating = cancion["rating"].split(", ")
	cancion["rating"] = rating


with open('reproducciones_final.json', 'w') as file:
    json.dump(reproducciones, file, indent=4)
    file.close

with open('canciones_final.json', 'w') as file:
	json.dump(canciones, file, indent=4)
	file.close