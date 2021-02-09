
/*
*	Author: Morgan Barnes
*	Date:   09.29.2020
*		  
*	Javascript Document for TVDash
*	
*	Filename:  script.js
**/

function updateAll(){
	updateClock();
	getWeather();
	getNews();
	updateThermos(parseURL('Sales'),parseURL('WIP'));
}

// parseURL() takes a parameter and parses the URL of the current document 
// 				and returns the value of that parameter if found, else it	
//				returns null;
function parseURL(param){
	var value; //holds value of parameter
	
	//gets the URL of the current page
	const URL = window.location.search;
	
	//sets a URLSearchParams object instance.
	const urlParams = new URLSearchParams(URL);
	
	//Sets the first value associated with the given search parameter.
	value = urlParams.get(param);
	
	return value;
}


//updateClock() gets the month, day, year and appends them to display mm/dd/yyyy
//				gets hours, minutes, seconds and appends them to display hh:mm:ss in military time
function updateClock(){
	var dt = new Date();
	
	var month = (("0"+(dt.getMonth()+1)).slice(-2));
	
	var day = (("0"+dt.getDate()).slice(-2));
	
	var year = (dt.getFullYear());
	
	document.getElementById("date").innerHTML = month + "/" + day + "/" + year;
	
	var hour = (("0"+dt.getHours()).slice(-2));
	
	var min = (("0"+dt.getMinutes()).slice(-2) );
	
	var sec = (("0"+dt.getSeconds()).slice(-2) )
	
	document.getElementById("time").innerHTML = hour + ":" + min + ":" + sec;
}


// getNews() fetches an RSS feed and reads the data into <td> elements
function getNews()
{
const RSS_URL = `https://cors-anywhere.herokuapp.com/https://www.wmur.com/topstories-rss`;
			fetch(RSS_URL)
			.then(response => response.text())
			.then(str => new window.DOMParser().parseFromString(str, "text/xml"))
			.then(data => { console.log(data);
						var items = data.querySelectorAll("item"); //gets item tags from rss feed
						var newTd; //holds td element
						var newContent; //holds textnode for title
						var newLink; //holds link element
						var link; //holds link to each news article 
						var title; //holds news title
						items.forEach(el =>
						{
							//set as title from news article
							title = el.querySelector("title").innerHTML;
							
							//set as link from article 
							link = el.querySelector("link").innerHTML;
							
							//create a <a> element to link to article
							newLink = document.createElement("a");
							
							//create a <td> element to hold link
							newTd = document.createElement("td");
							
							//create a textnode to display title
							newContent = document.createTextNode(title);
							
							//set the href attribue to the link of the article
							newLink.href = link;
							
							//makes link open in new page
							newLink.target = "_blank"
							
							//puts text node in <a> element
							newLink.appendChild(newContent);
							
							//puts link in <td> element
							newTd.appendChild(newLink);
							
							//appends each <td> element into a table element with the id "marquee"
							document.getElementById("marquee").appendChild(newTd);
						});
					});

}

// getWeather() gets weather widget. idk how i didnt actually 
//              write it... so like.. dont touch it.
function getWeather()
{
	!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];
		if(!d.getElementById(id)){js=d.createElement(s);
		js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';
		fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
}

// updateThermos() Takes 2 parameters and adjusts the thermostats accordingly
function updateThermos (salesInput, wipInput) 
{
	//varibles for new text
	var newSalesTxt;
	var newWIPTxt;
	
	//varibles for elements
	var salesGoalTxt = document.getElementById("salesg");
	var salesFill = document.getElementById("salesgh");
	var wipGoalTxt = document.getElementById("wipg");
	var wipFill = document.getElementById("wipgh");
	
	//creates new text for sales thermos
	newSalesTxt = document.createTextNode(salesInput + "%");
	newWIPTxt = document.createTextNode(wipInput + "%");
	//displays new value 
	salesGoalTxt.appendChild(newSalesTxt);
	wipGoalTxt.appendChild(newWIPTxt);
	//adjust height of value
	salesGoalTxt.style.bottom = salesInput + "%";
	wipGoalTxt.style.bottom = wipInput + "%";
	//chages the fill to new value
	salesFill.style.height = salesInput + "%";
	wipFill.style.height = wipInput + "%";
}

function modal()
{
	// Get the modal
	var modal = document.getElementById("update");

	// Get the button that opens the modal
	var btn = document.getElementById("updateBtn");

	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("close")[0];

	// When the user clicks on the button, open the modal
	btn.onclick = function() {
	  modal.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	  modal.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	  if (event.target == modal) {
		modal.style.display = "none";
	  }
	}
}