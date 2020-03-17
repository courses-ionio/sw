# Μάθημα: Τεχνολογία Λογισμικού
#
## Προσωπικά Στοιχεία:
#### A.M: Π2017080
#### Όνομα: Ελευθέριος
#### Επώνυμο: Μπαΐλης
#
### Προαπαιτούμενα: 
##### α) Εγκατάσταση Ubuntu σε Virtual Machine
#
##### β)Εγκατάσταση Python
###### sudo apt-get update
###### sudo apt install python
#
##### γ) Αλλαγή του .bashrc ώστε το Terminal να εμφανίζει το ΑΜ
###### cd ~
###### nano .bashrc
###### Πρόσθεση της εντολής  export PS1='P2017080:\w$ ' στο τέλος και CTRL+O για αποθήκευση
#
##### δ) Δημιουργία λογαριασμού στο Asciinema και εγκατάσταση του εργαλείου με την εντολή:
###### sudo apt-get install asciinema
#
### Άσκηση 1(Set-up cloud services)
#### Local Host Προαπαιτούμενα
###### Το εργαλείο SSH είναι ήδη εγκατεστημένο στα Kali Linux
#### Remote Host Προαπαιτούμενα
###### sudo apt-get install openssh-server 
#### Σύνδεση με τον Remote Host
###### ssh sleft@192.168.1.81
###### cd ~
###### mkdir dummy
###### cd dummy
###### cat > sample.txt
#### Link για Asciinema 
#
### Άσκηση 2(Choose Your Stack)
#### Εγκατάσταση howdoi
###### pip install howdoi
#### Εκτέλεση 
###### howdoi declare list in python
###### howdoi -a create random numbers java //-a για πλήρη προβολή του κειμένου
###### howdoi -n 3 free memory in c //-n NUM_ANSWERS προβολή NUM_ANSWERS απαντήσεων
###### howdoi -e duckduckgo allocate memory in c //Προβολή απαντήσεων από το duckduckgo
#### Link για Asciinema
#
### Άσκηση 3(send notifications to your desktop-mobile)
#### Εγκατάσταση ntfy
###### sudo pip install ntfy
#### Εκτέλεση
