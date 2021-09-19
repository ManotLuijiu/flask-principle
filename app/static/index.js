console.log('JavaScript is running');

var tag = document.createElement('p');
var text = document.createTextNode('*** Flask Tutorial ***');
tag.appendChild(text);
var element = document.getElementById('new');
element.appendChild(tag);
