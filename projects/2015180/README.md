# Οπτικοποίηση δεδομένων χορηγιών (UK) 
## Ανδρεάνα Στυλίδου Π2015180

*Forked Software Technologies repository: https://github.com/andreanastil/sw*
 
*Forked DataVisualisation repository: https://github.com/andreanastil/D3js-uk-political-donations*

*Personal DataVisualisation Github Page: https://andreanastil.github.io/D3js-uk-political-donations/*

*Link στην ιστοσελίδα της ΤΕΛΙΚΗΣ ΑΝΑΦΟΡΑΣ:  https://andreanastil.github.io/sw-report/*

# Παραδοτέο 1
## Ζητούμενα στα οποία απαιτούνται αλλαγές στο προσωπικό μας αποθετήριο

* Ο σύνδεσμος της σελίδας μου με την εφαρμογή: https://andreanastil.github.io/D3js-uk-political-donations/ .
Αφού ενεργοποιηθεί το GitHub Pages, φτιάχνουμε κλαδί gh-pages από τα αρχεία του οποίου ο σύνδεσμος τραβάει τις αλλαγές .

* Για την απαλοιφή της κατάληξης ".html" στο url της εφαρμογής, αρκεί να μετονομάσουμε το αρχείο full-viz.html σε index.html.


* Για την αλλαγή των χρωμάτων στις μπάλες με τα δεδομένα τροποποιούμε τον κώδικα στο chart.js

  ```
  var fill = d3.scale.ordinal().range(["#F88379", "#002E62", "#8C92AC"]);
  ```
  Για την αλλαγή των χρωμάτων στα τρία πεδία ομαδοποίησης *Split by party* τροποποιούμε τον κώδικα στο style.css
  
  ```
  /*  Party view */
  #conservative, #labour, #libdem { padding: 10px; }
  #conservative {
      background: rgba(0, 46, 98, 0.2);
      top: 110px;
  }
  #labour {
      background: rgba(248, 131, 121, 0.2);
      top: 330px;
  }
  #libdem {
      background: rgba(140, 146, 172, 0.2);
      top: 550px;
  }
  ```
