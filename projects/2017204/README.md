### ΤΕΧΝΟΛΟΓΙΑ ΛΟΓΙΣΜΙΚΟΥ
### Ονοματεπώνυμο: Χρήστος Δήμας
### Α.Μ.: Π2017204

### Άσκηση 1:
Assignment: try different terminals and shells.

Για να γίνει η διεκπεραίωση της εργασίας αυτής έκανα τη χρήση 5 διαφορετικών τέρμιναλς (guake, konsole, tilda, yuakake και terminology) και έγινε η εγκατάσταση αυτών με τις παρακάτω εντολες:

```
 $ sudo apt-get -f install guake
 $ sudo apt-get -f install tilda
 $ sudo apt-get -f install yakuake
 $ sudo apt-get -f install terminology
```
Για την επίδειξη του κάθε τέρμιναλ χρησιμοποίησα απλές εντολές, οποίες περιγράφονται στο αντίστοιχο βίντεο του aasciinema, δημιουργώντας κάθε φορά ένα φάκελο με το όνομα του κάθε τέρμιναλ και μέσα σε αυτόν ένα αρχείο python με όνομα hello.py και με έξοδο κατα την εκτέλεσή του "hello world!!!". Κατά την καταγραφή της διαδικασίας του εκάστοτε τέρμιναλ χρησιμοποίηθηκε το asciinema και ένα αντίστοιχο στιγμιότυπο "screenshot" για την επίδειξη του αποτελέσματος, καθώς στα βίντεο δεν καταγράφονται τα χρώματα και άλλα χαρακτηριστικά του κάθε τέρμιναλ.

### guake: είναι ένα τέρμιναλ, όπου ο χρήστης το μετακινεί στο πάνω ή στο κάτω μέρος της οθόνης, πατώντας το πλήκτρο F12 και είναι γραμένο σε python. Τέλος, ο χρήστης μπρεί να αλλάξει την εμφάνισή του καθώς επίσης και να αλλάξει και τα διάφορα πλήκτρα με βάση τις ανάγκες του.

### Asciinema URL: [guake](https://asciinema.org/a/gzz8Ei9dT3bhcdFgyLtzcKjJL)

### Εικόνα του τέρμιναλ "guake".

