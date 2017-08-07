/*
INSTRUCTIONS:

1. Create a list of 5 names of girls
2. Store 3 friends for each of these 5 girls
3. When the user enters the name of a girl from the list,
   and clicks "Get Friends" display friends of that girl
*/

/*ENTER CODE HERE*/
var frnds= {
	"Aleef": [ "Innath", " Farzana", " Abigail"],
	"Innath": ["Aleef", " Moky", " Nusrat"],
	"Melinda": ["Boba", " Katy", " Moca"],
	"Rebecca":["Bella", " Josephine", " Aleef"],
	"Abigail": ["Aleef", " Faith", " Koka"],
};

function getFriends() {
var getfrnds = document.getElementById('friends');
var userinput= document.getElementById('nameInput').value;
var input= frnds[userinput];
getfrnds.innerHTML = input;
}

/*EXTENSION*/

function addFriend() {
var gname= document.getElementById('nameOfGirl').value;
var fname= document.getElementById('nameOfFriend').value;
frnds[gname].push(fname);
}
