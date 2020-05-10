
# Τεχνολογία Λογισμικού

  ## Αναφορά:

Όνομα: Πολίτης Αλέξανδρος
AM: Π2017202


  ## Άσκηση 1 Software
   ## Ntfy
   ### Desktop Notifications
   
   Στην εργασία αυτή εγκαταστήσαμε το [b]ntfy[/b] ώστε να μας εμφανίζει ειδοποιήσεις στο Desktop. Η εγκατάση έγινε με την εντολή:
   >sudo pip install ntfy
   
   Στην συνέχεια στείλαμε μια ειδοποίηση με την εντολή:
   >ntfy send "Hello World, Kalispera!"
   
   ![Pop up](https://imgur.com/m7ejtjm.png)
   
   [Asciinema Link Using ntfy](https://asciinema.org/a/X85kKZL7I0TGkHBEnsKLmGkQT)
   
   ## Άσκηση 2 Software
   ## Terminals
   ### Installing & Using different terminals
   
   Για την εργασία αυτή χρησιμοποιήθηκαν τα terminals [b]st[/b] και [b]zsh[/b] . Η εγκατάση έγινε με τις εντολές:
   
   Zsh:
   >apt install zsh
   
   St:
   >git clone https://github.com/LukeSmithxyz/st
   
   >cd st
   
   >sudo make install
   
  
   ![St terminal](https://imgur.com/RinEULZ.png)
   
   [Asciinema Link Using terminals](https://asciinema.org/a/2591J10vY1jiMJaAd4Ij05lFW)
   
   ## Άσκηση 3 Software
   ## How Do I
   ### Helping to code and more
   
   Το How Do I βοηθάει τον χρήστη να βρεί τις εντολές που του χρειάζονται. Το μόνο που έχει να κάνει είναι να πληκτρολογήσει στο terminal την αναζητησή του και η βοήθεια θα του εμφανιστεί. Για παράδειγμα:
   
   >howdoi convert mp4 to mov
   
   H εγκατάσταση του Howdoi έγινε ως εξής:
   >pip install howdoi
   
   [Asciinema Link HowDoI](https://asciinema.org/a/8eq7TIHolsV4CTNwtDwTHglwM)
   
   ## Άσκηση 4 Software
   ## Python Virtual Enviroment
   ### Creating and setting up a virtual enviroment
   
   Στόχος της εργασίας είναι η δημιουργία εικονικού περιβάλλοντος ώστε να δημιουργήσουμε και να τρέξουμε Python scripts. 
   
   Εγκατάσταση του Pipenv:
   >pip install --user pipenv
   
   Επειδή η εγκατάσταση γίνεται στο --user ώστε να μην δημιουργηθούν προβλήματα στο γενικό σύνολο των πακέτων θα πρέπει να προστεθεί το κατάλληλο PATH στο αρχείο user base:
   >export PATH="$PATH:/root/.local/bin"
   
   Στη συνέχεια δημιουργούμε έναν φάκελο που θα είναι το εικονικό μας project
   >mkdir git_p17poli
   
   >cd git_p17poli
   
   Εγκαθιστούμε τα απαραίτητα πακέτα για το project
   >pipenv install requests
   
   Δημιουργούμε και τρέχουμε ένα αρχείο python
   >cat > p17poli.py
   
   >pipenv run python p17poli.py
   
   [Asciinema Link Python Virtual Enviroment](https://asciinema.org/a/43Pp4bALd9zgYy3MvzaVseyIS)
   
 ## Συμμετοχικό Υλικό

  [Link σελιδας συμμετοχικου](https://alexandrosp38.github.io/gr/)

  [Link αντιγράφου αποθετηρίου](https://github.com/AlexandrosP38/gr)

   Μέρος της εργασίας στην Τεχνολογία Λογισμικού είναι η προσθήκη 2 εικόνων με έλευθερα πνευματικά δικαιώματα στο ["O Προγραμματισμός της Διάδρασης"](https://mibook.org/gr/)
   
  
   [Link 1ης εικόνας](https://alexandrosp38.github.io/gr/gallery/mac-pc/)
   
   [Link 2ης εικόνας](https://alexandrosp38.github.io/gr/gallery/Latex/)
   
   ## Άσκηση 5 Software
   ## Py-Spy
   ### Performance monitoring
   
   Το py-spy δίνει την δυνατότητα να γίνει καταγραφη της αποδοσης καθώς τρέχει ενα python script. Με την εκτέλεση του αρχείου μέσω του command py-spy καταγράφετε η διεργασια PID του αρχειου python και εμφανίζεται σε μορφή εικόνας .svg 
   Στο παράδειγμά μας τρέχουμε ένα αρχείο python που στέλνει sms στο κινητό μας μέσω του twilio:
   
   >py-spy record -o profile.svg -- python send_sms.py
   
   το αποτέλεσμα εμφανίζεται στην εικόνα με κατάληξη .svg
   
   ![py-spy](https://imgur.com/ZI8HYTV.png)
   
   H εγκατάσταση του Py-spy έγινε ως εξής:
   >pip install py-spy

   
   [Asciinema Link py-spy](https://asciinema.org/a/qfZGPa57oXUSgV6Z3z8AvYxFS)
   
   ## Άσκηση 6 Software
   ## Twilio
   ### Call forwarding
   
   Το Twilio δίνει την επιλογή στον χρήστη μέσω τoυ API να διαχειρστεί ένα σύστημα τηλεφωνικών εντολών. Αποστολή και λήψη μηνυμάτων, εκτροπή και απόρριψη κλήσων μέσω του λογαριασμού του χρήστη στο Twilio είναι μερικές απο τις επιλογές που έχει.
   Αρχικά ο χρήστης πρέπει να κάνει έναν λογαριασμο, είτε επι πληρωμή είτε για εκπαιδευτικούς σκοπούς με 14 ημέρες trial μέσω του επίσημου site https://www.twilio.com/
   Στη συνέχεια κάνουμε εγκατάσταση στα linux μέσω terminal
   
   >pip install twilio
   
   Δημιουργούμε στην συνέχεια ενα αρχείο python με όνομα send_sms.py στο οποίο μέσα πρέπει να έχουμε τα credentials(acount_sid και auth_token) που μας δίνονται στην Console του Twilio account καθώς και το κινητό που θα έρθει το δοκιμαστικό μήνυμα.
   
     from twilio.rest import Client
     # Your Account SID from twilio.com/console
     account_sid = "xxxxxxxxxxxx"
    # Your Auth Token from twilio.com/console
    auth_token  = "xxxxxxxxxxxxxxxxxxxxxx"
    client = Client(account_sid, auth_token)
     message = client.messages.create(
     to="+30698xxxxxx", 
    from_="+13602268931",
    body="Hello from Python!")
    print(message.sid)
   
  Τρέχουμε την εντολή μέσα απο τον φάκελο ως εξής:
  
  >python send_sms.py

  
