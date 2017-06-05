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