* Για να ακούγεται ήχος κάθε φορά που πατάμε ένα κουμπί ομαδοποίησης, αρκεί να διαλέξουμε ένα ηχητικό κλιπ.
  Κατεβάζουμε ένα mp3 αρχείο από το διαδίκτυο: 

  ![download mp3 click sound](https://user-images.githubusercontent.com/22656813/31944348-6d9ea0aa-b8d4-11e7-82a2-1b131ccf83c2.PNG)


  Ανεβάζουμε το αρχείο στο repository και εισάγουμε ένα script tag στο index.html

  ```
  <script>		
    
    var button_sound = new Audio("coin-drop-4.mp3");
        
    
  </script>
  ```
  καθώς και τον κώδικα 
  ```
  onmousedown="button_sound.play()"
  ```
  σε κάθε μία από τις ετικέτες &lt;a&gt;&lt;/a&gt; της λίστας των κουμπιών  

  ```
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="all-donations">All money</a>
  </li>
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-money-source">The public's purse</a> 
  </li>
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-party">Split by party</a>
  </li>
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-donor-type">Split by type of donor</a>
  </li>
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-amount">Split by amount of donation</a>
  ```    
* Για να ανοίγει ένα νέο παράθυρο όταν κάνουμε κλικ σε κάποια μπάλα, με το αποτέλεσμα google search για τον δωρητή της μπάλας αυτής,
  τροποποιούμε το chart.js.
  
  Ορίζουμε μία νέα συνάρτηση click(d)
  
  ```
  function click(d) {
	var donor = d.donor;
	window.open("https://www.google.com/search?q=" + donor) ;
  }
  ```
  η οποία δέχεται σαν όρισμα τα δεδομένα της μπάλας και με τη βοήθεια της window.open ανοίγει ένα παράθυρο google search με
  κατάληξη το όνομα του εκάστοτε δωρητή.
  
  Ύστερα, χρησιμοποιούμε τη συνάρτηση on μαζί με τη συνάρτηση που φτιάξαμε και την εισάγουμε κάτω από τις υπόλοιπες (μέσα στη συνάρτηση
  start)
  
  ```
  .on("mouseover", mouseover)
  .on("mouseout", mouseout)
  // Alternative title based 'tooltips'
  // node.append("title")
  //	.text(function(d) { return d.donor; });
  .on("click", click);
  ```
  Επίσης, θα θέλαμε κάθε φορά που μετακινούμε τον κέρσορα πάνω από κάποια μπάλα, αυτός να μετατρέπεταi σε χεράκι, ώστε να καταλαβαίνουμε   ότι σε αυτό το σημείο υπάρχει κάποιος υπερσύνδεσμος. Έτσι, εισάγουμε μια γραμμή κώδικα μέσα στον ορισμό της συνάρτησης mouseover(d, i)
  
  ```
  this.style.cursor="hand";
  ```
  
  και αντίστοιχα μία γραμμή στον ορισμό της mouseout()
  
  ```
  this.style.cursor="default";
  ```
  που θα επαναφέρει στον κέρσορα την κανονική του εμφάνιση.
  

* Για το ζητούμενο με τον μεγεθυντικό φακό (αύξηση μεγέθους γραμματοσειράς ανά λέξη του κειμένου) θα χρειαστεί να τροποποιήσουμε πρώτα   το html του κειμένου αυτού, 
  για να μπορούμε να προσδιορίζουμε σε ποια κομμάτια θα γίνει ποια ενέργεια. 

  Στην περίπτωση μας θα θέλαμε να διαχωρίσουμε την κάθε μία λέξη του κειμένου από την άλλη, οπότε θα μας βόλευε να βάζαμε την κάθε μία   λέξη του κειμένου μέσα σε μία ετικέτα &lt;span&gt;&lt;/span&gt;.

  Ύστερα όμως έρχεται το ερώτημα: ποια είναι τα σημεία του κειμένου που χρειάζονται μεγέθυνση; 

  Παρατηρούμε ότι οι τίτλοι (h) είναι όλοι αρκετά μεγάλοι και έντονοι. Τα σημεία που χρειάζονται μεγέθυνση είναι οι παράγραφοι οι         οποίες βρίσκονται ανάμεσα σε ετικέτες &lt;p&gt;&lt;/p&gt;. Άρα θα θέλαμε να βάλουμε την κάθε λέξη της κάθε παραγράφου                   &lt;p&gt;&lt;/p&gt; μέσα σε μία ετικέτα &lt;span&gt;&lt;/span&gt;. 

  Έχοντας στο νου μας τα παραπάνω θα χρησιμοποιήσουμε μία συνάρτηση που μας βολεύει πολύ:

  ```
  $("html").find('p').each(function(){......});
  ```
  Η παραπάνω συνάρτηση βρίσκει την κάθε παράγραφο p μέσα σε όλο το &lt;html&gt;&lt;/html&gt; και για το κάθε ένα p εκτελεί τη συνάρτηση   function. 
  
  Ορίζουμε έτσι τη συνάρτηση function:
  
  ```
  function(){
 	
   var text = $(this).text().split(' ');//Η κάθε μία λέξη της παραγράφου που διαχωρίζεται με κένο από την άλλη μπαίνει στον πίνακα.
   for( var i = 0, len = text.length; i<len; i++ ) { //Στην κάθε μία λέξη προστίθεται μία ετικέτα <span></span>.
   text[i] = '<span onmouseover=(this.style.fontSize="xx-large") onmouseout=(this.style.fontSize="initial") >'+text[i]+'</span>';
   }
     
   paragraphContent = text.join(' '); //Όλο το ανανεωμένο περιεχόμενο του πίνακα περνάει στη μεταβλητή paragraphContent. 
   $(this).html(paragraphContent);//Η συνάρτηση αυτή αντικαταστεί το περιεχόμενο αυτής της παραγράφου με το καινούργιο της μεταβλητής.
   
   
   }
  ```
   Στην κάθε &lt;span&gt;&lt;/span&gt; ετικέτα, προσθέσαμε επί τόπου τις ιδιότητες για την αλλαγή της γραμματοσειράς που θέλαμε.
   
   Έτσι, το τελικό κομμάτι κώδικα είναι: 
   ```
   var paragraphContent = "";
  
   $("html").find('p').each(function(){
 
   var text = $(this).text().split(' ');//
   for( var i = 0, len = text.length; i<len; i++ ) {
   text[i] = '<span onmouseover=(this.style.fontSize="xx-large") onmouseout=(this.style.fontSize="initial") >'+text[i]+'</span>';
   }
          
   paragraphContent = text.join(' ');
   $(this).html(paragraphContent);
   });
   ```
   και το εισάγουμε μέσα στη συνάρτηση start() στο αρχείο chart.js.
   
   Τέλος, στο αρχείο index.html στο &lt;div id="value-scale"&gt; βάζουμε τα ποσά 25k, 50k, 100k, 500k, 1m και αυτά σε ετικέτες &lt;p&gt;&lt;/p&gt; γιατί θέλουμε ο κωδικάς μας να μεγεθύνει και αυτά. 
   
   ```
   <div id="value-scale">
            <div id="f">
                <p>&#8212;UK average salary</p>
            </div>
            <div id="a">
                <p><strong>&#163;25k &#8212;</strong></p>
            </div>
            <div id="b">
                <p><strong>&#163;50k &#8212;</strong></p>
            </div>
            <div id="c">
                <p><strong>&#163;100k &#8212;</strong></p>
            </div>
            <div id="d">
                <p><strong>&#163;500k &#8212;</strong></p>
            </div>
            <div id="e">
                <p><strong>&#163;1m &#8212;</strong></p>
            </div>
    </div>
    ```
* Για να βάλουμε ήχο πάνω από τον κάθε κύκλο που θα λέει την ονομασία του δωρητή και το ποσό της δωρεάς, πρέπει να προσθέσουμε κάποιον   κώδικα μέσα στη συνάρτηση mouseover(d, i), ο οποίος θα πέρνει σαν όρισμα το donor και το amount του κάθε κύκλου. Ο κώδικας αυτός θα     είναι: 
  ```
  responsiveVoice.speak(donor + ' £' + amount);
  ```
  Χρησιμοποιούμε τη βιβλιοθήκη responsiveVoice.
  Εισάγουμε στη παρένθεση της συνάρτησης speak το μήνυμα που θέλουμε να αναπαράγουμε.
  
  Επίσης, βάζουμε και αντιστοίχη γραμμή κώδικα στη συνάρτηση mouseout()
  ```
  responsiveVoice.cancel(); 
  ```  
  που θα σταματάει το μήνυμα όταν το ποντίκι βγαίνει από τον κύκλο, ούτως ώστε να αποτρέψουμε τη συσυσσώρευση πολλών μηνυμάτων προς       αναπαραγωγή.
  
  H responsiveVoice είναι εξωτερική βιβλιοθήκη, γι'αυτό περνάμε τη δηλωσή της στο τέλος του html αρχείου μας. Το link το βρίσκουμε στο https://responsivevoice.org/api/

* Δημιουργούμε μία ακόμα επιλογή ομαδοποίησης των δεδομένων με όνομα Split by amount of donation.
  
  Στο αρχείο index.html "δομούμε" τη νέα μας ομαδοποίηση:
  
  Πρώτα, θα δημιουργήσουμε ένα καινούργιο κουμπί για την παράγραφο της ομαδοποίησης αυτής κάτω από τα υπόλοιπα κουμπιά της λίστας:
  ```
  <li><a href="#" onmousedown="button_sound.play()" role="button" class="pure-button switch" id="group-by-amount">Split by amount of donation</a>
  ```
  
  Φτιάχνουμε ένα κανούργιο &lt;div id="view-donation-amount"&gt; με αντιπροσωπευτικό id και το εισάγουμε κάτω από τα υπόλοιπα             &lt;div&gt; ομαδοποίησης.  
  ```
          <div id="view-donation-amount">
            <h2 id = "amount-title"> Split by amount of donation </h2>
                <div id="amounts-scale">
                      <div id="first">
                            <p><strong>Donations over &#163;1m </strong></p>
                      </div>
                      <div id="second">
                            <p><strong>Donations over &#163;500k </strong></p>
                      </div>
                      <div id="third">
                            <p><strong>Donations over &#163;100k</strong></p>
                      </div>
                      <div id="fourth">
                      <p><strong>Donations over &#163;50k </strong></p>
                      </div>
                      <div id="fifth">
                      <p><strong>Donations over &#163;25k </strong></p>
                      </div>
                      <div id="sixth">
                      <p><strong>Smaller donations </strong></p>
                      </div>  
                </div>
        </div>
  ```
 Το &lt;div&gt; αυτό περίεχει τον τίτλο της ομαδοποίησης μέσα στην ετικέτα &lt;h3&gt;, και 6 φωλιασμένα &lt;div&gt; για τα ποσά βάσει    των οποίων θα γίνει η oμαδοποίηση, με δικά τους μοναδικά ids τα οποία κατόπιν θα μας χρειαστούν για τη μορφοποίηση τους. Τα περιεχόμενα τους τα βάζουμε σε &lt;p&gt; και τα κάνουμε &lt;strong&gt;. 
 
 Στο αρχείο chart.js:

Διαβάζοντας τον κώδικα παρατηρούμε ότι η μετάβαση από το ένα στυλ ομαδοποίσης σε ένα άλλο γίνεται στη συνάρτηση transition(). Θα "πειράξουμε" την transition() και θα της προσθέσουμε ένα επιπλέον if (name === "group-by-amount") {} το οποίο όταν θα επιλέγεται μέσω του αντίστοιχου κουμπιού θα κάνει fade in στο #view-donation-amount που δημιουργήσαμε, fade out σε όλα τα υπόλοιπα # και θα επιστρέφει τη συνάρτηση amountsGroup().

```
if (name === "group-by-amount") {
		$("#initial-content").fadeOut(250);
		$("#value-scale").fadeOut(250);
		$("#view-party-type").fadeOut(250);
		$("#view-source-type").fadeOut(250);
		$("#view-donation-amount").fadeIn(1000);
		$("#view-donor-type").fadeOut(250);
		
		return amountsGroup();
	}
```
Επίσης, βάζουμε ένα fade out από το group-by-amount στα υπόλοιπα if της transition().

Φτιάχνουμε τώρα την amountsGroup(), με τον τρόπο που είναι φτιαγμένες οι αντίστοιχες total, partyGroup, donorType και fundsType :

```
function amountsGroup() {
	force.gravity(0)
		.friction(0.8)
		.charge(function(d) { return -Math.pow(d.radius, 2.0) / 3; })
		.on("tick", amounts)
		.start()
		.colourByParty();
}
```
Στο .on("tick", amounts) καλείται η amounts() την οποία φτίαχνουμε με τον τρόπο των all, parties, entities και types:

```
function amounts(e) {
	node.each(moveToAmounts(e.alpha));

		node.attr("cx", function(d) { return d.x; })
			.attr("cy", function(d) {return d.y; });
}
```
Οι κόμβοι μετακινούνται με τη συνάρτηση moveToAmounts(alpha) την οποία δημιουργούμε. Ορίζουμε ένα σταθερό κέντρο για τη θέση Y των κόμβων και ανάλογα με το value του κάθε κόμβου (το ποσό της δωρεάς) ορίζουμε το X σε μία τιμή που ταιριάζει με τα 6 ποσά που διαλέξαμε νωρίτερα.

```
function moveToAmounts(alpha) {
	return function(d) {
		var centreY = svgCentre.y;
		if (d.value <= 25001) {
				centreX = svgCentre.x + 500;
			} else if (d.value <= 50001) {
				centreX = svgCentre.x + 400;
			} else if (d.value <= 100001) {
				centreX = svgCentre.x + 300;
			} else  if (d.value <= 500001) {
				centreX = svgCentre.x + 200;
			} else  if (d.value <= 1000001) {
				centreX = svgCentre.x + 100;
			} else  if (d.value <= maxVal) {
				centreX = svgCentre.x ;
			} else {
				centreX = svgCentre.x; // εάν το ποσό υπερβαίνει το maxVal πάλι θα μπει μαζί με τα μεγαλύτερα
			}
		
		d.x += (centreX - d.x) * (brake + 0.02) * alpha * 2;
		d.y += (centreY - d.y) * (brake + 0.02) * alpha * 2;
	};
}

```
 Απομένει να αλλάξουμε τη θέση του τίτλου ομαδοποίησης και των 6 ετικετών με τους τίτλους των ποσών στο αρχείο style.css:

```
/*Amounts*/
#amount-title {
    position: absolute; 
    top:25%;
    left: 35%;
}

#first {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 230px;
    width: 93px;
}

#second {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 354px;
    width: 93px;
}

#third {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 475px;
    width: 93px;
}

#fourth {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 599px;
    width: 93px;
}

#fifth {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 705px;
    width: 93px;
}

#sixth {
    font-weight: bold;
    position: absolute;
    top: 200px;
    left: 825px;
    width: 93px;
}
```
και να αποτρέψουμε το #view-donation-amount από το να εμφανίζεται στο load της σελίδας:

```
/* Initial appearance on load */
#view-party-type, #view-donor-type, #view-source-type, #view-donation-amount {
    display: none;
}
```

![page ruler](https://user-images.githubusercontent.com/22656813/33617685-08dd63aa-d9e9-11e7-91ff-78a98fc0a2eb.PNG)
 
*Για βοήθεια κατέβασα ένα extension του chrome που λέγεται Page Ruler και κατάφερα έτσι να βρω τα pixel που ήθελα.* 

## Ζητούμενα στα οποία απαιτούνται αλλαγές (pull request) στο κοινό αποθετήριο του κώδικα

Όπως ζητήθηκε, οι αλλαγές για αυτό το είδος παραδοτέου έγιναν σε ξεχωριστό καθαρό κλαδί (στο master για το παραδοτέο 1).

* Δημιουργήθηκε αρχείο 2015180.csv στο φάκελο participants.

* Τοποθετήθηκαν 5 εικόνες για τους εξής δωρητές:
1. JCB Research-Bamford
2. EUK Consulting
3. Exotix
4. Aggregate Industries
5. IM Group of Companies
  
     οι οποίες πληρούν τις προδιαγραφές: 42x42px, format .ico και οι ονομασίες τους είναι οι επωνυμίες των δωρητών, όπως εμφανίζονται στο     αρχείο με τους δωρητές.
  
    Η δέσμευση των δωρητών έγινε, όπως ζητήθηκε, σε αντίστοιχο σχόλιο του issue του Παραδοτέου 1 και το pull request έγινε δεκτό στο         κεντρικό αποθετήριο.
    
# Παραδοτέο 2

* Για να εμφανίζονται εικόνες δωρητών εντός της ιστοσελίδας, ορίζουμε μία περιοχή στο html αρχείο σε ετικέτα div.
  ```
  <div id="sidebar">
  </div>   
  ```
  Στο αρχείο chart.js, μέσα στη συνάρτηση mouseover() δημιουργούμε τη μεταβλητή http με τη βοήθεια της οποίας προσπαθούμε να               προσπελάσουμε το αρχείο εικόνας   (imagefile) του κάθε δωρητή. Στέλνουμε και ελέγχουμε http αίτημα με τη διεύθυνση της εικόνας έτσι     ώστε εάν αυτή δε βρεθεί να μην         εμφανιστεί καμία εικόνα. Ύστερα ελέγχουμε έαν η εικόνα έχει ήδη προσπελαστεί, έτσι ώστε να       αποφύγουμε διπλότυπες εμφανίσεις. Αυτό το     πετυχαίνουμε διατηρώντας τα ονόματα των δωρητών σε μία λίστα (names[]).Πραγματοποιώντας   τους παραπάνω ελέγχους, δημιουργούμε ένα html   element εικόνας με την εικόνα του δωρητή και διαστάσεις 42x42 και ύστερα το             τοποθετούμε στο div με το id = "sidebar".

  ```
  var http = new XMLHttpRequest();
  http.open('HEAD', imageFile, false);
  http.send();
  if (http.status != 404){
	  if ((names.indexOf(donor) > -1)==false) {

	  var elem = document.createElement("img");	
	  elem.src = imageFile;
	  elem.setAttribute("height", "42");
	  elem.setAttribute("width", "42");
	  document.getElementById("sidebar").appendChild(elem);
	  names.push(donor);	
	  }
  }	
  ```
  Τέλος, προσαρμόζουμε το μέγεθος και τη θέση του sidebar στο style.css:

  ```
  #sidebar {
      position: absolute;
      left: 1100px;
      width: 336px;
  }
  ```
  ![screen](https://user-images.githubusercontent.com/22656813/39389148-943f1fcc-4a8e-11e8-8c5b-71cfd7fc8322.PNG)
  
* Για την δημιουργία καινούργιου γραφήματος οπτικοποίησης των ίδιων δεδομένων, εργάστηκα κυρίως στον υπολογιστή μου μέσω local hosting.
Για αρχή, δημιουργήθηκε καινόυργιο αρχείο html στο αποθετήριο με όνομα [new-D3.html](https://github.com/andreanastil/D3js-uk-political-donations/blob/gh-pages/new-D3.html), καινούργιο αρχείο [pie.js](https://github.com/andreanastil/D3js-uk-political-donations/blob/gh-pages/pie.js) με τον κώδικα των διαγραμμάτων καθώς και το [style2.css](https://github.com/andreanastil/D3js-uk-political-donations/blob/gh-pages/style2.css) το οποίο ουσιαστικά ακολουθεί την ίδια λογική styling με το style.css. Το αρχείο new-D3.html περιέχει τη βασική δομή της ιστοσελίδας, αξιοποιώντας τα χαρακτηριστικά της ήδη υπάρχουσας, όπως είναι τα κουμπιά που εναλλάσσουν ανάμεσα στις επιλογές ομαδοποίησης και το κείμενο. 
Γενικότερα, όλα τα διαγράμματα υλοποιήθηκαν εκ' νέου και για τον σκοπό αυτόν μελετήθηκαν και δοκιμάστηκαν πολλά παραδείγματα γραφημμάτων πίτας που βρήκα online. Όλος ο κώδικας είναι διαθέσιμος στο αρχείο pie.js, αξίζει όμως να σχολιαστεί ο τρόπος με τον οποίο κατασκευάστηκαν οι διαφορετικές επιλογές ομαδοποίησης.
Με το πάτημα του κουμπιού κάθε διαφορετικής επιλογής, καλείται αντίστοιχη συνάρτηση και τα δεδομένα, φορτώνονται από το αρχείο 7500up.csv και μεταβαίνουν στην μεταβλητή data, ενώ πρώτα εφαρμοστεί το κατάλληλο nesting. Παρακάτω φαίνεται πώς γίνεται το nesting για την επιλογή partydisplay(). To key που χρησιμοποιείται είναι το partyname και για το key αυτο αθροίζονται όλα τα ποσοστά δωρεών για τα οποία το key είναι ίδιο. Κατά αυτόν τον τρόπο ύστερα, οπτικοποιόυνται τα γραφήματα των δωρεών ύπο τη μορφή πίτας. Στο τέλος του nesting των δεδομένων καλείται η συνάρτηση myPie η οποία είναι λειτουργεί με τον ίδιο τρόπο για όλα τα γραφήματα. 

```
function partydisplay () {
        d3.csv("data/7500up.csv", function( data) {
        var data = d3.nest()
        .key(function(d) {
          return d.partyname;
        })
        .rollup(function(d) {
          return d3.sum(d, function(g) {
            return g.amount;
          });
        }).entries(data);

        tots = d3.sum(data, function(d) { 
            return d.values; 
            });

          data.forEach(function(d) {
                d.percentage = d.values  / tots;
            });

        return myPie(data);
        });
    }
```
  Ενδεικτικές εικόνες των γραφημάτων της πίτας φαίνονται παρακάτω:
  
![byentity](https://user-images.githubusercontent.com/22656813/39834189-d94a4b7e-53d4-11e8-94a3-d3b1bef97090.PNG)
*Καινούργιο D3 διάγραμμα σε μορφή πίτας (ομαδοποίηση by source)*

![party](https://user-images.githubusercontent.com/22656813/39834105-9fc82f38-53d4-11e8-99b1-9dc5661618c3.PNG)
*Καινούργιο D3 διάγραμμα σε μορφή πίτας (ομαδοποίηση by party)*

![private](https://user-images.githubusercontent.com/22656813/39834282-1e64c2c0-53d5-11e8-830c-e4f5cf6dbcd6.PNG)

*Καινούργιο D3 διάγραμμα σε μορφή πίτας (ομαδοποίηση private/public)*

![amount](https://user-images.githubusercontent.com/22656813/39834280-1e357b3c-53d5-11e8-848e-9f546fae21d8.PNG)
*Καινούργιο D3 διάγραμμα σε μορφή πίτας (ομαδοποίηση by amount)*
  
  
  
  ## Ζητούμενα στα οποία απαιτούνται αλλαγές (pull request) στο κοινό αποθετήριο του κώδικα
  
  Οι αλλαγές πραγματοποιήθηκαν στο κλαδί master.
    
* Έπειτα από δέσμευση του position 13 συμπληρώθηκε το αντίστοιχο κομμάτι κώδικα στο αρχείο index του φακέλου participants. Ο κώδικας       εμφανίζει τα στοιχεία του github account μου (όνομα και εικόνα) και προσθέτει κίνηση στο όνομα. Παρακάτω φαίνεται η εμφάνιση του username και την εικόνας μου στην ιστοσελίδα:

![credits](https://user-images.githubusercontent.com/22656813/39836687-dd4df560-53dc-11e8-8e65-7048f81f6b4b.PNG)

* Έγινε δημιουργία ενός αρχείου [2015180.html](https://github.com/andreanastil/D3js-uk-political-donations/blob/master/participants/2015180.html) στο οποίο χρησιμοποιώντας το API του Github έγινε οπτικοποίηση των contributions που έγιναν από του χρήστες στο κεντρικό αποθετήριο της εργασίας. Παρακάτω φαίνεται η τελική μορφή της ιστοσελίδας:

![insights](https://user-images.githubusercontent.com/22656813/39835753-dc7927d4-53d9-11e8-8028-37c2295ec28e.PNG)
 
    
  Τα pull requests των αλλαγών αυτών, έγιναν δεκτά στο κεντρικό αποθετήριο.
