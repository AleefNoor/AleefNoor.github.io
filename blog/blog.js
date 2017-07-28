class BlogEntry {
	constructor(name, blogtext){
		this.name= name;
		this.blogtext= blogtext;

	}
}

function addEntryToBlog() {
  //Create new blog entry
  var name =document.getElementById("blogEntryName").value;
  var blog = document.getElementById("blogEntryText").value;
  var blogEntry = new BlogEntry(name, blog );


  //Add the new entry, name and date to the blog
  createBlogEntryElement(blogEntry);
  createFooterElement(blogEntry);

  //Clear the inputs
  document.getElementById("blogEntryName").value = "";
  document.getElementById("blogEntryText").value = "";

}

function createBlogEntryElement(blogEntry) {
	var bloggerblog = blogEntry.blogtext;
	Newdivs= document.createElement('div');
	Newdivs.classname= "blogentry"
	Newdivs.innerHTML = bloggerblog;
	blogDetails.appendChild(Newdivs);

}

function createFooterElement(blogEntry) {
	var bloggername= blogEntry.name
	Newdivs= document.createElement('div');
	Newdivs.className= "blogDate";
	Newdivs.innerHTML = "by " + bloggername + " on " + Date();
	blogDetails.appendChild(Newdivs);
}
