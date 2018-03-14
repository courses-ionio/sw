# Οπτικοποίηση δεδομένων χορηγιών (UK) 
## Αφεντούλης Κωνσταντίνος Π2015021

*Forked Software Technologies repository: https://github.com/p15afen/sw*
 
*Forked DataVisualisation repository: https://github.com/p15afen/D3js-uk-political-donations*

*Personal DataVisualisation Github Page: https://p15afen.github.io/D3js-uk-political-donations/*

# Παραδοτέο 1
## Ζητούμενα στα οποία απαιτούνται αλλαγές στο προσωπικό μας αποθετήριο.

* Ο σύνδεσμος της σελίδας μου με την εφαρμογή: https://p15afen.github.io/D3js-uk-political-donations/ .

* Για την απαλοιφή της κατάληξης "/full-viz.html" στο url της εφαρμογής, αρκεί να μετονομάσουμε το αρχείο full-viz.html σε index.html.

* Αλλαγή χρωμάτων(μπάλες) στο αρχείο chart.js στα σημεία: 

  ```
  var fill = d3.scale.ordinal().range(["#9a32cd", "#000000", "#ffff00"]);
  ```


* Αλλαγή των χρωμάτων στα πεδία του *Split by party* στο αρχείο style.css:
  
  ```
  /*  Party view */
   #conservative, #labour, #libdem { padding: 10px; }
   #conservative {
     background: rgba(66, 133, 244, 0.2);
     top: 110px;
   }
   #labour {
      background: rgba(116, 33, 87, 0.2);
     top: 330px;
    }
    #libdem {
     background: rgba(242, 97, 131, 0.2);
     top: 550px;
  }
  ```