![guake](https://user-images.githubusercontent.com/44117722/77182803-02c17580-6ad6-11ea-91d3-7c7b98f7de32.png)

### tilda: είναι ένα τέρμιναλ, που δεν καταλαμβάνει ολόκληρη την οθόνη, αλλά έχει το χαρακτηριστικό να μετακινείς το τέρμιναλ στο πάνω ή στο κάτω μέρος της οθόνης, χρησιμοποιώντας το F1 πλήκτρο. Επίσης, υπάρχει το χαρακτηριστικό ότι ο χρήστης μπορεί να αλλάξει την εμφάνισή του, αλλάζοντας τον φόντο του τέρμιναλ. Τέλος, υπάρχει η δυνατότητα αλλαγής πλήκτρων με βάση τις ανάγκες μας.

### Asciinema URL: [tilda](https://asciinema.org/a/uvMgNoIrHYh0yVr9nNxMCmAid)

### Εικόνα του τέρμιναλ "tilda".
![tilda](https://user-images.githubusercontent.com/44117722/77183469-09042180-6ad7-11ea-96c0-6284ef2dced0.png)


### yakuake: είναι ένα τέρμιναλ, το οποίο μετακινείται στο πάνω και στο κάτω μέρος της οθόνης, πατώντας το πλήκτρο F12. Αποτελεί ένα ελαφρύ τέρμιναλ με πολλά χαρακτηριστικά και γρήγορο ευρετήριο.

### Asciinema URL: [yakuake](https://asciinema.org/a/Aed4S6XajE9Kpk4JY3N7JCLyu)
### Εικόνα του τέρμιναλ "yakuake".
![yakuake](https://user-images.githubusercontent.com/44117722/77183870-a3fcfb80-6ad7-11ea-8182-59f7714f9e1d.png)


### terminology: είναι ένα τέρμιναλ, το οποίο δεν καταλαμβάνει όλη την οθόνη, μπορεί να διαμορφωθεί όσον αφορά την εμφάνιση του χρησιμοποιώντας διάφορα χρώματα και εικόνες σαν φόντο. Χαρακτηριστικό του είναι ότι δεν μπορεί να εμφανίσει άλλα αρχεία ή λίνκς και γενικότερα εφαρμογές, οποίες λειτουργούν σε άλλο γραφικό περιβάλλον.  

### Asciinema URL: [terminology](https://asciinema.org/a/FmQ6j8i9HLt1avNbnj608mFON)
### Εικόνα του τέρμιναλ "terminology".
![terminology](https://user-images.githubusercontent.com/44117722/77184148-0d7d0a00-6ad8-11ea-808d-c4abc4beb09b.png)

### Στη συγκεκριμένη εργασία έγινε η εγκατάσταση και η χρήση του shell "fish" και η επίδειξη του με βίντεο μέσω του asciinema. Χρησιμοποίηθηκε για την δημιουργία ενός φακέλου με το όνομα "fish" και η δημιουργία σε αυτόν ένα αρχείο hello.py, όπου δίνει το αποτέλεσμα "hello world!!!". Για την εγκατλασταση χρησιμοποιήθηκαν κατά σειρα οι παρακάτω εντολές:
```
 1) $ sudo apt-add-repository ppa:fish-shell/release-3
 2) $ sudo apt-get update
 3) $ sudo apt-get install fish
```
### Asciinema URL: [fish](https://asciinema.org/a/nlhsWjVWQEb320ttdMNeLMPv3)

Για να χρησιμοποίησει ο χρήστης το shell fish πρέπει να πατήσει την εντολή fish. Έπειτα μπορεί να βρεί αρκετές πληροφορίες όσον αφορά τις εντολές χρήσης πατώντας την ακόλουθη εντολή:

```
~> man set
```


### References

[fishshell](https://launchpad.net/~fish-shell/+archive/ubuntu/release-3)
[terminals](https://linuxhint.com/best_terminal_aternatives_ubuntu/)

---

### Άσκηση 2:
Assignment: performance monitoring.

Για να γίνει η εγκατάσταση του hyperfine έγραψα τις παρακάτω εντολές στο τέρμιναλ:

```
 1) $ wget https://github.com/sharkdp/hyperfine/releases/download/v1.9.0/hyperfine_1.9.0_amd64.deb
 
 2) $ sudo dpkg -i hyperfine_1.9.0_amd64.deb
```

Για την εκπόνηση της εργασίας αυτής χρησιμοποιήθηκαν δύο python scripts, ώστε να γίνει παρακολούθηση των αρχείων αυτών κατά την εκτέλεσή τους. Πιο συγκεκριμένα, χρησιμοποιήθηκαν τα αρχεία example1.py και example2.py, όπου με την χρήση της παρακάτω εντολής βγήκαν κάποια αποτλέσμαατα όσον αφορά τον χρόνο εκτέλεσής τους (ελάχιστο, μέγιστο, μέσο χρόνο και μαζί με την τυπική απόκλιση).

```
 $ hyperfine 'pyhton3 example1.py' 'python3 example2.py'
```

### Asciinema URL: [hyperfine](https://asciinema.org/a/Hlyjysq7KhFegTIvReVB16Fu9)

Ακόμη, υπάρχει η δυνατότητα τα αποτελέσματα να εξαχθούν σε εξωτερικό αρχείο, για παράδειγμα σε αρχείο output.csv και αυτό επιτεύχθηκε με την παρακάτω εντολή:

```
 $ hyperfine --export-csv output 'pyhton3 example1.py' 'python3 example2.py'
```
### Τα αποτελέσματα στο αρχείο output.csv
![hyperfine](https://user-images.githubusercontent.com/44117722/76889676-af111b00-688e-11ea-91ba-aab67618e128.png)

### References

[Hyperfine](https://github.com/sharkdp/hyperfine)

---
### Άσκηση 3:
Assignment: set-up cloud services.

### Για να γίνει η εγκατάσταση του OpenSSH έγραψα αρχικά την παρακάτω εντολή:
```
 $ sudo apt-get install openssh-server
```
Για να γίνει η επιβεβαίωση ότι η εγκατάσταση ήταν επιτυχής έγραψα την παρακάτω εντολή, όπου είδα στο τέρμιναλ το μήμυμα Active: active (running):

```
 $ sudo systemctl status ssh
```
Το επόμενο βήμα ήταν να ενεργοποιήσω το "firewall" του συστήματος με την παρακάτω εντολή:
```
 $ sudo ufw allow ssh
```
Τέλος, για την σύνδεση δύο συστημάτων χρησιμοποίησα την παρακάτω εντολή:
```
 $ ssh username@ip_address
```
Όπου το username είναι το όνομα του συστήματος και ip_address είναι η διεύθυνση και βρίσκονται από την παρακάτω εντολή:
```
 $ ip a
```

Στη συγκεκριμένη εργασία χρησιμοποίησα ένα λάπτοπ με λειτουργικό Ubuntu 16.04 και ένα Raspberry pi 4 με λειτουργικό Raspbian. Αφού πρώτα έκανα όλη την παραπάνω διαδικασία σχετικά με την εγκατάσταση χρησιμοποίησα το username του Raspberry pi 4 και την διευθυνση ip, όπως φαίνεται παρακάτω.


![myscreen](https://user-images.githubusercontent.com/44117722/76658074-f2f8dd00-657b-11ea-9328-5248f4648c49.png)

Στη συνέχεια χρησιμοποίησα την παρακάτω εντολή για τη σύνδεση των δύο συστημάτων:
```
 $ ssh pi@192.168.1.21
```
Αφού λοιπόν έγινε η σύνδεση των δύο συστημάτων, από το τέρμιναλ του λειτουργικού συστήματος Ubuntu εκτέλεσα το αρχείο cv με nano cv, το οποίο ήταν αποθηκευμένο στο Raspberry pi 4. Όλη η διαδικασία περιγράφεται παρακάτω στο βίντεο:

### Asciinema URL: [openSSH](https://asciinema.org/a/WjQ1cvKtJcGpUtuwJ34ZUYIes)

Όπως φαίνεται στο παραπάνω βίντεο, άνοιξα το cv αρχείο, το οποίο είναι αποθηκευμένο στο raspaberry pi και στο οποίο μπορούσα να κάνω οποιαδήποτε αλλαγή επιθυμούσα δηλαδή να προσθέσω και να αφαιρέσω γραμμές από το αρχείο. Με τον ίδιο τρόπο μπορώ να τροποποιήσω και άλλα αρχεία απομακρυσμένα ή να δημιουργήσω νέα, χωρίς καμία δυσκολία.

### References

[openSSh](https://linuxize.com/post/how-to-enable-ssh-on-ubuntu-18-04/)

---

### Άσκηση 4:
Assignment: send notifications to your desktop-mobile.

### Για να γίνει η εγκατάσταση του Ntfy έγραψα την παρακάτω εντολή:

```
 $ sudo pip install ntfy
```
Το επόμενο βήμα ήταν να ενεργοποιήσω τα μηνύματα και να στέλνονται μετά την ολοκλήρωση της κάθε εργασίας. Αυτό πραγματοποιήθηκε γράφωντας την παρακάτω εντολή στο .bashrc με nano .bashrc:

```
 eval "$(ntfy shell-integration)"
```
Για να πραγματοποιήσω την εργασία κατέβασα ένα βίντεο από το youtube με τη χρήση του youtube-dl όπως φαίνεται στο παρακάτω βίντεο που έφτιαξα. Με την ολοκλήρωση του κατεβάσματος του βίντεο στάλθηκε μήνυμα ότι ολοκληρώθηκε η διεργασία του κατεβάσματος όπως φαίνεται παρακάτω.

![ntfy3](https://user-images.githubusercontent.com/44117722/76169046-5ef2d400-617d-11ea-95f7-e25dab899b56.png)

### Asciinema URL: [ntfy](https://asciinema.org/a/yrLNEWHwtuYB7RuSYbHD79F6Q)

### Όταν κατέβηκε το αρχείο βίντεο εμφανίστηκε το μήνυμα πάνω από το τέρμιναλ.
![Screenshot from 2020-03-08 19-50-25](https://user-images.githubusercontent.com/44117722/76168422-6c598f80-6178-11ea-92da-c9378161fe24.png)

### References

[ntfy](https://github.com/dschep/ntfy)

---

### Άσκηση 5:
Assignment: create a docker image for your development stack.

### Για να γίνει η εγκατάσταση του docker ακολούθησα τα παρακάτω βήματα κατά σειρά:

```

1) $ sudo apt-get update

2) $ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    
3) $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4) $ sudo apt-key fingerprint 0EBFCD88

5) $ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
6) $ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
### Δημιουργία image Apache σε php με το Docker:
 Αρχικά δημιούργησα ένα αρχείο index.php σε ένα φάκελο που τον ονόμασα docker και χρησιμοποίησα το docker για να δημιουργήσω μία εικόνα "image" του Apache σε php χρησιμοποιώντας την παρακάτω εντολή:
 
```
 
 $ docker run -d -p 80:80 --name my-apache-php-app -v "$PWD":/var/www/html php:7.2-apache
 
```

### Asciinema URL: [docker](https://asciinema.org/a/2WotEN86jJDNILA4YkEDPTSC6)

### Με τη δημιουργία "εικόνας" Apache στο docker, μπορούμε να παμε στον browser Mozila Firefox και γράφοντας localhost εμφανίζεται ότι γράψαμε στο αρχείο index.php:

![Screenshot from 2020-03-02 22-22-39](https://user-images.githubusercontent.com/44117722/75714499-81e03c80-5cd4-11ea-988b-7d6d2700c3c3.png)

### Κάποιες χρήσιμες εντολές είναι οι παρακάτω:

Container που τρέχει.
```
 $ docker ps
```
Containers που τρέχουν ή είναι ανενεργά.
```
 $ docker ps -a
```
Τερματίζω ένα conatainer.
```
 $ docker stop "id"
```
Σβήνω ένα container αφού πρώτα το σταματήσω με την παραπάνω εντολή.
```
 $ docker rm "id"
```
Βλέπω όλα τα "images"
```
 $ docker images
```
Σβήνω ένα "image".
```
 $ docker rmi "id"
```
### References

[docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
[dockerhub](https://hub.docker.com/_/php)

---

