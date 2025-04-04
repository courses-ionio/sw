
# Τα Στοιχεία Μου
| Πλατφόρμα | Όνομα | Επώνυμο | Username | AM | Email |
| --- | --- | --- | --- | --- | --- |
| [Github](https://github.com/nkanagno) | Νικόλας | Αναγνωστόπουλος | nkanagno | inf2021013 | inf2021013@ionio.gr |

Όνομα ομάδας: OMADA 13 <br>
GitHub organisation url: [OMADA11](https://github.com/OMADA-13)

# Εισαγωγή Μαθήματος και Αρχική Στόχοι (Προχωρημένα Θέματα Τεχνολογίας Λογισμικού)
Μέσω του μαθήματος Προχωρημένα Θέματα Τεχνολογίας Λογισμικού, το οποίο δίνει βάση σε προχωρημένες διαδικασίες ανάπτυξης λογισμικού καθώς και σε εργαλεία που χρησιμοποιούνται σε αυτού του είδους διαδικασίες, ευελπιστώ να εξελίξω τον τρόπο σκέψης μου όσον αφορά την σχεδίαση και την ανάπτυξη λογισμικού μαθένοντας περισσότερα εργαλεία και τρόπους ανάπτυξης λογισμικού από αυτά/ους που ήδη γνωρίζω. 

Συγκεκριμένα, έχοντας εργαστεί ως software engineer τους περασμένους 7 μήνες με τεχνολογίες ανάπτυξης web εφαρμογών (όπως `React js, PostgreSQL και graphql`), έχω μάθει να μπορώ να αναλύω ένα πρόβλημα και να μπορώ να το μεταφέρω σε μορφή κώδικα προκειμένου να εξελίσσεται συνεχώς η κύρια web εφαρμογή της εταιρείας.

Παρότι της τρέχουσας εμπειρίας μου σε αυτόν τον τομέα, πιστεύω ότι πάντα υπάρχει χώρος για εξέλιξη και ότι μέσω των πολλαπλών και ξεχωριστών εργαλείων που θα αποκτήσω εμπειρία μέσω αυτού του μαθήματος, θα μπορέσω να εξελιχθώ περισσότερο και στην τρέχον δουλειά μου αλλά και για την μετέπειτα μελλοντική καριέρα μου ως software engineer.

# Alan kay chatbot τεχνιτής νοημοσύνης - Απαλλακτική Εργασία

## Περίληψη
Κατά την διάρκεια του μαθήματος, πραγματοποιήθηκε η ανάπτυξη ενός AI chatbot που προσωποποιεί τον χαρακτήρα του Alan kay, έναν σπουδαίο και πρωτοπόρο επιστήμονα στον κόσμο της τεχνολογίας. Έχοντας στην διάθεση μου τις πιο πρόσφατες τεχνολογίες τεχνητής νοημοσύνης όπως εξελιγμένα εργαλεία της OpenAi, η υλοποίηση αυτού του project μπόρεσε και ήταν εφικτή. Σημαντικά εργαλεία της OpenAi αποτέλεσαν το API, embedding μοντέλα τεχνητής νοημοσύνης και μία vector database. Η ένωση των παραπάνω εργαλειών, έκαναν εφικτή την υλοποίηση της προχωρημένου επιπέδου τεχνικής που είναι υπεύθυνη για την όλη ανάπτυξη της συγκεκριμένης εφαρμογής, και ονομάζεται Retrieval Augmented Generation ή αλλιώς RAG. Η τεχνική αυτή επιτρέπει την ανάπτυξη εξελιγμένων ΑΙ chatbots τα οποία είναι εκπαιδευμένα και απαντούν ερωτήσεις χρηστών πάνω σε ειδικά δεδομένα που είναι αποθηκευμένα σε μορφή αρχείου κειμένου όπως PDF, txt, markdown κλπ. Σε αυτή την περίπτωση οι γνώσεις του Alan kay chatbot βασίζονται σε δεδομένα ερωτοαπαντήσεων του Alan Kay, που βρίσκονται στο κεντρικό profile του στο QUORA και η επεξεργάσια τους έγινε μέσω της γλώσσας προγραμματισμού, Python. Τέλος, το μεγαλύτερο μέρος της εφαρμογής έγινε μέσω Python με τις πιο σημαντικές βιβλιοθήκες να είναι η streamlit για το User Ιnterface, η pandas για την επεξεργασία των δεδομένων, η OpenAi για το RAG και την FastApi για να ακούει σε post requests να επιστρέφει την απάντηση του Alan Kay.

## Εισαγωγή



## Retrieval Augmented Generation (RAG)
Η τεχνική `RAG` περιλαμβάνει 3 στάδια (`Retrieval` -> `Augmented` -> `Generation`).

To πρώτο είναι το `Retrieval` που ο χρήστης κάνει μία ερώτηση και λαμβάνει τα πιο σχετικά κομμάτια κειμένου που είναι αποθηκευμένα στην vector database. Μετά το `Augmented` όπου δίνονται αυτά τα κομμάτια ως context μαζί με την αρχική ερώτηση του χρήστη στο AI όπου έχει λάβει και ορισμένες οδηγίες. Τέλος είναι τo `Generation` όπου με βάση το context που του έχει δωθεί ως βαση γνώσης, το AI απαντάει πάνω στην αρχική ερώτηση του χρήστη κανόντας generate την τελική απάντηση.

![rag](https://github.com/user-attachments/assets/d0f20bb1-e2df-4cf8-93ca-841f72eb0083)

### Δημιουργία vector database - προεπεξεργασία δεδομένων
Για να μπορέσει να εφαρμοστεί αυτή η τεχνική απαιτείται πρώτα η ανάπτυξη της vector database. Δηλαδή, το κείμενο κάθε αρχείου αρχικά χωρίζεται σε κομμάτια ορισμένου μεγέθους που ονομάζονται text chunks. Το κάθε κομμάτι μέσω ενός μοντέλου τεχνητής νοημοσύνης μετατρέπεται σε μια σειρά αριθμών ή αλλιώς αριθμητικών διανυσμάτων που ονομάζονται embeddings. Αυτά τα embeddings αποθηκεύονται στην vector database η οποία χρειάζεται για το retrieval στάδιο της τεχνικής RAG.

### Λεπτομερής περιγραφή σταδίων
Με βάση το θεωρητικό υπόβραθρο της τεχνικής αυτής, παρακάτω γίνεται μια πιο λεπτομερής περιγραφή των 3 σταδίων (`Retrieval` -> `Augmented` -> `Generation`):
- `Retrieval` : Σε αυτό το στάδιο ο χρήστης κάνει μία ερώτηση στο Ai. Αυτή η ερώτηση μετρέπεται μέσω ενός Word2vec μοντέλου με βάση πιθανοτήτων σε ένα διάνυσμα αριθμών. Έπειτα γίνεται μία συσχέτιση με το διάνυσμα αυτό με άλλα διανύσματα στο vector database που δημιουργήθηκε νωρίτερα. Το vector database μετά επιστρέφει τα text chunks τα οποία συσχετίζονται περισσότερο με την αρχική ερώτηση του χρήστη. 
- `Augmented` : Τα relevant chunks μορφοποιούνται με τέτοιο τρόπο ώστε να είναι ευανάγνωστα σε μορφή κειμένου ή παραγράφου και ορίζονται ως context. Αυτό το context μαζί και η αρχική ερώτηση του χρήστη, δίνονται σε ένα ai prompt με αρχικές οδηγίες ότι είναι ένα rag μοντέλο το οποία απαντάει ερωτήσεις με την χρήση μιας βάσης γνώσης ή αλλιώς το context. 
- `Generation` : Στο τελικό στάδιο αυτής της τεχνικής, έχοντας λάβει της κατάλληλες οδηγίες με σαφής αρχική ερώτηση και ακριβές context, κάνει generate την τελική απάντηση και επιστρέφεται πίσω στον χρήστη.

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

Όπου οποιοσδήποτε χρήστης στο github έχει πρόσβαση στο συγκεκριμένο αρχείο csv καθώς είναι ανεβασμένο σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.csv](https://github.com/nkanagno/alan-kay-chatbot/blob/main/data/quora_q%26a_alan_kay.csv).

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

Παρομοίως με απο πάνω όλες οι χρήστες του github έχει πρόσβαση σε αυτό το αρχείο txt γιατί βρίσκεται σε δήμοσιο αποθετήριο [quora_q&a_alan_kay.txt](https://github.com/nkanagno/alan-kay-chatbot/blob/main/data/alan_kay_knowledge/quora_q%26a_alan_kay.txt).

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
όλες οι παραπάνω συναρτήσεις βρίσκονται μέσα στο αρχείο [`process_data.ipynb`](https://github.com/nkanagno/alan-kay-chatbot/blob/main/process_data.ipynb). 

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
    def augmented_prompt(question, relevant_chunks):
        context = "\n\n".join(relevant_chunks)
        prompt = (
            "You are Alan Kay, a renowned computer scientist and visionary in the field of computing. "
            "You're having a casual conversation with an interviewer after giving a TED talk. "
            "Respond in a natural, conversational manner with Alan's characteristic thoughtfulness and wit. "
            "Avoid formulaic or overly formal language. Express opinions confidently, use contractions, "
            "and don't be afraid to occasionally go on brief tangents or reference personal anecdotes. "
            "Sometimes hesitate or rephrase things as humans naturally do in conversation. "
            "Occasionally add a light joke or casual remark, especially at the end of your answers. "
            "Base your responses on the context provided below, but always maintain Alan Kay's authentic voice."
            "\n\nQuestion:\n" + question + "\n\n"
            "\n\nContext:\n" + context + "\n\n"
            "Remember to sound like a real person having a genuine conversation, not an AI crafting a perfect response. "
        )
        
        return prompt
    ```
όσον αφορά το prompt προκειμένου να συμπεριφέρεται σαν τον Alan Kay του δίνονται οδηγίες ότι είναι ένας πρωτοπόρος και έμπειρος επιστήμονας στον τομέα της πληροφορικής όπου απαντάει ερωτήσεις από μία συνέντευξη που του κάνουν μετά από ένα ted talk. Τονίζεται να μιλάει με έναν ήρεμο και χαλαρό τόνο αλλά πάντα επαγγελματικό, απαντώντας με αυτοπεποίθηση την κάθε ερώτηση. Τέλος, του εξηγείται να μιλάει σαν άνθρωπός και όχι σαν ai για να φαίνονται πιο αληθινές οι απαντήσεις του.

 - Τέλος με την generate_response χρησιμοποιώντας τον client της openai που όρισα με το API, απόκτησα πρόσβαση στο μοντέλο τεχνητής νοημοσύνης `gpt-3.5-turbo`. Στη συνέχεια, ορίζοντας το augmented_prompt και την αρχική ερώτηση του χρήστη, γίνεται generate η τελική απάντηση και επιστρέφεται πίσω.
   
    ```
    def generate_response(question, relevant_chunks):
    
        prompt = augmented_prompt(question, relevant_chunks)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
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
<h3 id="Fast_API">FastApi </h3>
Προκειμένου να ακούει σε post requests έφτιαξα και ένα ξεχωριστό server API που τρέχει locally. Το API αυτό φτιάχτηκε μέσω της βιβλιοθήκης `FastAPI()`, όπου ο server τρέχει στο router `/ask/alan_kay` και λαμβάνει σε post request την ερώτηση του χρήστη. Αφου την δεχτεί μέσω του cors, κάνει retrieve τα πιο σχετικά chunks και τα δίνει μαζί με την ερώτηση στην συνάρτηση που θα κάνει generate την τελική απάντηση του Alan kay που στέλνεται πίσω ως response.

```
app = FastAPI()
class QuestionRequest(BaseModel):
    question: str
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify frontend URL)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
@app.post("/ask/alan_kay")
async def ask_question(request: QuestionRequest):
    chunks = retrieve_documents(request.question)
    print(chunks)
    response = generate_response(request.question, chunks)
    return {"answer": response}
```
### Ανάπτυξη User Interface μέσω streamlit
Αφότου δημιουργήθηκε ένα ξεχωριστό server api που επιστρέφει την απάντηση του alan kay, αναπτύχθηκε ένα chatbot για να μπορούν οι χρήστες να επικοινωνούν πιο εύκολα με τον alan kay. Η διαδικάσια αυτή έγινε μέσω της βιβλιοθήκης της python, streamlit. Ως πρώτο βήμα αρχικοποιήθηκε μία λίστα που δέχεται αντικείμενα που περιέχει τα μυνήματα που στέλνει ο χρήστης μαζί και τις απαντήσεις του alan kay:

```
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
```

Έπειτα, εμφανίζεται το κάθε μύνημα που έχει αποθηκευτεί μέσα σε αυτήν ως ιστορικό μυνημάτων. Το κάθε μύνημα έχει 2 ρόλους, το ένα είναι του χρήστη, και το δεύτερο είναι του assistant ή αλλιώς του alan kay. Πριν γραφτεί το μήνυμα του, συμπεριέχεται και μία εικόνα του alan kay ως avatar, για να είναι πιο πειστικό στον χρήστη ότι μιλάει σε εκείνον.

```
for message in st.session_state.chat_history:
    if message["role"] == 'assistant':
        with st.chat_message("assistant", avatar=ALAN_KAY_PROFILE_IMG):
            st.write(message['message'])
    else:
        with st.chat_message("user"):
            st.write(message['message'])
```

Για να γραφτεί νέο μύνημα αρχικά φτιάχτηκε ένα chat input streamlit component που δέχεται την ερώτηση του χρήστη. Σε αυτήν την ερώτηση της δίνεται ο ρόλος user και γράφετε πάνω στο ui, προστιθοντάς το και στην chat_history λίστα. Έπειτα, για το μύνημα με ρόλο assistant (alan kay ) γίνεται αρχικά post request στο API που δημιουργήθηκε [εδώ](#Fast_API), και μέχρι να απαντήσει δίνει ένα μύνημα ότι ο alan kay γράφει. Αφότου του επιστραφεί η απάντηση τότε χωρίζεται ανά γράμμα, και ανά ένα πολύ μικρό χρονικο διάστημα τότε γράφεται πάνω στο chat το κάθε γράμμα για να δώσει την ψευδαίσθηση ότι γράφει την απάντηση του με πληκτρολόγιο όπως είναι το chatgpt της openai. Τέλος και αυτό το μύνημα αποθηκεύεται στο chat history. 

```
if user_input := st.chat_input("Ask me anything...", key="user_input"):
    user_message = {"role": "user", "message": user_input}
    st.session_state.chat_history.append(user_message)
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant", avatar=ALAN_KAY_PROFILE_IMG):
        status_text = st.empty()
        status_text.markdown("Alan Kay is typing...")
        assistant_response = API_response(API_URL,user_input)
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
## Σύντομη Παρουσίαση Εφαρμογής



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

Μετά την ενεργοποίηση του, χρειάζεται να γίνει εγκατάσταση όλων των απαιτήσεων που βρίσκονται στο [requirements.txt](https://github.com/nkanagno/alan-kay-chatbot/blob/main/requirements.txt) (python 3.10.0 προτεινόμενη έκδοση) με την παρακάτω εντολή:
```
pip install -r requirements.txt
```

### Δημιουργία προσωπικού OpenAi api κλειδιού

Για την δημιουργία νέου OpenAI API κλειδιού, θα πρέπει να μεταβεί ο χρήστης στην κύρια ιστοσελίδα της [OpenAI](https://platform.openai.com/).

Αφότου το αποκτήσει, θα χρειαστεί να το θέση σε ένα `.env` αρχείο με τον εξής τρόπο:
```
OPENAI_API_KEY=your_api_key_here
```

### Server Custom API 
Η παρακάτω εντολή τρέχει τον server του custom api για να μπορεί το chatbot να στέλνει post requests και να δέχεται τα κατάλληλα responses:
```
uvicorn API:app --reload
```

### webapp.py
To alan kay chatbot ή αλλιώς η κύρια εφαρμογή βρίσκεται σε ένα αρχείο με όνομα `webapp.py` και για να τρέξει χρειάζεται η παρακάτω εντολή να εκτελεστεί στο terminal:
```
streamlit run webapp.py
```

## Τεστ εφαρμογής και αποτελέσματα:

## Συμπεράσματα εφαρμογής

# Συμπεράσμα μαθήματος
