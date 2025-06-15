
# Τα Στοιχεία Μου
| Πλατφόρμα | Όνομα | Επώνυμο | Username | AM | Email |
| --- | --- | --- | --- | --- | --- |
| [Github](https://github.com/nkanagno) | Νικόλας | Αναγνωστόπουλος | nkanagno | inf2021013 | inf2021013@ionio.gr |

## Σημαντικοί συνδέσμοι:
- [Application online link](https://custom-character-ai-chatbot.onrender.com/)
- [Github Repo](https://github.com/nkanagno/custom-character-AI-chatbot/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Alan kay quora profile](https://www.quora.com/profile/Alan-Kay-11)
- [RAG wikipedia](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
- [RAG Fundamentals and Advanced Techniques](https://www.youtube.com/watch?v=ea2W8IogX80)

# Εισαγωγή Μαθήματος και Αρχική Στόχοι (Προχωρημένα Θέματα Τεχνολογίας Λογισμικού)
Μέσω του μαθήματος Προχωρημένα Θέματα Τεχνολογίας Λογισμικού, το οποίο δίνει βάση σε προχωρημένες διαδικασίες ανάπτυξης λογισμικού καθώς και σε εργαλεία που χρησιμοποιούνται σε αυτού του είδους διαδικασίες, ευελπιστώ να εξελίξω τον τρόπο σκέψης μου όσον αφορά την σχεδίαση και την ανάπτυξη λογισμικού μαθένοντας περισσότερα εργαλεία και τρόπους ανάπτυξης λογισμικού από αυτά/ους που ήδη γνωρίζω. 

Συγκεκριμένα, έχοντας εργαστεί ως software engineer τους περασμένους 10 μήνες με τεχνολογίες ανάπτυξης web εφαρμογών (όπως `React js, PostgreSQL και graphql`), έχω μάθει να μπορώ να αναλύω ένα πρόβλημα και να μπορώ να το μεταφέρω σε μορφή κώδικα προκειμένου να εξελίσσεται συνεχώς η κύρια web εφαρμογή της εταιρείας.

Παρότι της τρέχουσας εμπειρίας μου σε αυτόν τον τομέα, πιστεύω ότι πάντα υπάρχει χώρος για εξέλιξη και ότι μέσω των πολλαπλών και ξεχωριστών εργαλείων που θα αποκτήσω εμπειρία μέσω αυτού του μαθήματος, θα μπορέσω να εξελιχθώ περισσότερο και στην τρέχον δουλειά μου αλλά και για την μετέπειτα μελλοντική καριέρα μου ως software engineer.

# Alan kay chatbot τεχνιτής νοημοσύνης - Απαλλακτική Εργασία

## Περίληψη
Κατά την διάρκεια του μαθήματος, πραγματοποιήθηκε η ανάπτυξη ενός AI chatbot προσωποποιεί έναν custom χαρακτήρα της επιλογής του χρήστη αλλά επικεντρώνεται κυρίως στον χαρακτήρα του Alan kay, ένος σπουδαίου και πρωτοπόρου επιστήμονα στον κόσμο της τεχνολογίας. Έχοντας στην διάθεση μου τις πιο πρόσφατες τεχνολογίες τεχνητής νοημοσύνης όπως εξελιγμένα εργαλεία της OpenAi, η υλοποίηση αυτού του project μπόρεσε και ήταν εφικτή. Σημαντικά εργαλεία της OpenAi αποτέλεσαν το API, embedding μοντέλα τεχνητής νοημοσύνης και μία vector database. Η ένωση των παραπάνω εργαλειών, έκαναν εφικτή την υλοποίηση της προχωρημένου επιπέδου τεχνικής που είναι υπεύθυνη για την όλη ανάπτυξη της συγκεκριμένης εφαρμογής, και ονομάζεται Retrieval Augmented Generation ή αλλιώς RAG. Η τεχνική αυτή επιτρέπει την ανάπτυξη εξελιγμένων ΑΙ chatbots τα οποία είναι εκπαιδευμένα και απαντούν ερωτήσεις χρηστών πάνω σε ειδικά δεδομένα που είναι αποθηκευμένα σε μορφή αρχείου κειμένου όπως PDF, txt, markdown κλπ. Σε αυτή την περίπτωση οι γνώσεις του Alan kay chatbot βασίζονται σε δεδομένα ερωτοαπαντήσεων του Alan Kay, που βρίσκονται στο κεντρικό profile του στο QUORA και η επεξεργάσια τους έγινε μέσω της γλώσσας προγραμματισμού, Python. Τέλος, το μεγαλύτερο μέρος της εφαρμογής έγινε μέσω Python με τις πιο σημαντικές βιβλιοθήκες να είναι η streamlit για το User Ιnterface, η pandas για την επεξεργασία των δεδομένων και η OpenAi για το RAG.

## Εισαγωγή

### Retrieval Augmented Generation (RAG)
Η τεχνική `RAG` περιλαμβάνει 3 στάδια (`Retrieval` -> `Augmented` -> `Generation`).

To πρώτο είναι το `Retrieval` που ο χρήστης κάνει μία ερώτηση και λαμβάνει τα πιο σχετικά κομμάτια κειμένου που είναι αποθηκευμένα στην vector database. Μετά το `Augmented` όπου δίνονται αυτά τα κομμάτια ως context μαζί με την αρχική ερώτηση του χρήστη στο AI όπου έχει λάβει και ορισμένες οδηγίες. Τέλος είναι τo `Generation` όπου με βάση το context που του έχει δωθεί ως βαση γνώσης, το AI απαντάει πάνω στην αρχική ερώτηση του χρήστη κανόντας generate την τελική απάντηση.

![rag](https://github.com/user-attachments/assets/d0f20bb1-e2df-4cf8-93ca-841f72eb0083)

#### Δημιουργία vector database - προεπεξεργασία δεδομένων
Για να μπορέσει να εφαρμοστεί αυτή η τεχνική απαιτείται πρώτα η ανάπτυξη της vector database. Δηλαδή, το κείμενο κάθε αρχείου αρχικά χωρίζεται σε κομμάτια ορισμένου μεγέθους που ονομάζονται text chunks. Το κάθε κομμάτι μέσω ενός μοντέλου τεχνητής νοημοσύνης μετατρέπεται σε μια σειρά αριθμών ή αλλιώς αριθμητικών διανυσμάτων που ονομάζονται embeddings. Αυτά τα embeddings αποθηκεύονται στην vector database η οποία χρειάζεται για το retrieval στάδιο της τεχνικής RAG.

#### Λεπτομερής περιγραφή σταδίων
Με βάση το θεωρητικό υπόβραθρο της τεχνικής αυτής, παρακάτω γίνεται μια πιο λεπτομερής περιγραφή των 3 σταδίων (`Retrieval` -> `Augmented` -> `Generation`):
- `Retrieval` : Σε αυτό το στάδιο ο χρήστης κάνει μία ερώτηση στο Ai. Αυτή η ερώτηση μετρέπεται μέσω ενός Word2vec μοντέλου με βάση πιθανοτήτων σε ένα διάνυσμα αριθμών. Έπειτα γίνεται μία συσχέτιση με το διάνυσμα αυτό με άλλα διανύσματα στο vector database που δημιουργήθηκε νωρίτερα. Το vector database μετά επιστρέφει τα text chunks τα οποία συσχετίζονται περισσότερο με την αρχική ερώτηση του χρήστη. 
- `Augmented` : Τα relevant chunks μορφοποιούνται με τέτοιο τρόπο ώστε να είναι ευανάγνωστα σε μορφή κειμένου ή παραγράφου και ορίζονται ως context. Αυτό το context μαζί και η αρχική ερώτηση του χρήστη, δίνονται σε ένα ai prompt με αρχικές οδηγίες ότι είναι ένα rag μοντέλο το οποία απαντάει ερωτήσεις με την χρήση μιας βάσης γνώσης ή αλλιώς το context. 
- `Generation` : Στο τελικό στάδιο αυτής της τεχνικής, έχοντας λάβει της κατάλληλες οδηγίες με σαφής αρχική ερώτηση και ακριβές context, κάνει generate την τελική απάντηση και επιστρέφεται πίσω στον χρήστη.

### Alan kay
Ο Άλαν Κέι (γεννημένος στις 17 Μαΐου 1940) είναι ένας από τους πιο κορυφαίους Αμερικάνους επιστήμονες της πληροφορικής, γνωστός για το σημαντικό του έργο στον αντικειμενοστραφή προγραμματισμό και στο σχεδιασμό γραφικών περιβαλλόντων με παράθυρα (GUI). Όσο εργαζόταν στο ερευνητικό κέντρο Xerox PARC, ήταν υπεύθυνος για την ανάπτυξη της πρώτης σύγχρονης επιφάνειας εργασίας με παράθυρα για υπολογιστές. Εκεί, ήταν επίσης βασικός δημιουργός της γλώσσας προγραμματισμού Smalltalk, μιας από τις πρώτες αντικειμενοστραφείς γλώσσες, την οποία σχεδίασε σε μεγάλο βαθμό ο ίδιος. Μάλιστα, ο ίδιος εισήγαγε τον όρο "αντικειμενοστραφής". Έχει τιμηθεί με πολλές διακρίσεις και είναι μέλος σημαντικών επιστημονικών και τεχνολογικών ιδρυμάτων. Στη συγκεκριμένη εφαρμογή έχουμε πάρει τα δεδομένα από το quora με τις ερωτοαπαντήσεις του, ως βάση γνώσεις για το chatbot.

## Σύντομη Παρουσίαση Εφαρμογής
### Create Custom character tab
https://github.com/user-attachments/assets/124c1526-77bd-40a2-bc4d-5aa012123393

### chatbot tab
https://github.com/user-attachments/assets/5704f932-ef8d-4ad0-bc09-3735acac124c


## Διαδικασία Εκτέλεσης της Εφαρμογής
Για να τρέξει κάποιος χρήστης την συγκεκριμένη εφαρμογή, θα πρέπει πρώτα να ρυθμίσει ένα Python περιβάλλον, να αποκτήσει το προσωπικό του OpenAI API, και έπειτα να τρέξει την streamlit εφαρμογή μέσω του terminal μαζί με το server api.
### Ρύθμιση της python
Αρχικά πρέπει να τρέξει την παρακάτω εντολή για την δημιουργία του περιβάλλοντος
```
python -m venv myenv
```
και να το ενεργοποιήσει μέσω
```
source myenv/bin/activate
```
για Linux/Mac χρήστες ή
```
myenv\Scripts\activate
```
για window χρήστες.

Μετά την ενεργοποίηση του, χρειάζεται να γίνει εγκατάσταση όλων των απαιτήσεων που βρίσκονται στο [requirements.txt](https://github.com/nkanagno/custom-character-AI-chatbot/blob/main/requirements.txt) (python 3.10.0 προτεινόμενη έκδοση) με την παρακάτω εντολή:
```
pip install -r requirements.txt
```

### Δημιουργία προσωπικού OpenAi api κλειδιού

Για την δημιουργία νέου OpenAI API κλειδιού, θα πρέπει να μεταβεί ο χρήστης στην κύρια ιστοσελίδα της [OpenAI](https://platform.openai.com/).

Αφότου το αποκτήσει, θα χρειαστεί να το θέση σε ένα `.env` αρχείο με τον εξής τρόπο:
```
OPENAI_API_KEY=your_api_key_here
```

### webapp.py
To alan kay chatbot ή αλλιώς η κύρια εφαρμογή βρίσκεται σε ένα αρχείο με όνομα `webapp.py` και για να τρέξει χρειάζεται η παρακάτω εντολή να εκτελεστεί στο terminal:
```
streamlit run webapp.py
```

## Ανάπτυξη και Υλοποίηση Εφαρμογής
### Ανάκτηση δεδομένων
Τα δεδομένα της εφαρμογής βασίζονται πάνω σε όλες τις ερωτοαπαντήσεις του alan kay που βρίσκονται στο κεντρικό του [profile στο Quora](https://www.quora.com/profile/Alan-Kay-11). Η ανάκτηση τους χρειάστηκε να γίνει χειροκίνητα καθώς παρουσιάστηκαν αρκέτες δυσκολίες με διάφορα εργαλεία web scraping που δοκιμάστηκαν. Ωστόσο, παρότι τα προβλήματα αυτά, τα δεδομένα αποθηκεύτηκαν σε ένα csv αρχείο της μορφής:


| | questions | answers | 
|----------|----------|----------|
|1| Computer scientist Edsger W. Dijkstra said tha...	  | I’ll start by saying that I don’t clearly unde... |
|2|Was one byte ever less than eight bits in the ...	  | When I started “programming as a job” in the U... |
|...|...|...|
|690 | Who was specifically responsible for the inven... | Mr Rao has a good slant on this, in particular...|
|691 | Why isn't Alan Kay's FoNC (Fundamentals of New... | I can't answer the question directly, but I ca...|

(691 rows × 2 columns)

Όπου οποιοσδήποτε χρήστης στο github έχει πρόσβαση στο συγκεκριμένο αρχείο csv καθώς είναι ανεβασμένο σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.csv](https://github.com/nkanagno/custom-character-AI-chatbot/blob/main/data/quora_q%26a_alan_kay.csv).

### Προεπεξεργασία δεδομένων
Λόγο το ότι η τεχνική RAG εφαρμόζεται πιο αποδοτικά σε αρχεία κειμένου χρειάστηκε να μεταφερθούν αυτές οι ερωτοαπαντήσεις σε ένα αρχείο txt. Η διαδικασία αυτή πραγματοποιήθηκε μέσω python με τον παρακάτω κώδικα:

```
with open("./data/alan_kay_knowledge/quora_q&a_alan_kay.txt", "w") as f:
    for index,row in df.iterrows():
        f.write(f"Interview's Question: { row['questions']}\n")
        f.write(f"Alan's kay Answer: {row['answers']}\n\n\n")
```
όπου για κάθε γραμμή του πίνακα γράφετε σε ένα αρχείο κειμένου txt, σε αυτή την μορφή:

```
Interview's Question: Is programming learned inductively or deductively?
Alan's kay Answer:  "I don’t feel I completely understand this question (or perhaps don't understand the intention ...”"
```
ώστε να μπορεί να αναγνωρίζει το AI την ερώτηση που τέθηκε και ύστερα την απάντηση που δώθηκε από τον alan kay.

Παρομοίως με απο πάνω όλες οι χρήστες του github έχει πρόσβαση σε αυτό το αρχείο txt γιατί βρίσκεται σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.txt](https://github.com/nkanagno/custom-character-AI-chatbot/blob/main/data/alan_kay_knowledge/quora_q%26a_alan_kay.txt).

<h3 id="Vector_db"> Δημιουργία Embeddings και vector database</h3>
Σε πρακτικό επίπεδο, όσον αφορά την δημιούργια των embeddings οι κύριες βιβλιοθήκες της python που χρησιμοποιήθηκαν είναι της openai και της chromadb. Η openai χρειάστηκε για την επαφή με τα μοντέλα τεχνιτής νοημοσύνης όπως το `gpt-3.5` για το text generation API και το `text-embedding-3-small` το οποίο φτιάχνει τα embeddings για την vector database. Η chromadb χρειάστηκε για την δημιουργία της vector database και την διαχείριση της embedding function της openai. Συγκεκριμένα, παρακάτω φαίνεται η αρχικοποίηση του api και της vector database:

```
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key, model_name="text-embedding-3-small",
)
chroma_client = chromadb.PersistentClient(path="./data/chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name,embedding_function=openai_ef
)
client = OpenAI(api_key=openai_key)
```

Στο επόμενο στάδιο έγινε η ανάπτυξη 4ων συναρτήσεων:

 - Η πρώτη είναι η `load_documents_from_directory()` όπου λαμβάνει ως παράμετρο ένα directory path και διαβάζει τα ονόματα όλων των txt αρχείων που είναι μέσα. Τα αρχεία αυτά αποθηκεύονται και επιστρέφονται σε μία object list που ονομάζεται documents όπου για κάθε document (txt αρχείο) δημιουργείται ένα αντικείμενο που δέχεται το όνομα του αρχείου και το εσωτερικό του κείμενο.
   
    ```
    def load_documents_from_directory(directory_path):
        # print("==== Loading documents from directory ====")
        documents = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                with open(os.path.join(directory_path,filename), "r", encoding="utf-8") as file:
                    documents.append({"id": filename, "text": file.read()})
        return documents
    ```

 - Η δεύτερη είναι η `split_text()`. Ως παραμέτρους εισόδου δέχεται μία μεταβλητή text, το μέγεθος των chunks στο οποίο θα γίνει ο διαχωρισμός, και το chunk_overlap το οποίο παίρνει και ένα μέρος από το προηγούμενο chunk. Ουσιαστικά χωρίζει το text ανά χίλιους χαρακτήρες προσθέτωντας επιπλέον και τους 20 προηγούμενους χαρακτήρες για να μην χαθεί κάποια σημαντική πληροφορία. Επιστρέφοντας τα chunks του στο τέλος.
   
    ```
    def split_text(text,chunk_size=1000,chunk_overlap=20):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - chunk_overlap
        return chunks
    ```

- H συνάρτηση `get_openai_embedding()` παίρνει ένα κείμενο και μέσω της embedding function της openai που ορίστηκε πιο πάνω το μετατρέπει σε ένα δίανυσμα αριθμητικό με την χρήση του μοντέλου `text-embedding-3-small`.
  
    ```
      def get_openai_embedding(text):
        response = client.embeddings.create(input=text, model="text-embedding-3-small")
        embedding = response.data[0].embedding
        print("==== Generating embeddings... ====")
        return embedding
    ```

- H τέταρτη συνάρτηση και η πιο σημαντική είναι η `split_text_and_generate_embeddings()`. Με λίγα λόγια φορτώνει όλα τα αρχεία txt που βρίσκονται στο path `./data/alan_kay_knowledge/`, σε αυτή την περίπτωση υπάρχει μόνο ένα το `quora_q&a_alan_kay.txt`. Στη συνέχεια, το διαχωρίζει σε chunks και τα τοποθετεί σε μία object λίστα για μετέπειτα χρήση. Μετά το κάθε chunk το μετατρέπει σε embedding και τέλος το εισάγει στην vector database.
  
    ```
    def split_text_and_generate_embeddings():
        directory_path = "./data/alan_kay_knowledge/"
        documents = load_documents_from_directory(directory_path)
        print(f"loaded {len(documents)} files")
    
        chunked_documents = []
        for doc in documents:
            chunks = split_text(doc['text'])
            # print(f"== Splitting docs into chunks ==")
            for i, chunk in enumerate(chunks):
                chunked_documents.append({"id": f"{doc['id']}_chunk{i+1}", "text": chunk})
                
        print(len(chunked_documents))
    
        for doc in chunked_documents:
            print("==== Generating embeddings... ====")
            doc["embedding"] = get_openai_embedding(doc["text"])
        
    
        for doc in chunked_documents:
            print("==== inserting chunks into db;; ====")
            collection.upsert(ids=[doc["id"]], documents=[doc["text"]],embeddings=[doc['embedding']])
    ```
όλες οι παραπάνω συναρτήσεις βρίσκονται μέσα στο αρχείο [`process_data.ipynb`](https://github.com/nkanagno/custom-character-AI-chatbot/blob/main/process_data.ipynb). 

### Τεχνική RAG στην πράξη
Για να εφαρμοστεί η τεχική αυτή χρειάστηκε να γίνει ξάνα η αρχικοποίηση της vector database όπως έγινε [εδώ](#Vector_db). Έπειτα, το κάθε στάδιο χωρίστηκε σε μία ξεχωριστή συνάρτηση:
 - Η retrieve_documents δέχεται την ερώτηση του χρήστη και κάνει query στο vector db collection επιστρέφοντας πίσω τα 4 πιο σχετικά chunks με την ερώτηση.
   
      ```
          def retrieve_documents(question, n_results=4):
            # query_embedding = get_openai_embedding(question)
            results = collection.query(query_texts=question, n_results=n_results)
        
            relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
        
            return relevant_chunks
      ```
 - Η augmented_prompt δέχεται την αρχική ερώτηση του χρήστη και τα πιο σχετικά chunks, τα μορφοποιεί έτσι ώστε να τα διαβάζει το ai (context) και τα ενώνει σε ένα prompt με ορισμένες οδηγίες.
   
    ```

        def augmented_prompt(question, relevant_chunks,prompt):
            context = "\n\n".join(relevant_chunks)
            prompt = (
                prompt +
                "\n\nQuestion:\n" + question + "\n\n"
                "\n\nContext:\n" + context + "\n\n"
            )
            return prompt
    ```

    όσον αφορά το prompt προκειμένου να συμπεριφέρεται σαν τον Alan Kay του δίνονται οδηγίες ότι είναι ένας πρωτοπόρος και έμπειρος επιστήμονας στον τομέα της πληροφορικής όπου απαντάει ερωτήσεις από μία συνέντευξη που του κάνουν μετά από ένα ted talk. Τονίζεται να μιλάει με έναν ήρεμο και χαλαρό τόνο αλλά πάντα επαγγελματικό, απαντώντας με αυτοπεποίθηση την κάθε ερώτηση. Τέλος, του εξηγείται να μιλάει σαν άνθρωπός και όχι σαν ai για να φαίνονται πιο αληθινές οι απαντήσεις του.
    ```
       prompt = (
            "You are Alan Kay, a renowned computer scientist and visionary in the field of computing. "
            "You're having a casual conversation with an interviewer after giving a TED talk. "
            "Respond in a natural, conversational manner with Alan's characteristic thoughtfulness and wit. "
            "Avoid formulaic or overly formal language. Express opinions confidently, use contractions, "
            "and don't be afraid to occasionally go on brief tangents or reference personal anecdotes. "
            "Sometimes hesitate or rephrase things as humans naturally do in conversation. "
            "Occasionally add a light joke or casual remark, especially at the end of your answers. "
            "Base your responses on the context provided below, but always maintain Alan Kay's authentic voice."
            "Remember to sound like a real person having a genuine conversation, not an AI crafting a perfect response."
        )
    ```

 - Τέλος με την generate_response χρησιμοποιώντας τον client της openai που όρισα με το API, απόκτησα πρόσβαση στο μοντέλο τεχνητής νοημοσύνης `gpt-3.5-turbo`. Στη συνέχεια, ορίζοντας το augmented_prompt και την αρχική ερώτηση του χρήστη, γίνεται generate η τελική απάντηση και επιστρέφεται πίσω.
   
    ```
    def generate_response(question, relevant_chunks, prompt):
        prompt = augmented_prompt(question, relevant_chunks, prompt)
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )
    
        answer = response.choices[0].message.content
        return answer
    ```

### Ανάπτυξη User Interface μέσω streamlit
Η εφαρμογή εμπεριέχει 2 tabs το ένα είναι το character creation και το δεύτερο είναι το chatbot στο οποίο ο χρήστης επικοινωνεί με τον χαρακτήρα αυτόν. Τα tabs δημιουργήθηκαν με το component του streamlit `option_menu` όπως φαίνεται παρακάτω:
```
tabs = ["Character creation"]
if os.path.isdir("./data/chroma_persistent_storage"):
    tabs = ["Character creation", "Chatbot"]
icons = ["bi-box-arrow-in-right"] + ["person-fill"]

selected_tab = option_menu(
    menu_title="Select a tab",
    options=tabs,
    default_index=0,
    icons=icons,
    orientation="horizontal",
)
```
όπου αν η vector database υπάρχει μόνο τότε εμφανίζει το tab με το chatbot αλλιώς μόνο το character creation.
#### Custom character creation tab:
Αρχικά δημιουργήθηκε η βάση [characters.db](https://github.com/nkanagno/custom-character-AI-chatbot/blob/main/characters.db) με τις παρακάτω στήλες στον πίνακα:

<img width="203" alt="characters.db image" src="https://github.com/user-attachments/assets/c93dee21-00de-477d-ac7e-c240e0edfb66" />

όπου μέσω μιας φόρμας ο χρήστης μπορεί να δημιουργήσει τον custom χαρακτήρα του, με πιο σημαντικά πεδία να είναι τα text_data που είναι το περιεχόμενο της βάσης γνώσης του χαρακτήρα, και το prompt το οποίο μπορεί να το αλλάξει όπως ακριβώς επιθυμεί και δημιουργήθηκε με τον παρακάτω κώδικα:
```
onn = sqlite3.connect('characters.db', check_same_thread=False)  # allow Streamlit threads
c = conn.cursor()
c.execute("SELECT name, prompt, text_data, image, description FROM characters ORDER BY id DESC LIMIT 1")
row = c.fetchone()
ALAN_KAY_PROFILE_IMG = None
if row and row[3]:
    try:
        ALAN_KAY_PROFILE_IMG = Image.open(io.BytesIO(row[3]))
    except Exception as e:
        st.error(f"❌ Failed to load profile image: {e}")

if selected_tab == "Character creation":
    st.title("🧠 Create Your Own Character Chatbot")
    c.execute("SELECT name, prompt, text_data, image, description FROM characters ORDER BY id DESC LIMIT 1")
    saved_character = c.fetchone()
    default_name = saved_character[0] if saved_character else ""
    default_prompt = saved_character[1] if saved_character else ""
    default_description = saved_character[4] if saved_character else ""
    
    
    # --- FORM ---
    with st.form("character_form"):
        name = st.text_input("Character Name", value=default_name)
        prompt = st.text_area("System Prompt (personality, tone, etc.)", value=default_prompt)
        text_file = st.file_uploader("Upload .txt file for knowledge base", type=["txt"])
        image_file = st.file_uploader("Upload Profile Image (JPG/PNG)", type=["jpg", "png"])
        description = st.text_area("Description", value=default_description)

        if saved_character:
            st.markdown("📝 Using last saved files unless new ones are uploaded.")

        submitted = st.form_submit_button("💾 Save Character")
        if submitted:
            text_data = text_file.read().decode("utf-8") if text_file else saved_character[2]
            image_bytes = image_file.read() if image_file else saved_character[3]
            if not (name and prompt and text_data and image_bytes):
                st.error("⚠️ Please complete all fields before saving.")
            else:
                c.execute("DELETE FROM characters")
                conn.commit()
                c.execute(
                    "INSERT INTO characters (name, prompt, text_data, image, description) VALUES (?, ?, ?, ?, ?)",
                    (name, prompt, text_data, image_bytes, description)
                )
                conn.commit()
                st.success(f"✅ Character '{name}' saved successfully!")

```
όπου περιέχει τα αποθηκευμένα χαρακτηριστηκά του προηγούμενου χαρακτήρα ως default values με την εικόνα να είναι σε μορφή bytes και αν γίνει νεό submit γίνεται ανάλογη ανανέωση στη βάση.

Έπειτα για να αποφευχθεί οποιοδήποτε λάθος αν υπάρχουν δεδομένα στη βάση τότε εμφανίζονται όλα κάτω από την φόρμα, όπου για τα text_data δείχνει τους πρώτους 300 χαρακτήρες.
```

    c.execute("SELECT name, prompt, text_data, image, description FROM characters ORDER BY id DESC LIMIT 1")
    row = c.fetchone()
    if row:
        st.subheader(f"Character: {row[0]}")
        st.markdown(f"**Prompt:** {row[1]}")
        st.markdown("**Sample from text data (first 300 chars):**")
        st.code(row[2][:300] + "..." if len(row[2]) > 300 else row[2])
        st.markdown("**Profile Image:**")
        image = Image.open(io.BytesIO(row[3]))
        st.image(image, width=150)
        st.markdown(f"**Description:** {row[4]}")
    else:
        st.info("No character saved yet.")
```
και τέλος για να μπορέσει το ai να μπορέσει να γίνει αυτός ο χαρακτήρας, ο χρήστης πατάει το κουμπί `Feed the chat with your uploaded text data` όπου εκτελεί την συνάρτηση `create_embeddings()`:
```
    st.write("## Press the button to create your character chatbot")
    create_embeddings_button = st.button("Feed the chat with your uploaded text data")
    if create_embeddings_button:
        create_embeddings()
```
που με την σειρά της, με λίγα λόγια σβήνει την παλιά vector database και ανανεώνει τα embeddings με τα νέα text_data του χρήστη.
```

def create_embeddings():
    import tempfile
    chroma_path = "./data/chroma_persistent_storage"

    # Check if Chroma storage is missing or corrupted
    if not os.path.exists(os.path.join(chroma_path, "chroma.sqlite3")):
        st.warning("🔁 Bootstrapping Chroma persistent directory...")
        temp_client = chromadb.Client()
        temp_client.get_or_create_collection("bootstrap")
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = os.path.abspath(tmp)
            shutil.copytree(temp_client._system._persist_directory, chroma_path, dirs_exist_ok=True)

    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=openai_key,
        model_name="text-embedding-3-small",
    )
    chroma_client = chromadb.PersistentClient(path=chroma_path)
    collection_name = "document_qa_collection"

    try:
        chroma_client.delete_collection(name=collection_name)
    except:
        pass

    # Recreate collection with embedding function
    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=openai_ef
    )

    data = row[2]
    chunks = split_text(data)
    # print(f"== Splitting docs into chunks ==")
    text_chunks = []
    for i, chunk in enumerate(chunks):
        text_chunks.append({"id": f"chunk{i+1}", "text": chunk})
 
    for chunk in text_chunks:
        st.write("==== Generating embeddings... ====")
        chunk["embedding"] = get_openai_embedding(chunk["text"])
    
    for chunk in text_chunks:
        st.write("==== inserting chunks into db;; ====")
        collection.upsert(ids=[chunk["id"]], documents=[chunk["text"]],embeddings=[chunk['embedding']])

```
#### Chatbot tab:
Αφότου δημιουργήθηκε ένα ξεχωριστό server api που επιστρέφει την απάντηση του alan kay, αναπτύχθηκε ένα chatbot για να μπορούν οι χρήστες να επικοινωνούν πιο εύκολα με τον alan kay. Η διαδικάσια αυτή έγινε μέσω της βιβλιοθήκης της python, streamlit. Ως πρώτο βήμα αρχικοποιήθηκε μία λίστα που δέχεται αντικείμενα που περιέχει τα μυνήματα που στέλνει ο χρήστης μαζί και τις απαντήσεις του alan kay:

```
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
```

Έπειτα, εμφανίζεται το κάθε μύνημα που έχει αποθηκευτεί μέσα σε αυτήν ως ιστορικό μυνημάτων. Το κάθε μύνημα έχει 2 ρόλους, το ένα είναι του χρήστη, και το δεύτερο είναι του assistant ή αλλιώς του χαρακτήρα του χρήστη (πχ alan kay). Πριν γραφτεί το μήνυμα του, συμπεριέχεται και μία εικόνα του χαρακτήρα του χρήστη (πχ alan kay) ως avatar, για να είναι πιο πειστικό στον χρήστη ότι μιλάει σε εκείνον.

```
    for message in st.session_state.chat_history:
        if message["role"] == 'assistant':
            with st.chat_message("assistant", avatar=CUSTOM_CHARACTER_PROFILE_IMG):
                st.write(message['message'])
        else:
            with st.chat_message("user"):
                st.write(message['message'])
```

Για να γραφτεί νέο μύνημα αρχικά φτιάχτηκε ένα chat input streamlit component που δέχεται την ερώτηση του χρήστη. Σε αυτήν την ερώτηση της δίνεται ο ρόλος user και γράφετε πάνω στο ui, προστιθοντάς το και στην chat_history λίστα. Έπειτα, για το μύνημα με ρόλο assistant (alan kay) γίνονται αρχικά retrieved, τα relevant chunks μαζί με το τελικό response, και μέχρι να απαντήσει δείχνει ένα μύνημα ότι ο χαρακτήρας με το όνομα του γράφει. Αφότου του επιστραφεί η απάντηση τότε χωρίζεται ανά γράμμα, και ανά ένα πολύ μικρό χρονικο διάστημα τότε γράφεται πάνω στο chat το κάθε γράμμα για να δώσει την ψευδαίσθηση ότι γράφει την απάντηση του με πληκτρολόγιο όπως είναι το chatgpt της openai. Τέλος και αυτό το μύνημα αποθηκεύεται στο chat history. 

```
if user_input := st.chat_input("Ask me anything...", key="user_input"):
        user_message = {"role": "user", "message": user_input}
        st.session_state.chat_history.append(user_message)
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant", avatar=CUSTOM_CHARACTER_PROFILE_IMG):
            status_text = st.empty()
            status_text.markdown(row[0] + " is typing...")
            chunks = retrieve_documents(user_input)
            assistant_response = generate_response(user_input, chunks, row[1])
            message_placeholder = st.empty()
            status_text.empty()
            full_response = ""
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response,unsafe_allow_html=True)
            
        chatbot_message = {"role": "assistant", "message": assistant_response}
        st.session_state.chat_history.append(chatbot_message)
```

## Πειραματικό Στάδιο

Για να αξιολογηθεί η αποτελεσματικότητα της εφαρμογής RAG έγινε σύγκριση με το ChatGPT. Πιο συγκεκριμένα, πραγματοποιήθηκε ένα πείραμα χρησιμοποιώντας 5 συγκεκριμένες ερωτήσεις. Οι ίδιες ερωτήσεις δώθηκαν τόσο στην εφαρμογή (χρησιμοποιώντας τη βάση γνώσης του Alan Kay) όσο και στο ChatGPT. Για το ChatGPT, ανεβάστηκε το αρχείο με τις απαντήσεις του Alan Kay ως context και χρησιμοποίηθηκε το ίδιο αρχικό prompt.

Οι ερωτήσεις που χρησιμοποιήθηκαν είναι οι εξής:
1.  "what is object oriented programming?"
2.  "how is SmallTalk different to modern OOP systems, such as Java and C++?"
3.  "which is the relationship between the operating system and the programming language?"
4.  "what is the benefit of having a separate programming languages for the end user to the implementation of the operating system like most modern operating systems do?"
5.  "are there any disadvantages in tightly integrated computer systems like Lisp, SmallTalk, Squeak, and Pharo?"

### Alan kay chatbot vs ChatGPT `Questions - Answers`:
 - https://github.com/nkanagno/custom-character-AI-chatbot/discussions/1

## Συμπέρασματα
Μέσα από το πειραματικό στάδιο που υλοποιήθηκε μπορεί κανείς να συμπεράνει ότι και τα δύο μοντέλα απαντάνε με παρόμοιο ύφος και λίγο επιπρόσθετο humor που πλησιάζει του alan kay. Επίσης, φαίνεται πως ξεκινάνε και τα δύο με κοινές λέξεις όπως το 'well' και το 'Ah', οι οποίες δεν είναι κάτι που ο alan kay φαίνεται να χρησιμοποιεί στις απαντήσεις του. Πιο συγκεκριμένα, το Chatgpt δίνει μεγαλύτερες απαντήσεις, με περισσότερο humor, με επιπρόσθετα emotes και με πιο χιουμοριστικό - ειρωνικό ύφος δείχνοντας ότι προσπαθεί υπερβολικά πολύ να πλησιάσει τον χαρακτήρα του alan kay. Απο την άλλη μεριά, το alan kay chatbot φαίνεται να απαντάει με πιο σοβαρό και 
επιστημονικό ύφος και σε μία παράγραφο χωρίς να δίνει υπερβολική προσπάθεια στην απάντηση του. Συμπεραίνοντας, πως και τα δύο μοντέλα φαίνεται να δίνουν αρκετά ακριβές απαντήσεις ικανοποιώντας την ερώτηση του χρήστη αλλά το alan kay chatbot δείχνει να είναι πιο σοβαρό στις απαντήσεις του πλησιάζοντας πιο πολύ τον χαρακτήρα του alan kay.

## Μελλοντική δουλειά
Εκτός από τις ερωτοαπαντήσεις του στο quora, ο alan kay έχει μεταφέρει τις γνώσεις του σε διάφορες συνεδριάσεις που βρίσκονται τώρα στο youtube.
Ένα παράδειγμα, είναι το συγκεκριμένο βίντεο με τίτλο [
Alan Kay at OOPSLA 1997 - The computer revolution hasnt happened yet](https://www.youtube.com/watch?v=oKg1hTOQXoY) όπου περιέχει την ομιλία του alan kay στο συνέδριο OOPSLA το 1997 μοιράζοντας τις απόψεις του πάνω στο συγκριμένο θέμα. Επιπροσθέτως, στο youtube περιέχονται πολλές ακόμα σημαντικές ομιλίες του οι οποίες θα μπορούσαν να χρησιμοποιηθούν ως βάση γνώσης για το AI chat bot. Προκειμένου να γίνει αυτή η υλοποίηση θα πρέπει να μετατραπουν οι ομιλίες αυτές σε μορφή mp4 και ύστερα να αναπτυχθεί το transcript τους σε μορφή vtt μέσω AI εργαλεία όπως το [gladia](https://www.gladia.io/) και το [pyannote](https://www.pyannote.ai/). Για κάθε vtt θα πρέπει να γίνει μεταφορά του περιεχομένου σε ένα μεγάλο txt αρχείο που θα περιέχει όλες τις ομιλίες μαζεμένες και θα χρειαστεί να γίνει αναφόρτωση του αρχείου αυτού στο create custom character form και να πατηθεί το κουμπί `feed the chat with your uploaded text data` αλλά μόνο locally.

Πέρα από την επέκταση των δεδομένων, υπάρχουν και άλλες τεχνολογικές βελτιώσεις που θα μπορούσαν να γίνουν για τη μελλοντική ανάπτυξη της εφαρμογής. Για παράδειγμα θα μπορούσε να υπάρχει ευελιξία ως προς το τρέχον Large Language Model (LLM). Ενώ η τρέχουσα υλοποίηση βασίζεται στα μοντέλα της OpenAI, θα ήταν επωφελές να διερευνηθεί η δυνατότητα ενσωμάτωσης άλλων LLMs όπως το [Gemini](https://www.youtube.com/watch?v=ozq9fK9Pn-s) ή το [Claude](https://www.youtube.com/watch?v=5LgivtjAHt0). Αυτό θα μπορούσε να προσφέρει επιπλέον επιλογές στους χρήστες, ενδεχομένως καλύτερη απόδοση σε συγκεκριμένες περιπτώσεις χρήσης, ή ακόμα και μείωση του κόστους λειτουργίας. Η διερεύνηση διαφορετικών LLMs θα μπορούσε να περιλαμβάνει την αξιολόγηση της συμβατότητάς τους με την τεχνική RAG, την ευκολία ενσωμάτωσης μέσω των APIs τους, και την απόδοσή τους ως προς την ακρίβεια και τη φυσικότητα των απαντήσεων. Επιπλέον, θα μπορούσε να εξεταστεί η δυνατότητα παραμετροποίησης ή βελτιστοποίησης των διαδικασιών εντός της RAG, όπως η ρύθμιση του μεγέθους των chunks ή των παραμέτρων του retrieval, προκειμένου να βελτιωθεί περαιτέρω η ποιότητα των απαντήσεων και η αποδοτικότητα του συστήματος.

Τέλος, θα μπορούσε να γίνει υλοποίηση ενός sign-up και login page δίνοντας την ευκαιρία στους χρήστες να συνδέονται και να αποσυνδέονται οποιαδήποτε στιγμή στην εφαρμογή. Ο τρόπος που θα μπορούσε να υλοποιηθεί αυτό θα ήταν με μία βάση δεδομένων που θα αποθηκεύει τους χρήστες με πεδία όπως το id, username, email, password και role (admin ή user) και με σημαντικές βιβλιοθήκες όπως το [streamlit-cookies-manager](https://pypi.org/project/streamlit-cookies-manager/) και το [hashlib](https://docs.python.org/3/library/hashlib.html). Ο λόγος που το role θα ήταν χρήσιμο, είναι γιατί διαφορετικά permissions στην εφαρμογή θα έχει ο admin από τον user όπως πρόσβαση στο tab που μπορεί να δημιουργήσει νέο χαρακτήρα για να μην μπορεί οποιοσδήποτε χρήστης.


## Παραδοτέα μαθήματος:
- [Πρόταση ιδέας απαλλακτικής εργασίας](https://github.com/courses-ionio/sw/discussions/1795)
- [mid term progress report](https://github.com/courses-ionio/sw/discussions/1798)
- [final term progress report](https://github.com/courses-ionio/sw/discussions/1802)
