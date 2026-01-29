# Μελέτη Περίπτωσης: Έκθεση REST API στο API Management ως MCP Server

Το Azure API Management είναι μια υπηρεσία που παρέχει μια Πύλη πάνω από τα API Endpoints σας. Ο τρόπος λειτουργίας του είναι ότι το Azure API Management λειτουργεί ως proxy μπροστά από τα APIs σας και μπορεί να αποφασίσει τι να κάνει με τις εισερχόμενες αιτήσεις.

Χρησιμοποιώντας το, προσθέτετε μια σειρά από δυνατότητες όπως:

- **Ασφάλεια**, μπορείτε να χρησιμοποιήσετε τα πάντα, από API keys, JWT έως managed identity.
- **Περιορισμός ρυθμού (Rate limiting)**, μια εξαιρετική δυνατότητα που σας επιτρέπει να αποφασίσετε πόσες κλήσεις επιτρέπονται ανά συγκεκριμένη χρονική μονάδα. Αυτό βοηθά να διασφαλιστεί ότι όλοι οι χρήστες έχουν μια καλή εμπειρία και ότι η υπηρεσία σας δεν υπερφορτώνεται από αιτήσεις.
- **Κλιμάκωση και Εξισορρόπηση Φορτίου (Scaling & Load balancing)**. Μπορείτε να ρυθμίσετε έναν αριθμό endpoints για να εξισορροπήσετε το φορτίο και να αποφασίσετε πώς να το "εξισορροπήσετε".
- **Λειτουργίες AI όπως semantic caching**, περιορισμός tokens, παρακολούθηση tokens και άλλα. Αυτές είναι εξαιρετικές δυνατότητες που βελτιώνουν την απόκριση και σας βοηθούν να παρακολουθείτε τη χρήση των tokens. [Διαβάστε περισσότερα εδώ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Γιατί MCP + Azure API Management;

Το Model Context Protocol γίνεται γρήγορα ένα πρότυπο για agentic AI εφαρμογές και για το πώς να εκθέσετε εργαλεία και δεδομένα με συνεπή τρόπο. Το Azure API Management είναι μια φυσική επιλογή όταν χρειάζεστε να "διαχειριστείτε" APIs. Οι MCP Servers συχνά ενσωματώνονται με άλλα APIs για την επίλυση αιτημάτων προς ένα εργαλείο, για παράδειγμα. Επομένως, ο συνδυασμός του Azure API Management και του MCP έχει πολύ νόημα.

## Επισκόπηση

Σε αυτή τη συγκεκριμένη περίπτωση χρήσης, θα μάθουμε πώς να εκθέτουμε API endpoints ως MCP Server. Με αυτόν τον τρόπο, μπορούμε εύκολα να κάνουμε αυτά τα endpoints μέρος μιας agentic εφαρμογής, ενώ παράλληλα αξιοποιούμε τις δυνατότητες του Azure API Management.

## Βασικά Χαρακτηριστικά

- Επιλέγετε τις μεθόδους endpoint που θέλετε να εκθέσετε ως εργαλεία.
- Οι πρόσθετες δυνατότητες που αποκτάτε εξαρτώνται από το τι διαμορφώνετε στην ενότητα πολιτικής για το API σας. Εδώ θα σας δείξουμε πώς να προσθέσετε περιορισμό ρυθμού.

## Προετοιμασία: Εισαγωγή ενός API

Εάν έχετε ήδη ένα API στο Azure API Management, τότε μπορείτε να παραλείψετε αυτό το βήμα. Αν όχι, δείτε αυτόν τον σύνδεσμο, [εισαγωγή ενός API στο Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Έκθεση API ως MCP Server

Για να εκθέσετε τα API endpoints, ακολουθήστε τα εξής βήματα:

1. Μεταβείτε στο Azure Portal και στη διεύθυνση <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Μεταβείτε στην περίπτωση του API Management σας.

1. Στο αριστερό μενού, επιλέξτε APIs > MCP Servers > + Δημιουργία νέου MCP Server.

1. Στο API, επιλέξτε ένα REST API για να το εκθέσετε ως MCP server.

1. Επιλέξτε μία ή περισσότερες λειτουργίες API (API Operations) για να τις εκθέσετε ως εργαλεία. Μπορείτε να επιλέξετε όλες τις λειτουργίες ή μόνο συγκεκριμένες.

    ![Επιλογή μεθόδων για έκθεση](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Επιλέξτε **Δημιουργία**.

1. Μεταβείτε στην επιλογή μενού **APIs** και **MCP Servers**, θα πρέπει να δείτε το εξής:

    ![Δείτε τον MCP Server στον κύριο πίνακα](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Ο MCP server δημιουργείται και οι λειτουργίες API εκτίθενται ως εργαλεία. Ο MCP server εμφανίζεται στον πίνακα MCP Servers. Η στήλη URL δείχνει το endpoint του MCP server που μπορείτε να καλέσετε για δοκιμή ή μέσα σε μια εφαρμογή πελάτη.

## Προαιρετικό: Διαμόρφωση πολιτικών

Το Azure API Management έχει την κεντρική έννοια των πολιτικών, όπου ρυθμίζετε διαφορετικούς κανόνες για τα endpoints σας, όπως για παράδειγμα περιορισμό ρυθμού ή semantic caching. Αυτές οι πολιτικές γράφονται σε XML.

Δείτε πώς μπορείτε να ρυθμίσετε μια πολιτική για να περιορίσετε τον ρυθμό του MCP Server σας:

1. Στο portal, κάτω από APIs, επιλέξτε **MCP Servers**.

1. Επιλέξτε τον MCP server που δημιουργήσατε.

1. Στο αριστερό μενού, κάτω από MCP, επιλέξτε **Policies**.

1. Στον επεξεργαστή πολιτικών, προσθέστε ή επεξεργαστείτε τις πολιτικές που θέλετε να εφαρμόσετε στα εργαλεία του MCP server. Οι πολιτικές ορίζονται σε XML μορφή. Για παράδειγμα, μπορείτε να προσθέσετε μια πολιτική για να περιορίσετε τις κλήσεις στα εργαλεία του MCP server (σε αυτό το παράδειγμα, 5 κλήσεις ανά 30 δευτερόλεπτα ανά διεύθυνση IP πελάτη). Εδώ είναι το XML που θα προκαλέσει τον περιορισμό ρυθμού:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Εδώ είναι μια εικόνα του επεξεργαστή πολιτικών:

    ![Επεξεργαστής πολιτικών](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Δοκιμάστε το

Ας διασφαλίσουμε ότι ο MCP Server μας λειτουργεί όπως αναμένεται.

Για αυτό, θα χρησιμοποιήσουμε το Visual Studio Code και το GitHub Copilot στη λειτουργία Agent. Θα προσθέσουμε τον MCP server σε ένα αρχείο *mcp.json*. Με αυτόν τον τρόπο, το Visual Studio Code θα λειτουργεί ως πελάτης με agentic δυνατότητες και οι τελικοί χρήστες θα μπορούν να πληκτρολογούν ένα prompt και να αλληλεπιδρούν με τον server.

Ας δούμε πώς να προσθέσουμε τον MCP server στο Visual Studio Code:

1. Χρησιμοποιήστε την εντολή MCP: **Add Server από το Command Palette**.

1. Όταν σας ζητηθεί, επιλέξτε τον τύπο server: **HTTP (HTTP ή Server Sent Events)**.

1. Εισάγετε το URL του MCP server στο API Management. Παράδειγμα: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (για SSE endpoint) ή **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (για MCP endpoint), σημειώστε τη διαφορά μεταξύ των μεταφορών `/sse` ή `/mcp`.

1. Εισάγετε ένα server ID της επιλογής σας. Αυτή η τιμή δεν είναι σημαντική, αλλά θα σας βοηθήσει να θυμάστε τι είναι αυτή η περίπτωση server.

1. Επιλέξτε αν θα αποθηκεύσετε τη διαμόρφωση στις ρυθμίσεις του workspace ή στις ρυθμίσεις χρήστη.

  - **Ρυθμίσεις workspace** - Η διαμόρφωση του server αποθηκεύεται σε ένα αρχείο .vscode/mcp.json διαθέσιμο μόνο στο τρέχον workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ή αν επιλέξετε streaming HTTP ως μεταφορά, θα είναι ελαφρώς διαφορετικό:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Ρυθμίσεις χρήστη** - Η διαμόρφωση του server προστίθεται στο παγκόσμιο αρχείο *settings.json* και είναι διαθέσιμη σε όλα τα workspaces. Η διαμόρφωση μοιάζει με την εξής:

    ![Ρύθμιση χρήστη](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Πρέπει επίσης να προσθέσετε μια διαμόρφωση, μια κεφαλίδα για να διασφαλίσετε ότι γίνεται σωστή αυθεντικοποίηση προς το Azure API Management. Χρησιμοποιεί μια κεφαλίδα που ονομάζεται **Ocp-Apim-Subscription-Key**.

    - Δείτε πώς μπορείτε να την προσθέσετε στις ρυθμίσεις:

    ![Προσθήκη κεφαλίδας για αυθεντικοποίηση](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), αυτό θα προκαλέσει την εμφάνιση ενός prompt για να εισάγετε την τιμή του API key, την οποία μπορείτε να βρείτε στο Azure Portal για την περίπτωση του Azure API Management σας.

   - Για να την προσθέσετε στο *mcp.json*, μπορείτε να το κάνετε ως εξής:

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

### Χρήση λειτουργίας Agent

Τώρα είμαστε έτοιμοι είτε στις ρυθμίσεις είτε στο *.vscode/mcp.json*. Ας το δοκιμάσουμε.

Θα πρέπει να υπάρχει ένα εικονίδιο Εργαλείων όπως το εξής, όπου τα εκτεθειμένα εργαλεία από τον server σας παρατίθενται:

![Εργαλεία από τον server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Κάντε κλικ στο εικονίδιο εργαλείων και θα πρέπει να δείτε μια λίστα εργαλείων όπως το εξής:

    ![Εργαλεία](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Εισάγετε ένα prompt στη συνομιλία για να καλέσετε το εργαλείο. Για παράδειγμα, αν επιλέξατε ένα εργαλείο για να λάβετε πληροφορίες σχετικά με μια παραγγελία, μπορείτε να ρωτήσετε τον agent για μια παραγγελία. Εδώ είναι ένα παράδειγμα prompt:

    ```text
    get information from order 2
    ```

    Θα σας εμφανιστεί ένα εικονίδιο εργαλείων που σας ζητά να προχωρήσετε στην κλήση ενός εργαλείου. Επιλέξτε να συνεχίσετε την εκτέλεση του εργαλείου, και θα πρέπει να δείτε ένα αποτέλεσμα όπως το εξής:

    ![Αποτέλεσμα από prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Αυτό που βλέπετε εξαρτάται από τα εργαλεία που έχετε ρυθμίσει, αλλά η ιδέα είναι ότι λαμβάνετε μια απάντηση σε κείμενο όπως παραπάνω.**

## Αναφορές

Δείτε πώς μπορείτε να μάθετε περισσότερα:

- [Οδηγός για το Azure API Management και MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Παράδειγμα Python: Ασφαλής απομακρυσμένοι MCP servers χρησιμοποιώντας Azure API Management (πειραματικό)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Εργαστήριο εξουσιοδότησης MCP πελάτη](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Χρήση της επέκτασης Azure API Management για το VS Code για εισαγωγή και διαχείριση APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Εγγραφή και ανακάλυψη απομακρυσμένων MCP servers στο Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Εξαιρετικό αποθετήριο που δείχνει πολλές δυνατότητες AI με το Azure API Management
- [Εργαστήρια AI Gateway](https://azure-samples.github.io/AI-Gateway/) Περιέχει εργαστήρια χρησιμοποιώντας το Azure Portal, που είναι ένας εξαιρετικός τρόπος για να ξεκινήσετε την αξιολόγηση δυνατοτήτων AI.

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.