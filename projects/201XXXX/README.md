## ΠΡΟΣΩΠΙΚΑ ΣΤΟΙΧΕΙΑ:

### Αντρέας Παππούτας
### ΑΜ: Π2017148
### [Github Profile](https://github.com/andreaspappoutas/)

| Εβδομάδα* | Παραδοτέο |
| --- | --- |
| <a href="#P">1</a> |<a href="#P">Φορκ του αποθετηρίου και δημιουργία της σελίδας της αναφοράς με τα προσωπικά στοιχεία σας, της σύνοψης με αυτόν τον πίνακα περιεχομένων, και συγγραφή της εισαγωγής με περιγραφή των αναγκών και των στόχων σας για το αντίστοιχο μάθημα* </a> |
| <a href="#P-1">2</a> |<a href="#P-1"> Άσκηση προγραμματισμού</a> |
| <a href="#P-2">3</a> |<a href="#P-2">  Άσκηση γραμμής εντολών</a> |
| <a href="#P-3">4</a> |<a href="#P-3"> αίτημα ενσωμάτωσης (CSCW, IV) </a> + <a href="#P-3-1">Άσκηση προγραμματισμού </a>  |
|  <a href="#P-4">5 </a> |<a href="#P-4"> Άσκηση γραμμής εντολών</a> |
| <a href="#P-5">6 </a>|<a href="#P-5"> συμμετοχικό περιεχόμενο</a> + <a href="#P-5-1"> Άσκηση προγραμματισμού 3</a> |
| <a href="#P-6">7 </a>|<a href="#P-6">αίτημα ενσωμάτωσης (CSCW, IV)</a> |
| 8 | Άσκηση προγραμματισμού (HCI) ή γραμμής εντολών (SW) |
| <a href="#P-8">9</a> |<a href="#P-8">αίτημα ενσωμάτωσης (CSCW, IV)</a> |
| <a href="#P-7">10</a> | <a href="#P-7">συμμετοχικό περιεχόμενο </a>|
| <a href="#P-8">11</a> |<a href="#P-8"> αίτημα ενσωμάτωσης (CSCW, IV)</a> |
| <a href="#P-10">12</a> | <a href="#P-10">Τελική αναφορά* </a>|

## <a name="P">ΕΙΣΑΓΩΓΗ:</a>
Μέσο της οπτικοποίηση της πληροφορίας προσπαθούμε να δημιουργήσουμε μια διάδραση με τα δεδομένα που έχουμε έτσι ώστε να γίνουν πιο διακριτά. Έχω σαν στόχο να μάθω να οργανώνω με σωστό τρόπο τα δεδομένα σε ένα υψηλότερο επίπεδο. Σκοπός μου είναι να μάθω τεχνικές διαχείρισης τον διάφορων πληροφοριών(γραφικά , εικόνες , βίντεο κτλ) ενώ επίσης να αποκτήσω γνώση στις σύγχρονες τεχνολογίες που χρησιμοποιούνται για τη οπτικοποίηση τους.

---


## <a name="P-1">Παραδοτέο 1</a>
### Άσκηση: Τροποποιήστε τον κώδικα του παραδείγματος προσθέτοντας και οπτικοποιώντας στο ίδιο πλαίσιο περισσότερα από 2 σετ δεδομένων (datasets).


Επέλεξα για άσκηση προγραμματισμού να αλλάξω το visualization dataset. 
Στη άσκηση αυτή αρχικά δήλωσα στη javascript το νέο *"datasetC=[..]"* . 
Στη html δημιούργησα ένα κουμπί ίδιο τα με τα άλλα 2 για το datasetC και άλλαξα μόνο το *onclick* να πηγαίνει στο *triggerDatasetC*. 
Στη συνέχεια δημιούργησα ακριβώς το ίδιο function με αυτό που χρησιμοποιείτε για τα άλλα 2 όπου και το ονόμασα *triggerDatasetC*. 
Σε αυτό το νέο function η μόνη αλλαγή που χρειάζονταν ήτανε στη αρχή το *"var dataset = datasetC"*. 
Στο τέλος εφόσον είχα δηλωμένο ένα νέο datasetC με δικό του function και κουμπί που να πηγαίνει σε αυτό το function τότε μπορούσαμε να απεικονίσουμε 3 dataset.

