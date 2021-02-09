function updateAll(){
	updateClock();
	getWeather();
	getNews();
}

//updateClock() gets the month, day, year and appends them to display mm/dd/yyyy
//				gets hours, minutes, seconds and appends them to display hh:mm:ss in military time
function updateClock(){
	let dt = new Date();
	
	let month = (("0"+(dt.getMonth()+1)).slice(-2));
	
	let day = (("0"+dt.getDate()).slice(-2));
	
	let year = (dt.getFullYear());
	
	document.getElementById("date").innerHTML = month + "/" + day + "/" + year;
	
	let hour = (("0"+dt.getHours()).slice(-2));
	
	let min = (("0"+dt.getMinutes()).slice(-2) );
	
	let sec = (("0"+dt.getSeconds()).slice(-2) )
	
	document.getElementById("time").innerHTML = hour + ":" + min + ":" + sec;
}


// getNews() fetches an RSS feed and reads the data into <td> elements
function getNews()
{
const RSS_URL = `https://cors-anywhere.herokuapp.com/https://www.wmur.com/topstories-rss`;
			fetch(RSS_URL)
			.then(response => response.text())
			.then(str => {
				return new window.DOMParser().parseFromString(str, "text/xml");
			})
			.then(data => { console.log(data);
						let items = data.querySelectorAll("item"); //gets item tags from rss feed
						let newTd; //holds td element
						let newContent; //holds textnode for title
						let newLink; //holds link element
						let link; //holds link to each news article
						let title; //holds news title
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