* Προστέθηκε ήχος στα κουμπιά της εφαρμογής μέσω ενός ανεβασμένου αρχείου sound.mp3.
    Χρησιμοποίθηκε ένα script στο αρχείο index.html στα σημεία:


  ```
  <script>
       var button_sound = new Audio();                                                 			
	    button_sound.src = "sound.mp3";                                                 			
           </script>
  ```
  
  
  ```
            <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="all-donations">All money</a>
            </li>
            <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-money-source">The public's purse</a>
            </li>
            <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-party">Split by party</a>
            </li>
            <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-donor-type">Split by type of donor</a>
            </li>
	          <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-amount">Split by amount</a>
            </li>
  ```    
  
  
  * Προστέθηκε δυνατότητα αναζήτησης κάνωντας κλικ πάνω σε κάθε μια από της μπάλες.
     
     Οι αλλαγές πραγματοποίθηκαν στο αρχείο chart.js στο σημείο:
 
 
 ```
  .on("mouseover", mouseover)
	.on("click", function(d) { window.open("http://www.google.com/search?q=" + d.donor);})
  .on("mouseout", mouseout);
  ```
  
  
  * Προστέθηκε μεγενθυτικός φακός όταν ο χρήστης μετακινεί τον κέρσορα του πάνω από κάποιο κέιμενο.
     
     Οι αλλαγές έγιναν στο αρχείο style.css με την προσθήκη της function zoom στο σημείο:
     
  
  ```
  .zoom{
      -webkit-transition: font-size .4s;
      transition: font-size .4s;
  }
  .zoom:hover{
      font-size : 1.8em;
 }
  ```
 
 
 και στο αρχείο index.html σε όποιο σημείο θέλουμε να δουλεύει:
  
  π.χ.
  
  
  ```
   <h2 class = "zoom">Political donations and funding accepted by the Conservatives, Labour and Liberal Democrats between the 2010 general election and August 2013, when this data was collected.</h2>
             <p class = "zoom">Each circle represents the total amount donated by a single donor group, funding organisation or individual during that period.</p>
             <p class = "zoom">Hover over a circle to show further information.</p>

             <p class = "zoom">Get an immediate overview of how party funding is shaped in Britain today by selecting one of the options at the top of the page.</p>
             <p class = "zoom">Data is based on all reportable donations over &#163;7500.</p>
             <p class = "zoom">Data source: <a href="http://www.electoralcommission.org.uk/">The Electoral Commission.</a>
   </p>
  ```
  
  
  * Προστέθηκε εκφώνηση του δωρητή και του ποσού της δωρεάς κατά την μετακίνηση του κέρσορα πάνω από κάποια μπάλα.
    
    Οι αλλαγές έγιναν στο αρχείο chart.jss στα σημεία του mouseover:
  
  
  ```
   responsiveVoice.speak(donor + amount); 
  ```
   
   και του mouseout:
  
  
  ```
   responsiveVoice.cancel(); 
  ```
  
   
   H βιβλιοθήκη responsiveVoice είναι εξωτερική οπότε τη δηλώνουμε στο τέλος του index.html αρχείου μας.
  
 
 * Επίσης κατασκευάστηκε ένα νέο κουμπί split by amount.
    Οι αλλαγές έγιναν στο αρχείο index.html κάτω από τα υπόλοιπα κουμπιά :
  
  
  ```
  <div id="view-amount-type" >
            
       <h2 class="zoom" style="text-align: center;">Amount of donation</h2>
        <span class="zoom" style="position: relative; left: 5vw; top: 4vh;"> Up to 25.000 British Pounds. </span>    
        <span class="zoom" style="position: relative; left: 5vw; top: 8vh;"> Up to 250.000 British Pounds. </span>
        <span class="zoom" style="position: relative; left: 5vw; top: 12vh;"> Below 10.000.000 British Pounds. </span>
	      <span class="zoom" style="position: relative; left: 5vw; top: 16vh;"> Over 10.000.000 British Pounds.  </span> 	 
   
  </div> 
  ```
  
 
 στο αρχείο chart.jss
  
  
  ```
 if (name === "group-by-amount") 
		  $("#initial-content").fadeOut(250);
		  $("#value-scale").fadeOut(250);
		  $("#view-donor-type").fadeOut(250);
		  $("#view-party-type").fadeOut(250);
		  $("#view-source-type").fadeOut(1000);
		  $("#view-amount-type").fadeIn(250);
		  return amountType();
	
}
  ```
  (Προστέθηκε και ένα fade out από το group-by-amount στα υπόλοιπα if της transition().)
  
  ```
  function amountType() {
	force.gravity(0)
		.friction(0.75)
		.charge(function(d) { return -Math.pow(d.radius, 2.0) / 3; })
		.on("tick", amounts)
		.start();
} 
  ```
  
  Στο σημείο .on("tick", amounts) καλείται η amounts()
  
  
  ```
  function amounts(e) {
	node.each(moveToAmounts(e.alpha));


		node.attr("cx", function(d) { return d.x; })
			.attr("cy", function(d) {return d.y; });
}
  ```
 
 Η μετακίνηση των σφαιρών γίνεται με τον εξής τρόπο:
  
  
  ```
  function moveToAmounts(alpha) {
	    return function(d) {
		    var centreY = entityCentres[d.entity].y;
		    var centreX = entityCentres[d.entity].x;
		      if (d.value <= 25000) { 
			      centreX = svgCentre.x ;
			      centreY = svgCentre.y;
		        }else if (d.value <= 250000) { 
			      centreX = svgCentre.x + 150;
			      centreY = svgCentre.y;
		        }else if (d.value <= 9999999){ 
			      centreX = svgCentre.x + 300;
			      centreY = svgCentre.y;
		        }else{
			      centreX = svgCentre.x + 450;
			      centreY = svgCentre.y;
		        }

		  d.x += (centreX - d.x) * (brake + 0.02) * alpha * 1.1;
		  d.y += (centreY - d.y) * (brake + 0.02) * alpha * 1.1;
	    };
  }
  ```
  
  και τελικώς οι αλλαγές στο style.css στο σημείο:
   

```
 /* Initial appearance on load */
#view-party-type, #view-donor-type, #view-source-type, #view-amount-type {
    display: none;
}
 ```
  
