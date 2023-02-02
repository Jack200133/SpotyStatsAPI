import random
import json

usuarios = [
	{
		"nombre": "Todd Byers",
		"edad": 17,
		"pais": "Ireland",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Emery Cohen",
		"edad": 65,
		"pais": "Belgium",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Martha Jensen",
		"edad": 64,
		"pais": "United Kingdom",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Willow Thompson",
		"edad": 42,
		"pais": "Chile",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Lareina Patton",
		"edad": 14,
		"pais": "Nigeria",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Amethyst Fernandez",
		"edad": 50,
		"pais": "Indonesia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Xenos Daugherty",
		"edad": 51,
		"pais": "Nigeria",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Wallace Turner",
		"edad": 26,
		"pais": "China",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Chase Goodman",
		"edad": 54,
		"pais": "Canada",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Colorado Quinn",
		"edad": 25,
		"pais": "India",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Rahim Jordan",
		"edad": 45,
		"pais": "Poland",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Ursa Wallace",
		"edad": 46,
		"pais": "Germany",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Rashad Yates",
		"edad": 29,
		"pais": "Singapore",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Moses Parsons",
		"edad": 0,
		"pais": "Indonesia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Maxwell Soto",
		"edad": 35,
		"pais": "Ireland",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Buffy Warren",
		"edad": 18,
		"pais": "Pakistan",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Yen Whitfield",
		"edad": 46,
		"pais": "Indonesia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Yoshio Dickson",
		"edad": 22,
		"pais": "Indonesia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Fritz Langley",
		"edad": 45,
		"pais": "Belgium",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Kareem Mclean",
		"edad": 16,
		"pais": "Vietnam",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Cairo Perry",
		"edad": 12,
		"pais": "Sweden",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Ramona Mcpherson",
		"edad": 65,
		"pais": "New Zealand",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Fritz Pena",
		"edad": 40,
		"pais": "India",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Amena Neal",
		"edad": 41,
		"pais": "Philippines",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Hiram Quinn",
		"edad": 41,
		"pais": "South Korea",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Reese Cherry",
		"edad": 35,
		"pais": "Chile",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Darrel Velasquez",
		"edad": 42,
		"pais": "Nigeria",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Penelope Nieves",
		"edad": 51,
		"pais": "United States",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Noel Duncan",
		"edad": 15,
		"pais": "Austria",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Cade Hurley",
		"edad": 62,
		"pais": "Costa Rica",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Allen Cross",
		"edad": 27,
		"pais": "Costa Rica",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Aileen Salazar",
		"edad": 32,
		"pais": "Indonesia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Nolan Crane",
		"edad": 30,
		"pais": "Poland",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hakeem Brennan",
		"edad": 57,
		"pais": "Vietnam",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Hector Curtis",
		"edad": 60,
		"pais": "Peru",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Tobias Buckner",
		"edad": 27,
		"pais": "China",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Ferris Calderon",
		"edad": 33,
		"pais": "Germany",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Tyler Pate",
		"edad": 24,
		"pais": "Norway",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Meghan Russell",
		"edad": 6,
		"pais": "Norway",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Bert Giles",
		"edad": 43,
		"pais": "Sweden",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Anika Underwood",
		"edad": 51,
		"pais": "Ukraine",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Gavin Buck",
		"edad": 4,
		"pais": "United Kingdom",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Fuller Ellison",
		"edad": 0,
		"pais": "France",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Dai Frost",
		"edad": 4,
		"pais": "Ukraine",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Ali Alexander",
		"edad": 36,
		"pais": "Poland",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Justin Finley",
		"edad": 43,
		"pais": "Mexico",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Phyllis Emerson",
		"edad": 22,
		"pais": "New Zealand",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Felicia Ayers",
		"edad": 30,
		"pais": "Indonesia",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Maryam Weber",
		"edad": 63,
		"pais": "Norway",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Linus Nichols",
		"edad": 27,
		"pais": "Pakistan",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Raphael Mayer",
		"edad": 1,
		"pais": "Costa Rica",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Chastity Mcdaniel",
		"edad": 37,
		"pais": "Canada",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Raven Gibbs",
		"edad": 29,
		"pais": "South Korea",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Hyacinth Atkinson",
		"edad": 41,
		"pais": "France",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Brendan Justice",
		"edad": 2,
		"pais": "New Zealand",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Bruno Weaver",
		"edad": 21,
		"pais": "South Africa",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Matthew Dickerson",
		"edad": 49,
		"pais": "Mexico",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Lester Drake",
		"edad": 50,
		"pais": "Norway",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Mark Vincent",
		"edad": 37,
		"pais": "United Kingdom",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Howard Avery",
		"edad": 11,
		"pais": "Austria",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Calista Rios",
		"edad": 9,
		"pais": "Netherlands",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Arden Stafford",
		"edad": 3,
		"pais": "Spain",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Mallory Robertson",
		"edad": 9,
		"pais": "Ireland",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Emery Barron",
		"edad": 9,
		"pais": "Ukraine",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Wing Stephenson",
		"edad": 30,
		"pais": "Austria",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Sonia Riggs",
		"edad": 67,
		"pais": "Italy",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Otto Sandoval",
		"edad": 48,
		"pais": "Indonesia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Todd Aguirre",
		"edad": 11,
		"pais": "United Kingdom",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Jade Salas",
		"edad": 59,
		"pais": "India",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Hayes Kim",
		"edad": 24,
		"pais": "Norway",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Vera Dillard",
		"edad": 22,
		"pais": "Germany",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Price Mckinney",
		"edad": 45,
		"pais": "Netherlands",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Tanner Gilbert",
		"edad": 4,
		"pais": "Ireland",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Urielle Valentine",
		"edad": 43,
		"pais": "Austria",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Brock Beach",
		"edad": 43,
		"pais": "United Kingdom",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Lareina Hines",
		"edad": 3,
		"pais": "Australia",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Wanda Holman",
		"edad": 54,
		"pais": "Pakistan",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Mary Ruiz",
		"edad": 69,
		"pais": "Colombia",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Jonah Gould",
		"edad": 15,
		"pais": "Ukraine",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Noble Lamb",
		"edad": 27,
		"pais": "Ireland",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Demetrius Le",
		"edad": 8,
		"pais": "Costa Rica",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Steel Rasmussen",
		"edad": 54,
		"pais": "Belgium",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hunter Robertson",
		"edad": 51,
		"pais": "Netherlands",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Blythe Browning",
		"edad": 50,
		"pais": "Austria",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Kelly Rivera",
		"edad": 8,
		"pais": "Singapore",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Ruby Saunders",
		"edad": 17,
		"pais": "Belgium",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Martena Melendez",
		"edad": 25,
		"pais": "Costa Rica",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Yoshio Ward",
		"edad": 41,
		"pais": "Costa Rica",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Channing Leon",
		"edad": 14,
		"pais": "Belgium",
		"suscripcion": 0,
		"genero": "Femenino"
	},
	{
		"nombre": "Lionel Cole",
		"edad": 35,
		"pais": "France",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hillary Barton",
		"edad": 30,
		"pais": "Pakistan",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Kasper Edwards",
		"edad": 55,
		"pais": "United Kingdom",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Veronica Nash",
		"edad": 3,
		"pais": "Ukraine",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Kareem Peterson",
		"edad": 20,
		"pais": "Ireland",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Macey Knowles",
		"edad": 42,
		"pais": "Poland",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "Harrison Mcintosh",
		"edad": 6,
		"pais": "Australia",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Hedda Barber",
		"edad": 30,
		"pais": "Germany",
		"suscripcion": 1,
		"genero": "Femenino"
	},
	{
		"nombre": "Carter Buckley",
		"edad": 19,
		"pais": "South Africa",
		"suscripcion": 0,
		"genero": "Masculino"
	},
	{
		"nombre": "India Hopkins",
		"edad": 60,
		"pais": "Ukraine",
		"suscripcion": 1,
		"genero": "Masculino"
	},
	{
		"nombre": "Grant Horton",
		"edad": 37,
		"pais": "Ireland",
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
		"nombre": "non, egestas a,",
		"duracion": 61,
		"autor": "Vincent Witt",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 4,
		"danzabilidad": 5
	},
	{
		"nombre": "mollis lectus pede",
		"duracion": 50,
		"autor": "Jessamine Nicholson",
		"generos": "Hip-Hop",
		"popularidad": 0,
		"danzabilidad": 2
	},
	{
		"nombre": "sem. Pellentesque ut",
		"duracion": 175,
		"autor": "Cara Page",
		"generos": "Góspel Blues Country",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "ultricies sem magna",
		"duracion": 34,
		"autor": "Rebekah Lindsey",
		"generos": "Rock Pop Clásica Bachata",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "enim non nisi.",
		"duracion": 115,
		"autor": "Colorado Sykes",
		"generos": "Rock Pop",
		"popularidad": 5,
		"danzabilidad": 1
	},
	{
		"nombre": "vitae semper egestas,",
		"duracion": 33,
		"autor": "Reese Pacheco",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "Vivamus rhoncus. Donec",
		"duracion": 17,
		"autor": "Brynne Conrad",
		"generos": "Country Disco Techno",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "urna. Nullam lobortis",
		"duracion": 33,
		"autor": "Darius Baker",
		"generos": "Blues Country Disco",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "massa. Integer vitae",
		"duracion": 6,
		"autor": "Rhiannon Chase",
		"generos": "K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 0
	},
	{
		"nombre": "sed, facilisis vitae,",
		"duracion": 162,
		"autor": "Melanie Holt",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "sed turpis nec",
		"duracion": 106,
		"autor": "Maryam Peters",
		"generos": "Góspel Blues Country",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "Mauris vestibulum, neque",
		"duracion": 25,
		"autor": "Moana Hale",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 10,
		"danzabilidad": 2
	},
	{
		"nombre": "pede. Cum sociis",
		"duracion": 156,
		"autor": "Imelda Cantu",
		"generos": "Bachata Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 1
	},
	{
		"nombre": "fames ac turpis",
		"duracion": 158,
		"autor": "Ryder England",
		"generos": "Hip-Hop Salsa",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "auctor. Mauris vel",
		"duracion": 48,
		"autor": "Helen Thomas",
		"generos": "Bachata Raeguetton",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "sit amet ante.",
		"duracion": 16,
		"autor": "Maris Curtis",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 10,
		"danzabilidad": 0
	},
	{
		"nombre": "rutrum. Fusce dolor",
		"duracion": 40,
		"autor": "Ahmed Simmons",
		"generos": "K-pop Metal Jazz",
		"popularidad": 7,
		"danzabilidad": 8
	},
	{
		"nombre": "lacinia orci, consectetuer",
		"duracion": 169,
		"autor": "Conan Lancaster",
		"generos": "Country Disco",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "a felis ullamcorper",
		"duracion": 14,
		"autor": "Yasir Underwood",
		"generos": "Country",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "eget laoreet posuere,",
		"duracion": 124,
		"autor": "Kenneth Aguilar",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "at pretium aliquet,",
		"duracion": 173,
		"autor": "Mia Smith",
		"generos": "Salsa R&B",
		"popularidad": 5,
		"danzabilidad": 7
	},
	{
		"nombre": "tincidunt orci quis",
		"duracion": 58,
		"autor": "Zelda Walls",
		"generos": "Rock Pop Clásica",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "Vivamus euismod urna.",
		"duracion": 56,
		"autor": "Zena Sharp",
		"generos": "Salsa R&B K-pop",
		"popularidad": 0,
		"danzabilidad": 10
	},
	{
		"nombre": "arcu eu odio",
		"duracion": 6,
		"autor": "Ivor Chandler",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 0,
		"danzabilidad": 4
	},
	{
		"nombre": "Praesent eu nulla",
		"duracion": 172,
		"autor": "Martha Anderson",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "molestie sodales. Mauris",
		"duracion": 166,
		"autor": "Hashim Mason",
		"generos": "Hip-Hop Salsa",
		"popularidad": 0,
		"danzabilidad": 7
	},
	{
		"nombre": "dui lectus rutrum",
		"duracion": 154,
		"autor": "Eliana Nguyen",
		"generos": "Góspel",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "est tempor bibendum.",
		"duracion": 82,
		"autor": "Marsden Wall",
		"generos": "Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 3
	},
	{
		"nombre": "Nunc sed orci",
		"duracion": 161,
		"autor": "Ria Burton",
		"generos": "R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 7
	},
	{
		"nombre": "turpis. Nulla aliquet.",
		"duracion": 167,
		"autor": "Serina Myers",
		"generos": "R&B K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 8
	},
	{
		"nombre": "nec, diam. Duis",
		"duracion": 41,
		"autor": "Brady Huber",
		"generos": "Góspel Blues",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "justo nec ante.",
		"duracion": 76,
		"autor": "Karen Frazier",
		"generos": "Hip-Hop Salsa",
		"popularidad": 2,
		"danzabilidad": 8
	},
	{
		"nombre": "morbi tristique senectus",
		"duracion": 86,
		"autor": "Karina Paul",
		"generos": "Metal Jazz",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "Quisque libero lacus,",
		"duracion": 117,
		"autor": "Kennedy Pratt",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 2,
		"danzabilidad": 3
	},
	{
		"nombre": "et ultrices posuere",
		"duracion": 178,
		"autor": "Shelley Fleming",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 8,
		"danzabilidad": 6
	},
	{
		"nombre": "nulla at sem",
		"duracion": 75,
		"autor": "Yvonne Mclean",
		"generos": "K-pop Metal",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "lacinia vitae, sodales",
		"duracion": 113,
		"autor": "Ulysses Blair",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "penatibus et magnis",
		"duracion": 115,
		"autor": "Drew Underwood",
		"generos": "Metal Jazz",
		"popularidad": 10,
		"danzabilidad": 8
	},
	{
		"nombre": "at risus. Nunc",
		"duracion": 51,
		"autor": "Brody Haynes",
		"generos": "Techno Flamenco",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "Proin vel arcu",
		"duracion": 27,
		"autor": "Yvonne Rivera",
		"generos": "Bachata Raeguetton",
		"popularidad": 0,
		"danzabilidad": 5
	},
	{
		"nombre": "mus. Aenean eget",
		"duracion": 138,
		"autor": "Leigh Stanley",
		"generos": "Salsa",
		"popularidad": 1,
		"danzabilidad": 3
	},
	{
		"nombre": "egestas. Sed pharetra,",
		"duracion": 28,
		"autor": "Chiquita Lee",
		"generos": "Jazz Góspel",
		"popularidad": 2,
		"danzabilidad": 3
	},
	{
		"nombre": "tristique ac, eleifend",
		"duracion": 65,
		"autor": "Rogan Bryan",
		"generos": "Blues Country Disco Techno",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "eu odio tristique",
		"duracion": 147,
		"autor": "Keane Webster",
		"generos": "Flamenco",
		"popularidad": 10,
		"danzabilidad": 8
	},
	{
		"nombre": "magna. Lorem ipsum",
		"duracion": 33,
		"autor": "Noelle Hawkins",
		"generos": "Country Disco",
		"popularidad": 2,
		"danzabilidad": 4
	},
	{
		"nombre": "augue id ante",
		"duracion": 57,
		"autor": "Hadassah Phillips",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "egestas blandit. Nam",
		"duracion": 169,
		"autor": "Imogene Kidd",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "orci sem eget",
		"duracion": 120,
		"autor": "Harlan Nolan",
		"generos": "Blues",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "lorem vitae odio",
		"duracion": 66,
		"autor": "Herman Ayers",
		"generos": "Rock Pop Clásica",
		"popularidad": 4,
		"danzabilidad": 8
	},
	{
		"nombre": "quis lectus. Nullam",
		"duracion": 174,
		"autor": "Rigel Hunt",
		"generos": "Hip-Hop Salsa R&B",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "vel quam dignissim",
		"duracion": 22,
		"autor": "Ulric Kaufman",
		"generos": "Hip-Hop Salsa",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "nostra, per inceptos",
		"duracion": 159,
		"autor": "Rogan Vance",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 8,
		"danzabilidad": 0
	},
	{
		"nombre": "eu erat semper",
		"duracion": 45,
		"autor": "Chaim Contreras",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "odio. Nam interdum",
		"duracion": 179,
		"autor": "Cameron Randall",
		"generos": "Jazz Góspel Blues",
		"popularidad": 6,
		"danzabilidad": 3
	},
	{
		"nombre": "Quisque fringilla euismod",
		"duracion": 150,
		"autor": "Octavia Hamilton",
		"generos": "Pop Clásica",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "convallis erat, eget",
		"duracion": 103,
		"autor": "Sandra Middleton",
		"generos": "R&B K-pop",
		"popularidad": 5,
		"danzabilidad": 7
	},
	{
		"nombre": "elit. Curabitur sed",
		"duracion": 127,
		"autor": "Francis Alvarado",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 4,
		"danzabilidad": 10
	},
	{
		"nombre": "Vivamus sit amet",
		"duracion": 135,
		"autor": "Luke Collins",
		"generos": "Country Disco",
		"popularidad": 8,
		"danzabilidad": 4
	},
	{
		"nombre": "velit. Pellentesque ultricies",
		"duracion": 33,
		"autor": "Natalie Fulton",
		"generos": "Disco Techno",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "eleifend non, dapibus",
		"duracion": 78,
		"autor": "Melyssa O'Neill",
		"generos": "Pop Clásica",
		"popularidad": 10,
		"danzabilidad": 10
	},
	{
		"nombre": "cursus non, egestas",
		"duracion": 116,
		"autor": "Hilary Little",
		"generos": "Clásica Bachata",
		"popularidad": 0,
		"danzabilidad": 6
	},
	{
		"nombre": "tortor nibh sit",
		"duracion": 39,
		"autor": "Ivory Macdonald",
		"generos": "K-pop",
		"popularidad": 8,
		"danzabilidad": 4
	},
	{
		"nombre": "euismod mauris eu",
		"duracion": 116,
		"autor": "Bell Dawson",
		"generos": "Metal Jazz Góspel Blues Country",
		"popularidad": 6,
		"danzabilidad": 1
	},
	{
		"nombre": "Nulla tempor augue",
		"duracion": 38,
		"autor": "Finn Parker",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "tincidunt orci quis",
		"duracion": 28,
		"autor": "Ishmael Montgomery",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 3,
		"danzabilidad": 5
	},
	{
		"nombre": "Integer vulputate, risus",
		"duracion": 155,
		"autor": "Amity Dickerson",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "erat. Sed nunc",
		"duracion": 100,
		"autor": "Byron Noble",
		"generos": "Hip-Hop Salsa",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "Duis mi enim,",
		"duracion": 85,
		"autor": "Paul Burris",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 6
	},
	{
		"nombre": "felis, adipiscing fringilla,",
		"duracion": 124,
		"autor": "Charles Vance",
		"generos": "Jazz",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "Quisque libero lacus,",
		"duracion": 172,
		"autor": "Rigel Chang",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 10,
		"danzabilidad": 5
	},
	{
		"nombre": "justo sit amet",
		"duracion": 5,
		"autor": "Duncan Vincent",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 6,
		"danzabilidad": 2
	},
	{
		"nombre": "Sed auctor odio",
		"duracion": 170,
		"autor": "Yardley Frye",
		"generos": "Salsa",
		"popularidad": 10,
		"danzabilidad": 5
	},
	{
		"nombre": "metus facilisis lorem",
		"duracion": 54,
		"autor": "Malachi Garrett",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "neque tellus, imperdiet",
		"duracion": 28,
		"autor": "Demetrius Mckee",
		"generos": "R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "nonummy ipsum non",
		"duracion": 52,
		"autor": "Jorden Henry",
		"generos": "Hip-Hop Salsa R&B",
		"popularidad": 8,
		"danzabilidad": 8
	},
	{
		"nombre": "lorem eu metus.",
		"duracion": 18,
		"autor": "Fitzgerald Talley",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "in faucibus orci",
		"duracion": 109,
		"autor": "Ora Owen",
		"generos": "Metal",
		"popularidad": 5,
		"danzabilidad": 10
	},
	{
		"nombre": "ligula elit, pretium",
		"duracion": 22,
		"autor": "Nevada Contreras",
		"generos": "R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "et, commodo at,",
		"duracion": 135,
		"autor": "Levi Blankenship",
		"generos": "Metal Jazz Góspel Blues Country",
		"popularidad": 7,
		"danzabilidad": 9
	},
	{
		"nombre": "massa. Quisque porttitor",
		"duracion": 86,
		"autor": "Iris Houston",
		"generos": "Hip-Hop Salsa",
		"popularidad": 9,
		"danzabilidad": 2
	},
	{
		"nombre": "eros. Nam consequat",
		"duracion": 135,
		"autor": "Ciaran Torres",
		"generos": "Bachata Raeguetton Hip-Hop",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "nec, eleifend non,",
		"duracion": 158,
		"autor": "Beau Roman",
		"generos": "Salsa R&B K-pop",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "eros nec tellus.",
		"duracion": 87,
		"autor": "Brennan Dyer",
		"generos": "Góspel Blues",
		"popularidad": 7,
		"danzabilidad": 4
	},
	{
		"nombre": "libero nec ligula",
		"duracion": 56,
		"autor": "Carla Gordon",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "Mauris ut quam",
		"duracion": 37,
		"autor": "Abigail Witt",
		"generos": "Country Disco",
		"popularidad": 6,
		"danzabilidad": 7
	},
	{
		"nombre": "scelerisque dui. Suspendisse",
		"duracion": 4,
		"autor": "Orla Short",
		"generos": "Pop Clásica Bachata",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "velit eget laoreet",
		"duracion": 113,
		"autor": "Ishmael Graves",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "erat eget ipsum.",
		"duracion": 145,
		"autor": "Winter Farrell",
		"generos": "Salsa R&B",
		"popularidad": 6,
		"danzabilidad": 7
	},
	{
		"nombre": "orci quis lectus.",
		"duracion": 95,
		"autor": "Neville Meyers",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "vel sapien imperdiet",
		"duracion": 116,
		"autor": "Sarah Martinez",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "et netus et",
		"duracion": 168,
		"autor": "Zenaida Mcleod",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 8,
		"danzabilidad": 2
	},
	{
		"nombre": "aliquet odio. Etiam",
		"duracion": 49,
		"autor": "William Mcmahon",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 2,
		"danzabilidad": 0
	},
	{
		"nombre": "Morbi quis urna.",
		"duracion": 69,
		"autor": "Price Kemp",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 10,
		"danzabilidad": 8
	},
	{
		"nombre": "cursus. Integer mollis.",
		"duracion": 108,
		"autor": "Gregory Stone",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 8,
		"danzabilidad": 0
	},
	{
		"nombre": "fringilla, porttitor vulputate,",
		"duracion": 88,
		"autor": "Quynn Munoz",
		"generos": "Góspel Blues",
		"popularidad": 7,
		"danzabilidad": 8
	},
	{
		"nombre": "diam nunc, ullamcorper",
		"duracion": 123,
		"autor": "Leo Kirkland",
		"generos": "Blues Country Disco",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "eu tellus eu",
		"duracion": 37,
		"autor": "Leandra Dominguez",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "hendrerit id, ante.",
		"duracion": 105,
		"autor": "Kieran Brewer",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 5,
		"danzabilidad": 3
	},
	{
		"nombre": "risus a ultricies",
		"duracion": 118,
		"autor": "Calvin Ramos",
		"generos": "Rock Pop Clásica",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "arcu imperdiet ullamcorper.",
		"duracion": 101,
		"autor": "Xena Sears",
		"generos": "K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 5
	},
	{
		"nombre": "purus mauris a",
		"duracion": 103,
		"autor": "Rafael Olsen",
		"generos": "Country Disco Techno Flamenco",
		"popularidad": 3,
		"danzabilidad": 1
	},
	{
		"nombre": "nonummy ultricies ornare,",
		"duracion": 33,
		"autor": "Rhona Hyde",
		"generos": "Pop Clásica Bachata",
		"popularidad": 5,
		"danzabilidad": 10
	},
	{
		"nombre": "ac turpis egestas.",
		"duracion": 115,
		"autor": "Phoebe Wolfe",
		"generos": "Jazz",
		"popularidad": 6,
		"danzabilidad": 7
	},
	{
		"nombre": "vel, vulputate eu,",
		"duracion": 91,
		"autor": "Lamar Moore",
		"generos": "Jazz Góspel",
		"popularidad": 1,
		"danzabilidad": 8
	},
	{
		"nombre": "et magnis dis",
		"duracion": 87,
		"autor": "Shoshana Norris",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 5,
		"danzabilidad": 6
	},
	{
		"nombre": "imperdiet ornare. In",
		"duracion": 50,
		"autor": "Calista Kirkland",
		"generos": "Salsa R&B K-pop Metal Jazz",
		"popularidad": 1,
		"danzabilidad": 3
	},
	{
		"nombre": "Duis sit amet",
		"duracion": 34,
		"autor": "Yardley Vaughan",
		"generos": "K-pop Metal",
		"popularidad": 2,
		"danzabilidad": 10
	},
	{
		"nombre": "diam. Pellentesque habitant",
		"duracion": 53,
		"autor": "Orlando Joyner",
		"generos": "Jazz Góspel Blues Country Disco",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "rutrum magna. Cras",
		"duracion": 98,
		"autor": "Knox Pace",
		"generos": "Rock Pop Clásica Bachata Raeguetton",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "et libero. Proin",
		"duracion": 66,
		"autor": "Ferdinand Brady",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 5
	},
	{
		"nombre": "inceptos hymenaeos. Mauris",
		"duracion": 46,
		"autor": "Celeste Barron",
		"generos": "Pop Clásica",
		"popularidad": 1,
		"danzabilidad": 0
	},
	{
		"nombre": "quis, pede. Suspendisse",
		"duracion": 114,
		"autor": "Leonard Maddox",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "primis in faucibus",
		"duracion": 106,
		"autor": "Melodie Tyler",
		"generos": "Clásica",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "imperdiet, erat nonummy",
		"duracion": 61,
		"autor": "Fletcher Hinton",
		"generos": "Raeguetton Hip-Hop Salsa R&B K-pop",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "Curabitur sed tortor.",
		"duracion": 36,
		"autor": "Ross Mcdowell",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "mollis dui, in",
		"duracion": 86,
		"autor": "Logan Manning",
		"generos": "Blues Country Disco Techno",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "Etiam vestibulum massa",
		"duracion": 1,
		"autor": "Mari Sweeney",
		"generos": "Pop Clásica",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "feugiat. Lorem ipsum",
		"duracion": 133,
		"autor": "Akeem Mayer",
		"generos": "Góspel",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "sociis natoque penatibus",
		"duracion": 30,
		"autor": "Anthony Small",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "nascetur ridiculus mus.",
		"duracion": 12,
		"autor": "Sage Doyle",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "nibh enim, gravida",
		"duracion": 59,
		"autor": "Kiara Wilkinson",
		"generos": "K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "quis massa. Mauris",
		"duracion": 171,
		"autor": "Valentine Morris",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "Donec vitae erat",
		"duracion": 2,
		"autor": "Shannon Cantu",
		"generos": "Metal Jazz",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "tristique aliquet. Phasellus",
		"duracion": 162,
		"autor": "Ferris Zimmerman",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 5,
		"danzabilidad": 3
	},
	{
		"nombre": "vel arcu eu",
		"duracion": 48,
		"autor": "Uta Hahn",
		"generos": "Country Disco Techno",
		"popularidad": 3,
		"danzabilidad": 2
	},
	{
		"nombre": "et risus. Quisque",
		"duracion": 40,
		"autor": "Buckminster Stewart",
		"generos": "Blues Country",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "orci lacus vestibulum",
		"duracion": 35,
		"autor": "Cassandra Wilkins",
		"generos": "Country Disco",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "mi, ac mattis",
		"duracion": 108,
		"autor": "Abbot Keller",
		"generos": "Blues Country",
		"popularidad": 5,
		"danzabilidad": 6
	},
	{
		"nombre": "magna. Nam ligula",
		"duracion": 112,
		"autor": "Roth Saunders",
		"generos": "Clásica Bachata",
		"popularidad": 5,
		"danzabilidad": 3
	},
	{
		"nombre": "purus ac tellus.",
		"duracion": 85,
		"autor": "Keaton Prince",
		"generos": "Blues",
		"popularidad": 5,
		"danzabilidad": 7
	},
	{
		"nombre": "scelerisque neque sed",
		"duracion": 156,
		"autor": "Winifred Robinson",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "auctor quis, tristique",
		"duracion": 166,
		"autor": "Alan Kramer",
		"generos": "Disco Techno",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "nulla. Cras eu",
		"duracion": 81,
		"autor": "Josiah Rowe",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 4,
		"danzabilidad": 4
	},
	{
		"nombre": "eget, venenatis a,",
		"duracion": 167,
		"autor": "Nathaniel Sullivan",
		"generos": "K-pop Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "Aliquam fringilla cursus",
		"duracion": 83,
		"autor": "Serena Wheeler",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 1,
		"danzabilidad": 2
	},
	{
		"nombre": "at risus. Nunc",
		"duracion": 121,
		"autor": "Tallulah Avery",
		"generos": "Salsa R&B",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "diam nunc, ullamcorper",
		"duracion": 34,
		"autor": "Ann Anderson",
		"generos": "Jazz Góspel Blues",
		"popularidad": 10,
		"danzabilidad": 3
	},
	{
		"nombre": "Aliquam rutrum lorem",
		"duracion": 124,
		"autor": "Emmanuel Bullock",
		"generos": "R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "non, cursus non,",
		"duracion": 175,
		"autor": "Constance Glover",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "urna suscipit nonummy.",
		"duracion": 22,
		"autor": "Melvin Mcneil",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 10,
		"danzabilidad": 3
	},
	{
		"nombre": "posuere at, velit.",
		"duracion": 165,
		"autor": "Cassidy Tucker",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "eu dui. Cum",
		"duracion": 140,
		"autor": "Germane Suarez",
		"generos": "Metal",
		"popularidad": 8,
		"danzabilidad": 8
	},
	{
		"nombre": "fermentum fermentum arcu.",
		"duracion": 142,
		"autor": "Kessie Whitehead",
		"generos": "Techno",
		"popularidad": 5,
		"danzabilidad": 6
	},
	{
		"nombre": "turpis. Aliquam adipiscing",
		"duracion": 138,
		"autor": "Colt King",
		"generos": "Country",
		"popularidad": 9,
		"danzabilidad": 10
	},
	{
		"nombre": "blandit congue. In",
		"duracion": 133,
		"autor": "Fritz Schroeder",
		"generos": "Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "diam. Sed diam",
		"duracion": 86,
		"autor": "Steel Carver",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 6
	},
	{
		"nombre": "Mauris ut quam",
		"duracion": 84,
		"autor": "Kyra Daniel",
		"generos": "R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 7
	},
	{
		"nombre": "ac risus. Morbi",
		"duracion": 45,
		"autor": "Kyla Mcdaniel",
		"generos": "Bachata Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "malesuada fringilla est.",
		"duracion": 101,
		"autor": "Zoe Hunt",
		"generos": "Clásica Bachata",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "arcu vel quam",
		"duracion": 19,
		"autor": "Alexander Wilder",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 2,
		"danzabilidad": 1
	},
	{
		"nombre": "magna. Lorem ipsum",
		"duracion": 149,
		"autor": "John Vance",
		"generos": "Jazz",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "lacus. Nulla tincidunt,",
		"duracion": 60,
		"autor": "Rana Heath",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "orci sem eget",
		"duracion": 69,
		"autor": "Arden Faulkner",
		"generos": "K-pop",
		"popularidad": 10,
		"danzabilidad": 6
	},
	{
		"nombre": "a purus. Duis",
		"duracion": 150,
		"autor": "Uta Brewer",
		"generos": "Hip-Hop Salsa",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "dis parturient montes,",
		"duracion": 42,
		"autor": "Gavin Lott",
		"generos": "Blues Country Disco Techno Flamenco",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "scelerisque neque. Nullam",
		"duracion": 45,
		"autor": "Doris Moss",
		"generos": "Blues Country Disco",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "Nam nulla magna,",
		"duracion": 134,
		"autor": "Lane Sawyer",
		"generos": "Blues Country",
		"popularidad": 7,
		"danzabilidad": 1
	},
	{
		"nombre": "cursus luctus, ipsum",
		"duracion": 29,
		"autor": "Ezekiel Conrad",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "nulla. Integer vulputate,",
		"duracion": 36,
		"autor": "Iris Sweet",
		"generos": "Metal Jazz Góspel",
		"popularidad": 8,
		"danzabilidad": 6
	},
	{
		"nombre": "a, facilisis non,",
		"duracion": 112,
		"autor": "Thor Garrett",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 1,
		"danzabilidad": 8
	},
	{
		"nombre": "dolor sit amet,",
		"duracion": 77,
		"autor": "Tatiana Good",
		"generos": "Rock Pop Clásica Bachata",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "Maecenas ornare egestas",
		"duracion": 165,
		"autor": "Caesar Fitzgerald",
		"generos": "K-pop Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 5
	},
	{
		"nombre": "Nunc sed orci",
		"duracion": 22,
		"autor": "Isaac Perez",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "risus. Donec nibh",
		"duracion": 128,
		"autor": "Carissa Brewer",
		"generos": "Techno Flamenco",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "aliquet molestie tellus.",
		"duracion": 78,
		"autor": "Declan Cruz",
		"generos": "Disco Techno",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "arcu. Aliquam ultrices",
		"duracion": 55,
		"autor": "Evangeline Tate",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 5,
		"danzabilidad": 1
	},
	{
		"nombre": "feugiat nec, diam.",
		"duracion": 109,
		"autor": "Lillian Mccray",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 0,
		"danzabilidad": 2
	},
	{
		"nombre": "mollis vitae, posuere",
		"duracion": 13,
		"autor": "Clio Ochoa",
		"generos": "Pop Clásica",
		"popularidad": 10,
		"danzabilidad": 8
	},
	{
		"nombre": "ullamcorper. Duis at",
		"duracion": 48,
		"autor": "Garrett Park",
		"generos": "Góspel Blues",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "luctus et ultrices",
		"duracion": 74,
		"autor": "Fuller Craig",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "mus. Aenean eget",
		"duracion": 15,
		"autor": "Cullen Kirk",
		"generos": "Flamenco",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "tempus eu, ligula.",
		"duracion": 73,
		"autor": "Naida Barton",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "Maecenas libero est,",
		"duracion": 58,
		"autor": "Kelsie Mccarthy",
		"generos": "Rock Pop Clásica Bachata",
		"popularidad": 8,
		"danzabilidad": 4
	},
	{
		"nombre": "ante bibendum ullamcorper.",
		"duracion": 81,
		"autor": "Lucy Sullivan",
		"generos": "K-pop Metal",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "dolor sit amet,",
		"duracion": 169,
		"autor": "Zahir Gamble",
		"generos": "Disco Techno",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "semper egestas, urna",
		"duracion": 65,
		"autor": "Patrick Moon",
		"generos": "R&B K-pop",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "lectus pede et",
		"duracion": 82,
		"autor": "Warren Mccray",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 2,
		"danzabilidad": 3
	},
	{
		"nombre": "Donec sollicitudin adipiscing",
		"duracion": 145,
		"autor": "Fulton Mcclure",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 2,
		"danzabilidad": 3
	},
	{
		"nombre": "libero. Donec consectetuer",
		"duracion": 167,
		"autor": "Driscoll Cameron",
		"generos": "R&B K-pop Metal",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "non quam. Pellentesque",
		"duracion": 144,
		"autor": "Finn Howe",
		"generos": "Blues Country Disco Techno Flamenco",
		"popularidad": 0,
		"danzabilidad": 8
	},
	{
		"nombre": "orci, in consequat",
		"duracion": 161,
		"autor": "Virginia Mcfadden",
		"generos": "Pop Clásica",
		"popularidad": 10,
		"danzabilidad": 2
	},
	{
		"nombre": "Nunc laoreet lectus",
		"duracion": 175,
		"autor": "Leandra Morris",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 7,
		"danzabilidad": 4
	},
	{
		"nombre": "sit amet ornare",
		"duracion": 178,
		"autor": "Jin Estrada",
		"generos": "Hip-Hop Salsa",
		"popularidad": 7,
		"danzabilidad": 0
	},
	{
		"nombre": "ut mi. Duis",
		"duracion": 43,
		"autor": "Keaton Stone",
		"generos": "Country Disco Techno",
		"popularidad": 3,
		"danzabilidad": 2
	},
	{
		"nombre": "risus. Nunc ac",
		"duracion": 23,
		"autor": "Jasmine Bowman",
		"generos": "Pop Clásica",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "urna. Ut tincidunt",
		"duracion": 10,
		"autor": "Reuben Herman",
		"generos": "K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "nec, mollis vitae,",
		"duracion": 5,
		"autor": "Denise Black",
		"generos": "Metal Jazz Góspel",
		"popularidad": 5,
		"danzabilidad": 2
	},
	{
		"nombre": "mollis. Phasellus libero",
		"duracion": 119,
		"autor": "Sharon Bishop",
		"generos": "Salsa R&B K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "quis turpis vitae",
		"duracion": 55,
		"autor": "Deborah Rosario",
		"generos": "Raeguetton",
		"popularidad": 2,
		"danzabilidad": 7
	},
	{
		"nombre": "dis parturient montes,",
		"duracion": 87,
		"autor": "Armand Pratt",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 0,
		"danzabilidad": 4
	},
	{
		"nombre": "facilisi. Sed neque.",
		"duracion": 165,
		"autor": "Colin Mcdowell",
		"generos": "Pop",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "arcu. Curabitur ut",
		"duracion": 132,
		"autor": "Dominique Casey",
		"generos": "Country Disco",
		"popularidad": 0,
		"danzabilidad": 6
	},
	{
		"nombre": "nunc interdum feugiat.",
		"duracion": 114,
		"autor": "Dai Cote",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "purus. Duis elementum,",
		"duracion": 73,
		"autor": "Zachary Lynn",
		"generos": "Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 4
	},
	{
		"nombre": "et ultrices posuere",
		"duracion": 106,
		"autor": "Uriel Cruz",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 2
	},
	{
		"nombre": "Sed auctor odio",
		"duracion": 137,
		"autor": "Kadeem Zamora",
		"generos": "Flamenco",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "semper tellus id",
		"duracion": 81,
		"autor": "Xanthus Little",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "Donec luctus aliquet",
		"duracion": 20,
		"autor": "Emerald Kinney",
		"generos": "Jazz Góspel Blues",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "semper erat, in",
		"duracion": 178,
		"autor": "Sasha Hewitt",
		"generos": "Rock Pop Clásica",
		"popularidad": 7,
		"danzabilidad": 9
	},
	{
		"nombre": "scelerisque scelerisque dui.",
		"duracion": 117,
		"autor": "Emery Booth",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "Morbi quis urna.",
		"duracion": 152,
		"autor": "Winifred Lamb",
		"generos": "Salsa R&B",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "in molestie tortor",
		"duracion": 131,
		"autor": "Brenden Cross",
		"generos": "R&B K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 1
	},
	{
		"nombre": "ornare sagittis felis.",
		"duracion": 172,
		"autor": "Daryl Donaldson",
		"generos": "Góspel Blues Country",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "rutrum magna. Cras",
		"duracion": 158,
		"autor": "Mannix Alvarado",
		"generos": "Bachata Raeguetton",
		"popularidad": 7,
		"danzabilidad": 6
	},
	{
		"nombre": "quam. Pellentesque habitant",
		"duracion": 61,
		"autor": "Juliet Dunlap",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 10
	},
	{
		"nombre": "Ut tincidunt orci",
		"duracion": 140,
		"autor": "Tobias Kelley",
		"generos": "Góspel",
		"popularidad": 1,
		"danzabilidad": 8
	},
	{
		"nombre": "tincidunt dui augue",
		"duracion": 84,
		"autor": "Deacon Mckinney",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "at sem molestie",
		"duracion": 14,
		"autor": "Lesley Franks",
		"generos": "Pop Clásica",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "Donec vitae erat",
		"duracion": 91,
		"autor": "Clark Dixon",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 3,
		"danzabilidad": 10
	},
	{
		"nombre": "non, dapibus rutrum,",
		"duracion": 46,
		"autor": "Dalton Harvey",
		"generos": "Salsa R&B K-pop",
		"popularidad": 8,
		"danzabilidad": 0
	},
	{
		"nombre": "justo. Praesent luctus.",
		"duracion": 114,
		"autor": "Scott Washington",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 10,
		"danzabilidad": 5
	},
	{
		"nombre": "felis orci, adipiscing",
		"duracion": 116,
		"autor": "Marvin Sweet",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 7,
		"danzabilidad": 0
	},
	{
		"nombre": "eget laoreet posuere,",
		"duracion": 32,
		"autor": "Summer Sawyer",
		"generos": "Disco",
		"popularidad": 10,
		"danzabilidad": 4
	},
	{
		"nombre": "litora torquent per",
		"duracion": 13,
		"autor": "Felix Blake",
		"generos": "Country Disco Techno",
		"popularidad": 4,
		"danzabilidad": 1
	},
	{
		"nombre": "ac mattis semper,",
		"duracion": 20,
		"autor": "Raja Calhoun",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "nec, mollis vitae,",
		"duracion": 92,
		"autor": "Brody Pate",
		"generos": "Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "mauris. Suspendisse aliquet",
		"duracion": 175,
		"autor": "Charlotte Ruiz",
		"generos": "R&B K-pop Metal",
		"popularidad": 10,
		"danzabilidad": 5
	},
	{
		"nombre": "justo. Praesent luctus.",
		"duracion": 69,
		"autor": "Raven Waller",
		"generos": "Góspel",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "arcu et pede.",
		"duracion": 4,
		"autor": "Hayes Sandoval",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "eget ipsum. Suspendisse",
		"duracion": 81,
		"autor": "Natalie Bolton",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "lacus. Mauris non",
		"duracion": 71,
		"autor": "Griffin Spence",
		"generos": "R&B K-pop Metal",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "placerat. Cras dictum",
		"duracion": 36,
		"autor": "Portia Chaney",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "sagittis placerat. Cras",
		"duracion": 171,
		"autor": "Akeem Black",
		"generos": "Bachata Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "sed libero. Proin",
		"duracion": 129,
		"autor": "Xaviera Hopkins",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "enim consequat purus.",
		"duracion": 124,
		"autor": "Shannon Bowman",
		"generos": "K-pop Metal",
		"popularidad": 1,
		"danzabilidad": 6
	},
	{
		"nombre": "mus. Proin vel",
		"duracion": 74,
		"autor": "Cassandra Schneider",
		"generos": "Rock Pop Clásica Bachata Raeguetton",
		"popularidad": 6,
		"danzabilidad": 8
	},
	{
		"nombre": "amet massa. Quisque",
		"duracion": 92,
		"autor": "Imogene Compton",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 3,
		"danzabilidad": 1
	},
	{
		"nombre": "Lorem ipsum dolor",
		"duracion": 89,
		"autor": "Ivy Terry",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 2,
		"danzabilidad": 4
	},
	{
		"nombre": "libero est, congue",
		"duracion": 100,
		"autor": "Kirestin Herrera",
		"generos": "Disco Techno",
		"popularidad": 10,
		"danzabilidad": 1
	},
	{
		"nombre": "nunc, ullamcorper eu,",
		"duracion": 11,
		"autor": "Barry Alexander",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "faucibus leo, in",
		"duracion": 126,
		"autor": "Fatima Wyatt",
		"generos": "Hip-Hop Salsa",
		"popularidad": 8,
		"danzabilidad": 6
	},
	{
		"nombre": "Suspendisse sed dolor.",
		"duracion": 64,
		"autor": "Paul Owens",
		"generos": "Metal Jazz Góspel",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "molestie in, tempus",
		"duracion": 75,
		"autor": "Patricia Caldwell",
		"generos": "K-pop Metal Jazz",
		"popularidad": 2,
		"danzabilidad": 8
	},
	{
		"nombre": "amet lorem semper",
		"duracion": 67,
		"autor": "Simone Harding",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 8,
		"danzabilidad": 5
	},
	{
		"nombre": "egestas hendrerit neque.",
		"duracion": 36,
		"autor": "Dahlia Houston",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "dis parturient montes,",
		"duracion": 78,
		"autor": "Caesar Grant",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "Integer vitae nibh.",
		"duracion": 79,
		"autor": "Amity Estrada",
		"generos": "R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "mattis. Cras eget",
		"duracion": 115,
		"autor": "Samuel Leon",
		"generos": "Blues Country",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "metus. Aenean sed",
		"duracion": 119,
		"autor": "Tad Cleveland",
		"generos": "Góspel Blues Country",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "orci quis lectus.",
		"duracion": 110,
		"autor": "Indira Johnson",
		"generos": "Góspel Blues",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "Donec nibh. Quisque",
		"duracion": 61,
		"autor": "Andrew Owen",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "vitae dolor. Donec",
		"duracion": 52,
		"autor": "Katelyn Duke",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 8,
		"danzabilidad": 8
	},
	{
		"nombre": "arcu. Curabitur ut",
		"duracion": 143,
		"autor": "Maxine Wilson",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "nostra, per inceptos",
		"duracion": 167,
		"autor": "Joseph Watts",
		"generos": "Disco",
		"popularidad": 10,
		"danzabilidad": 6
	},
	{
		"nombre": "Vivamus euismod urna.",
		"duracion": 37,
		"autor": "Bell Mercer",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 9,
		"danzabilidad": 8
	},
	{
		"nombre": "aliquam iaculis, lacus",
		"duracion": 27,
		"autor": "Jasmine Kemp",
		"generos": "Blues Country Disco Techno",
		"popularidad": 7,
		"danzabilidad": 0
	},
	{
		"nombre": "vel, venenatis vel,",
		"duracion": 37,
		"autor": "Lev Frederick",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "enim non nisi.",
		"duracion": 19,
		"autor": "Fuller Francis",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "sociis natoque penatibus",
		"duracion": 95,
		"autor": "Jonah Gregory",
		"generos": "K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 1
	},
	{
		"nombre": "vestibulum lorem, sit",
		"duracion": 9,
		"autor": "Christine Craig",
		"generos": "Country Disco",
		"popularidad": 6,
		"danzabilidad": 8
	},
	{
		"nombre": "Praesent interdum ligula",
		"duracion": 136,
		"autor": "Melinda Bryant",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 3,
		"danzabilidad": 0
	},
	{
		"nombre": "Donec felis orci,",
		"duracion": 91,
		"autor": "Kiara Richardson",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 6,
		"danzabilidad": 9
	},
	{
		"nombre": "purus gravida sagittis.",
		"duracion": 42,
		"autor": "Aurora Adkins",
		"generos": "Jazz Góspel",
		"popularidad": 6,
		"danzabilidad": 7
	},
	{
		"nombre": "Morbi quis urna.",
		"duracion": 163,
		"autor": "Ivor Cox",
		"generos": "Disco Techno",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "at sem molestie",
		"duracion": 122,
		"autor": "Amal Stewart",
		"generos": "Salsa R&B K-pop",
		"popularidad": 9,
		"danzabilidad": 8
	},
	{
		"nombre": "ultrices. Vivamus rhoncus.",
		"duracion": 13,
		"autor": "Cheyenne Haney",
		"generos": "Jazz Góspel Blues Country",
		"popularidad": 9,
		"danzabilidad": 0
	},
	{
		"nombre": "convallis erat, eget",
		"duracion": 168,
		"autor": "Callum Barron",
		"generos": "K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "commodo ipsum. Suspendisse",
		"duracion": 82,
		"autor": "Levi Velez",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 8,
		"danzabilidad": 2
	},
	{
		"nombre": "et, euismod et,",
		"duracion": 51,
		"autor": "Hammett Chen",
		"generos": "Salsa R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "nec, eleifend non,",
		"duracion": 13,
		"autor": "Hop Bray",
		"generos": "Pop Clásica",
		"popularidad": 2,
		"danzabilidad": 1
	},
	{
		"nombre": "scelerisque scelerisque dui.",
		"duracion": 131,
		"autor": "Logan Rose",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "in, tempus eu,",
		"duracion": 134,
		"autor": "Jasper Kelly",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 7,
		"danzabilidad": 8
	},
	{
		"nombre": "tellus justo sit",
		"duracion": 118,
		"autor": "Sonia Logan",
		"generos": "Blues Country Disco Techno",
		"popularidad": 1,
		"danzabilidad": 7
	},
	{
		"nombre": "lectus rutrum urna,",
		"duracion": 85,
		"autor": "Tana Sosa",
		"generos": "Bachata Raeguetton",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "id, ante. Nunc",
		"duracion": 86,
		"autor": "Grady Crane",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 6,
		"danzabilidad": 3
	},
	{
		"nombre": "pede. Cras vulputate",
		"duracion": 106,
		"autor": "Roth Marquez",
		"generos": "K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 2
	},
	{
		"nombre": "mollis. Integer tincidunt",
		"duracion": 25,
		"autor": "Amber Downs",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 7,
		"danzabilidad": 8
	},
	{
		"nombre": "aliquet diam. Sed",
		"duracion": 105,
		"autor": "Yuli Beach",
		"generos": "Blues Country Disco",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "nec ante. Maecenas",
		"duracion": 7,
		"autor": "Travis Rosa",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 3,
		"danzabilidad": 5
	},
	{
		"nombre": "metus eu erat",
		"duracion": 52,
		"autor": "Hayden Santiago",
		"generos": "R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 3
	},
	{
		"nombre": "eu turpis. Nulla",
		"duracion": 78,
		"autor": "Marvin Moon",
		"generos": "Jazz Góspel Blues Country",
		"popularidad": 2,
		"danzabilidad": 4
	},
	{
		"nombre": "Nullam suscipit, est",
		"duracion": 30,
		"autor": "Xyla Mcfadden",
		"generos": "Metal Jazz Góspel Blues Country",
		"popularidad": 5,
		"danzabilidad": 2
	},
	{
		"nombre": "ipsum porta elit,",
		"duracion": 171,
		"autor": "Summer Duffy",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 8,
		"danzabilidad": 2
	},
	{
		"nombre": "amet, risus. Donec",
		"duracion": 143,
		"autor": "Maggie Parsons",
		"generos": "Blues Country",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "mi. Duis risus",
		"duracion": 7,
		"autor": "Leonard Vinson",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 2
	},
	{
		"nombre": "eu tellus. Phasellus",
		"duracion": 112,
		"autor": "Sandra Weaver",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 6,
		"danzabilidad": 8
	},
	{
		"nombre": "auctor quis, tristique",
		"duracion": 179,
		"autor": "Xyla Gross",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 2,
		"danzabilidad": 4
	},
	{
		"nombre": "amet, consectetuer adipiscing",
		"duracion": 77,
		"autor": "Yvonne Adams",
		"generos": "Bachata Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "nonummy ultricies ornare,",
		"duracion": 159,
		"autor": "Derek Mckenzie",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 0,
		"danzabilidad": 6
	},
	{
		"nombre": "non, egestas a,",
		"duracion": 120,
		"autor": "Tarik Zamora",
		"generos": "Disco",
		"popularidad": 3,
		"danzabilidad": 10
	},
	{
		"nombre": "turpis egestas. Fusce",
		"duracion": 121,
		"autor": "Nicholas Farrell",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 10,
		"danzabilidad": 4
	},
	{
		"nombre": "sem ut cursus",
		"duracion": 61,
		"autor": "Norman Blake",
		"generos": "Disco Techno",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "Proin mi. Aliquam",
		"duracion": 12,
		"autor": "Adrian Mitchell",
		"generos": "Pop Clásica",
		"popularidad": 10,
		"danzabilidad": 1
	},
	{
		"nombre": "taciti sociosqu ad",
		"duracion": 128,
		"autor": "Merritt Carrillo",
		"generos": "Disco Techno",
		"popularidad": 9,
		"danzabilidad": 0
	},
	{
		"nombre": "sed sem egestas",
		"duracion": 112,
		"autor": "Gavin Yates",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 7,
		"danzabilidad": 4
	},
	{
		"nombre": "amet, dapibus id,",
		"duracion": 69,
		"autor": "Larissa Dejesus",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "rutrum urna, nec",
		"duracion": 16,
		"autor": "Simon Wiggins",
		"generos": "K-pop Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "velit. Aliquam nisl.",
		"duracion": 68,
		"autor": "Hyatt Barlow",
		"generos": "Góspel Blues",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "auctor odio a",
		"duracion": 81,
		"autor": "Jaden Wilkerson",
		"generos": "Pop Clásica Bachata",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "Duis at lacus.",
		"duracion": 45,
		"autor": "Wendy Burke",
		"generos": "Disco",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "ut nisi a",
		"duracion": 95,
		"autor": "Kuame Nielsen",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "ultrices. Duis volutpat",
		"duracion": 40,
		"autor": "Coby Barry",
		"generos": "Country Disco Techno Flamenco",
		"popularidad": 2,
		"danzabilidad": 1
	},
	{
		"nombre": "a nunc. In",
		"duracion": 130,
		"autor": "Wallace Sanchez",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "augue ac ipsum.",
		"duracion": 101,
		"autor": "Wynter Rice",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "non ante bibendum",
		"duracion": 172,
		"autor": "Mikayla Lewis",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "Proin dolor. Nulla",
		"duracion": 4,
		"autor": "Paul O'donnell",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 6
	},
	{
		"nombre": "libero. Morbi accumsan",
		"duracion": 151,
		"autor": "Arden Barrett",
		"generos": "Metal Jazz Góspel Blues Country",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "mauris id sapien.",
		"duracion": 100,
		"autor": "Asher Figueroa",
		"generos": "Techno",
		"popularidad": 8,
		"danzabilidad": 7
	},
	{
		"nombre": "id enim. Curabitur",
		"duracion": 68,
		"autor": "Dacey Petty",
		"generos": "Jazz Góspel Blues",
		"popularidad": 4,
		"danzabilidad": 5
	},
	{
		"nombre": "massa rutrum magna.",
		"duracion": 125,
		"autor": "Joseph Vance",
		"generos": "Rock Pop Clásica Bachata",
		"popularidad": 1,
		"danzabilidad": 2
	},
	{
		"nombre": "Suspendisse ac metus",
		"duracion": 94,
		"autor": "Sara Burton",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "mauris a nunc.",
		"duracion": 6,
		"autor": "John Savage",
		"generos": "R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 8
	},
	{
		"nombre": "ultrices iaculis odio.",
		"duracion": 169,
		"autor": "Jermaine Bentley",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 2,
		"danzabilidad": 1
	},
	{
		"nombre": "dis parturient montes,",
		"duracion": 81,
		"autor": "Debra Gregory",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 4,
		"danzabilidad": 4
	},
	{
		"nombre": "sed dictum eleifend,",
		"duracion": 134,
		"autor": "Cole Dennis",
		"generos": "Pop Clásica",
		"popularidad": 5,
		"danzabilidad": 6
	},
	{
		"nombre": "tellus. Phasellus elit",
		"duracion": 62,
		"autor": "Virginia Garcia",
		"generos": "Góspel",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "Nulla tempor augue",
		"duracion": 7,
		"autor": "Fuller Gomez",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "Nunc lectus pede,",
		"duracion": 129,
		"autor": "Denise Trevino",
		"generos": "Pop Clásica Bachata",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "Morbi quis urna.",
		"duracion": 153,
		"autor": "Lamar Mcgee",
		"generos": "Jazz Góspel",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "Nam nulla magna,",
		"duracion": 73,
		"autor": "Rhona Cortez",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 2
	},
	{
		"nombre": "nulla. Cras eu",
		"duracion": 36,
		"autor": "Lavinia Cain",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "blandit at, nisi.",
		"duracion": 159,
		"autor": "Shannon Ware",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 4
	},
	{
		"nombre": "amet diam eu",
		"duracion": 2,
		"autor": "Chanda Howell",
		"generos": "Jazz Góspel Blues",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "pharetra ut, pharetra",
		"duracion": 92,
		"autor": "Dustin Cooper",
		"generos": "K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 6
	},
	{
		"nombre": "sed orci lobortis",
		"duracion": 71,
		"autor": "Zenaida Mayer",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "faucibus ut, nulla.",
		"duracion": 132,
		"autor": "Lucy Medina",
		"generos": "K-pop Metal Jazz",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "molestie orci tincidunt",
		"duracion": 163,
		"autor": "Judith Salinas",
		"generos": "Techno Flamenco",
		"popularidad": 6,
		"danzabilidad": 4
	},
	{
		"nombre": "diam vel arcu.",
		"duracion": 102,
		"autor": "Aphrodite Johnson",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "libero mauris, aliquam",
		"duracion": 91,
		"autor": "Idona Mcfadden",
		"generos": "Pop Clásica Bachata",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "malesuada fames ac",
		"duracion": 103,
		"autor": "Felix Gibbs",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 4,
		"danzabilidad": 1
	},
	{
		"nombre": "metus. In nec",
		"duracion": 92,
		"autor": "Aurora Shaw",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 2,
		"danzabilidad": 6
	},
	{
		"nombre": "sed pede. Cum",
		"duracion": 13,
		"autor": "Vance Calderon",
		"generos": "K-pop Metal Jazz",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "eu dui. Cum",
		"duracion": 78,
		"autor": "Carl Little",
		"generos": "K-pop Metal Jazz",
		"popularidad": 10,
		"danzabilidad": 7
	},
	{
		"nombre": "orci, consectetuer euismod",
		"duracion": 162,
		"autor": "Halla Glenn",
		"generos": "Disco",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "ultrices a, auctor",
		"duracion": 3,
		"autor": "Bernard Mullen",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 0,
		"danzabilidad": 8
	},
	{
		"nombre": "ligula. Aenean gravida",
		"duracion": 180,
		"autor": "Stephen Lee",
		"generos": "Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "eleifend non, dapibus",
		"duracion": 146,
		"autor": "Gary Juarez",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "malesuada ut, sem.",
		"duracion": 43,
		"autor": "Erich Knight",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"danzabilidad": 5
	},
	{
		"nombre": "risus. In mi",
		"duracion": 106,
		"autor": "Fitzgerald Chaney",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 10,
		"danzabilidad": 1
	},
	{
		"nombre": "sapien, cursus in,",
		"duracion": 65,
		"autor": "Rhona Romero",
		"generos": "Jazz Góspel",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "Suspendisse dui. Fusce",
		"duracion": 8,
		"autor": "Elijah Patel",
		"generos": "K-pop",
		"popularidad": 2,
		"danzabilidad": 7
	},
	{
		"nombre": "scelerisque dui. Suspendisse",
		"duracion": 176,
		"autor": "Dai Hurley",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "venenatis a, magna.",
		"duracion": 165,
		"autor": "Uma Moon",
		"generos": "Jazz",
		"popularidad": 6,
		"danzabilidad": 5
	},
	{
		"nombre": "magna et ipsum",
		"duracion": 171,
		"autor": "Dai Santos",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "nulla vulputate dui,",
		"duracion": 71,
		"autor": "Dora Day",
		"generos": "Disco Techno",
		"popularidad": 3,
		"danzabilidad": 5
	},
	{
		"nombre": "Sed nec metus",
		"duracion": 81,
		"autor": "Nevada Gentry",
		"generos": "Blues Country",
		"popularidad": 7,
		"danzabilidad": 4
	},
	{
		"nombre": "Integer in magna.",
		"duracion": 85,
		"autor": "Justina Crosby",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "sapien, gravida non,",
		"duracion": 95,
		"autor": "Maya Berry",
		"generos": "Góspel Blues",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "sapien molestie orci",
		"duracion": 51,
		"autor": "Sawyer Petty",
		"generos": "Salsa R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "enim commodo hendrerit.",
		"duracion": 160,
		"autor": "Cailin Suarez",
		"generos": "Metal Jazz",
		"popularidad": 1,
		"danzabilidad": 0
	},
	{
		"nombre": "ultrices posuere cubilia",
		"duracion": 112,
		"autor": "Deborah Boyd",
		"generos": "Blues Country Disco Techno",
		"popularidad": 1,
		"danzabilidad": 0
	},
	{
		"nombre": "Suspendisse non leo.",
		"duracion": 108,
		"autor": "Leah Deleon",
		"generos": "K-pop Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 3
	},
	{
		"nombre": "semper. Nam tempor",
		"duracion": 52,
		"autor": "Nadine Gould",
		"generos": "Bachata Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "nulla at sem",
		"duracion": 102,
		"autor": "Raymond Marks",
		"generos": "Salsa R&B",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "Aenean gravida nunc",
		"duracion": 1,
		"autor": "Cairo Buck",
		"generos": "R&B K-pop Metal Jazz Góspel",
		"popularidad": 1,
		"danzabilidad": 2
	},
	{
		"nombre": "at auctor ullamcorper,",
		"duracion": 134,
		"autor": "Kylie Velez",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 8
	},
	{
		"nombre": "orci quis lectus.",
		"duracion": 134,
		"autor": "Nehru Casey",
		"generos": "Clásica Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 0,
		"danzabilidad": 9
	},
	{
		"nombre": "tellus, imperdiet non,",
		"duracion": 111,
		"autor": "Ocean Rocha",
		"generos": "Jazz Góspel",
		"popularidad": 6,
		"danzabilidad": 9
	},
	{
		"nombre": "Vivamus euismod urna.",
		"duracion": 140,
		"autor": "Keaton Rutledge",
		"generos": "R&B K-pop Metal",
		"popularidad": 6,
		"danzabilidad": 3
	},
	{
		"nombre": "felis orci, adipiscing",
		"duracion": 168,
		"autor": "Mira Carter",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 3,
		"danzabilidad": 5
	},
	{
		"nombre": "cursus luctus, ipsum",
		"duracion": 19,
		"autor": "Griffin Mcgowan",
		"generos": "Pop Clásica Bachata",
		"popularidad": 0,
		"danzabilidad": 1
	},
	{
		"nombre": "eu nibh vulputate",
		"duracion": 51,
		"autor": "Devin Sherman",
		"generos": "Disco Techno Flamenco",
		"popularidad": 5,
		"danzabilidad": 1
	},
	{
		"nombre": "quam dignissim pharetra.",
		"duracion": 169,
		"autor": "Knox Emerson",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 4,
		"danzabilidad": 5
	},
	{
		"nombre": "facilisis eget, ipsum.",
		"duracion": 109,
		"autor": "Dorian Wolfe",
		"generos": "Country Disco Techno",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "fringilla purus mauris",
		"duracion": 41,
		"autor": "Hilel Delacruz",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "arcu. Sed et",
		"duracion": 23,
		"autor": "Sybill Moon",
		"generos": "K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 8
	},
	{
		"nombre": "non, sollicitudin a,",
		"duracion": 18,
		"autor": "Boris Kelley",
		"generos": "Pop Clásica Bachata",
		"popularidad": 5,
		"danzabilidad": 3
	},
	{
		"nombre": "mauris blandit mattis.",
		"duracion": 96,
		"autor": "Irma Dennis",
		"generos": "R&B K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 5
	},
	{
		"nombre": "non magna. Nam",
		"duracion": 83,
		"autor": "Catherine Richards",
		"generos": "Country Disco Techno Flamenco",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "nec urna suscipit",
		"duracion": 100,
		"autor": "Olga Parker",
		"generos": "Metal",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "tincidunt vehicula risus.",
		"duracion": 94,
		"autor": "Gil Carey",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 7,
		"danzabilidad": 4
	},
	{
		"nombre": "Donec non justo.",
		"duracion": 16,
		"autor": "Mariko Horton",
		"generos": "Jazz Góspel Blues",
		"popularidad": 2,
		"danzabilidad": 1
	},
	{
		"nombre": "tristique senectus et",
		"duracion": 138,
		"autor": "Venus Oneil",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "tincidunt tempus risus.",
		"duracion": 149,
		"autor": "Ralph Bates",
		"generos": "Bachata Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 9,
		"danzabilidad": 8
	},
	{
		"nombre": "urna, nec luctus",
		"duracion": 39,
		"autor": "Idona Robles",
		"generos": "Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "ullamcorper, velit in",
		"duracion": 164,
		"autor": "Liberty Walters",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 8
	},
	{
		"nombre": "et magnis dis",
		"duracion": 178,
		"autor": "Rhoda Powers",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 3,
		"danzabilidad": 0
	},
	{
		"nombre": "adipiscing lobortis risus.",
		"duracion": 100,
		"autor": "Kirk Harris",
		"generos": "Bachata Raeguetton",
		"popularidad": 2,
		"danzabilidad": 5
	},
	{
		"nombre": "Mauris vel turpis.",
		"duracion": 178,
		"autor": "Joshua Kim",
		"generos": "Clásica",
		"popularidad": 7,
		"danzabilidad": 6
	},
	{
		"nombre": "sem ut dolor",
		"duracion": 109,
		"autor": "Ashely Donovan",
		"generos": "Blues Country",
		"popularidad": 6,
		"danzabilidad": 2
	},
	{
		"nombre": "quam dignissim pharetra.",
		"duracion": 133,
		"autor": "Neil Lee",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "Cras lorem lorem,",
		"duracion": 97,
		"autor": "Athena Ramirez",
		"generos": "Clásica Bachata",
		"popularidad": 7,
		"danzabilidad": 1
	},
	{
		"nombre": "lacus. Ut nec",
		"duracion": 56,
		"autor": "Rama Aguilar",
		"generos": "Metal Jazz",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "adipiscing elit. Curabitur",
		"duracion": 110,
		"autor": "Kenneth Pugh",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 9,
		"danzabilidad": 0
	},
	{
		"nombre": "ligula. Nullam feugiat",
		"duracion": 148,
		"autor": "Anjolie Mcfarland",
		"generos": "Country Disco Techno",
		"popularidad": 10,
		"danzabilidad": 0
	},
	{
		"nombre": "Phasellus ornare. Fusce",
		"duracion": 5,
		"autor": "Damian Davenport",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "euismod in, dolor.",
		"duracion": 154,
		"autor": "Richard Stone",
		"generos": "Góspel Blues",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "mauris elit, dictum",
		"duracion": 73,
		"autor": "Wing Calderon",
		"generos": "Disco Techno Flamenco",
		"popularidad": 7,
		"danzabilidad": 6
	},
	{
		"nombre": "quis turpis vitae",
		"duracion": 48,
		"autor": "Colt Perez",
		"generos": "Disco Techno",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "Sed molestie. Sed",
		"duracion": 47,
		"autor": "Dolan Cole",
		"generos": "Pop Clásica",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "urna convallis erat,",
		"duracion": 79,
		"autor": "Mark Delaney",
		"generos": "Bachata Raeguetton",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "Etiam laoreet, libero",
		"duracion": 96,
		"autor": "Laith Marquez",
		"generos": "Bachata Raeguetton",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "Quisque ac libero",
		"duracion": 74,
		"autor": "Winifred Hebert",
		"generos": "Góspel Blues",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "nec, cursus a,",
		"duracion": 119,
		"autor": "Omar Green",
		"generos": "Blues Country Disco",
		"popularidad": 3,
		"danzabilidad": 1
	},
	{
		"nombre": "sem mollis dui,",
		"duracion": 90,
		"autor": "Dai Reese",
		"generos": "Clásica Bachata",
		"popularidad": 9,
		"danzabilidad": 4
	},
	{
		"nombre": "id, mollis nec,",
		"duracion": 156,
		"autor": "Helen Kline",
		"generos": "K-pop Metal Jazz",
		"popularidad": 0,
		"danzabilidad": 1
	},
	{
		"nombre": "hymenaeos. Mauris ut",
		"duracion": 154,
		"autor": "Ingrid Benton",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "magna. Ut tincidunt",
		"duracion": 40,
		"autor": "Thor Potts",
		"generos": "Bachata",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "quam a felis",
		"duracion": 14,
		"autor": "Knox Macdonald",
		"generos": "Techno Flamenco",
		"popularidad": 3,
		"danzabilidad": 8
	},
	{
		"nombre": "Suspendisse non leo.",
		"duracion": 130,
		"autor": "Hop Alvarado",
		"generos": "Techno Flamenco",
		"popularidad": 4,
		"danzabilidad": 8
	},
	{
		"nombre": "pede. Cras vulputate",
		"duracion": 30,
		"autor": "Devin Meadows",
		"generos": "Techno",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "eu, ultrices sit",
		"duracion": 101,
		"autor": "Iona Walters",
		"generos": "K-pop Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 6
	},
	{
		"nombre": "Proin non massa",
		"duracion": 168,
		"autor": "Scarlett Gay",
		"generos": "Metal Jazz",
		"popularidad": 8,
		"danzabilidad": 9
	},
	{
		"nombre": "ultrices posuere cubilia",
		"duracion": 41,
		"autor": "Lisandra Cardenas",
		"generos": "Salsa R&B K-pop Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "felis. Nulla tempor",
		"duracion": 169,
		"autor": "Hilda Kline",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "dictum placerat, augue.",
		"duracion": 9,
		"autor": "Kiara Cobb",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 8,
		"danzabilidad": 1
	},
	{
		"nombre": "ridiculus mus. Aenean",
		"duracion": 177,
		"autor": "Fiona Delacruz",
		"generos": "Country Disco Techno",
		"popularidad": 4,
		"danzabilidad": 4
	},
	{
		"nombre": "commodo ipsum. Suspendisse",
		"duracion": 177,
		"autor": "Yetta Ortega",
		"generos": "K-pop Metal",
		"popularidad": 10,
		"danzabilidad": 4
	},
	{
		"nombre": "est, congue a,",
		"duracion": 119,
		"autor": "Chastity Mcclain",
		"generos": "Jazz Góspel Blues",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "elit, pretium et,",
		"duracion": 154,
		"autor": "Neville Burke",
		"generos": "Blues Country Disco",
		"popularidad": 7,
		"danzabilidad": 2
	},
	{
		"nombre": "varius et, euismod",
		"duracion": 124,
		"autor": "Leah Neal",
		"generos": "Blues Country Disco",
		"popularidad": 2,
		"danzabilidad": 8
	},
	{
		"nombre": "Mauris vestibulum, neque",
		"duracion": 131,
		"autor": "Allegra Crane",
		"generos": "Metal Jazz",
		"popularidad": 6,
		"danzabilidad": 3
	},
	{
		"nombre": "Morbi non sapien",
		"duracion": 7,
		"autor": "Clayton Larson",
		"generos": "Hip-Hop Salsa",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "In at pede.",
		"duracion": 169,
		"autor": "Chelsea Christensen",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 7,
		"danzabilidad": 1
	},
	{
		"nombre": "Quisque fringilla euismod",
		"duracion": 89,
		"autor": "Amal Hines",
		"generos": "K-pop Metal Jazz",
		"popularidad": 1,
		"danzabilidad": 7
	},
	{
		"nombre": "et malesuada fames",
		"duracion": 103,
		"autor": "Emerson Shepherd",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "dolor quam, elementum",
		"duracion": 110,
		"autor": "Palmer Middleton",
		"generos": "K-pop",
		"popularidad": 2,
		"danzabilidad": 6
	},
	{
		"nombre": "turpis. In condimentum.",
		"duracion": 18,
		"autor": "Louis Roy",
		"generos": "Salsa",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "ut nisi a",
		"duracion": 169,
		"autor": "Damon Gonzales",
		"generos": "Country",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "tortor nibh sit",
		"duracion": 77,
		"autor": "Samantha Dale",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 4,
		"danzabilidad": 4
	},
	{
		"nombre": "faucibus leo, in",
		"duracion": 45,
		"autor": "Cherokee Whitfield",
		"generos": "Jazz Góspel Blues Country",
		"popularidad": 5,
		"danzabilidad": 0
	},
	{
		"nombre": "sodales nisi magna",
		"duracion": 166,
		"autor": "Ann Huffman",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 7,
		"danzabilidad": 1
	},
	{
		"nombre": "lorem, luctus ut,",
		"duracion": 118,
		"autor": "Samson Stuart",
		"generos": "Góspel Blues Country",
		"popularidad": 8,
		"danzabilidad": 5
	},
	{
		"nombre": "lobortis tellus justo",
		"duracion": 29,
		"autor": "Whitney Willis",
		"generos": "Góspel Blues Country",
		"popularidad": 7,
		"danzabilidad": 5
	},
	{
		"nombre": "Proin eget odio.",
		"duracion": 88,
		"autor": "Demetrius Sanford",
		"generos": "Disco Techno",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "a, dui. Cras",
		"duracion": 27,
		"autor": "Shad Lott",
		"generos": "Metal",
		"popularidad": 6,
		"danzabilidad": 1
	},
	{
		"nombre": "ridiculus mus. Aenean",
		"duracion": 170,
		"autor": "Colin Mccall",
		"generos": "R&B",
		"popularidad": 2,
		"danzabilidad": 8
	},
	{
		"nombre": "at augue id",
		"duracion": 18,
		"autor": "Hannah Barry",
		"generos": "Disco Techno",
		"popularidad": 4,
		"danzabilidad": 0
	},
	{
		"nombre": "volutpat. Nulla dignissim.",
		"duracion": 169,
		"autor": "Kellie Wyatt",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 3,
		"danzabilidad": 0
	},
	{
		"nombre": "pharetra ut, pharetra",
		"duracion": 3,
		"autor": "Brendan Pugh",
		"generos": "Jazz Góspel Blues",
		"popularidad": 1,
		"danzabilidad": 9
	},
	{
		"nombre": "odio sagittis semper.",
		"duracion": 79,
		"autor": "Cadman Burks",
		"generos": "Pop Clásica",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "justo. Praesent luctus.",
		"duracion": 29,
		"autor": "Rosalyn Bean",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 2,
		"danzabilidad": 2
	},
	{
		"nombre": "Nullam lobortis quam",
		"duracion": 30,
		"autor": "Kenyon Webb",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 4,
		"danzabilidad": 3
	},
	{
		"nombre": "Proin velit. Sed",
		"duracion": 67,
		"autor": "Zane Bailey",
		"generos": "Raeguetton Hip-Hop Salsa R&B",
		"popularidad": 1,
		"danzabilidad": 6
	},
	{
		"nombre": "nisi. Aenean eget",
		"duracion": 8,
		"autor": "Wyoming Reeves",
		"generos": "Blues Country",
		"popularidad": 4,
		"danzabilidad": 10
	},
	{
		"nombre": "Integer in magna.",
		"duracion": 164,
		"autor": "Damian Pierce",
		"generos": "Disco Techno",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "accumsan neque et",
		"duracion": 65,
		"autor": "Ivory Hull",
		"generos": "Salsa R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "Morbi accumsan laoreet",
		"duracion": 10,
		"autor": "Kylynn Jackson",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "nibh lacinia orci,",
		"duracion": 163,
		"autor": "Odessa Weiss",
		"generos": "Bachata Raeguetton Hip-Hop",
		"popularidad": 1,
		"danzabilidad": 4
	},
	{
		"nombre": "vitae, orci. Phasellus",
		"duracion": 21,
		"autor": "Leonard Russell",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 8,
		"danzabilidad": 4
	},
	{
		"nombre": "est. Nunc ullamcorper,",
		"duracion": 119,
		"autor": "Fuller Gilmore",
		"generos": "Pop Clásica",
		"popularidad": 0,
		"danzabilidad": 3
	},
	{
		"nombre": "elit. Curabitur sed",
		"duracion": 46,
		"autor": "Moses Schwartz",
		"generos": "Raeguetton",
		"popularidad": 7,
		"danzabilidad": 0
	},
	{
		"nombre": "scelerisque, lorem ipsum",
		"duracion": 98,
		"autor": "Mason Bowman",
		"generos": "R&B K-pop Metal",
		"popularidad": 9,
		"danzabilidad": 7
	},
	{
		"nombre": "ipsum. Donec sollicitudin",
		"duracion": 173,
		"autor": "Tiger Parks",
		"generos": "Clásica Bachata Raeguetton",
		"popularidad": 10,
		"danzabilidad": 2
	},
	{
		"nombre": "elementum sem, vitae",
		"duracion": 74,
		"autor": "Rudyard Weaver",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 9,
		"danzabilidad": 3
	},
	{
		"nombre": "et nunc. Quisque",
		"duracion": 151,
		"autor": "Pandora Meyers",
		"generos": "R&B K-pop Metal Jazz",
		"popularidad": 9,
		"danzabilidad": 5
	},
	{
		"nombre": "lobortis, nisi nibh",
		"duracion": 64,
		"autor": "Andrew Madden",
		"generos": "Disco Techno",
		"popularidad": 1,
		"danzabilidad": 3
	},
	{
		"nombre": "erat semper rutrum.",
		"duracion": 100,
		"autor": "Aspen Kinney",
		"generos": "Pop Clásica Bachata",
		"popularidad": 10,
		"danzabilidad": 5
	},
	{
		"nombre": "senectus et netus",
		"duracion": 97,
		"autor": "Kennedy Bean",
		"generos": "Jazz",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "a ultricies adipiscing,",
		"duracion": 75,
		"autor": "Wynter Mckee",
		"generos": "Bachata Raeguetton Hip-Hop Salsa",
		"popularidad": 2,
		"danzabilidad": 4
	},
	{
		"nombre": "felis orci, adipiscing",
		"duracion": 61,
		"autor": "Xander Dominguez",
		"generos": "Jazz",
		"popularidad": 9,
		"danzabilidad": 8
	},
	{
		"nombre": "Nulla facilisi. Sed",
		"duracion": 104,
		"autor": "Lael Gallagher",
		"generos": "K-pop Metal",
		"popularidad": 10,
		"danzabilidad": 9
	},
	{
		"nombre": "odio tristique pharetra.",
		"duracion": 88,
		"autor": "Hyatt Marsh",
		"generos": "Góspel Blues Country Disco Techno",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "vitae, posuere at,",
		"duracion": 120,
		"autor": "Rahim Hampton",
		"generos": "Jazz Góspel Blues Country",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "metus. Aliquam erat",
		"duracion": 75,
		"autor": "Warren Ratliff",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "in aliquet lobortis,",
		"duracion": 151,
		"autor": "Sylvia Matthews",
		"generos": "K-pop Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 4
	},
	{
		"nombre": "Aenean eget magna.",
		"duracion": 12,
		"autor": "Nolan Snider",
		"generos": "Country Disco",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "cursus in, hendrerit",
		"duracion": 28,
		"autor": "Megan Blanchard",
		"generos": "Clásica",
		"popularidad": 5,
		"danzabilidad": 1
	},
	{
		"nombre": "libero nec ligula",
		"duracion": 154,
		"autor": "Christen Casey",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 9
	},
	{
		"nombre": "Suspendisse aliquet molestie",
		"duracion": 113,
		"autor": "Priscilla Riggs",
		"generos": "Disco",
		"popularidad": 0,
		"danzabilidad": 9
	},
	{
		"nombre": "sed, sapien. Nunc",
		"duracion": 38,
		"autor": "Hoyt Benson",
		"generos": "Country Disco Techno",
		"popularidad": 1,
		"danzabilidad": 0
	},
	{
		"nombre": "odio a purus.",
		"duracion": 27,
		"autor": "Chastity Berger",
		"generos": "Blues Country Disco",
		"popularidad": 0,
		"danzabilidad": 4
	},
	{
		"nombre": "in, dolor. Fusce",
		"duracion": 136,
		"autor": "Xandra Jennings",
		"generos": "Góspel Blues",
		"popularidad": 10,
		"danzabilidad": 0
	},
	{
		"nombre": "iaculis, lacus pede",
		"duracion": 138,
		"autor": "Dustin Cline",
		"generos": "Pop Clásica Bachata Raeguetton",
		"popularidad": 4,
		"danzabilidad": 10
	},
	{
		"nombre": "magna a neque.",
		"duracion": 16,
		"autor": "Holmes Walter",
		"generos": "Pop",
		"popularidad": 0,
		"danzabilidad": 7
	},
	{
		"nombre": "Phasellus nulla. Integer",
		"duracion": 90,
		"autor": "Shad Carlson",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 8,
		"danzabilidad": 10
	},
	{
		"nombre": "mollis. Duis sit",
		"duracion": 88,
		"autor": "Damon Finch",
		"generos": "Pop Clásica",
		"popularidad": 10,
		"danzabilidad": 3
	},
	{
		"nombre": "velit egestas lacinia.",
		"duracion": 78,
		"autor": "Danielle Gamble",
		"generos": "Metal Jazz",
		"popularidad": 5,
		"danzabilidad": 2
	},
	{
		"nombre": "tempus mauris erat",
		"duracion": 107,
		"autor": "Kareem Daniel",
		"generos": "Hip-Hop Salsa",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "metus. Aliquam erat",
		"duracion": 39,
		"autor": "Malcolm Cabrera",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 0,
		"danzabilidad": 6
	},
	{
		"nombre": "Vivamus euismod urna.",
		"duracion": 133,
		"autor": "Nora Aguilar",
		"generos": "Clásica",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "Phasellus ornare. Fusce",
		"duracion": 129,
		"autor": "Rebekah Sawyer",
		"generos": "Góspel Blues Country Disco",
		"popularidad": 7,
		"danzabilidad": 3
	},
	{
		"nombre": "fringilla euismod enim.",
		"duracion": 72,
		"autor": "Aretha Delaney",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 9,
		"danzabilidad": 5
	},
	{
		"nombre": "scelerisque dui. Suspendisse",
		"duracion": 117,
		"autor": "Hashim Stephenson",
		"generos": "Disco Techno",
		"popularidad": 0,
		"danzabilidad": 8
	},
	{
		"nombre": "facilisis facilisis, magna",
		"duracion": 93,
		"autor": "Noelani Booth",
		"generos": "Country Disco Techno",
		"popularidad": 4,
		"danzabilidad": 2
	},
	{
		"nombre": "imperdiet non, vestibulum",
		"duracion": 10,
		"autor": "Hiram Graham",
		"generos": "Pop Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 3,
		"danzabilidad": 5
	},
	{
		"nombre": "vel nisl. Quisque",
		"duracion": 67,
		"autor": "Keelie Pearson",
		"generos": "Hip-Hop Salsa R&B K-pop",
		"popularidad": 1,
		"danzabilidad": 2
	},
	{
		"nombre": "justo. Proin non",
		"duracion": 53,
		"autor": "Vera Dillon",
		"generos": "Raeguetton Hip-Hop Salsa",
		"popularidad": 8,
		"danzabilidad": 5
	},
	{
		"nombre": "mauris erat eget",
		"duracion": 97,
		"autor": "Eagan Chen",
		"generos": "Clásica Bachata",
		"popularidad": 9,
		"danzabilidad": 1
	},
	{
		"nombre": "In tincidunt congue",
		"duracion": 130,
		"autor": "Graiden Mendez",
		"generos": "Jazz",
		"popularidad": 6,
		"danzabilidad": 8
	},
	{
		"nombre": "ut erat. Sed",
		"duracion": 74,
		"autor": "Callie Mcguire",
		"generos": "Bachata Raeguetton",
		"popularidad": 6,
		"danzabilidad": 9
	},
	{
		"nombre": "lectus, a sollicitudin",
		"duracion": 85,
		"autor": "Ila Aguilar",
		"generos": "K-pop Metal Jazz",
		"popularidad": 3,
		"danzabilidad": 3
	},
	{
		"nombre": "tempus scelerisque, lorem",
		"duracion": 43,
		"autor": "Adam Love",
		"generos": "Rock",
		"popularidad": 2,
		"danzabilidad": 5
	},
	{
		"nombre": "malesuada malesuada. Integer",
		"duracion": 138,
		"autor": "Gillian Goff",
		"generos": "Pop Clásica",
		"popularidad": 4,
		"danzabilidad": 1
	},
	{
		"nombre": "Nulla tempor augue",
		"duracion": 37,
		"autor": "Jeanette Howard",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 7,
		"danzabilidad": 1
	},
	{
		"nombre": "pede, nonummy ut,",
		"duracion": 33,
		"autor": "Cadman Dorsey",
		"generos": "Salsa R&B K-pop",
		"popularidad": 7,
		"danzabilidad": 9
	},
	{
		"nombre": "risus. Morbi metus.",
		"duracion": 63,
		"autor": "Bell Whitley",
		"generos": "K-pop Metal Jazz Góspel",
		"popularidad": 2,
		"danzabilidad": 9
	},
	{
		"nombre": "Suspendisse non leo.",
		"duracion": 62,
		"autor": "Beau Cannon",
		"generos": "Clásica Bachata Raeguetton Hip-Hop",
		"popularidad": 2,
		"danzabilidad": 6
	},
	{
		"nombre": "dis parturient montes,",
		"duracion": 168,
		"autor": "Oren Hays",
		"generos": "Hip-Hop Salsa",
		"popularidad": 4,
		"danzabilidad": 7
	},
	{
		"nombre": "ullamcorper. Duis at",
		"duracion": 133,
		"autor": "Reuben James",
		"generos": "Country Disco Techno",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "enim commodo hendrerit.",
		"duracion": 153,
		"autor": "Zeus Dorsey",
		"generos": "Salsa R&B K-pop",
		"popularidad": 5,
		"danzabilidad": 1
	},
	{
		"nombre": "mauris sapien, cursus",
		"duracion": 46,
		"autor": "Melissa Beach",
		"generos": "Disco Techno",
		"popularidad": 3,
		"danzabilidad": 2
	},
	{
		"nombre": "aliquam iaculis, lacus",
		"duracion": 29,
		"autor": "Kadeem Pitts",
		"generos": "Rock Pop Clásica Bachata",
		"popularidad": 5,
		"danzabilidad": 9
	},
	{
		"nombre": "arcu iaculis enim,",
		"duracion": 8,
		"autor": "Jenna Mclaughlin",
		"generos": "Salsa R&B K-pop Metal Jazz",
		"popularidad": 2,
		"danzabilidad": 10
	},
	{
		"nombre": "lacinia orci, consectetuer",
		"duracion": 134,
		"autor": "Troy Spears",
		"generos": "Jazz Góspel Blues Country",
		"popularidad": 6,
		"danzabilidad": 1
	},
	{
		"nombre": "gravida nunc sed",
		"duracion": 33,
		"autor": "Jaquelyn Evans",
		"generos": "Blues",
		"popularidad": 6,
		"danzabilidad": 1
	},
	{
		"nombre": "iaculis enim, sit",
		"duracion": 113,
		"autor": "Dorian Roy",
		"generos": "Blues Country Disco Techno",
		"popularidad": 10,
		"danzabilidad": 3
	},
	{
		"nombre": "ipsum non arcu.",
		"duracion": 142,
		"autor": "Flynn Roberts",
		"generos": "R&B",
		"popularidad": 7,
		"danzabilidad": 10
	},
	{
		"nombre": "non, vestibulum nec,",
		"duracion": 53,
		"autor": "Reed Rollins",
		"generos": "Góspel Blues",
		"popularidad": 6,
		"danzabilidad": 1
	},
	{
		"nombre": "Quisque varius. Nam",
		"duracion": 55,
		"autor": "Medge Cline",
		"generos": "Jazz Góspel Blues",
		"popularidad": 9,
		"danzabilidad": 6
	},
	{
		"nombre": "adipiscing lacus. Ut",
		"duracion": 167,
		"autor": "Colette Fuller",
		"generos": "Disco",
		"popularidad": 3,
		"danzabilidad": 6
	},
	{
		"nombre": "arcu iaculis enim,",
		"duracion": 82,
		"autor": "Lydia Mays",
		"generos": "Salsa R&B K-pop Metal",
		"popularidad": 3,
		"danzabilidad": 4
	},
	{
		"nombre": "velit eget laoreet",
		"duracion": 159,
		"autor": "Stone Cervantes",
		"generos": "Pop Clásica",
		"popularidad": 1,
		"danzabilidad": 5
	},
	{
		"nombre": "nibh vulputate mauris",
		"duracion": 15,
		"autor": "Vielka Mckee",
		"generos": "Hip-Hop",
		"popularidad": 6,
		"danzabilidad": 6
	},
	{
		"nombre": "risus. In mi",
		"duracion": 16,
		"autor": "Rana Mercado",
		"generos": "Hip-Hop Salsa R&B K-pop Metal",
		"popularidad": 5,
		"danzabilidad": 5
	},
	{
		"nombre": "metus facilisis lorem",
		"duracion": 142,
		"autor": "Ursa Love",
		"generos": "Clásica Bachata",
		"popularidad": 7,
		"danzabilidad": 7
	},
	{
		"nombre": "lobortis. Class aptent",
		"duracion": 91,
		"autor": "Tucker Pate",
		"generos": "Metal Jazz Góspel Blues",
		"popularidad": 3,
		"danzabilidad": 9
	},
	{
		"nombre": "sociis natoque penatibus",
		"duracion": 67,
		"autor": "Fay Hudson",
		"generos": "Raeguetton Hip-Hop",
		"popularidad": 0,
		"danzabilidad": 9
	},
	{
		"nombre": "egestas lacinia. Sed",
		"duracion": 90,
		"autor": "Hedley Ellison",
		"generos": "Pop Clásica",
		"popularidad": 8,
		"danzabilidad": 5
	},
	{
		"nombre": "quis urna. Nunc",
		"duracion": 24,
		"autor": "Brianna Hoover",
		"generos": "Jazz Góspel",
		"popularidad": 7,
		"danzabilidad": 1
	}
]

for reproduccion in reproducciones:
    cancion = canciones[random.randint(0, len(canciones) - 1)]
    usuario = usuarios[random.randint(0, len(usuarios) - 1)]
    reproduccion["usuario"] = usuario
    reproduccion["cancion"] = cancion["nombre"]


with open('reproducciones_final.json', 'w') as file:
    json.dump(reproducciones, file, indent=4)
    file.close

