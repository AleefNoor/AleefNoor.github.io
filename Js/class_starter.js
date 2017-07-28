class person {
	constructor (first_name, last_name, address){
		this.first_name= first_name;
		this.last_name= last_name;
		this.address= address; 
	} Fullname( ) {
		document.getElementById('myName').innerHTML= this.first_name + this.last_name;

	} Address() {
	document.getElementById('myAddress').innerHTML=	this.address;
	}
}; 

var Aleef= new person(" Aleef ", "Noor", "90-15, afi street");
Aleef.Fullname();
Aleef.Address();