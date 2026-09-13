# Μελέτη Περίπτωσης: Έκθεση REST API σε API Management ως MCP server

Το Azure API Management είναι μια υπηρεσία που παρέχει μια Πύλη πάνω από τα API Endpoints σας. Ο τρόπος λειτουργίας είναι ότι το Azure API Management λειτουργεί σαν μεσολαβητής μπροστά από τα APIs σας και μπορεί να αποφασίσει τι να κάνει με τα εισερχόμενα αιτήματα.

Χρησιμοποιώντας το, προσθέτετε μια σειρά από λειτουργίες όπως:

- **Ασφάλεια**, μπορείτε να χρησιμοποιήσετε τα πάντα από κλειδιά API, JWT μέχρι διαχειριζόμενη ταυτότητα.
- **Περιορισμός ρυθμού κλήσεων**, μια εξαιρετική λειτουργία είναι η δυνατότητα να αποφασίσετε πόσες κλήσεις περνούν ανά μονάδα χρόνου. Αυτό βοηθά να διασφαλίσετε ότι όλοι οι χρήστες έχουν μια εξαιρετική εμπειρία και επίσης ότι η υπηρεσία σας δεν κατακλύζεται από αιτήματα.
- **Κλιμάκωση & Ισορροπία φορτίου**. Μπορείτε να ορίσετε έναν αριθμό endpoints για να εξισορροπήσετε το φορτίο και επίσης μπορείτε να αποφασίσετε πώς να γίνει η "ισορροπία φορτίου".
- **Λειτουργίες AI όπως σημασιολογική προσωρινή αποθήκευση (semantic caching)**, όριο tokens και παρακολούθηση tokens και άλλα. Αυτές είναι εξαιρετικές λειτουργίες που βελτιώνουν την ανταπόκριση καθώς και σας βοηθούν να έχετε τον έλεγχο των δαπανών token. [Διαβάστε περισσότερα εδώ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Γιατί MCP + Azure API Management;

Το Model Context Protocol γίνεται γρήγορα ένα πρότυπο για εφαρμογές πρακτόρων AI και για το πώς να εκθέτουμε εργαλεία και δεδομένα με συνεπή τρόπο. Το Azure API Management είναι η φυσική επιλογή όταν χρειάζεται να "διαχειριστείτε" APIs. Οι MCP Servers συχνά ενσωματώνονται με άλλα APIs για να επιλύσουν αιτήματα σε ένα εργαλείο, για παράδειγμα. Επομένως, ο συνδυασμός Azure API Management και MCP έχει πολύ νόημα.

## Επισκόπηση

Σε αυτήν την συγκεκριμένη περίπτωση χρήσης θα μάθουμε πώς να εκθέτουμε τα API endpoints ως MCP Server. Κάνοντας αυτό, μπορούμε εύκολα να κάνουμε αυτά τα endpoints μέρος μιας εφαρμογής πράκτορα ενώ παράλληλα εκμεταλλευόμαστε τις λειτουργίες του Azure API Management.

## Βασικά Χαρακτηριστικά

- Επιλέγετε τις μεθόδους endpoint που θέλετε να εκθέσετε ως εργαλεία.
- Οι επιπρόσθετες λειτουργίες που λαμβάνετε εξαρτώνται από το τι ρυθμίζετε στο τμήμα πολιτικών για το API σας. Εδώ όμως θα σας δείξουμε πώς να προσθέσετε περιορισμό ρυθμού κλήσεων (rate limiting).

## Προ-βήμα: εισαγωγή ενός API

Αν έχετε ήδη ένα API στο Azure API Management, υπέροχα, τότε μπορείτε να παραλείψετε αυτό το βήμα. Αν όχι, δείτε αυτόν τον σύνδεσμο, [εισαγωγή API στο Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Έκθεση API ως MCP Server

Για να εκθέσουμε τα API endpoints, ας ακολουθήσουμε τα εξής βήματα:

1. Μεταβείτε στο Azure Portal στη διεύθυνση <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Μεταβείτε στην παρουσία Azure API Management σας.

1. Στο αριστερό μενού, επιλέξτε APIs > MCP Servers > + Create new MCP Server.

1. Στο API, επιλέξτε ένα REST API που θέλετε να εκθέσετε ως MCP server.

1. Επιλέξτε μία ή περισσότερες λειτουργίες API (API Operations) για να τις εκθέσετε ως εργαλεία. Μπορείτε να επιλέξετε όλες τις λειτουργίες ή μόνο συγκεκριμένες.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Επιλέξτε **Create**.

1. Μεταβείτε στην επιλογή μενού **APIs** και **MCP Servers**, θα δείτε το εξής:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Ο MCP server δημιουργήθηκε και οι API λειτουργίες εκτέθηκαν ως εργαλεία. Ο MCP server εμφανίζεται στην καρτέλα MCP Servers. Η στήλη URL δείχνει το endpoint του MCP server που μπορείτε να καλέσετε για δοκιμές ή μέσω μιας εφαρμογής πελάτη.

## Προαιρετικά: Ρύθμιση πολιτικών

Το Azure API Management έχει την βασική έννοια των πολιτικών (policies) όπου ρυθμίζετε διάφορους κανόνες για τα endpoints σας, όπως για παράδειγμα περιορισμό ρυθμού κλήσεων ή σημασιολογική προσωρινή αποθήκευση. Αυτές οι πολιτικές ορίζονται σε XML.

Να πώς μπορείτε να ρυθμίσετε μια πολιτική για περιορισμό ρυθμού κλήσεων στον MCP Server σας:

1. Στην πύλη (portal), κάτω από APIs, επιλέξτε **MCP Servers**.

1. Επιλέξτε τον MCP server που δημιουργήσατε.

1. Στο αριστερό μενού, κάτω από MCP, επιλέξτε **Policies**.

1. Στον επεξεργαστή πολιτικών, προσθέστε ή επεξεργαστείτε τις πολιτικές που θέλετε να εφαρμόσετε στα εργαλεία του MCP server. Οι πολιτικές ορίζονται σε μορφή XML. Για παράδειγμα, μπορείτε να προσθέσετε μια πολιτική που περιορίζει τις κλήσεις στα εργαλεία του MCP server (σε αυτό το παράδειγμα, 5 κλήσεις ανά 30 δευτερόλεπτα ανά διεύθυνση IP πελάτη). Ακολουθεί XML που θα προκαλέσει το περιορισμό:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Εδώ μια εικόνα του επεξεργαστή πολιτικών:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Δοκιμάστε το

Ας διασφαλίσουμε ότι ο MCP Server μας λειτουργεί όπως αναμένεται.

> [!NOTE]
> Το Azure API Management εκθέτει επί του παρόντος αυτόν τον server μέσω του Streamable
> HTTP endpoint `/mcp`. Η παλαιότερη μεταφορά HTTP+SSE `/sse` έχει καταργηθεί και
> θα πρέπει να χρησιμοποιείται μόνο με παλιούς πελάτες.

Για αυτό, θα χρησιμοποιήσουμε το Visual Studio Code και το GitHub Copilot στη λειτουργία Agent. Θα προσθέσουμε τον MCP server σε ένα αρχείο *mcp.json*. Κάνοντας αυτό, το Visual Studio Code θα λειτουργεί ως πελάτης με ικανότητες πράκτορα και οι τελικοί χρήστες θα μπορούν να πληκτρολογούν εντολές και να αλληλεπιδρούν με τον server.

Ας δούμε πώς, για να προσθέσουμε τον MCP server στο Visual Studio Code:

1. Χρησιμοποιήστε την εντολή MCP: **Add Server από το Command Palette**.

1. Όταν σας ζητηθεί, επιλέξτε τον τύπο server: **HTTP (HTTP ή Server Sent Events)**.

1. Εισαγάγετε το Streamable HTTP URL που εμφανίζεται για τον MCP server στο API Management.
    Για παράδειγμα:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Εισαγάγετε ένα ID server της επιλογής σας. Αυτή δεν είναι μια σημαντική τιμή, αλλά θα σας βοηθήσει να θυμάστε ποια είναι αυτή η περίπτωση server.

1. Επιλέξτε αν θα αποθηκεύσετε τη ρύθμιση στα workspace settings ή στα user settings.

  - **Workspace settings** - Η ρύθμιση server αποθηκεύεται σε ένα αρχείο .vscode/mcp.json που είναι διαθέσιμο μόνο στο τρέχον workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Η ρύθμιση server προστίθεται στο παγκόσμιο αρχείο *settings.json* και είναι διαθέσιμη σε όλα τα workspaces. Η ρύθμιση φαίνεται ως εξής:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Πρέπει επίσης να προσθέσετε ρύθμιση, μια κεφαλίδα για να διασφαλιστεί ότι γίνεται σωστή αυθεντικοποίηση προς το Azure API Management. Χρησιμοποιεί μια κεφαλίδα που ονομάζεται **Ocp-Apim-Subscription-Key**.

    - Να πώς μπορείτε να την προσθέσετε στις ρυθμίσεις:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), αυτό θα προκαλέσει να εμφανιστεί μια προτροπή για την τιμή του κλειδιού API η οποία μπορεί να βρεθεί στο Azure Portal για την παρουσία Azure API Management σας.

   - Για να το προσθέσετε απευθείας στο *mcp.json*, μπορείτε να το κάνετε ως εξής:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Χρησιμοποιήστε τη λειτουργία Agent

Τώρα είμαστε έτοιμοι είτε στις ρυθμίσεις ή στο *.vscode/mcp.json*. Ας το δοκιμάσουμε.

Πρέπει να υπάρχει ένα εικονίδιο Εργαλείων (Tools) όπως αυτό, όπου εμφανίζονται τα εκτεθειμένα εργαλεία από τον server σας:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Κάντε κλικ στο εικονίδιο εργαλείων και θα δείτε μια λίστα εργαλείων όπως αυτή:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Πληκτρολογήστε μια ερώτηση στο chat για να καλέσετε το εργαλείο. Για παράδειγμα, αν επιλέξατε ένα εργαλείο για να λάβετε πληροφορίες σχετικά με μια παραγγελία, μπορείτε να ρωτήσετε τον πράκτορα για μια παραγγελία. Να ένα παράδειγμα εντολής:

    ```text
    get information from order 2
    ```

    Τώρα θα εμφανιστεί ένα εικονίδιο εργαλείων που θα σας ζητήσει να προχωρήσετε στην εκτέλεση του εργαλείου. Επιλέξτε να συνεχιστεί η εκτέλεση του εργαλείου, θα δείτε τώρα ένα αποτέλεσμα όπως το παρακάτω:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **όσα βλέπετε παραπάνω εξαρτώνται από τα εργαλεία που έχετε ρυθμίσει, αλλά η ιδέα είναι να λάβετε μια κειμενική απάντηση όπως παραπάνω**


## Αναφορές

Να πώς μπορείτε να μάθετε περισσότερα:

- [Εγχειρίδιο για το Azure API Management και MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Παράδειγμα Python: Ασφαλείς απομακρυσμένοι MCP servers με Azure API Management (πειραματικό)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP για πελάτη εργαστήριο εξουσιοδότησης](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Χρήση επέκτασης Azure API Management για VS Code για εισαγωγή και διαχείριση APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Καταγραφή και εύρεση απομακρυσμένων MCP servers στο Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Εξαιρετικό αποθετήριο που δείχνει πολλές δυνατότητες AI με Azure API Management
- [AI Gateway εργαστήρια](https://azure-samples.github.io/AI-Gateway/) Περιλαμβάνει εργαστήρια που χρησιμοποιούν το Azure Portal, ο οποίος είναι ένας εξαιρετικός τρόπος να ξεκινήσετε την αξιολόγηση δυνατοτήτων AI.

## Τι Ακολουθεί

- Πίσω στο: [Επισκόπηση Μελετών Περίπτωσης](./README.md)
- Επόμενο: [Πράκτορες Ταξιδιού Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->