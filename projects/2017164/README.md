# Σιδεράς Γεώργιος

## AM : Π2017164

## 1η Άσκηση : 

Assignment : send notifications to your desktop-mobile.
Deliverables : send a notifcation when a big task completes, eg download, compiling, etc.  
Σύνδεσμος των εντολών στο Asciinema : 
Εργαλεία που χρησιμοποίησα :
notify(ntfy) : https://github.com/dschep/ntfy
Εφαρμογη για το κινητο : 
Pushbullet : https://www.pushbullet.com
Περιγραφή : Αρχικά κατέβασα το ntfy με την εντολή
$sudo pip3 install ntfy 
και πρόσθεσα ως extra dependencies το pid και το pushbullet με τις εντολές 
$pip3 install ntfy[pid] 
$pip3 install ntfy[pushbullet].
Στην συνέχεια κατεβασα το app για το smartphone pushbullet και εκανα εγραφη και σύνδεση , έπειτα πήγα -> settings -> account και μετα πατησα να μου δωσει ενα access token.Στο termina δημιουργησα ενα αρχειο με την εντολη 
$sudo nano ~/.ntfy.yml
και μέσα έγραψα : 
backends:
    - pushbullet
pushbullet:
    access_token: o.QTyuazAvmXQE9pp0D8eDCiRcayFigQ21ο
 στο acces token εβαλα αυτο που πηρα απο την εφαρμογη.)



