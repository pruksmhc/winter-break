
 	var xhr = new XMLHttpRequest();
xhr.open('GET', chrome.extension.getURL('inspiration.txt'), true);
var count = 0; 
xhr.onreadystatechange = function()
{
	if(count < 1){
	console.log("AT LEAST HERE "); 
    if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200)
    {
    	console.log("The stories are "+ xhr.responseText);
        //... The content has been read in xhr.responseText
        localStorage["inspiration"] =xhr.responseText.split("//") //an array of inspiraiotnla storeis now. 

    } 


 if (!("Notification" in window)) {
    alert("This browser does not support desktop notification");
  }

  // Let's check if the user is okay to get some notification
  else if (Notification.permission === "granted") {
    // If it's okay let's create a notification
        var arr = localStorage["inspiration"].split("//"); 
        arr = arr[0].split(",");
        var max = arr.length; 
		 console.log("Max is "+max); 
		 do {
      rand = Math.floor(Math.random()*max)
 } while( rand % 2 == 1 );
    	console.log("The rnadomness is "+ rand.toString());
    	console.log("Arr is "+arr); 
    	console.log("First thing is "+arr[0]);
    	var story = arr[rand]; 
    	var body_story = arr[rand+1]; //body is always one ahead. 
    	  localStorage["current"] = body_story;

    	console.log("THe story chosen is "+story+" with body "+body_story);  

    	var options = {
      body:  body_story
  }

    var notification = new Notification(story, options);
  }

  // Otherwise, we need to ask the user for permission
  // Note, Chrome does not implement the permission static property
  // So we have to check for NOT 'denied' instead of 'default'
  else if (Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {

      // Whatever the user answers, we make sure we store the information
      if(!('permission' in Notification)) {
        Notification.permission = permission;
      }

      // If the user is okay, let's create a notification
      if (permission === "granted") {
      	 var arr = localStorage["inspiration"].split("//"); 
        arr = arr[0].split(",");
        var max = arr.length; 
		 do {
      rand = Math.floor(Math.random()*max)
 } while( rand % 2 == 1 );
    	var story = arr[rand]; 
    	var body_story = arr[rand+1]; //body is always one ahead. 
    	  localStorage["current"] = body_story;

    	console.log("THe story chosen is "+story+" with body "+body_story);  

    	var options = {
      body:  body_story
  }

    var notification = new Notification(story, options);
  }
 
    });
  }
  count++; 
  console.log("OUT HERE IS "+body_story);
  localStorage["current"] = body_story;
}
};
xhr.send();

chrome.runtime.onMessage.addListener(function(message,sender,sendResponse){
	console.log("WOAH"); 
  if(message.method == "getStory"){
    //depending on how the word is stored you can do this in one of several ways
    // 1. If it is a global variable, we can just return it directly
    sendResponse({story: localStorage["current"]});
    // 2. It needs to be retrieved asynchronously, in that case we do this
    return true;
    // This passes the ability to reply to the function where we get the info
    // Once we have the info we can just use sendResponse(word); like before
  }
});

