# Author: P2014170 Alexandros Kalavitis


Course : SW


Project: Sentiment Analysis on Twitter


GitHub Repo Link: https://github.com/KALALEX/twitter-stream-globe


App Link: https://testappglobething.herokuapp.com/


## Paradoteo 1 & 2


Changes:

* Made it work with encrypted hashes for the tokens.
* Removed extra \ in page html file (error).
* Fixed a bug where browser threw errors with null references when tweets have no GPS coordinates.
* Changed color bandwith between 10 colors (for tweet-items && average sentiment && beacons).
  * Colors from bad sentiment to good:
    * #FF0000
    * #FF5A00
    * #FF9000
    * #FFCD00
    * #FFFF00
    * #CDFFFF
    * #CEFF00
    * #ABFF00
    * #8BFF00
    * #51FF00
    * #00FF00
* Created function getAvgSentimentState so that average sentiment changes color because it's an average number and most of the time between -1 and 1.
* Translated Words:
  * kickback
    * ανάκρουση
    * αμοιβή για κάποια υπηρεσία
    * αμοιβή για υπηρεσία
    * δωροδοκία
    * δωροδοκία για υπηρεσία
    * δωροδοκία για υπηρεσία
    * προμήθεια
  * kickbacks
    * μίζες
  * kidnap
    * απαγωγή
  * kidnapped
    * απαχθείς
  * kidnapping
    * απαγωγή
  * kidnappings
    * απαγωγές
  * kidnaps
    * απαγάγει
  * kill
    * σκοτώνω
    * θανατώνω
    * φονεύω
    * εξουδετερώνω
    * φόνος
  * killed
    * σκότωσε
  * killing
    * φόνος
  * kills
    * σκοτώνει
  * kind
    * είδος
    * κατηγορία
    * γένος
    * ποικιλία
    * φιλόφρων
    * καλός
    * ευγενικός
    * αγαθός
    * ευνοϊκός
    * περιποιητικός
  * kind of
    * περίπου
  * kinder
    * ευγενικότερος
    * ποιό ευγενικός
  * kindness
    * καλοσύνη
    * καλωσύνη
    * αγαθότητα
    * αγαθότης
  * kiss
    * φιλί
    * φίλημα
  * kudos
    * δόξα
    * φήμη
  * lack
    * lack
    * έλλειψη
    * στέρηση
    * στερούμαι
    * έχω έλειψη
    * έχω έλειψη από
  * lackadaisical
    * αδιάφορος
    * άτονος
    * βαρυεστημένος
    * ψευδοαισθηματικός
  * lag
    * καθυστέρηση
    * επιπορεία
    * κατάδικος
    * χασομερώ
    * βραδύνω
    * χρονοτριβώ
    * καθυστερώ
  * lagged
    * με χρονική υστέρηση
  * lagging
    * μόνωση
    * βραδύτης
    * βραδύνων
  * lags
    * υστερήσεων
  * lame
    * κουτσός
    * χωλός
    * καθιστώ χωλόν
    * απαράδεκτος
  * landmark
    * ορόσημο
    * διακριτικό σημείο
    * αξιοθέατο
  * lapse
    * μεσολάβηση
    * παραγραφή
    * ολίσθημα
    * πταίσμα
    * πάροδος χρόνου
    * παραγράφω
    * ολισθαίνω
    * σφάλλω
    * υποπίπτω
  * lapsed
    * ληξιπρόθεσμος
  * laugh
    * γέλιο
  * laughed
    * γελασα
  * laughing
    * γελώ
    * γελώς
    * γελών
    * γελάω


## Paradoteo 3


* Changed Globe Texture to /images/world.jpg
  * [file](https://github.com/KALALEX/twitter-stream-globe/blob/report/public/javascripts/TwitterStreamGlobe.js)
  * line: 61
* Changed Globe Rotation Speed to 0.314 from 0.005
  * [file](https://github.com/KALALEX/twitter-stream-globe/blob/report/public/javascripts/TwitterStreamGlobe.js)
  * line: 174
* Restricted Beacon Tweets to Australia
  * [file](https://github.com/KALALEX/twitter-stream-globe/blob/report/public/javascripts/TwitterStreamGlobe.js)
  * line: 129



## Paradoteo 4


* Changed 3D earth to 2D earth map
  * [heroku link](https://testappglobething.herokuapp.com/)
  * [file](https://github.com/KALALEX/twitter-stream-globe/blob/report/public/javascripts/TwitterStreamGlobe.js)
  * line to : var sphereGeometry = new THREE.PlaneGeometry(1500, 1500, 32);
* Saving to a database [php script](https://github.com/KALALEX/twitter-stream-globe/blob/report/public/php/insert_to_db.php). Because github does not support backend (php etc...) in order to save something you need to run this on a server (apache... etc) in combination with a database. You can also do it with javascript client side to server but you need connection configuration on the client which is unsafe for you database. For this example I used MySQL-Apache calling making an ajax request with post to the php script passing lat and lot. In order for this to work you need a database named:db_tweets, a root user with no password based on this configuration and a table tweets with rows:
  * id(int, pk, AI)
  * lon (float), lat(float)
Also you need to call the following code from the point you want to insert the data to the database.

```javascript
var request;
$request = $.ajax({
        type: 'POST',
        data: {
        lat: $lat,
        lon: $lon
        },
        url: 'insert_to_db.php'
        });
```
