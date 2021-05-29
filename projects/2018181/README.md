<h2 align= center>Software Engineering</h2>
<h3 align= center>Maria Chalkioti | P2018181 |  <a href="mailto:p18chal@ionio.gr"><img src="https://img.shields.io/badge/-Email-blueviolet"/></a>&nbsp;&nbsp;&nbsp;&nbsp; <p></h3>  
</br>

 ### Table of Contents (I)
|**Week** | **Deliverable** | 
|:---------:| :--------: | 
|**First** |[Introduction](#Introduction) |
|**Second** | [CV](#Curiculum-of-Vitae) |
|**Third** |  [Integration Into Website](#PR-Site) |
|**Fourth**|  [Command-line Exercise](#Command-line-Exercise) |
|**Fifth** |  [Participatory Content](#Participatory-Content) |
|**Sixth** |  [Command-line Exercise](#Command-line-Exercise) |  
|**Seventh** | [CV](#Curiculum-of-Vitae)|
|**Eighth** |  [Integration Into Website](#PR-Site)|
|**Ninth** |   [Command-line Exercise](#Command-line-Exercise) |
|**Tenth** |   [Participatory Content](#Participatory-Content)|
|**Eleventh** | [Command-line Exercise](#Command-line-Exercise) |  
|**Twelth** | [Final Report](Final-Report) | 
</br>

### Table of Contents (II) 
|**Video Quiz** | **Done** | 
|:---------:| :--------: | 
|Alan Kay at MIT EECS | :ballot_box_with_check:|
|Τed Νelson-Computers for Cynics |:ballot_box_with_check: |
|Alan kay-Computing Simply|:ballot_box_with_check: |
|Bret Victor-The Future of Programming | :ballot_box_with_check:  |
|Alan Kay-Programming] |:ballot_box_with_check:  |
|Alan Kay-Turing Award Lecture|:ballot_box_with_check:|  
|Alan Kay-Invention|:ballot_box_with_check:|
|Jaron Lanier-Intertwingled|:ballot_box_with_check: |
|Alan Kay-Scaling |:ballot_box_with_check:|
|Alan Kay-Turing Tarpit|:ballot_box_with_check:|
|Alan Kay-Future Software Development|:ballot_box_with_check:|
|Ken Thompson and Unix at Bell Labs |:x:|
 
</br>

|**Classtime Sessions**| **Done**|
|:---------:| :--------: | 
|Course: 15-02-21|:ballot_box_with_check:|
|Course: 22-02-21|:ballot_box_with_check:|
|Course: 01-03-21|:ballot_box_with_check:|
|Course: 08-03-21|:ballot_box_with_check:|
|Course: 15-03-21|:ballot_box_with_check:|

</br>

|Meetings| 
|:---------:|
+ Wednesday 31 of March (Mr. Patiniotis)
+ Monday 10 of May (Mr.Patiniotis) 

</br>

<h2>Introduction</h2>  
My aim for this course is to break down the continuous process of software development into discrete stages. Such a procedure involves making the appropriate decisions about the   software design strategy that will accompany the software architecture. Those decisions can determine the software requirements that can be implemented by the use of many programming languages and tools such as version control, development environments and software automation, all of which are an integral part of the software engineering principles and common practices.
</br> 

<h2>Curiculum of Vitae</h2>

|First Part|
|:---------:|

A simple [CV](https://mariachlkt.github.io/resume-sw/) hosted online by `Github Pages` and built using `HTML5` and `CSS3`. Actual information are passed by as variables to `HTML` from a `.yaml` configuration file.
CV was deployed locally with `Jekyll` and hosted online by Github Pages. It has received many updates over the course of time and the initial folder structure and setup was recorded live on [Asciinema](https://asciinema.org/a/397011).
</br>

![cv-image](https://github.com/mariachlkt/cli/blob/main/cv.png)

</br>

|Second Part|
|:---------:|

In order to create a `PDF` version of my CV, I used a custom `Github Actions` workflow with the necessary script that automates the process of making it.
Evidently, whenever CV information gets modified via `det.yaml` the script creates an updated PDF with the latest additions.
</br>

![pdf](https://github.com/mariachlkt/resume-sw/blob/main/cv.pdf)

</br>

<h2>PR-Site</h2>
</br>

|First Part|
|:---------:|

Για το πρώτο μέρος του αιτήματος ενσωμάτωσης στην ιστοσελίδα, προσέθεσα το μάθημα "Αναλυτική Δεδομένων Υγείας".  

|**Issue** | **Pull-Request** | **Demo** | **Branch** |
|:---------:| :--------: |  :--------: |  :--------: | 
| **#56** | **#100** | [Course](https://brave-hodgkin-c52527.netlify.app/courses/health-analytics/) | [mariachlkt:healthanalytics](https://github.com/mariachlkt/sitegr/blob/healthanalytics/all_collections/_courses/health-analytics.md) |
</br>

|First Part|
|:---------:|

Για το δεύτερο αίτημα ενσωμάτωσης, παρέθεσα την πρόταση για την προσθήκη κουμπιού, το οποίο θα πραγματοποιούσε την εναλλαγή της ιστοσελίδας από φωτεινό σε σκοτείνο θέμα. Ωστόσο, η το issue, αν και δέχτηκε πράσινο φως από τον κύριο Πατηνιώτη, ακυρώθηκε από τον κύριο Χωριανόπουλο, λόγω αυξημένης δυσκολίας και περιορισμένου χρόνου. 

<h2>Command-line Exercise</h2>

|**Deliverable** | **Assignment** | **Demo** | 
|:---------:| :--------: |  :--------: |
|**First** |Send notifications to your desktop-mobile| [Asciinema Video](https://asciinema.org/a/398905) |   
|**Second**|Programmable Voice|[Asciinema Video](https://asciinema.org/a/409967)|
|**Third**|Performance Monitoring|[Asciinema Video](https://asciinema.org/a/413440)|
|**Fourth**| **Set-up Continuous Integration** | [CV-PDF](https://github.com/mariachlkt/resume-sw/blob/main/.github/workflows/autopdf.yml) |
</br>

|First Assignemt|
|:---------:|

+ In the first task, I chose to push notifications to desktop and mobile when package updates are available. I made a script that informs user if the system is up-to-date or not and I used the following tools, Apticron-Notify-Pushover in order to  complete it. 
  - The first one, Apticron, is a useful script which sends daily emails about pending package updates and it is available for Debian and Ubuntu based systems.
  - The seond one, [Notify](https://github.com/mariachlkt/cli/blob/main/desktop-notification.png), pushes notifications on desktop from terminal.
  - The last tool, [Pushover](https://user-images.githubusercontent.com/56742258/117950825-413e7300-b31c-11eb-8635-0cacdf731a20.png), is an application which pushes notifications on Desktop, [smartphones](https://user-images.githubusercontent.com/56742258/117883250-dbb69c00-b2b3-11eb-84d2-98a3fad8b154.gif)
and smartwatches.
  
|Sources|
|:-----:|
    - https://www.unixmen.com/how-to-get-email-notifications-for-new-updates-on-debianubuntu/
    - https://docs.oracle.com/cd/E88353_01/html/E37839/notify-send-1.html
    - https://pushover.net/
</br>

|Second Assignemt|
|:---------:|

+ In the second task, I used Twilio Application, which is an American Cloud Communications Platform. More specific, I bought a trial number and i made a script in order to [make calls](https://user-images.githubusercontent.com/56742258/117950500-ead13480-b31b-11eb-84cc-2051f3c36f52.png) and [send messages](https://user-images.githubusercontent.com/56742258/117951523-ec4f2c80-b31c-11eb-9a66-5032bb9299ee.png) from the virtual one to mine. 

|Sources|
|:-----:| 
    - https://www.twilio.com/

</br> 

|Third Assignemt|
|:---------:|

+ In the third task, I used `Python` libraries in order to profile two scripts. The first script generates random password with input length and the other returns the host name and the IP address. 
   Python Libraries: `CProfile` & `PyInstrument`

   Note: The scripts run on `Python 3.0`. 

The [`.gif`](https://user-images.githubusercontent.com/56742258/117882127-af4e5000-b2b2-11eb-8c37-914f96fcf0d8.gif) represents the perfomance results of the first script (password generator) using the `CProfile`. 

|Fourth Assignemt|
|:---------:|

+ In the fourth task, I used a custom `GitHub Actions` workflow with the necessary `script` that automates the process of making a PDF version of my CV.
Evidently, whenever CV information gets modified via `det.yaml` the script creates an updated `PDF` with the latest additions.

```
# This is a basic workflow to help you get started with Actions

name: AUTO GENERATE-PDF 

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
    paths:
      - '_data/det.yaml'
  #pull_request:
    #branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-20.04

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
        with:
          persist-credentials: false
          fetch-depth: 0

      # Runs a single command using the runners shell
      - name: Convert to PDF 
        uses: docker://pandoc/latex:2.13
        with:
          args: >-
            https://mariachlkt.github.io/resume-sw/
            -f html-native_divs
            --pdf-engine=xelatex
            -o cv.pdf
            
      # Runs a set of commands using the runners shell
      - name: Commit 
        run: |
          git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add -A
          git commit -m "Automatically generate PDF"
      - name: Push amended CV
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```

</br>
<h2>Participatory Content</h2>

|First Part|
|:---------:|

- For the first part of this task (a1), I added to the forked repository two new images, one of which refers to the IRIX OS and the other one is about the Visi On 

|**Caption's Link** | **Image's Link** | **Thumb Image's Link** | **Asciinena Video** | **Netlify Link** |
|:---------:| :--------: | :----------: | :----------: |:----------: |
|[Visi-On](https://github.com/mariachlkt/_gallery/blob/P2018181/vision.md)|[Visi On Image](https://github.com/mariachlkt/images/blob/P2018181/vision.png)| [Visi On Thumb Image](https://github.com/mariachlkt/images/blob/P2018181/vision-thumb.png) | [Asciinema Video](https://asciinema.org/a/403138)| https://sad-spence-5715fa.netlify.app/
| [Irix-OS](https://github.com/mariachlkt/_gallery/blob/P2018181/irix-os.md)|[Irix OS Image](https://github.com/mariachlkt/images/blob/P2018181/irix-os.png)| [Irix OS Thumb Image](https://github.com/mariachlkt/images/blob/P2018181/irix-os-thumb.png) | [Asciinema Video](https://asciinema.org/a/403138)| https://sad-spence-5715fa.netlify.app/

</br>

- For the second part of this task (a2), I added to an existed slide and timeline the above images.

|**Slide's Link** | **Timeline's Link** |
|:---------:| :--------: | 
|[GUI](https://github.com/mariachlkt/site/blob/P2018181/_slides/gui.md)|[Systems](https://github.com/mariachlkt/site/blob/P2018181/_timeline/systems.md)|

</br>

|Second Part|
|:---------:|

- For the second part of this task (b1), I added to my forked repository Richard Stallman's biography and a case-study for GNOME with the apropriate images and information. 
</br>

|**Biography's Links** | **Case-Study's Links** | **Netlify Link** |
|:---------:| :--------: | :----------: |
| [Richard Stallman](https://github.com/mariachlkt/site/blob/P2018181/_biography/richard-stallman.md) | [GNOME](https://github.com/mariachlkt/site/blob/P2018181/_case-study/gnome.md) | https://sad-spence-5715fa.netlify.app/ |
| [Image](https://github.com/mariachlkt/images/blob/P2018181/richard-stallman.jpg) | [Image](https://github.com/mariachlkt/images/blob/P2018181/gnome.png) | https://sad-spence-5715fa.netlify.app/ |
| [Extras](https://github.com/mariachlkt/extras/blob/P2018181/bio-stallman.md) | [Extras](https://github.com/mariachlkt/extras/blob/P2018181/cs-gnome.md) | https://sad-spence-5715fa.netlify.app/ |

**Images caching issue**: There's an underlying caching issue with image previews on my Netlify demo.

[Site](https://github.com/mariachlkt/site/tree/P2018181) **is configured to point to my own submodule forks** but some images don't show up as previews during website navigation, at specific locations. For example, Stallman's image preview at [Biographies](https://sad-spence-5715fa.netlify.app/biography/) section doesn't work. The same applies for GNOME image preview at [Case Studies](https://sad-spence-5715fa.netlify.app/case-study/) section. **On the contrary, all previews of newly added images (Irix OS & Vision) at [Gallery](https://sad-spence-5715fa.netlify.app/gallery/) section work as expected.**

In an attempt to fix this issue, I tried to start fresh by forking all the repositories again in hope that there was an underlying corrupted commit that prevented image previews from showing up at specific locations. Unfortunately, this didn't fix the issue and same troublesome image previews as before are still broken.

Prior to forking the repositories all over again, I created copies of them in order to preserve the commit history for the purpose of meeting deadlines. **Original commits can be viewed at these duplicate repositories:**<br>
(1) [site-history](https://github.com/mariachlkt/site-history), (2) [gallery-history](https://github.com/mariachlkt/_gallery-history) & (3) [images-history](https://github.com/mariachlkt/images-history)
</br>

<h2>Summary</h2>
Throughout the time spent in this course, we were introduced to many useful and established technologies used in Software Engineering.
With each weekly assignment in lab classes, we were able to enhance our knowledge in services like Github, Netlify, and Docker among others.
The coursework consisted of theoretical lectures as well, exploring early technologies of the 1960s-1980s that shaped the modern technology landscape as we know it today.
This historical background is rather important because it highlights the needs of the modern software market by singling out the technologies that stood the test of time.

The weekly video quizzes, Classtime quizzes and weekly assignments are included in the report and can be navigated by the table of contents.
Issues that have occurred are covered in detail in each respective section of this report.


</br>


<h2> Video Quiz</h2>

|**Alan Kay at MIT EECS**|  
| :--------: | 
<details>
  <summary>Ποια είναι σύμφωνα με τον Αλαν Κεη η μεγαλύτερη παγίδα σε ένα μάθημα υπολογιστών και ποια είναι κατά την γνώμη σας η αντίστοιχη της ΙΒΜ τεχνολογία λογισμικού στις μέρες μας;</summary>
</br>
Στην συγκεκριμένη ομιλία, ο Άλαν Κευ παραθέτει ως παράδειγμα έναν διδάκτορά του, ο οποίος ακολουθούσε την εξής τακτική διδασκαλίας. Συγκεκριμένα, κατείχε την θεώρηση πως οι μαθητές θα ήταν ωφέλιμο να αποκομίσουν όσο το δυνατόν περισσότερες γνώσεις για την επιστήμη της πληροφορικής από τα υπάρχοντα συγγράμματα και όχι από τον ίδιο. Παράλληλα, ένα από τα κατορθώματά του ήταν πως προσπαθούσε να αναδείξει τα σφάλματα των μαθητών χωρίς να τους παραθέτει τις επιλύσεις, με αποτέλεσμα να οι μαθητές να απαιτείται να σκεφτούν και να αναζητήσουν τις απαραίτητες διορθώσεις, αποκτώντας έτσι κριτική σκέψη και έχοντας την ευρύτερη εικόνα σε θέματα του κλάδου τους. Ωστόσο, ο προαναφερόμενος πραγματοποιούσε συζητήσεις, στις οποίες οι πεποιθήσεις των φοιτητών, που δεν ήταν ρεαλιστικές, αντικρούονταν από εκείνον, ώστε να τους μεταλαμπαδεύσει αντικειμενικές γνώσεις. Τα παραπάνω αποτελούν παγίδα σ’ ένα μάθημα υπολογιστών, αν δε εφαρμοστούν ανάλογα.
</details>
<details>
  <summary>Ποια είναι η αναλογία του πραγματικού κόσμου για την αρχιτεκτονική και για τα υλικά και για ποιο λόγο δεν είναι εφαρμόσιμη στην περίπτωση του λογισμικού;</summary>
</br>
Αναφορικά με την αναλογία του πραγματικού κόσμου για την αρχιτεκτονική και τα υλικά, καθώς και για τους λόγους που δεν είναι εφαρμόσιμη στην περίπτωση του λογισμικού ο Αλαν Κευ παραθέτει κάποια παραδείγματα, Ειδικότερα, αναφέρει πως ένα παιδί μικρής ηλικίας δύνανται να κατασκευάσει απλά αντικείμενα, όπως ένα σπίτι για σκύλους, αφού κατέχει απλή αρχιτεκτονική και ποίκιλλα υλικά μπορούν να χρησιμοποιηθούν, αφού μπορούν να το  υποστηρίξουν. Εν  αντιθέσει, τα άτομα που αναπτύσσουν λογισμικό, τα οποία απαιτούνται να έχουν γνώσεις και δεξιότητες σχετικά με το ζήτημα.
</details>
<details>
  <summary>Ποιες είναι οι βασικές αναφορές έμπνευσης που οδήγησαν τον Αλαν Κεη στην ιδέα του αντικειμενοστραφούς προγραμματισμού και πως λύνεται τελικά το πρόβλημα της αρχιτεκτονικής και των υλικών;</summary>
</br>  
Οι πηγές έμπνευσης, που οδήγησαν τον Αλαν Κεη στην ιδέα του αντικειμενοστραφούς προγραμματισμού αποτέλεσε ο τρόπος με τον οποίο ο David Evans υλοποίησε τα γραφικά στους υπολογιστές και η ενασχόληση του με το σύστημα Simula. 
</details>  
<details>
  <summary>Ποιες είναι οι δύο δυνατές ιδέες που χαρακτηρίζουν το λογισμικό του πρώτου ερευνητικού προσωπικού συστήματος;</summary>
</br>  
Οι δύο δυνατές ιδέες, που χαρακτηρίζουν το λογισμικό του πρώτου ερευνητικού προσωπικού συστήματος είναι οι εξής. Αρχικά, η πρώτη, η οποία  βασίζεται στον κλάδο της βιολογίας  παραθέτει πως ένας οργανισμός αποτελείται πολλά κύτταρα. Αυτό σημαίνει πως, ένα κύτταρο δεν είναι από μόνο του ένας οργανισμός αλλά μέρος αυτού. Αντίστοιχα, κι οι δομές δεδομένων και οι διαδικασίες δεν έχουν την ίδια ισχύ με έναν υπολογιστή. Η επόμενη ιδέα είναι εμπνευσμένη από την βιολογία και στην διαδικασία της μορφογένεσης, στην οποία το DNA δεν αρκεί για να σχηματίζει νέο κύτταρο, αλλά απαιτείται ένα κύτταρο να το περιβάλλει.
</details>
</br>

|**Τed Νelson-Computers for Cynics**|
| :--------: | 
</br>
<details>
  <summary>Ποιος είναι ορισμός της τεχνολογίας λογισμικού για τον Τεντ Νελσον και ποια είναι η διαφορά με το πακετάρισμα και τις πολιτικές της τεχνολογίας; Να δώσετε ένα      τουλάχιστον παράδειγμα όπου φαίνονται οι διαφορές.</summary>
</br>
Σύμφωνα με τον  Τεντ Νελσον, η  τεχνολογία λογισμικού παρομοιάζεται με  πατρική γονιμότητα, με αυτό να σημαίνει ότι υπάρχει πολύ αλλά  σε λιγότερο  βαθμό που τα άτομα πιστεύουν. Παράλληλα, το πακετάρισμα αποτελεί  το προιόν/λογισμικό, το οποίο  είναι διακριτό στα κοινό, ενώ οι πολιτικές τεχνολογίας αποτελούν βήματα/διαδικασίες με τις οποίες παράχθηκαν τα προαναφερόμενα προιόντα. Για παράδειγμα, το iPhone αποτελεί πακετάρισμα, ενώ το πρωτόκολλο TCP/IP μία πολιτική τεχνολογίας.
</details>
</br>
<details>
  <summary>Ποια ήταν η αρχική χρησιμότητα της τεχνολογίας των αρχείων; Είναι τα αρχεία ο καλύτερος τρόπος για την οργάνωση της πληροφορίας από την πλευρά του χρήστη;</summary>
</br>
Στην αρχική υπόσταση της τεχνολογίας των αρχείων, υπήρχαν περιορισμένες λειτουργίες και συγκεκριμένα είδη κειμένου δεν υποστηρίζονταν από λογισμικά ή τύπους αρχείων. Για παράδειγμα, τύπος σημειώσεων  (marginal notes/headnotes) δεν ήταν εφικτό να εγγραφούν σε  PDF ή σε Word File, λόγω έλλειψης χαρακτηριστικών και συμβατότητας.
Η αποθήκευση σε αρχεία αποτελεί ένα συνετό τρόπο οργάνωσης των δεδομένων, καθώς κάθε μεμονωμένο είδος πληροφορίας μπορεί να ανήκει σε διαφορετικό αρχείο και έπειτα υπάρχει η δυνατότητα ταξινόμησης των αρχείων με βάση την ημερομηνία δημιουργίας του, το όνομα  του ή ακόμη και από τον τύπο του. Αυτό έχει ως αποτέλεσμα την σύντομη και εύκολη  εκμαίευση   πληροφοριών.
</details>
</br>
<details>
  <summary>Ποια είναι σύμφωνα με τον Τεντ Νέλσον τα προβλήματα της γραφικής διεπαφής με αρχεία, φακέλους, και εφαρμογές και ποιες είναι οι τεχνολογίες στις οποίες θα πρέπει να βασίζεται με γραφική διεπαφή;</summary>
</br>
Με βάση τον Τεντ Νελσον, σε Unix λειτουργικά συστήματα  (Linux) δεν επιτρέπονταν η πρόσβαση και η ανάγνωση  αρχείων/εφαρμογών, όταν αυτά κατείχαν κενά στο όνομά τους, δημιουργώντας πρόβλημα συμβατότητας σε αρχεία που προέρχονταν από Windows  και MacOS. Παράλληλα, μία γραφική διεπαφή θα έπρεπε να στηρίζεται στην ιεραρχία των καταλόγων (directories), δηλαδή κάθε φάκελος να περιέχει ονόματα άλλων φακέλων (hierarchical directories).
</details> 
</br>
<details>
  <summary>Γιατί είναι τόσο απαραίτητοι όσοι γνωρίζουν την τεχνολογία λογισμικού στις βάσεις δεδομένων;</summary>
</br>
Η ανάπτυξη λογισμικού και η τεχνολογία των βάσεων δεδομένων σχετίζονται με διάφορους τρόπους. Συγκεκριμένα, χρησιμοποιούνται μέθοδοι λογισμικού και εργαλεία  για την ανάπτυξη εφαρμογών και λειτουργιών βάσεων δεδομένων. Αντίστοιχα, η τεχνολογία βάσεων δεδομένων μπορεί να υποστηρίζει μέσω κατάλληλων υπηρεσιών τις δραστηριότητες, τα εργαλεία και τις τεχνικές, που εφαρμόζονται στις διαδικασίες ανάπτυξης λογισμικού.   	
</details>
</br>

|**Alan kay-Computing Simply**|
| :--------: | 

<details> 
  <summary>Ποιες ήταν οι βασικές ιδέες που επηρέασαν τον Αλαν Κεη στην κατασκευή νέου λογισμικού;</summary>
</br>
Μία από τις βασικές ιδέες , που είχαν σημαντική επιρροή στον Αλαν Κεη για την κατασκευή νέου λογισμικού, ήταν ο παραλληλισμός του με ένα βιβλίο χημείας. Συγκεκριμένα, όσοι διάβαζαν το βιβλίο μπορούσαν να καταλάβουν την θεματική του και να αποκτήσουν πληροφορίες, ακόμη κι αν δεν κατείχαν τις απαραίτητες γνώσεις. Έτσι, οι χρήστες θα μάθαιναν να χρησιμοποιούν το λογισμικό κατά την διάρκεια της χρήσης τους, χωρίς να κατέχουν την εμπειρία και την γνώση.
</details>
</br>
<details>
  <summary>Να δώσετε παράδειγμα από την προσωπική σας εμπειρία για λογισμικό με καλή και με κακή αρχιτεκτονική με αναφορά στα κριτήρια της επιλογής σας.</summary>
</br>
Κατά την γνώμη μου, ένα χρήσιμο λογισμικό με ιδιαίτερα καλή αρχιτεκτονική αποτελεί το MS Office Word. Συγκεκριμένα, οι χρήστες εύκολα και σε σύντομο χρονικό διάστημα δύνανται να δημιουργήσουν εργασίες έχοντας ποίκιλλες επιλογές για το σχεδιασμό, την προσθήκη διάφορων εικόνων/σχημάτων/συμβόλων, την υλοποίηση μαθηματικών εξισώσεων και την υπαγόρευση κειμένου σε οποιαδήποτε γλώσσα. Τα άτομα μπορούν εύκολα να εντοπίσουν το κουμπί για την αντίστοιχη επιθυμητή λειτουργία, λόγω του φιλικού προς τον χρήστη UI (User Interface) , που διαθέτει.  Αντίθετα , το Ghost Browser αποτελεί έναν φυλλομετρητή, ο οποίος βασίζεται σε παλιότερες εκδόσεις άλλου browser (αν και υπάρχουν νεότερες εκδόσεις),δεν διαθέτει φιλικό UI και στο γενικό πλαίσιο η χρησιμοποίησή του δεν παρέχει την ιδιωτικότητα, που υπόσχεται σε σχέση μ΄ άλλα παρεμφερή λογισμικά.
</details>
</br>
<details>
  <summary>Ποια είναι τα βασικά δομικά στοιχεία στην αρχιτεκτονική του λογισμικού etoys και από που άντλησε ο Αλαν Κέη την έμπνευση για αυτά;</summary>
</br>
--
</details>
</br>
<details>
  <summary>Ποια είναι κάποια από τα λάθη των σύγχρονων λειτουργικών συστημάτων σύμφωνα με τον Αλαν Κέη;</summary>
</br>
Σύμφωνα με τον Αλαν Κεη, το UI των σύγχρονων λειτουργικών συστημάτων φαίνεται να μοιάζουν περισσότερο με Nuclear Reactor Control Panel, όπου οι χρήστες αποκτούσαν  πληροφορίες και γνώση για την χρήση του, εν αντιθέσει με το νέο περιβάλλον (Personal Amplification Environment), με το οποίο λάμβαναν ουσιαστικές  πληροφορίες έχοντας ως αποτέλεσμα την εκμάθηση και την απόκτηση  ικανοτήτων.  
</details>
</br> 
 
|**Bret Victor-The Future of Programming**|
| :--------: | 
</br>
<details>
  <summary>Γιατί υπάρχει αντίσταση απέναντι στις νέες γλώσσες προγραμματισμού υψηλού επιπέδου; Να δώσετε ένα παράδειγμα από την δική σας εμπειρία.</summary>
</br>
Σύμφωνα με τον Bret Victor, τα άτομα, που κατέχουν γνώσεις και δεξιότητες από ήδη υπάρχουσες γλώσσες προγραμματισμού, δεν είναι δεκτικοί σε νέες γλώσσες, καθώς χρειάζεται να μάθουν από την αρχή και να έχουν νέο και διαφορικό τρόπο σκέψης για την αφομοίωση καινούριων ιδεών.
</details>
</br>
<details>
  <summary>Προγραμματίζουμε την ιστοσελίδα της σχολής χωρίς στυλ και ετικέτες! Πέτυχε την πρόβλεψη του ή εμείς κάνουμε κάτι διαφορετικό από τον συνηθισμένο προγραμματισμό ιστοσελίδας;</summary>
</br>
Με βάση τον Victor, σε μελλοντικές δεκαετίες θα μπορούμε να προγραμματίζουμε την ιστοσελίδα της σχολής και γενικά γραφικό περιβάλλον με άμεσο χειρισμό χωρίς την χρήση γλωσσών σήμανσης (markup languages).
</details>
</br>
<details>
  <summary>Προγραμματίζουμε την ιστοσελίδα της σχολής με κείμενο. Γιατί πέφτει τόσο έξω στην πρόβλεψη του;</summary>
</br>
Ο προγραμματισμός της ιστοσελίδας της σχολής με κείμενο είναι πιθανό να μην αποφέρει τα επιθυμητά αποτελέσματα , καθώς με αυτό τον τρόπο προγραμματισμού δεν  αναφέρουμε τον τρόπο με τον οποίο θα  κατασκευάσουμε την ιστοσελίδα αλλά την τελική μορφή της. Αυτό έχει ως αποτέλεσμα, το ίδιο το πρόγραμμα να αποφασίζει τον τρόπο, που θα το υλοποιήσει.
</details>
</br>
<details>
  <summary>Ποιος είναι υπεύθυνος για το προγραμματιστικό δόγμα των ημερών μας και πως θα μπορούσαμε να σκεφτούμε με νέους τρόπους;</summary>
</br>
--
</details>
</br>

|**Alan Kay-Programming**|
| :--------: | 
</br>
<details>
  <summary>Ποια είναι η χρησιμότητα του προγραμματισμού στον συστημικό τρόπο σκέψης με παράδειγμα πέρα από αυτό που περιγράφει ο Άλαν Κέη;</summary>
</br>
Στην εποχή μας, τα άτομα δεν αρκείται να κατέχουν βασικές στοιχειώδεις γνώσεις, αλλά να μπορούν να συνδυάζουν τις δεξιότητές τους σε διαφορετικούς τομείς. Συγκεκριμένα, ποίκιλλα θέματα θα μπορούν να συνυπάρξουν μέσω του προγραμματισμού.  
</details>
</br>
<details>
  <summary>Για ποιο λόγο κατασκευάζουμε συνήθως το λογισμικό σε επίπεδα και με ποια κριτήρια ορίζουμε τον προγραμματισμό σε κάθε ένα από αυτά;</summary>
</br>
Ο κώδικας του λογισμικού αποτελείται συνήθως από επίπεδα, ώστε η κατασκευή του να είναι μία διαδικασία, η οποία εκπονείται με οργάνωση και βήματα, διευκολύνοντας στην εύρεση τυχών σφαλμάτων και στην ορθή ανάπτυξη του κώδικα. 
Τα επίπεδα αυτά είναι τα εξής. Αρχικά, το πιο χαμηλό επίπεδο είναι ο Processor (επεξεργαστής), στο οποίο ο χρήστης κατασκευάζει χαμηλού επιπέδου κώδικα. Στο επόμενο αντιστοιχεί το Small Talk Byte-Coded Virtual Machine, κάνοντας τον υπολογιστή να μοιάζει με μηχάνημα Small Talk και  έπειτα το Etoy’s Interpreter Machine, στο οποίο συγκεκριμένο μέρος του προγράμματος είναι γραμμένο σε  small talk. Στο τελευταίο επίπεδο είναι το Rule-based parallel Particle Interpreter Machine, όπου αντιμετωπίζονται τυχόν σφάλματα-προβλήματα από ολόκληρο τον κώδικα (από όλα τα επίπεδα).
</details>
</br>
<details>
  <summary>Γιατί το σύγχρονο λογισμικό έχει τόσες πολλές γραμμές κώδικα και πως θα μπορούσε ναtatαλλάξει σε κάτι πιο συμπαγές;</summary>
</br>
--
</details>
</br>
<details>
  <summary>Ποιες είναι οι σημαντικές ιδέες στο λογισμικό που χρησιμοποιεί ο Άλαν Κέη και πως διαφέρουν από αντίστοιχα σύγχρονα λογισμικά με αντίστοιχες δυνατότητες;</summary>
</br>
--
</details>
</br> 

|**Alan Kay - Turing Award Lecture**|
| :--------: | 
</br> 
<details>
  <summary>Είναι χρήσιμα στην πληροφορική τα μαθήματα των μαθηματικών που κάνατε στο 1ο έτος και γιατί;</summary>
</br>  
Η επιστήμη των μαθηματικών είναι άρρηκτα συνδεδεμένη με την επιστήμη της πληροφορικής. Συγκεκριμένα, τα μαθήματα Πιθανότητες και Στατιστική συμβάλλουν στην κατανόηση πιθανοθεωριτικών μοντέλων και υπολογιστικών εργαλείων, καθώς επίσης και τα μαθήματα  Μαθηματικός Λογισμός και  Γραμμική Άλγεβρα παρέχουν βασικές  δεξιότητες στην μοντελοποίηση υπολογιστικών συστημάτων μέσω ανάλογων θεωρημάτων. Επομένως, τα μαθήματα αυτού του κλάδου είναι ιδιαίτερα σημαντικά και χρήσιμα, συμβάλλοντας στην ομαλή προσέγγιση εισαγωγικών  ζητημάτων της πληροφορικής και στην επαφή με τον απαιτούμενο τρόπο σκέψης.
</details>
</br> 
<details> 
  <summary>Είναι η πληροφορική επιστήμη ή κλάδος των μηχανικών; ποια είναι τα κριτήρια για να ανήκει σε κάποιον από αυτούς τους κλάδους;</summary>
</br>
Σύμφωνα με τον Άλαν Κει, η πληροφορική αποτελεί επιστήμη. Συγκεκριμένα, παραθέτει ένα παράδειγμα διαφοροποίησής των δύο παραπάνω κλάδων το οποίο είναι το εξής. Αναφέρει, λοιπόν, για ένα project, που αφορά την μηχανική, την  κατασκευή του Empire State Building, η οποία  χρειάστηκε περίπου τρείς χιλιάδες άτομα και ολοκληρώθηκε στο χρονικό διάστημα των 11 μηνών. Αντίθετα, στον τομέα της πληροφορικής δεν θα ήταν δυνατό να συνεργαστούν τόσοι πολλοί άνθρωποι για την παραγωγή ενός  έργου σε τόσο λίγο χρόνο, το οποίο μάλιστα θα είχε τα επιθυμητά αποτελέσματα. 
</details>
</br> 
<details>
  <summary>Γιατί οι περισσότεροι δεν μπορούν να καταλάβουν τις ιδέες του Νταγκλας Ενγκελμπαρτ για την διάδραση με ψηφιακά συστήματα;</summary>
</br>
Στο τομέα της πληροφορικής, οι περισσότεροι άνθρωποι παρατηρείται πως επιλέγουν να αντιμετωπίζουν και να επιλύουν ανάλογα ζητήματα με πολύπλοκο τρόπο, καθώς νιώθουν ιδιαίτερη χαρά μ΄ αυτό. Αυτό έχει ως αποτέλεσμα, να μην μπορούν να αντιληφθούν τις ιδέες του Νταγκλας Ενγκελμπαρτ και να δυσκολεύουν την προσπάθεια διαχείρισης προβλημάτων χωρίς να χρειάζεται.
</details>
</br>
<details>
  <summary>Ποιες ήταν οι θεμελιώδεις εμπνεύσεις και αναλογίες για την δουλειά του;</summary>
</br>
--
</details>
</br>
<details>
  <summary>Ποια είναι τα βασικά προβλήματα της 3βάθμιας εκπαίδευσης στην πληροφορική;</summary>
</br>
Οι καθηγητές στην τριτοβάθμια εκπαίδευση στην πληροφορική παρατηρείται πως πραγματοποιούν το μάθημα με τέτοιο τρόπο, όπου απλά μεταδίδουν πληροφορίες σ’ μία συγκεκριμένη γκάμα και όχι αναλύοντας το ευρύτερο πλαίσιο (μεγάλη εικόνα) του μαθήματος δείχνοντας την ρεαλιστική του πλευρά. Αυτό έχει ως αποτέλεσμα, οι φοιτητές να μην κατέχουν ιδιαίτερα πολλές γνώσεις και δεξιότητες και ό,τι έχουν αποκομίσει, να το γνωρίζουν με λάθος και μη παραγωγικό τρόπο για την κριτική τους σκέψη. 
</details>
</br>
<details>
  <summary>Πως διαφέρει ο αντικειμενοστραφής προγραμματισμός που περιγράφει από αυτόν που διδαχτήκατε στο αντίστοιχο μάθημα;</summary>
</br>
Σύμφωνα με τον Άλαν Κευ, η διδασκαλία του αντικειμενοστραφούς προγραμματισμού περιγράφεται ως μία διαδικασία, στην οποία ο καθηγητής αναφέρει την ευρύτερο πλαίσιο του μαθήματος, συμβάλλοντας στην ομαλή επαφή   των μαθητών και στην απόκτηση του κατάλληλου τρόπου σκέψης. Ομοίως, διδαχτήκαμε το συγκεκριμένο μάθημα, με παρόμοιο τρόπο, δηλαδή ο καθηγητής μας ανέφερε τα χαρακτηριστικά αυτού του είδους προγραμματισμού και έπειτα προχώρησε σε περεταίρω λεπτομέρειες. 
</details>
</br>

|**Alan Kay-Invention**|
| :--------: | 
</br>
<details>
  <summary>Ποια πρέπει να είναι τα κριτήρια της αξιολόγησης στην εκπαίδευση και στο λογισμικό αν ο στόχος είναι η καινοτομία;</summary>
</br> 
Στο συγκεκριμένη ομιλία ο Αλαν Κευ, παραθέτει την οπτική του αναφορικά με τα κριτήρια αξιολόγησης στην εκπαίδευση και στο λογισμικό. Συγκεκριμένα, αναφέρει πως μαθητές από τα πρώτα τους σχολικά χρόνια, μαθαίνουν να διαχειρίζονται επιλυμένα προβλήματα, χωρίς να τους δίδετε η ευκαιρία να αναζητήσουν δικές τους λύσεις. Αυτό έχει ως αποτέλεσμα, να αρκούνται σε μηδαμινές προσπάθειες , αποκτώντας ανεπαρκείς γνώσεις και να μην μπορούν να αντιληφθούν την έννοια της σκληρής δουλειάς. 
</details>
</br> 
<details> 
  <summary>Πως μπορούμε να φτιάξουμε σήμερα το λογισμικό για τους υπολογιστές που θα έχουμε σε δέκα ή περισσότερα χρόνια;</summary>
</br> 
Με βάση τον Αλαν Κευ, η κατασκευή λογισμικού σήμερα για μελλοντικούς υπολογιστές, αρχικά θα επιτευχθεί με τον προγραμματιστή να μην σκέφτεται τις δυνατότητες των τωρινών μηχανημάτων, καθώς αυτά αντιπροσωπεύουν το παρόν και το παρελθόν. Επομένως, το άτομο, που θα κατασκευάσει το λογισμικό δεν πρέπει να λάβει υπόψιν του τέτοιες παραμέτρους  και λέξεις.
</details>
</br> 
<details> 
  <summary>Ποια είναι η αναλογία του ποδήλατου με βοηθητικές ρόδες για την περίπτωση του λογισμικού;</summary>
</br> 
Ο Αλαν Κευ παραθέτει το εξής παράδειγμα. Συγκεκριμένα, αναφέρει πως τα ποδήλατα με βοηθητικές ρόδες συντελούν στην απόκτηση τέτοιων δεξιοτήτων των παιδιών. Ωστόσο, ο συγκεκριμένος τρόπος εκμάθησης δεν έχει ταχύτερα ή καλύτερα αποτελέσματα, καθώς τα παιδιά μαθαίνουν να ισορροπούν στις τέσσερις ρόδες του ποδηλάτου και όχι στις δύο. Κατά συνέπεια, στην περίπτωση του λογισμικού δεν πρέπει να δίδονται κατευθυντήριες και βοηθητικές γραμμές, οι οποίες όχι μόνο δεν θα βοηθήσουν τον χρήστη να διορθωθεί, αλλά μπορεί να τον δυσκολέψει περισσότερο να εξελιχθεί και να επιτύχει τους στόχους του.  
</details>
</br>
<details>
  <summary>Για ποιο λόγο είναι δύσκολη η κατασκευή λογισμικού διεπαφής με τον χρήστη;</summary>
</br>
Με βάση τον Άλαν Κευ, η κατασκευή λογισμικού διεπαφής με τον χρήστη είναι δύσκολη, καθώς αυτό πρόκειται να χρησιμοποιηθεί από μεγάλο αριθμό ατόμων. Συγκεκριμένα, ο προγραμματιστείς για να επικυρώσει την επιτυχία του λογισμικού πρέπει να λάβει υπόψιν του, τις λειτουργίες και τα χαρακτηριστικά που επιθυμούν όλοι οι χρήστες. Ωστόσο, το προαναφερόμενο δεν είναι εφικτό να πραγματοποιηθεί, και επιστήμες όπως η ψυχολογία, μπορούν να συνδράμουν σημαντικά.  
</details>
</br>
<details> 
  <summary>Πως πρέπει να είναι οργανωμένη μια ομάδα για να αντιμετωπίσει με την βοήθεια της πληροφορικής δύσκολες αποφάσεις και τι σημαίνει αυτό για την οργάνωση μιας ομάδας που βρίσκεται στην διαδικασία της εκπαίδευσης;</summary>
</br>
Με βάση τον Αλαν Κευ, μία ομάδα για να μπορέσει να αντιμετωπίσει δύσκολες αποφάσεις,χρησιμοποιώντας τον κλάδο της πληροφορικής, θα ήταν ωφέλιμο να αποτελούνταν από διαφορετικό τύπο ατόμων, ώστε ο καθένας να μπορεί να συμβάλλει με τον δικό του ξεχωριστό τρόπο.
</details> 
</br>

|**Jaron Lanier-Intertwingled**|
| :--------: | 
</br>
<details>
  <summary>Ποια είναι η τεχνολογική λύση για το πρόβλημα της οικονομικής ανισότητας που δημιουργεί η συγκέντρωση οικονομικού κεφαλαίου σε λίγους;</summary>
</br>
Στην συγκεκριμένη ομιλία, ο Jaron Lanier παραθέτει μία επίλυση στο πρόβλημα της οικονομικής ανισότητας που δημιουργεί η συγκέντρωση οικονομικού κεφαλαίου σε λίγους. Συγκεκριμένα, προτείνει ένα σύστημα μικρών συναλλαγών, στο οποίο θα παρακολουθούνται οι συνεισφορές των ατόμων στο Ψηφιακό Οικοσύστημα. Μάλιστα, τα μηχανήματα εξαρτώνται από συστήματα πληροφόρησης με δεδομένα, που οι άνθρωποι παρέχουν και εξαιτίας του γεγονότος πως τα πληροφοριακά συστήματα χρειάζονται νέες πληροφορίες, αυτό θα έχει ως αποτέλεσμα να δημιουργηθεί μία κοινωνία, στην οποία καθένας θα συνεισφέρουν για την ομαλή και δίκαια λειτουργία της.
</details>
</br>
<details>
  <summary>Για ποιο λόγο η τεχνολογία της αντιγραφής και επικόλλησης είναι ασύμβατη με τους δικτυωμένους υπολογιστές;</summary>
</br>
Με βάση τον Jaron Lanier, η τεχνολογία της αντιγραφής και επικόλλησης είναι ασύμβατη, καθώς σε ένα δίκτυο το πρωτότυπο είναι διαθέσιμο και αρκεί μόνο μία αναφορά στο αρχείο για την χρήση του. Επιπλέον, διατηρώντας το πρωτότυπο, καθένας δύνανται να κατέχει συνεχείς πληροφόρηση για το ιστορικό και την προέλευσή του, με αποτέλεσμα να έχει περισσότερα δεδομένα.
</details>
</br>
<details>
  <summary>Ποιες είναι οι οικονομικές, πολιτισμικές, και πολιτικές επιπτώσεις της τεχνολογικής επιλογής των μονόδρομων υπερσυνδέσμων στα ψηφιακά έγγραφα;</summary>
</br>
Κατά διαδικασία υλοποίησης του διαδικτύου,  σημειώθηκε πως το Ίντερνετ περιέχει μονόδρομους υπερσυνδέσμους με γνωστές μόνο τις τελικές τοποθεσίες, ενώ παρέμεναν άγνωστες οι ενδιάμεσες  τοποθεσίες, που βοηθούσαν τον χρήστη να φτάσει στον τελικό του στόχο. Ωστόσο, ο τρόπος αυτός είχε αρνητικό αντίκτυπο στην κοινωνία. Συγκεκριμένα, την εύρεση όλων των τοποθεσιών και την ξεκαθάριση των υπερσυνδέσμων ανέλαβαν εταιρίες, οι οποίες παρείχαν τη διαδικασία αυτή ως πληρωτέα υπηρεσία. Αυτό είχε ως αποτέλεσμα, την μεγάλη ιδιωτικοποίηση και κατά συνέπεια την εισοδηματική ανισότητα και την συρρίκνωση της μεσαίας τάξης.
</details>
</br>
<details>
  <summary>Ποιες είναι οι βασικές συνεισφορές του Ted Nelson στην τεχνολογία σύμφωνα με τον Jaron Lanier και πως διαφέρουν από την τεχνολογία που έχουμε τώρα;</summary>
</br>
--
</details>
</br>

|**Alan Kay-Scaling**|
| :--------: | 
<details>
  <summary>Με ποιο τρόπο συνεργαστήκατε σε ιδέες δικές σας και άλλων σε αυτό το μάθημα</summary>
</br>
Στο συγκεκριμένο μάθημα, υπήρξε συνεργασία για την υλοποίηση κάποιων ιδεών ανάμεσα με μερικούς συμφοιτητές κι εμένα με τον εξής τρόπο. Ειδικότερα, προσπαθούσαμε να αλληλοβοηθηθούμε στην εκπόνηση συγκεκριμένων παραδοτέων για διαδικαστικούς λόγους είτε στο πλαίσιο εργαλείων είτε στο προγραμματιστικό τομέα, καθώς επίσης πραγματοποιούσαμε συζητήσεις για τον καταιγισμό ιδεών (brainstorming).
</details>
</br>
<details>
  <summary>Το καλύτερο μάθημα που παρακολούθησε ο Αλαν Κεη ως φοιτητής του έδωσε γνώσεις πάνω σε συστήματα που υπήρχαν;</summary>
</br>
Σύμφωνα με τον Αλαν Κεη, κατά την διάρκεια των σπουδών του παρακολούθησε το μάθημα Προηγμένος Σχεδιασμός Συστημάτων (Advanced system design), στο οποίο ο καθηγητής Bob Barton, επιδίωξε να αφαιρέσει τις πεποιθήσεις και τις ιδέες, που κατείχαν οι μαθητές. Αυτό είχε ως αποτέλεσμα, να αποκομίσουν γνώσεις και νέες ιδέες, οι οποίες δεν σχετίζονταν απαραίτητα με το ιδανικό μέλλον.
</details>
</br>
<details>
  <summary>Σε ποια εταιρεία αναφέρεται και γιατί είναι πρόβλημα να έχουμε πολλές γραμμές κώδικα;</summary>
</br>
Ο Αλαν Κευ αναφέρεται στην Microsoft και αναφέρει πως όταν έχουμε πολλές γραμμές κώδικα δεν είναι δυνατή η εύκολη εύρεση ενός σφάλματος (bug) και η πολυπλοκότητα του είναι υψηλή. 
</details>
</br>
<details>
  <summary>Με τι μοιάζει το λογισμικό σήμερα και ποιο είναι ένα καλύτερο παράδειγμα για το μέλλον αναφορικά με την αρχιτεκτονική και τον τρόπο ανάπτυξης του;</summary>
</br>
Το λογισμικό, στις μέρες μας, μοιάζει μ΄ ένα είδος που περιλαμβάνει αντικείμενα, όπως μηχανισμούς και βιολογικά είδη.
Ο Αλαν Κευ παραθέτει το εξής ερώτημα, ποιο θα ήταν το τελικό αποτέλεσμα εάν κατασκευάζαμε ένα διαδραστικό λογισμικό και τι παραπάνω λειτουργίες θα είχε πέρα από αυτές που εμείς δημιουργήσαμε, το οποίο σχετίζεται με έναν εξελιγμένο τρόπο ανάπτυξης του. Για παράδειγμα, η αναπροσαρμογή του λογισμικού ανάλογα με τις τρέχουσες ανάγκες ουσιαστικά μειώνει το κόστος παραγωγής και τροποποιεί τις υπάρχουσες απαιτήσεις. 
</details>
</br>
<details>
  <summary>Γιατί δεν αρκεί η εξυπνάδα και οι γνώσεις και απαιτείται όραμα, ποιο είναι το πρόβλημα με την δημοφιλή Javascript;</summary>
</br>
Σύμφωνα με τον Αλαν Κευ, ο προγραμματισμός με Javascript, μίας αντικειμενοστραφούς γλώσσας, δεν έχει καλύπτει ευρεία γκάμα θεμάτων, με αποτέλεσμα ένας τέτοιος κώδικας να δύναται να χρησιμοποιηθεί για περιορισμένους σκοπούς.
</details>
</br>
<details>
  <summary>Με ποιο τρόπο το μάθημα μας εφαρμόζει στην πράξη τις συμβουλές του Αλαν Κέη αναφορικά με την αξία παλιών ιδεών και εργαλείων;</summary>
</br>
Το μάθημα ‘Τεχνολογίες Λογισμικού’ διδάσκει διαχρονικά εργαλεία και πεποιθήσεις παλαιότερων ετών, που στιγμάτισαν τον κόσμο της Πληροφορικής. Συγκεκριμένα, υπάρχουν πολλές αναφορές στα άτομα-εφευρέτες, στον τρόπο κατασκευής και λειτουργίας των λογισμικών, ενώ ταυτόχρονα προσπαθεί να μας ωθήσει να αντιληφθούμε τις διαφορές μεταξύ των τότε ιδεών και εργαλείων με τα σημερινά αντίστοιχα.
</details>
</br>

|**Alan Kay-Turing Tarpit**|
| :--------: | 

<details>
  <summary>Αν ο προγραμματισμός δεν είναι η βασική δραστηριότητα της τεχνολογίας λογισμικού, ποια είναι κάποια καλά παραδείγματα;</summary>
</br>
-
</details>
</br>
<details>
  <summary>Με ποιο τρόπο το μάθημα μας σας εκπαιδεύει να εντοπίζετε νέα προβλήματα αντί να λύνετε προβλήματα που σας δίνονται έτοιμα;</summary>
</br>
Το μάθημα ‘Τεχνολογίες Λογισμικού διδάσκεται με συγκεκριμένο τρόπο, με τον οποίο ωθεί τους μαθητές να αναζητούν νέες προσωπικές λύσεις και εργαλεία για την επίλυση των ήδη υπάρχοντων προβλημάτων. Ωστόσο, κατά τη διάρκεια της προαναφερόμενης διαδικασίας, είναι πιθανή η δημιουργία νέων ζητημάτων. 
</details>
</br>
<details>
  <summary>Γιατί ο Αλαν Κέη χρησιμοποιεί ένα σύστημα χωρίς εφαρμογές και αρχεία και κάνει την παρουσιάση του χωρίς Powerpoint, τι θέλει να μας πει για την τεχνολογία λογισμικού με αυτήν την επιλογή του;</summary>
</br>  
Ο Αλαν Κευ, χρησιμοποιεί το σύστημα ‘Frank’ για την παρουσίαση του, το οποίο μπορούμε να το σκεφτούμε ως ένα λειτουργικό σύστημα. Παρατηρώντας τις ομιλίες και τις πεποιθήσεις του μπορούμε να αντιληφθούμε ότι προτιμούσε διαφορετικά εργαλεία από τα ευρέως γνωστά και η δυνατότητα διάδρασης και επεξεργασίας πολλών τύπων αρχείων σε ένα παράθυρο συντελεί στην χρησιμοποίηση του . Επιπλέον, το σύστημα αυτό αποτελείται από 20 χιλιάδες γραμμές κώδικα εν αντιθέσει με τα γνωστά ΛΣ, που κατέχουν τουλάχιστον 200 εκατομμύρια γραμμές, γεγονός που αποτελεί έναν ιδιαίτερο λόγο χρήσης, όπως αναφέρει και στην συγκεκριμένη ομιλία του.  
</details>
</br>
<details>
  <summary>Ποιος είναι καλύτερος τρόπος για να έχουμε μικρά και εκφραστικά προγράμματα;</summary>
</br>
-
</details>
</br>

|**Alan Kay-Future Software Development**|
| :--------: | 
</br>
<details>
  <summary>Πως διαφέρουν οι προδιαγραφές στο σύστημα που δείχνει από τα σύγχρονα λειτουργικά και εφαρμογές;
   </br>
 -
</summary>
</details>
</br>
<details>
  <summary>Γιατί θα πρέπει το λογισμικό να αναπτύσεται με την διαδοχική συγγραφή εικονικών μηχανών;
   </br>
Το λογισμικό θα πρέπει να αναπτύσσσεται με την διαδοχική συγγραφή εικονικών μηχανών, κσθώς με την χρήση οπτικών μεθόδων είναι πιο εύκολο να αντιληφθεί τον κώδικά, που έχει αναπτυχθεί, έχοντας την δυνατότητα να το βλέπει το παραγόμενο αποτέλεσμα, σε πραγματικό χρόνο. Αυτό έχει ως αποτέλεσμα,  η διαδικασία του εντοπισμού σφαλμάτων στον κώδικα (debugging) να είναι πιο βατή και υλοποιήσιμη σε μικρό χρονικό διάστημα. 
 </summary>
</details>
</br>
<details>
  <summary>Ποια είναι η διαφορά του συστήματος που δείχνει από τα σύγχρονα λειτουργικά και τον παγκόσμιο ιστό;
   </br>
 Στη συγκεκριμένη ομιλία, ο Αλαν Κευ, μας δείχνει ένα σύστημα, το οποίο είναι απλό, καθώς απευθύνεται σε άτομα μικρής ηλικιακής ομάδας (παιδιά), και πλήρως παραμετροποιήσιμο, με αποτέλεσμα να διαφέρει η χρησιμοποίηση του από χρήστη σε χρήστη. 
</summary>
</details>