[Codepen Link](https://codepen.io/andreaspappoutas/pen/ZEOQLvm)

[Link Κώδικα](https://github.com/andreaspappoutas/site/blob/master/_remix/visualization-dataset.md)

[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/visualization-dataset)


## <a name="P-2">Παραδοτέο 2</a>
### Άσκηση: visualize your data |	demo with your git commits history and percipation data per day for the last month from your city.

[Asciinema-Spark](https://asciinema.org/a/367160)

Ξεκίνησα τη πρώτη άσκηση γραμμής εντολών με τη οπτικοποίηση των commits μου στο IV μέσο του εργαλείου spark.
Άρχισα αυτή τη άσκηση με τη εγκατάσταση του spark:
```
sudo sh -c "curl https://raw.githubusercontent.com/holman/spark/master/spark -o /usr/local/bin/spark && chmod +x /usr/local/bin/spark"
```
Έτρεξα μια απλή εντολή για οπτικοποίηση μιας ακολουθίας αριθμών.
```
spark 0 2 4 6 8 10 12
```
Ακολούθως με τη παρακάτω εντολή έκανα εγκατάσταση του git spark ένα εργαλείο με το οποίο μπορούμε να οπτικοποιήσουμε πληροφορίες για το github.

```
curl -L http://cpanmin.us | perl - --sudo App::cpanminus
cpanm App::Git::Spark
```

Έφτιαξα ένα νέο φάκελο όπου και έβαλα μέσα το repository iv και έτρεξα τη παρακάτω εντολή για να δείξω πόσα commits έκανα τις τελευταίες 15 μέρες.
```
git spark --days 15 andreaspappoutas
```


## Βελτίωση άσκησης με χρήση pipelining και shell scripting

### Έφτιαξα 2 διαφορετικούς τρόπους για χρήση shell scripting και pipelining. Στο πρώτο τρόπο κάνω spark από ένα οποιοδήποτε αρχείο csv τη στήλη που θέλω. Στο δεύτερο τρόπο κάνω spark τα commits οποιουδήποτε συγγραφέα θέλω.

### [Asciinema-Spark Shell&PipeliningCSV](https://asciinema.org/a/368965)
 Για το παράδειγμα έκανα χρήση των δεδομένων: [Πίνακας πλήθους Ελλήνων εκλογέων ανά εκλογικό διαμέρισμα (Δημοτικές - Περιφερειακές εκλογές 2010)](https://geodata.gov.gr/en/dataset/plethos-ellenon-eklogeon-ana-eklogiko-diamerisma-demotikes--periphereiakes-ekloges-2010/resource/b67372da-aa78-4de1-ba76-9bb792c179c1)


### [Asciinema-Spark Shell&Pipelining Git Commits](https://asciinema.org/a/369127)
Έκανα χρήση του d3 σε αυτό το παράδειγμα εφόσον είχε περισσότερα commits.






### CSV Spark:
Μέσο shell scripting και pipelining πιάνω ένα αρχείο csv, δίνω όνομα της στήλης που θα ήθελα να κάνω σε γράφημα και εμφανίζετε στο τέλος μέσο της εντολής spark.
Για να γίνει αυτό έφτιαξα 2 shell script.
Η τελική εντολή είναι η παρακάτω:
```
bash Script1.sh https://WEBSITE.COM/OURFILE.csv | xargs -t bash Script2.sh "COLUMN_TO_SPARK" | xargs -t cut -d ',' -f | sed "s/[^0-9]//g" | spark
```
#### Script1.sh :
```
#!/bin/bash

curl -o output.csv $1
echo output.csv
```
#### Script2.sh
```
#!/bin/bash

colnames=$(head -n 1 < $2)
colnames2=$( echo -e "$colnames" | tr  ' ' '_'  )
arr=(${colnames2//,/ })


for item in ${arr[@]}; do
	etoimo=$(echo "$item" | tr -d '"')
	count=$((count+1))
   if [ "${etoimo}" == "${1}" ]; then
     echo "$count"
   fi
done
echo "$2"
```
Η ιδέα είναι μέσο του ονόματος της στήλης που θέλω από ένα csv να εμφανίζονται τα αποτελέσματα.
Στο Script1.sh μέσο του cURL κατεβάζω το πρώτο argument που δίνει ο χρήστης εφόσον είναι σύνδεσμος και το αποθηκεύω σαν output.csv. Έτσι το Script.1 χρησιμοποιείτε όπως παρακάτω:
```
bash Script1.sh https://WEBSITE.COM/OURFILE.csv 
```
Στο Script2 το πρώτο argument που θα δίνετε θα είναι το όνομα της στήλης που θέλουμε να φτιάξουμε το γραφημά μας άπο τα δεδομένα της και το δεύτερο θα είναι το όνομα του αρχείου. Έτσι ξέρω ότι $1 = όνομα στήλης και $2 = αρχείο. Το Script1 δεν είναι απαραίτητο αν έχεις ήδη κατεβασμένο το αρχείο csv.
Αρχικά παίρνω τους τίτλους της κάθε στήλης. Αντικαθιστώ οποιοδήποτε κενό με το χαρακτήρα "_" εφόσον μου δημιουργούσε προβλήματα. Τέλος το χωρίζω ανά κόμμα μέσα σε ένα πινάκα.
```
colnames=$(head -n 1 < $2)
colnames2=$( echo -e "$colnames" | tr  ' ' '_'  )
arr=(${colnames2//,/ })
```

Ακολούθως μέσο ενός for loop βλέπω το κάθε τίτλο ξεχωριστά σαν ένα item. Φεύγω το χαρακτήρα " για ευκολία στη σύγκριση στο if και δημιουργώ ένα counter για να ξέρω σε ποια στήλη είμαι.
```
etoimo=$(echo "$item" | tr -d '"')
	count=$((count+1))
```

Στο if ελένχω αν έχω τη στήλη που δόθηκε. Αν το argument 1, δηλαδή το όνομα της σειράς που δίνετε, είναι ίδιο με οποιοδήποτε από τους τίτλους μέσα στο πίνακα τότε το τυπώνουμε το αριθμό της για να το χρησιμοποιήσουμε στο επόμενο πρόγραμμα του pipe.
```
if [ "${etoimo}" == "${1}" ]; then
     echo "$count"
   fi
```

Τελειώνοντας με το αρχείο αυτό τυπώνω το όνομα του csv εφόσον θα είναι χρήσιμο για τα επόμενα προγράμματα.
```
echo "$2"
```
Χρήση του Script2. Χρήση xargs για περισσότερο έλενχο.
```
xargs -t bash Script2.sh "COLUMN_TO_SPARK"
```
Μετά μεσώ του cut έφυγα όλα τα δεδομένα εκτός της σειράς που επιλέξαμε:

```
xargs -t cut -d ',' -f
```
*Αμέσως μετά το -f θα ακολούθηση ο αριθμός της σειράς που τυπώσαμε πιο πάνω εάν βρέθηκε και το όνομα του αρχείου.*


Τέλος μέσο του sed φέυγω όλα τα γράμματα και αφήνω μόνο τους αριθμούς. Τρέχω τα αποτέλεσμα μέσο pipelining στο spark.
```
 sed "s/[^0-9]//g" | spark
```
  
<br/>
<br/>
<br/>
  
### Github Commits Spark:
Έφτιαξα 2 script. Το πρώτο φέρνει το log.csv ενώ το δεύτερο βρίσκει τη συχνότητα commits κάθε μέρας για το συγγραφέα που θα δώσουμε.
Το τελικό command:
```
bash log.sh "repository" "siggrafeas" | awk '{print $3,$4,$6}' log.csv > log2.csv | bash deutero.sh | 
sed "s/[^0-9]//g" | spark
```

#### log.sh:
```
#!/bin/bash

cd ~ && cd repositories && cd $1 && git log --pretty=format:'%h;%an;%ad;%s' --author=$2 > ~/sparkTouGithub/log.csv
```
#### deutero.sh
```
#!/bin/bash

tr -s ' ' '_' < log2.csv > log3.csv
tr -s ' ' '\n' < log3.csv | uniq -c -d | cut -b 1-7
```

Αρχικά στο log.sh μέσο του cd πάω στο φάκελο με τα git clones. Το πρώτο argument που έχουμε θα είναι το όνομα του repository έτσι και θα μπούμε στο φάκελο αυτού.
```
cd ~ && cd repositories && cd $1
```

Μετά μέσο του git log περνούμε τα commits σε μορφή csv και αποθηκεύουμε το αρχείο στο φάκελο που έχουμε τα 2 shell scripts. Ξέρουμε οτι το δεύτερο argument που θα δοθεί θα είναι το όνομα του συγγραφέα.
```
git log --pretty=format:'%h;%an;%ad;%s' --author=$2 > ~/sparkTouGithub/log.csv
```

Ακολούθως με το awk παίρνω τη τρίτη,τέταρτη και έκτη στήλη εφόσον αυτές δείχνουν την ημερομηνία commit που μας ενδιαφέρει. Το αποτέλεσμα το στέλνω στο αρχείο log2.csv.
```
awk '{print $3,$4,$6}' log.csv
```

Στο deutero.sh ξεκινώ με αντικατάσταση των κενών με το χαρακτήρα "_" εφόσον θα χρειαστεί να βρούμε duplicates.
```
tr -s ' ' '_' < log2.csv > log3.csv
```

Βρίσκουμε τη συχνότητα της κάθε ημερομηνίας έτσι ώστε να χρησιμοποιηθεί πιο μετά για δημιουργία γραφήματος μέσο του spark.
```
tr -s ' ' '\n' < log3.csv | uniq -c -d
```

Τελειώνοντας με το script αυτό κάνουμε cut τα πρώτα 7 bytes. Το αποτέλεσμα του command tr πιο πάνω μας έδινε δίπλα από της συχνότητες και τη ημερομηνία κάτι που δεν χρειαζόμαστε για το spark.
```
cut -b 1-7
```

Τέλος κρατώ μόνο τους αριθμούς μέσο του sed και τρέχω τα αποτελέσματα μέσω pipelining στο προγραμμα spark.
```
sed "s/[^0-9]//g" | spark
```

## <a >Παραδοτέο 3</a>
## <a name="P-3">Αίτημα ενσωμάτωσης 1</a>
### Αρχικά έφτιαξα ένα issue όπου έβαλα τις πιο κάτω αλλαγές:
### [Issue #8](https://github.com/ioniodi/sitegr/issues/8)
Άλλαξε ο καθηγητής του μαθήματος "Λογικός Προγραμματισμός". </br>
Άλλαξε ο καθηγητής του μαθήματος "Πολυμέσα" . </br>
Εισαγωγή του νέου μαθήματος "Οπτικοποίηση της Πληροφορίας" στο εξάμηνο 'Ε . </br>
Εισαγωγή του νέου μαθήματος "Ασφάλεια Λογισμικού και Εφαρμογών" στο εξάμηνο ΄Ζ . </br>

Εφόσον έπιασα green light έκανα τις αλλαγές και δημιούργησα το pull request </br>
### [Pull Request](https://github.com/ioniodi/sitegr/pull/11)

### Αποτελέσματα:
### [Λογικός Προγραμματισμός](https://andreaspappoutas-sitegr.netlify.app/courses/logic-programming/)
### [Πολυμέσα](https://andreaspappoutas-sitegr.netlify.app/courses/multimedia/)
### [Οπτικοποίηση της Πληροφορίας](https://andreaspappoutas-sitegr.netlify.app/courses/data-visualization/)
### [Ασφάλεια Λογισμικού και Εφαρμογών](https://andreaspappoutas-sitegr.netlify.app/courses/software-security/)
</br>
</br>

## <a name="P-3-1">Άσκηση προγραμματισμού keyboard input</a>

### Άσκηση 1: Τροποποιήστε το παράδειγμα έτσι ώστε όταν το αυτοκίνητο κινείται όπισθεν να έχει μικρότερη (τη μισή) ταχύτητα από το όταν κινείται έμπροσθεν.
### Άσκηση 2: Δημιουργείστε περιμετρικά όρια έτσι ώστε το αυτοκίνητο να μη βγαίνει ποτέ έξω από την πίστα.

Για τη άσκηση 1 βρήκα στο κώδικα javascript το "onkeydown" όπου και βλέπουμε ανά πόσα pixels αλλάζει το αυτοκίνητο όταν το κάθε κουμπί είναι πιεσμένο. Τα κουμπιά είναι γραμμένα με το κωδικό τους κάτι που μπορεί να βρεθεί εύκολα από αυτή τη [σελίδα](https://keycode.info).
```
if (key == 37) dx=-4; else if (key == 38) dy=-4; else if (key == 39) dx=4; else if (key == 40) dy=4;
```
Η όπισθεν είναι το κουμπί με το αριθμό 40 έτσι το αλλάζουμε να σε 2.
```
if (key == 40) dy=4
```

Στη άσκηση 2 αρχικά πρέπει να φτιάξουμε ένα function για το κάθε άξονα που θα ελέγχει αν το αυτοκίνητο είναι μέσα στα όρια του canvas.
```
function testX(x){
  if((x<1000) && (x>0)){
    return true;
  }
  else return false;
}

function testY(y){
  if((y<800) && (y>0)){
    return true;
  }
  else return false;
}
```
Αν είναι μέσα στα όρια επιστρέφει true αλλιώς false
Μέσο του ίδιου σκεπτικού φτιάχνουμε function για όταν το αυτοκίνητο είναι εκτός ορίων.
}
```
function AllagiX(x){
  if(x>=1000){
    x=x-1;
    //x=1; diaforetiko
    return x;
  }
  else if(x<=0){
    x=x+1;
    //x=999;
    return x;
  }
}
function AllagiY(y){
  if(y>=800){
    y=y-1;
    return y;
  }
  else if(y<=0){
    y=y+1;
    return y;
  }
}
}
```
Αν βγει εκτός ορίων αριστερά η πάνω από το canvas του προσθέτουμε ενώ αντίθετα αν είναι δεξιά ή κάτω του αφαιρούμε.
Τέλος συνδυάζουμε αυτά τα 2 functions με 2 απλά if όπου εφόσον έχουμε true δεν χρειάζεται να γίνει αλλαγή στη τοποθεσία του αυτοκινήτου έτσι δεν καλούνται οι function για αλλαγή.
```
if(testX(x)){
    x = x - dy * Math.cos(angle * Math.PI / 180);
  }
    else{
      x = AllagiX(x);
    }
    
  if(testY(y)){
    y = y - dy * Math.sin(angle * Math.PI / 180);
  }
    else{
      y = AllagiY(y);
    }
```
[Codepen Link](https://codepen.io/andreaspappoutas/pen/YzWwgMW)

[Link Κώδικα](https://github.com/andreaspappoutas/site/blob/master/_remix/keyboard-input.md)

[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/keyboard-input/)


## <a name="P-4">Παραδοτέο 4</a>
## Άσκηση: generate plots	create plots for your data from some other course or project
Χρήση δεδομένων από covid-19
COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University
https://github.com/CSSEGISandData/COVID-19
# [Asciinema MatPlotLib](https://asciinema.org/a/370795)
Έγινε χρήση shell scripting, pipelining και python. Μέσο του shell script κατεβάζω τα δεδομένα από το github. Μέσο του python φτιάχνω το plot. Εφόσον τα δεδομένα είναι πολλά το περισσότερο pipelining έγινε μέσα στο πρόγραμμα.
Οι 2 εντολές χρησιμοποιούνται όπως παρακάτω. Ο χρήστης δίνει τη χώρα που θέλει στο bash script και στο python script δίνει το όνομα για το plot του.
```
bash covid.sh COUNTRY_NAME

python covid.py CHART_NAME
```

Για υλοποίηση αυτής της άσκησης εγκατέστησα το MatPlotLib με τη παρακάτω εντολή.
```
python -m pip install -U matplotlib
```

## Το αρχείο covid.sh
```
#!/bin/bash

echo "" > ~/CovidResults/results.csv

cd ~ && cd ~/repositories/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports && git pull

lista=`cd ~ && ls repositories/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv`

for KatheFile in $lista

do

count=0

	cd ~ && cat $KatheFile|while IFS=, read -r col1 col2 col3 col4 col5 col6 col7 col8 col9 col10 col11 col13 col14

	do

    		if [[ $col4 == $1 ]]; then

			count=$((count+1))

			cd ~ && echo -n $(echo "$KatheFile" | cut -b 70-79 ) "," >> ~/CovidResults/results.csv && awk 'NR=='$count'' $KatheFile | cut -d ',' -f 8 >> ~/CovidResults/results.csv 

			break;

		else

			count=$((count+1))

		fi

	done

done
```
## Το αρχείο covid.py
```
#!/usr/bin/python
import csv
import datetime as dt
from matplotlib import pyplot as plt                                            
from matplotlib import style                                                    
import numpy as np
import sys                                                             
                                                                                
style.use('ggplot')    
x = []   
y = []

with open('results.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
	x.append(row[0])
	y.append(row[1])
                                                         
                                                          
test = [dt.datetime.strptime(d,'%m-%d-%Y ').date() for d in x]
arr = np.array(y)
arr2 = arr.astype(np.float)
                                                                          
plt.plot(test,arr2)                                                                                                                       
 
#plt.plot_date(test, arr2)
                                                                               
plt.title(sys.argv[1])                                                              
plt.ylabel("Confirmed")                                                            
plt.xlabel("Time")                                                                      
                                                                                
plt.show()                                                                      
                                                                                
plt.savefig('plot.pdf')                                                         
plt.savefig('plot.svg')                                                         
plt.savefig('plot.png')   
```

## Το results.csv θα είναι στο τέλος της παρακάτω μορφής
```
03-22-2020 ,624
03-23-2020 ,695
03-24-2020 ,743
03-25-2020 ,821
03-26-2020 ,892
03-27-2020 ,966
03-28-2020 ,1061
03-29-2020 ,1156
03-30-2020 ,1212
03-31-2020 ,1314
...
```


Αρχικά στο shell script αδειάζω το αρχείο results.csv για να το χρησιμοποιήσω για τα νέα δεδομένα.
```
echo "" > ~/CovidResults/results.csv
```
Μετά ελέγχω αν βγήκαν καινούργια δεδομένα στο github όπου είναι τα δεδομένα.
```
cd ~ && cd ~/repositories/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports && git pull
```
Ακολούθως μπαίνω στο cloned repository και παίρνω λίστα με όλα τα αρχεία που τελειώνουν σε csv.
```
lista=`cd ~ && ls repositories/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv`
```

Πιάνω ένα ένα τα αρχεία απο αυτή τη λιστα και μηδενίζω το counter για καθένα από αυτά στη αρχή έτσι ώστε να μην έχω προβλήματα.
```
for KatheFile in $lista

do

count=0
```
 Μετά στο κάθε αρχείο πιάνω ένα ένα τα column μέσα σε ένα while, οπού βάζω ότι χωρίζεται με ερωτηματικό.
 ```
 cd ~ && cat $KatheFile|while IFS=, read -r col1 col2 col3 col4 col5 col6 col7 col8 col9 col10 col11 col13 col14

	do
```
Τέλος συγκρίνω το όνομα του κάθε column της 4ης σειράς όπου στο κάθε αρχείο είναι το όνομα της χώρας και αν είναι ίδιο με αυτό που δίνει ο χρήστης τότε γράφω στο αρχείο results.csv . Αρχικά γράφω τη ημερομηνία όπου και είναι το όνομα του αρχείου έτσι κόβω αναλόγως τα byte(αυτό αλλάζει αναλόγος που είναι cloned το repository με δεδομένα). Μετά μέσο του awk και του counter που έχω κόβω στη γραμμή όπου είναι η χώρα. Τέλος μέσω cut πιάνω το αριθμό των confirmed που είναι στη 8η γραμμή. Αυτός ο έλενχως γίνεται για όλα τα file που υπάρχουν, έτσι το results.csv θα έχει γραμμές όσα file βρέθηκε η χώρα.
```
if [[ $col4 == $1 ]]; then

			count=$((count+1))

			cd ~ && echo -n $(echo "$KatheFile" | cut -b 70-79 ) "," >> ~/CovidResults/results.csv && awk 'NR=='$count'' $KatheFile | cut -d ',' -f 8 >> ~/CovidResults/results.csv 

			break;

		else

			count=$((count+1))

		fi
```

Στο covid.py αρχίζω με άνοιγμα του αρχείου csv όπου και αναθέτω τη κάθε γραμμή σε ένα πίνακα.
```
with open('results.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
	x.append(row[0])
	y.append(row[1])
```

Ακολούθως κάνω το y αριθμούς float και το x σε μορφή date.
```
test = [dt.datetime.strptime(d,'%m-%d-%Y ').date() for d in x]
arr = np.array(y)
arr2 = arr.astype(np.float)
```

Στο τέλος αυτού του αρχείου βάζω τίτλο αυτό που έδωσε ο χρήστης, δείχνω το plot και το κάνω export.
```
plt.title(sys.argv[1])                                                              
plt.ylabel("Confirmed")                                                            
plt.xlabel("Time")                                                                      
                                                                                
plt.show()                                                                      
                                                                                
plt.savefig('plot.pdf')                                                         
plt.savefig('plot.svg')                                                         
plt.savefig('plot.png')
```

Στο τελικό αποτέλεσμα μπορείς να δεις ακριβώς σε κάθε ημερομηνία πόσα κρούσματα υπάρχουν.

Το αποτέλεσμα σε εικόνα png:
![plott](https://user-images.githubusercontent.com/44147982/98317544-5b05a300-1fe5-11eb-8056-ed39240d22c1.png)



## <a name="P-5">Παραδοτέο 5</a>
## Συμμετοχικό εκπαιδευτικό υλικό
Εφτιαξα 3 καινούργια δικά μου εργαλεία στο codepen. Το πρωτο δειχνη πως λειτουργουν τα keyframe animations. Το δευτερο δειχνει οπτικοποιηση δεδομένων μέσο google charts. Τελος στο τρίτο έφτιαξα ένα απλό εργαλείο pen.
Τα βήματα και ο κώδικας για τη διμιουργία του κάθε εργαλείου βρίσκονται πιο κάτω.

### Css Animation:
[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/keyframes_animation/)</br>
[Codepen Link](https://codepen.io/andreaspappoutas/pen/dyXQxbb)</br>
[Link αρχείου md](https://github.com/andreaspappoutas/site/blob/master/_remix/Keyframes_Animation.md)</br>




### Google Charts:
[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/google-charts/)</br>
[Codepen Link](https://codepen.io/andreaspappoutas/pen/ExyOJZz)</br>
[Link αρχείου md](https://github.com/andreaspappoutas/site/blob/master/_remix/google-charts.md)</br>




### Pen Tool:
[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/pen-tool/)</br>
[Codepen Link](https://codepen.io/andreaspappoutas/pen/VwjqMgX)</br>
[Link αρχείου md](https://github.com/andreaspappoutas/site/blob/master/_remix/pen-tool.md)</br>





### CSS animation
Στο css animation αρχικά δημιούργησα ένα κύκλο div.
```
<div id="mycircle" class="circle"></div>

.circle {
  height: 50px;
  width: 50px;
  background-color: black;
  border-radius: 50%;
}
```

Στο κομμάτι του javascript έπιασα το div με όνομα circle ενώ επίσης έφτιαξα eventlisteners για αν μετακινηθεί το ποντίκι ή εάν γίνει κλικ.
```
var circle = document.getElementById("mycircle");
document.addEventListener("mousemove", Thesi); 
document.body.addEventListener('click', RunAnimation); 
```

Στο function Thesi παίρνω το χ και το ψ του ποντικιού και ακολούθως βάζω το κύκλο εκεί.
```
function Thesi(){
  x = event.x-20; //-20 gia na einai kentron
  y = event.y-20;//-20 gia na einia kentron
  circle.style.position = "absolute";
  circle.style.left = x + 'px';
  circle.style.top = y + 'px';
}
```

Στο function RunAnimation βάζω να τρέξει το animation και εφόσον τρέξει μέσο timout το αδειάζω έτσι ώστε να μπορεί να τρέξει αυτόματος ξανά στο κλικ.
```
function RunAnimation(){
  circle.style.animation="MyAnimation 4s ease-in-out";
  setTimeout('circle.style.animation=""', 4000)
}
```

Το keyframes MyAnimation
```
@keyframes MyAnimation {
  0% {
    
    transform: scale(1);
  }

  33% {
    background-color: blue;
    opacity: 0.5;
    transform: scale(0);
  }
  66% {
    opacity: 0.8;
    transform: scale(2);
  }
	100% {
    opacity: 1;
    transform: scale(1);
  }
```
  
  
### Google Charts
Αρχικά έβαλα όλα τα κατάλληλα που χρειάζονται για google charts μαζί με το div όπου θα μπει το chart.
```
<div id="Google_paradeigma" style="width: 700px; height: 400px"></div>

document.getElementById('Google_paradeigma')
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
```
Έβαλα το data και options για κάθε παράδειγμα.
```
var data = google.visualization.arrayToDataTable([
['Year', 'Cyprus', 'Greece'],
['1955', 529972, 8011124],
['1960', 572930, 8273629],
...
var options = {
          title: 'Country Population',
...
```

Έφτιαξα ένα dropdown μενού που καλεί τη function των google charts που λέγεται drawChart και μέσα βάζω μια μεταβλητή αναλόγως ποιο γράφημα θέλω.
```
<div class="dropdown">
  <button class="button">Datasets</button>
  <div class="list">
     <a onclick="drawChart(0)">Population</a>
    <a onclick="drawChart(1)">GDP per capita</a>
    
  </div>
</div>
```

Τέλος μέσο ενός switch μέσα στο drawChart εμφανίζω τα chart που θέλω.
```
switch(p){
          case 0:
            chart.clearChart() //oxi anagkastiko
            chart.draw(data, options);
            break;
          case 1:
            chart.clearChart() //oxi anagkastiko
            chart.draw(data2, options2);
            
        }
```

### Pen Tool
Ξεκίνησα φτιάχνοντας το canvas και περνώντας το αυτό μαζί με το context του στο κομμάτι του javascript
```
<canvas id="toCanvas" width="600" height="300"></canvas>

var canvas = document.getElementById("toCanvas");
var ctx = canvas.getContext("2d");
```

Στο επόμενο κομμάτι δήλωσα ένα control variable που θα χρησιμοποιήσω για να ξέρω τη κατάσταση του πλήκτρου space ενώ επίσης έθεσα τα χ, ψ και πάχος γραμμής
var control= false;
```
let x =0;
let y= 0;
ctx.lineWidth = 5;
```

Εδώ έβαλα αρχικά eventlistener εάν πατήσω κλικ και μετά ένα για αν πατήσω κάποιο πλήκτρο
```
document.body.addEventListener('mousedown', e => {
  document.body.onkeyup = function(e){
```  
  
Αν πατηθεί το space τότε αντιστρέφω το control και αναλόγως αλλάζω το χρώμα των γραμμάτων κάτω από το canvas. Επίσης θέτω τα χ και ψ στο offset του event κάτι που λειτουργεί σαν reset για αυτά.
```
if(e.keyCode == 32){
        control = !control
        if(control==false){
          document.getElementById("space").style.color="black";
        }else{
          document.getElementById("space").style.color="green";
        }
        
        x = e.offsetX
        y = e.offsetY
    }
```

Αν το control είναι θετικό τότε πατήθηκε το space. Οι συντεταγμένες που θα πάρει θα είναι από το eventlistener για κλικ εφόσον δεν θα περάσει από το πιο πάνω if. Τέλος εδώ δημιουργούμε το σχέδιο μέσο του moveTo και lineTo.   
```
if(control==true){
        const newX = e.offsetX;
        const newY = e.offsetY;
        ctx.beginPath();
        ctx.moveTo( x, y ); //apo p na 3ekina
        ctx.lineTo( newX, newY ); //pou na pigeni
        ctx.stroke();
  }
```

Eventlistener για να βρίσκουμε που να προχωρά η γραμμή.
```
window.addEventListener('mouseup', e => {
  x = e.offsetX
  y = e.offsetY
```

Έφτιαξα επίσης ένα κουμπί που κάνει clear το canvas.
```
<button onclick="clearCanvas()">clear</button>

function clearCanvas(){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
```

Επίσης ένα slider όπου επιλέγει μέγεθος. Επίσης αλλάζει πιο πάνω το innerHTML και δείχνω τι μέγεθος έχουμε.
```
<input type="range" min="1" max="10" value="5" id="LineWidth">
<h3>Width:</h3><h4 id="h4txt">5</h4>

var valueTXT = document.getElementById("h4txt");
lineWidth.oninput = function() {
  valueTXT.innerHTML = this.value;
  ctx.lineWidth = this.value
}
```

Τέλος έβαλα και την επιλογή να αλλάζει το χρώμα ο χρήστης.
```
<input id="color" type="color" value="#000000" onchange="color()">

function color(){
   ctx.strokeStyle = document.getElementById("color").value;
  
}
```

### <a name="P-5-1"> Άσκηση Προγραμματισμού 3: </a>
### Άσκηση: Τροποποιήστε το παράδειγμα χρησιμοποιώντας φίλτρα εικόνας και συνδυασμούς αυτών. Παραδείγματα φίλτρων βρίσκονται ως σχόλια στην ενότητα με τον CSS κώδικα του παραδείγματος.

Αρχικά έφτιαξα ένα dropdown menu όπου το κάθε κουμπί πάει σε ένα function με διαφορετικό αριθμό ενώ επίσης να αλλάζει το χρώμα του background.
```
<div class="dropdown">
  <button class="button">Filters</button>
  <div class="list">
     <a onclick="changeStyle(0);document.body.style.backgroundColor = '#4B4F4F';">grayscale</a>
 ...
```
Έβαλα και να γίνονται αλλαγές όταν γίνετε hover το κουμπί.
```
.dropdown:hover .button {
  background-color: #333636;
}
```

Στο κομμάτι του javascript αρχικά δημιουργώ style τύπου css όπου θα αλλάζω αργότερα.
```
var style = document.createElement('style');
    style.type = 'text/css';
```
Μετά φτιάχνω το function που καλούν τα κουμπιά και ένα case αναλόγως με τι αριθμό έχει το κάθε κουμπί.
```
function changeStyle(p){
  switch (p){
```

Εδώ θα δείξω 2 παραδείγματα case αλλά και τα υπόλοιπα έχουν το ίδιο σκεπτικό. Πιάνω το innerHTML του style που έφτιαξα και έβαλα πιο πάνω και εφόσον βάλω το στυλ που θέλω το κάνω append στο <head>, δηλαδή το βάζω μέσα στο html.

Με grayscale
```
case 0:
      style.innerHTML = "img:hover{filter:grayscale(1);}";
      document.getElementsByTagName("head")[0].appendChild(style);
      break;
```

Συνδυασμός
```
case 8:
      style.innerHTML = "img:hover{filter:hue-rotate(90deg) sepia(1) brightness(.15);}";
      document.getElementsByTagName("head")[0].appendChild( style );
```
[Codepen Link](https://codepen.io/andreaspappoutas/pen/LYZmzKN)

[Link Κώδικα](https://github.com/andreaspappoutas/site/blob/master/_remix/image-filter.md)

[Link σελίδας αποτελέσματος](https://andreaspappoutas.netlify.app/remix/image-filter/)


## <a name="P-6">Παραδοτέο 6</a>
## Αίτημα ενσωμάτωσης 2

### Link Αποτελέσματος στο sitegr: [sitegr results](https://epic-hamilton-da9ac8.netlify.app/people/)
### Link Αποτελέσματος στο δικό μου site: [andreaspappoutas-sitegr results](https://paradoteo2-fixed--andreaspappoutas-sitegr.netlify.app/people/)
### Repository branch: [minimal-ionio branch](https://github.com/andreaspappoutas/minimal-ionio/tree/paradoteo2-fixed)
###                    [sitegr-branch](https://github.com/andreaspappoutas/sitegr/tree/paradoteo2-fixed)
		   
### Issue  [Sitegr issue](https://github.com/ioniodi/sitegr/issues/15)
### Pull Request στο sitegr [sitegr pull-request](https://github.com/ioniodi/sitegr/pull/16)
### Pull request στο minimal-ionio [minimal-ionio pull-request](https://github.com/ioniodi/minimal-ionio/pull/37)

### Σε αυτό το παραδοτέο έφτιαξα κώδικα έτσι ώστε ανάλογα με τι αριθμό έχει ο κάθε καθηγητής στο rank του να μπαίνει σε μια κατηγορία. Τα βήματα που ακολούθησα είναι τα παρακάτω:

Αρχικά έφτιαξα grid-containers για τη κάθε βαθμίδα. Διάλεξα να κάνω χρήση grid εφόσον καθηγητές με μεγάλα ονόματα έκαναν overlap και μέσω grid θα είναι καλύτερο.
```
<div id="people-rank-1" class="grid-container" ><h1 class="rank_title">Καθηγητές</h1>
</div>
<div id="people-rank-2" class="grid-container" ><h1 class="rank_title">Αναπληρωτές Καθηγητές</h1>
</div>
..
..
```

Επίσης έβαλα ένα header σε καθένα από αυτά τα grid-containers. Αυτό θα είναι στο πρώτο κελί άλλα εφόσον θέλω να είναι ο τίτλος έκανα το παρακάτω κώδικα στο css κομμάτι. Αρχικά ο τίτλος είναι πρώτο κελί και πάει οριζοντίως 4. Επίσης έβαλα το container να είναι ανά 4 με gap 50. Τέλος έβαλα το κάθε container να μην φαίνεται εξ αρχής. Αυτό έγινε επειδή μπορεί κάποια βαθμίδα να μην έχει καθηγητές. Έτσι πιο μετά αν ο κώδικας βρει ένα καθηγητή αυτομάτως θα εμφανίζει τη βαθμίδα του σε grid.
```
.rank_title {
  grid-column: 1 / span 4;
}
.grid-container {
  display: none;
  float: inherit;
  grid-template-columns: auto auto auto auto;
  grid-gap: 50px;
}
```

Ακολούθως έφτιαξα ένα case που ελέγχει το αριθμό του rank του κάθε καθηγητή. Στη συνέχεια κάνει include το κώδικα που θα δείξω παρακάτω και περνά μέσα τη τιμή της κάθε βαθμίδας.
```
{% case post.rank %}
  {% when 1 %}
      {% include people-rank-div.html content="1" %}
  {% when 2 %}
      {% include people-rank-div.html content="2" %}
  {% when 3 %}
 ..
 .. 
```
Πιο κάτω έχουμε το people-rank-div include. Εδώ αρχικά έβαλα το id του κάθε grid-item, δηλαδή του κάθε κελιού με το καθηγητή του να έχει σαν id το reference του καθηγητή. Έβαλα μέσα στο κελί το archive-people το οποίο εμφανίζει το κάθε καθηγητή μαζί με τη εικόνα του. Μέτα έβαλα ένα javascript το οποίο βάζει αυτό το grid-item μέσα στο κατάλληλο container μέσο του αριθμού που έγινε passed από το προηγούμενο include ενώ επίσης εμφανίζει το container αυτό εφόσον τώρα ξέρουμε ότι υπάρχει καθηγητής μέσα.
```
<div id="{{ post.ref }}" style="float: left;" class="grid__item" >
        {% include archive-people.html %}
      </div>
      <script>
            document.getElementById("people-rank-{{ include.content }}").style.display = "grid";
            document.getElementById('people-rank-{{ include.content }}').appendChild(document.getElementById( "{{ post.ref }}" ));
</script>
```
Τέλος πέρασα από όλους τους καθηγητές και άλλαξα το αριθμό του rank τους αναλόγως με τι βαθμίδα έχουν.


## <a name="P-7">Παραδοτέο 7</a>
## Συμμετοχικό περιεχόμενο 2 - tweets

Αρχικά έφτιαξα ένα include που πέρνει σαν παράμετρο το όνομα κάπιου χρήστη και εμφανίζει τα tweets του μέσο κώδικα του publish.twitter.com
Έβαλα επίσης το κατάλληλο κώδικα έτσι ώστε να εμφανίζετε σωστά
```
<div class="feature__item">
  <div class="archive__item">
    <div class="archive__item-body">
      <h2 class="archive__item-title">Tweets</h2>
      <a class="twitter-timeline" 
         href="https://twitter.com/{{ include.content }}?ref_src=twsrc%5Etfw" 
         data-height="450" data-chrome="nofooter transparent noborders">
        Tweets by {{ include.content }}
      </a> 
      <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </div>
  </div>
</div>
```
Στο index.html κάλεσα το include με το όνομα του twitter μου.
```
{% include twitter-posts.html content="p17papp1" type="center" index=random %}
```

Τα tweets που έφτιαξα είναι τα παρακάτω:  
[tweet 1](https://twitter.com/p17papp1/status/1337450338861916161)  
[tweet 2](https://twitter.com/p17papp1/status/1337381055943335937)  
[tweet 3](https://twitter.com/p17papp1/status/1337377574868148225)  
[tweet 4](https://twitter.com/p17papp1/status/1337175898383114243)  
[tweet 5](https://twitter.com/p17papp1/status/1337173135725113344)  
[tweet 6](https://twitter.com/p17papp1/status/1337170593704271872)  
[tweet 7](https://twitter.com/p17papp1/status/1344378635386499076)  
[tweet 8](https://twitter.com/p17papp1/status/1344380704793235464)  
[tweet 9](https://twitter.com/p17papp1/status/1344384376084291586)  
[tweet 10](https://twitter.com/p17papp1/status/1348634216226058241)  



## λινκ αποτελέσματος:
[site](https://andreaspappoutas.netlify.app)


## <a name="P-8">Παραδοτέο 8+9</a>
## Αίτημα ενσωμάτωσης 3+4

### Link Αποτελέσματος στο sitegr: [sitegr results](https://epic-hamilton-da9ac8.netlify.app/ects-calculator)
### Link Αποτελέσματος στο δικό μου site: [andreaspappoutas-sitegr results](https://ects-demo--andreaspappoutas-sitegr.netlify.app/ects-calculator)
### Repository branch: [minimal-ionio branch](https://github.com/andreaspappoutas/minimal-ionio/tree/ects-calc)
###                    [sitegr-branch](https://github.com/andreaspappoutas/sitegr/tree/ects-calc)
		   
### Issue  [Sitegr issue](https://github.com/ioniodi/sitegr/issues/20)
### Pull Request στο sitegr [sitegr pull-request](https://github.com/ioniodi/sitegr/pull/21)
### Pull request στο minimal-ionio [minimal-ionio pull-request](https://github.com/ioniodi/minimal-ionio/pull/38)

### Σε αυτό το παραδοτέο έφτιαξα μια σελίδα για τους φοιτητές να υπολογίζουν ects.

Αρχικά στο sitegr έφτιαξα ένα νέο αρχείο με το όνομα ects-calculator.md με λινκ να είναι το /ects-calculator/. Ακολούθος μέσο του navigation.yml το πρόσθεσα στο μενού.
Επόμενο βήμα είναι η διμιουργία ενός include στο minimal-ionio με το οποίο να έχουμε checkbox δίπλα απο κάθε μάθημα. Αυτό αρχικά έγινε με το ίδιο τρόπο που εμφανίζονται τα άλλα μαθήματα. Η διαφορά είναι στο archive-single όπου στο δικό μου αρχείο πρόσθεσα τη παρακάτω γραμμή κώδικα:
```
<p><input type="checkbox" id="{{ post.ref }}" name="{{ post.ref }}" value="{{ post.ref }}" ects="{{ post.ects }}" sem="{{ post.semester }}" c_type="{{ post.type }}"><a href="{{ post.link }}">{{ title }}</a> <a href="{{ post.url | relative_url }}" rel="permalink"><i class="fas fa-link" aria-hidden="true" title="permalink"></i><span class="sr-only">Permalink</span></a></p>
```
Σε αυτό το κώδικα προσθέτο ενα checkbox με id το reference του κάθε μαθήματος. Επίσης βάζω attributes όπως πόσα ects είναι,εξάμηνο και το τύπο του.
Μέσα στο sitegr ects-calculator.md έφτιαξα ένα νέο div με το όνομα boxes έτσι ώστε να τα πέρνω με ευκολία πιο μετα. Μέσα σε αυτό το div έβαλα τα μαθήματα και επίσης το markdown του github σε δικό του div εφόσον το έπερνε σαν html.

```
<div id="boxes">
{% include toc title = "ΜΑΘΗΜΑΤΑ" icon = "graduation-cap" %}

<div markdown="1"> 
# ΠΡΟΠΤΥΧΙΑΚΟ 
</div>
...
```
Ακολούθος πρόσθεσα ένα span μέσο του οποίου να εμφανίζω τα ects.
```
<p><span id ="ects_span">0</span> <span>ects in total</span></p>
<p><span>Απομένουν:  </span><span id="ects_span_240"></span></p>
```
Επίσης πρόσθεσα ένα javascript αρχέιο το οποίο μετά το έφτιαξα στο minimal-ionio.
```
<script type="text/javascript" src="/assets/js/ects.js"></script>
```

Μέσα στο ects.js αρχικά πέρνουμε όλα τα checkboxes των μαθημάτων ένα ένα αλλά επίσης και τα span για να αλλάζουμε τα ects. Το LoadArrays() είναι ενα function το οποίο θα εξηγησω πιο μετά.
Εφόσον πιάννω ένα ένα τα checkbox τους βάζω ενα eventListener το οποίο βλέπει αν έγινε αλλαγή στη κατάσταση. Αν γίνει αλλαγή καλώ το ects_total().
```
function LoadVariables(){
  var all_courses = document.getElementById('boxes'); 
  var courses_input = all_courses.getElementsByTagName('input');
  var text = document.getElementById("text");

  for (var i=0, len=courses_input.length; i<len; i++) {
          if(courses_input[i].hasAttribute('ects')){
            courses_input[i].addEventListener("change", ects_total)
        }
    }

  LoadArrays();
}
```

Στο ects_total αρχικά πέρνουμε τα text με τα οποία θα οπτικοποιούμε στο χρήστη τα ects. Ακολούθος ελένχουμε αν το checkbox το οποίο κάλεσε αυτό το function είναι checked. Αν είναι τότε ο χρήστης το έκανε checked έτσι πρέπει να προσθέσουμε τα ects του. Ακολούθος τα οπτικοποιούμε. Αν είναι αρνητικό τότε το έκανε uncheck έτσι αφαιρούμε.
```
function ects_total(){
   var changing_text = document.getElementById("ects_span");
   var ects = parseInt(changing_text.innerHTML);
   var diff = document.getElementById("ects_span_240");

   if(this.checked){  
     ects += parseInt(this.getAttribute('ects'));
     changing_text.innerHTML=(ects);
     var difference = 240 - ects;
     diff.innerHTML=(difference);
   }
   else{
     ects -= parseInt(this.getAttribute('ects'));
     console.log(ects);
     changing_text.innerHTML=(ects);
     var difference = 240 - ects;
     diff.innerHTML=(difference);
   }

}
```

Για να έχουμε λιγότερα clicks έκανα τη επιλογή στους χρήστες να επιλέγουν πολλαπλά μαθήματα με ένα click. Αυτο αρχικα έγινε με το να βάλουμε τα checkboxes του κάθε μαθήματος σε πίνακες. Αυτό το function πέρνει το έξάμηνο και το τύπο και φτιάχνει πίνακα με τα ανάλογα μαθήματα. Ακολούθος εφόσον αυτός είναι απλά πίνακας με ονόματα και όχι τα elements ξαναπερνάμε απο το καινούργιο πίνακα και βάζουμε μέσα τα elements που αναλογούν.
```
function Create_Arrays(semester,type){
  var course_checkbox = document.getElementById('boxes'); 
  var course_input = course_checkbox.getElementsByTagName('input');
  var arrayrtn = new Array();

  for (var i=0, len=course_input.length; i<len; i++) {
           if( (course_input[i].getAttribute('c_type') == type) && ( course_input[i].getAttribute('sem') == semester) ){
                arrayrtn.push(course_input[i].id)
           }
    }

  for( var i=0, len=arrayrtn.length; i<len; i++){
    arrayrtn[i] = document.getElementById(arrayrtn[i]);
  }

  return arrayrtn;
}
```

Ακολούθος φτιάχνουμε όλους τους πίνακες.
```
function LoadArrays(){
 for (i = 1; i < 9; i++) {
   window['mandatory'+i] = Create_Arrays(i,"M");
   window['AE'+i] = Create_Arrays(i,"H");
   window['PS'+i] = Create_Arrays(i,"I");
  }

 window.mandatory_all = mandatory1.concat(mandatory2, mandatory3,mandatory4,mandatory5,mandatory6,mandatory7,mandatory8);
 window.AE_all = AE1.concat(AE2, AE3,AE4,AE5,AE6,AE7,AE8);
 window.PS_all = PS1.concat(PS2, PS3,PS4,PS5,PS6,PS7,PS8);
}
```

Μετά φτιάχνουμε function με το οπόιο θα μπόρουμε να ελένξουμε αν έκανε κλικ πάνω στο checkbox για πολλαπλά. Το function πιάννει σαν μεταβλητές το πίνακα με μαθήματα που θέλουμε αυτομάτος να γινουν checked αλλά και το element_box το όποιο το καλεί αυτό. Περνάμε μέσα απο όλα τα μαθήματα και ελένχουμε αν είναι checked ή όχι. Αν είναι ήδη checked απο πριν τα αφήνουμε ενω διαφορετικα καλούμε το ects_total_multiple με μεταβλήτη το μάθημα. Όλο αυτό είναι μέσα στο if που ελένχει τη κατάσταση του checkbox που καλεί το autoCheck.
```
function autoCheck(m,element_box){
  var check_for_all = document.getElementById('mandatory_checkbox');


  for (var i=0, len2=m.length; i<len2; i++) {
    if(element_box.checked==true){
      if(m[i].checked==true){
        m[i].checked=true;
      }else{
        m[i].checked=true;
       ects_total_multiple(m[i]);
      }

    }else{
      if(m[i].checked==true){
        m[i].checked=false;
       ects_total_multiple(m[i]);
      }else{
        m[i].checked=false;
      }
    }
  }
```
  
  
Τέλος αυτο ακολουθή τη ίδια λογική με το ects_total() με τη διαφορά οτι πιάννει μεταβλητή αντί απλά να πιάννει το "this".
```
  function ects_total_multiple(m){//function gia xrisi tou autoCheck

  var changing_text = document.getElementById("ects_span");

  var ects = parseInt(changing_text.innerHTML);

  var diff = document.getElementById("ects_span_240");

  if(m.checked){
    ects += parseInt(m.getAttribute('ects'));
    changing_text.innerHTML=(ects);
    var difference = 240 - ects;
    diff.innerHTML=(difference);
  }
  else{
    ects -= parseInt(m.getAttribute('ects'));
    changing_text.innerHTML=(ects);
    var difference = 240 - ects;
    diff.innerHTML=(difference);
  }

  window.autocheck = 0;
}
  ```
  
Έτσι στο τέλος πίσω στο ects-calculator.md φτιάχνουμε νέα checkbox με τα οποία καλούμε το autoCheck. Δίνουμε μεταβλητές το πίνακα που θέλουμε και το checkbox το ίδιο.
```
<p><input onclick="autoCheck(mandatory5,this)" type="checkbox" id="mandatory5_checkbox" name="mandatory5_checkbox">
<label style="display: initial;" for="mandatory5_checkbox">Όλα τα υποχρεωτικά - Δ εξάμηνο</label></p>

<p><input onclick="autoCheck(AE5,this)" type="checkbox" id="AE5_checkbox" name="AE5_checkbox">
<label style="display: initial;" for="AE5_checkbox">Όλα του Α.Ε - Ε εξάμηνο</label></p>
 ```
 
 Τέλος εφόσον τα προσθέσαμε για όλα τα εξάμηνα το calculator λειτουργά κανονικά.


## extra
Το plugin PWA-jekyll έκανε update και είχαν εμφανιστή προβλήματα. Έκανα τη πιο κάτω αλλαγή.
```
gem 'jekyll-pwa-plugin', git: 'https://github.com/lavas-project/jekyll-pwa'
```
[pull request](https://github.com/ioniodi/sitegr/pull/23)
[issue](https://github.com/ioniodi/sitegr/issues/22)

## <a name="P-10">Παραδοτέο 10</a>
### Σύνοψη:
#### Ξεκίνησα με το γράψιμο της εισαγωγής μου όπου μιλάω γιατί επέλεξα το μάθημα αυτό. Ασκήσεις προγραμματισμού επέλεξα στο σύνολο να φτιάξω 3. Στο πρώτη άσκηση τροποποίησα κώδικα για οπτικοποίηση σε d3.js . Στη δεύτερη άσκηση άλλαξα το κώδικα για ένα παιχνίδι canvas και να πρόσθεσα όρια για το παίχτη. Στη τρίτη άσκηση μέσο css και javascript έβαλα τη δυνατότητα μια εικόνα να αλλάζει φίλτρα μέσο ενός μενού. Όλες οι ασκήσεις προγραμματισμού έγιναν με τη χρήση του codepen. Έφτιαξα 2 ασκήσεις γραμμής εντολών. Στη πρώτη άσκηση μέσο shell scripting και pipelining έφτιαξα 2 προγράμματα. Στο πρώτη οπτικοποιώ μια σειρά ενός csv αρχείο ενώ στο δεύτερο τα commits κάποιου συγγραφέα μέσα στο github. Στη δεύτερη άσκηση πάλι με τη χρήση bash,pipelining αλλά επίσης και python οπτικοποίω αυτόματα σε ένα plot τα κρούσματα κορονοϊού οποιασδήποτε χώρας. Στο κομμάτι του συμμετοχικού έφτιαξα από τη αρχή 3 διαφορετικά προγράμματα για εκπαιδευτική χρήση. Το πρώτο είναι είναι animations στο css. Το δεύτερο είναι οπτικοποίηση δεδομένων μέσο της βιβλιοθήκης google charts. Το τρίτο είναι ένα pen-tool που δημιούργησα μέσο canvas. Στο δεύτερο συμμετοχικό περιεχόμενο μου έφτιαξα 10 tweets που μετά απο δική μου έρευνα πιστεύω να έχουν σχέση με το μάθημα. Για πρώτο αίτημα ενσωμάτωσης έκανα αλλαγές στο sitegr για αλλαγές καθηγητών και νέα μαθήματα. Δεύτερο αίτημα ενσωμάτωσης ήτανε η δημιουργία κώδικα για αυτόματη κατηγοριοποίηση καθηγητών. Τρίτο και τέταρτο παραδοτέο για αίτημα ενσωμάτωσης είναι η δημιουργία ενός ects-calculator όπου ο χρήστης υπολογίζει ects μαθημάτων.

### Συμπεράσματα:
#### Οι στόχοι μου για το μάθημα ήτανε η οργάνωση δεδομένων σε υψηλότερο επίπεδο, να μάθω τεχνικές διαχείρισης πληροφοριών και να αποκτήσω γνώση στις σύγχρονες τεχνολογίες που χρησιμοποιούνται για τη οπτικοποίηση δεδομένων. Κατά τη άποψή μου έχω πετύχει τους στόχους αυτούς. Μέσω των ασκήσεων γραμμής εντολών έμαθα να φτιάχνω προγράμματα με τη χρήση άλλων προγραμμάτων. Πολλές φορές η καλή οπτικοποίηση δεδομένων γίνεται μόνο από λογισμικά που απαιτούν πληρωμή. Μέσω τον δεξιοτήτων που έμαθα μπορώ να συνδυάσω πολλά προγράμματα στη γραμμή εντολών και να φτιάξω το πρόγραμμα που είναι κατάλληλο για εμένα. Οι ασκήσεις προγραμματισμού μου φάνηκαν πολύ καλές εφόσον έμαθα καλά html,javascript και css. Επιπλέον έμαθα βιβλιοθήκες για οπτικοποίηση δεδομένων. Απο το συμμετιχικό κομμάτι έκανα τις γνώσεις μου πάνω στη οπτικοποίηση καλύτερες. Τα αιτήματα ενσωμάτωσες είχαν να κάνουν με νέους πιο δυναμικούς τρόπους δημιουργίας και οπτικοποίησης ιστοσελίδων. Με τη liquid μπορείς να εξοικονόμησης πολλή χρόνο και να κάνεις τη διαδικασία επέκτασης μιας ιστοσελίδας πιο εύκολη. Η κάθε άσκηση απαιτούσε χρήση διαφορετικού περιβάλλοντος κάτι που με βοήθησε να μάθω καινούργιους τρόπους και διαδικασίες για δημιουργία έργον. Ένα καλό παράδειγμα είναι η χρήση του github issues για τη δημιουργία ενός έργο από πολλαπλά άτομα. Τέλος πιστεύω ότι το μάθημα και οι γνώσεις που απέκτησα από αυτό θα μου φανούν αρκετά χρήσιμες στο μέλλον.
