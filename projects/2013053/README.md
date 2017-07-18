Μαθημα:  Τεχνολογία Λογισμικού 
Ονοματεπώνυμο: Παναγιωτης Κορμπας
ΑριθμοςΜητρώου:Π2013053
Εργασια:Pacman

# Pacman edited version

https://p13korb.github.io/pacman/

Παραδοτέο 1

Δήλωση και δέσμευση θέματος. Θέμα εργασίας: Pacman
Ονοματεπώνυμο: ΠΑΝΑΓΙΩΤΗΣ ΚΟΡΜΠΑΣ
ΑΜ: Π2013053

Παραδοτέο 2

Στο 2ο παραδοτέο στόχος είναι η αλλαγή του png εικονιδίου του pacman, των dots και η εισαγωγή νέου terrain. Πρώτα πρέπει να γίνουν upload τα αντίστοιχα αρχεία(π.χ. pacman2,dot2,terrain2) που θέλουμε να εισάγουμε. Για την διατήρηση των μεγεθών κατεβάζουμε πρώτα τις αντίστοιχες εικόνες png και επεξεργαζόμαστε την εικόνα εισάγωντας το δικό μας σχέδιο. Έπειτα στον κώδικα αλλάζουμε τις γραμμές : this.load.image('dot', 'assets/dot.png') και this.load.spritesheet('pacman', 'assets/pacman.png', 32, 32); 
Αυτές οι 2 γραμμές κώδικα κάνουν Load τα αρχεία dot.png και pacman.png. Αλλάζουμε τα ονόματα σε dot2.png και pacman2.png.

Για την δημιουργία του terrain θα χρησιμοποιήσουμε το Tiled (http://www.mapeditor.org/). Η γραμμή κώδικα που κάνει load το terrain είναι η εξής: this.load.tilemap('map', 'assets/pacman-map.json', null, Phaser.Tilemap.TILED_JSON);
Επίσης αλλάχτηκε το αρχείο tiles, μετατρέπωντας το μπλέ χρώμα στα τοιχώματα σε πράσινο. Επεξεργασία εικόνας έγινε με το paint.net.

Παραδοτέο 3

Για την προσθήκη μουσικής προστέθηκε το τμήμα κώδικα : 

     <audio autoplay loop>
        <source src="assets/Anonymous - Ductia.mp3" type="audio/mp3">
    </audio>
   
Για την καταμέτρηση του score, τροποποιήθηκε η συνάρτηση eatDot. Συγκεκριμένα προστέθηκε ήχος για κάθε φορά που χάνεται ένα νόμισμα, η συνάρτηση dot.play() καλέι τον ήχο "click.mp3" και αυξάνει το score κατά 1 "score=score+1".
Τέλος τοποθετεί την τιμή της μεταβλητής score στο μήνυμα. "TextScore". Οι μεταβλητές αυτές δηλώθηκαν στην αρχή του script "var score=0, var TextScore".

            var dot = new Audio('assets/click.mp3');
            dot.play()
            score = score + 1;
            TextScore.text='Score: ' + score;



