# Μάθημα: Τεχνολογία Λογισμικού

### Ονοματεπώνυμο: Ιωάννης Πανόπουλος
### Αριθμός Μητρώου: Π2019217
### Edpuzzle Profile: [P2019217](https://asciinema.org/~P2019217)
### Github Profile: [P2019217](https://github.com/P2019217)<br><br>

# Παραδοτέο 1
*Εισαγωγή*</br>
Το μάθημα πιστεύω θα με βοηθήσει αρκετά μιας και θέλω να ασχοληθώ με το ethical hacking και γίνεται στην περιοχή του Github που είναι μία περιοχή που έχει και αρκετά repositories για ethical hacking όπως πχ.airgeddon. Επιπλέον θα με βοηθήσει να μάθω συστήματα πέρα από το systemd, μιας και τα Kali Linux που χρησιμοποιώ, χρησιμοποιούν το systemd. Επιπλέον οι ασκήσεις γραμμής εντολών πιστεύω θα με βοηθήσουν αρκετά και ειδικά η άσκηση με το [NTFY[telegram]](https://github.com/dschep/ntfy) μιας και θα μπορώ να ενημερώνομαι με μήνυμα μόλις μια διεργασία τελειώσει π.χ ένα [nmap](https://github.com/nmap/nmap) scan σε κάποιον server με πολλά ports. Τέλος θα βοηθηθώ στο να έχω μια πιο πλήρη κατανόηση του τρόπου λειτουργίας των Unix based συστημάτων.

[Discussions](https://github.com/courses-ionio/sw/discussions/1172)

# Παραδοτέο 2
*Γραμμή εντολών*</br>
Tο systemd υπάρχει εγκατεστημένο στα Kali Linux μιας και Debian based επομένως χρησιμοποίησα αυτό για την άσκηση,έτσι δημιούργησα ένα πρόγραμμα σε Bash που σκανάρει για ανοιχτά ports στο 192.168.1.1 (router), αποθηκεύει το scan σαν αρχείο txt και έπειτα διαβάζει αυτό το αρχείο txt, το αποθηκεύει σαν μεταβλητή message και χρησιμοποιεί το [NTFY[telegram]](https://github.com/dschep/ntfy) για να αποστείλει αυτό το scan σε μήνυμα από το Panopoulos_bot στο κινητό μου.
[![asciicast](https://asciinema.org/a/NN2x9lToaRAJ85A7SbWFiPKx2.svg)](https://asciinema.org/a/NN2x9lToaRAJ85A7SbWFiPKx2)


Παρακάτω βλέπετε το nmapscantomsg.sh:
```bash
#!/bin/bash
#Κάνει nmap σκαν και δημιουργεί στο directory που βρίσκεται ένα αρχείο message.txt
nmap -oG $(pwd)/message.txt 192.168.1.1
#Διαβάζει με το cat το αρχείο message.txt και το αποθηκεύει σε μία μεταβλητή $message
message=$(cat message.txt)
#Χρησιμοποιεί το ntfy[Telegram] προκειμένου να αποστείλει το περιεχόμενο της μεταβλητής $message
ntfy -b telegram send "$message"
```
Το μηνύματα στο Telegram σε screenshot:

![screenshot](https://user-images.githubusercontent.com/100226514/220226677-2ceeafb8-51dd-444f-9cc8-01e8b54518c4.png)

[Discussions](https://github.com/courses-ionio/sw/discussions/1236)

